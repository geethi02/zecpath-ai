
# Zecpath AI - ATS API Schemas

## 1. Resume Upload
Endpoint: POST /api/v1/resumes/upload

Input:
- file: required PDF or DOCX file
- Content-Type: multipart/form-data

Response:
{
  "resume_id": "resume_123",
  "job_id": "job_123",
  "status": "queued",
  "message": "Resume accepted for processing"
}

## 2. Resume Parsing
Endpoint: POST /api/v1/resumes/{resume_id}/parse

Response:
{
  "resume_id": "resume_123",
  "job_id": "job_124",
  "status": "queued"
}

## 3. Resume Scoring
Endpoint: POST /api/v1/resumes/{resume_id}/score

Input:
{
  "job_description": "Python, SQL, and data analysis experience"
}

Response:
{
  "resume_id": "resume_123",
  "job_id": "job_125",
  "status": "queued"
}

## 4. Candidate Shortlisting
Endpoint: POST /api/v1/shortlists

Input:
{
  "candidate_ids": ["resume_123", "resume_124"],
  "job_description": "Python and SQL data analyst",
  "minimum_score": 70
}

Response:
{
  "job_id": "job_126",
  "status": "queued"
}

## 5. Job Status
Endpoint: GET /api/v1/jobs/{job_id}

Response:
{
  "job_id": "job_123",
  "status": "queued",
  "result": null,
  "error": null
}

Allowed statuses: queued, running, completed, failed.

## 6. Error Response
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Request validation failed",
    "request_id": "req_123"
  }
}

## 7. Validation Rules
- Accept PDF and DOCX files only.
- Require a non-empty job description.
- Keep minimum_score between 0 and 100.
- Use unique resume and job IDs.
- Never expose sensitive resume information in errors.