
from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone
import logging
import io
import re

from pypdf import PdfReader
from docx import Document

app = FastAPI(
    title="Zecpath AI ATS API",
    version="1.0.0",
    description="REST API for resume upload, parsing, scoring and shortlisting."
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("zecpath_ats")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_EXTENSIONS = {".pdf", ".docx"}

# Temporary in-memory storage for local development.
resumes = {}
jobs = {}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def create_job():
    job_id = f"job_{uuid4().hex[:12]}"
    jobs[job_id] = {
        "job_id": job_id,
        "status": "queued",
        "result": None,
        "error": None,
        "created_at": utc_now()
    }
    return job_id


def extract_text(content: bytes, extension: str) -> str:
    if extension == ".pdf":
        reader = PdfReader(io.BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    document = Document(io.BytesIO(content))
    return "\n".join(paragraph.text for paragraph in document.paragraphs)


def calculate_baseline_score(resume_text: str, job_description: str):
    """Temporary keyword-overlap baseline, not the production ATS scorer."""
    tokenize = lambda text: set(re.findall(r"\b[a-zA-Z0-9+#.]+\b", text.lower()))
    job_terms = tokenize(job_description)
    resume_terms = tokenize(resume_text)

    if not job_terms:
        return 0.0, [], []

    matched = sorted(job_terms & resume_terms)
    missing = sorted(job_terms - resume_terms)
    score = round(len(matched) / len(job_terms) * 100, 2)
    return score, matched, missing


def process_parse_job(job_id: str, resume_id: str):
    jobs[job_id]["status"] = "running"
    try:
        resume = resumes[resume_id]
        text = extract_text(resume["content"], resume["extension"])

        resumes[resume_id]["text"] = text
        jobs[job_id]["result"] = {
            "resume_id": resume_id,
            "text_length": len(text),
            "text": text
        }
        jobs[job_id]["status"] = "completed"
    except Exception:
        logger.exception("Resume parsing failed; job_id=%s", job_id)
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = {
            "code": "PARSING_FAILED",
            "message": "The resume could not be parsed."
        }


def process_score_job(job_id: str, resume_id: str, job_description: str):
    jobs[job_id]["status"] = "running"
    try:
        resume_text = resumes[resume_id].get("text", "")
        if not resume_text:
            raise ValueError("Resume has no parsed text. Parse it first.")

        score, matched, missing = calculate_baseline_score(
            resume_text, job_description
        )
        jobs[job_id]["result"] = {
            "resume_id": resume_id,
            "match_score": score,
            "matched_skills": matched,
            "missing_skills": missing,
            "scoring_method": "temporary_keyword_overlap_baseline"
        }
        jobs[job_id]["status"] = "completed"
    except Exception:
        logger.exception("Resume scoring failed; job_id=%s", job_id)
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = {
            "code": "SCORING_FAILED",
            "message": "The resume could not be scored."
        }


class ScoreRequest(BaseModel):
    job_description: str = Field(min_length=1, max_length=20000)


class ShortlistRequest(BaseModel):
    candidate_ids: list[str] = Field(min_length=1)
    job_description: str = Field(min_length=1, max_length=20000)
    minimum_score: float = Field(default=70, ge=0, le=100)


@app.middleware("http")
async def request_logging(request: Request, call_next):
    request_id = uuid4().hex
    start = datetime.now(timezone.utc)
    try:
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        duration = (datetime.now(timezone.utc) - start).total_seconds()
        logger.info(
            "request_id=%s method=%s path=%s status=%s duration=%.3f",
            request_id, request.method, request.url.path,
            response.status_code, duration
        )
        return response
    except Exception:
        logger.exception("request_id=%s unexpected request error", request_id)
        raise


@app.exception_handler(HTTPException)
async def http_error_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": "REQUEST_ERROR",
                "message": str(exc.detail),
                "request_id": request.headers.get("X-Request-ID")
            }
        }
    )


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "zecpath-ats-api",
        "version": "1.0.0"
    }


@app.post("/api/v1/resumes/upload", status_code=202)
async def upload_resume(file: UploadFile = File(...)):
    extension = Path(file.filename or "").suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(415, "Only PDF and DOCX files are supported.")

    content = await file.read(MAX_FILE_SIZE + 1)
    if not content:
        raise HTTPException(400, "The uploaded file is empty.")
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(413, "Maximum file size is 5 MB.")

    # Basic file signature checks; not a replacement for malware scanning.
    if extension == ".pdf" and not content.startswith(b"%PDF-"):
        raise HTTPException(400, "The file does not appear to be a valid PDF.")
    if extension == ".docx" and not content.startswith(b"PK"):
        raise HTTPException(400, "The file does not appear to be a valid DOCX.")

    resume_id = f"resume_{uuid4().hex[:12]}"
    resumes[resume_id] = {
        "resume_id": resume_id,
        "filename": Path(file.filename).name,
        "extension": extension,
        "content": content,
        "text": ""
    }

    return {
        "resume_id": resume_id,
        "status": "uploaded",
        "message": "Resume uploaded. Submit a parsing request to process it."
    }


@app.post("/api/v1/resumes/{resume_id}/parse", status_code=202)
def parse_resume(resume_id: str, background_tasks: BackgroundTasks):
    if resume_id not in resumes:
        raise HTTPException(404, "Resume not found.")

    job_id = create_job()
    background_tasks.add_task(process_parse_job, job_id, resume_id)

    return {
        "resume_id": resume_id,
        "job_id": job_id,
        "status": "queued"
    }


@app.post("/api/v1/resumes/{resume_id}/score", status_code=202)
def score_resume(
    resume_id: str,
    request: ScoreRequest,
    background_tasks: BackgroundTasks
):
    if resume_id not in resumes:
        raise HTTPException(404, "Resume not found.")
    if not resumes[resume_id].get("text"):
        raise HTTPException(409, "Parse the resume before scoring.")

    job_id = create_job()
    background_tasks.add_task(
        process_score_job, job_id, resume_id, request.job_description
    )

    return {
        "resume_id": resume_id,
        "job_id": job_id,
        "status": "queued"
    }


@app.post("/api/v1/shortlists", status_code=202)
def shortlist_candidates(
    request: ShortlistRequest,
    background_tasks: BackgroundTasks
):
    for candidate_id in request.candidate_ids:
        if candidate_id not in resumes:
            raise HTTPException(404, f"Candidate not found: {candidate_id}")
        if not resumes[candidate_id].get("text"):
            raise HTTPException(
                409, f"Candidate must be parsed first: {candidate_id}"
            )

    job_id = create_job()

    def run_shortlisting():
        jobs[job_id]["status"] = "running"
        try:
            shortlisted = []
            rejected = []

            for candidate_id in request.candidate_ids:
                score, matched, missing = calculate_baseline_score(
                    resumes[candidate_id]["text"],
                    request.job_description
                )
                candidate = {
                    "resume_id": candidate_id,
                    "match_score": score,
                    "matched_skills": matched,
                    "missing_skills": missing
                }
                if score >= request.minimum_score:
                    shortlisted.append(candidate)
                else:
                    rejected.append(candidate)

            shortlisted.sort(
                key=lambda item: item["match_score"], reverse=True
            )
            jobs[job_id]["result"] = {
                "shortlisted_candidates": shortlisted,
                "rejected_candidates": rejected,
                "scoring_method": "temporary_keyword_overlap_baseline"
            }
            jobs[job_id]["status"] = "completed"
        except Exception:
            logger.exception("Shortlisting failed; job_id=%s", job_id)
            jobs[job_id]["status"] = "failed"
            jobs[job_id]["error"] = {
                "code": "SHORTLISTING_FAILED",
                "message": "Candidate shortlisting failed."
            }

    background_tasks.add_task(run_shortlisting)

    return {"job_id": job_id, "status": "queued"}


@app.get("/api/v1/jobs/{job_id}")
def get_job_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(404, "Job not found.")
    return jobs[job_id]


@app.get("/api/v1/jobs/{job_id}/result")
def get_job_result(job_id: str):
    if job_id not in jobs:
        raise HTTPException(404, "Job not found.")

    job = jobs[job_id]
    if job["status"] in {"queued", "running"}:
        raise HTTPException(409, "Job is still processing.")
    if job["status"] == "failed":
        raise HTTPException(409, "Job failed; check its error details.")

    return {"job_id": job_id, "result": job["result"]}