
# ATS API Specification

## 1. Purpose
This document defines the REST API contract for the Zecpath AI Applicant Tracking System (ATS). It allows backend applications to upload resumes, parse resume information, calculate job-match scores, and shortlist candidates.

## 2. API Standards
- Architecture: REST
- Data format: JSON
- File upload format: multipart/form-data
- API version: v1
- Base path: /api/v1
- Success responses use appropriate HTTP status codes.
- Timestamps use ISO 8601 format in UTC.
- Uploaded resumes must be validated before processing.
- Production deployments must use authentication and HTTPS.

## 3. Endpoints

### 3.1 Health Check
- Method: GET
- Path: /health
- Purpose: Check whether the API is running.
- Success status: 200 OK

Example response:
{
  "status": "healthy",
  "service": "zecpath-ats-api",
  "version": "1.0.0"
}

### 3.2 Resume Upload
- Method: POST
- Path: /api/v1/resumes/upload
- Content-Type: multipart/form-data
- Required field: file
- Supported file types: PDF and DOCX
- Success status: 202 Accepted

Purpose:
Validate the uploaded file, assign a resume ID, and return a processing job ID.

Example response:
{
  "resume_id": "resume_123",
  "job_id": "job_123",
  "status": "queued",
  "message": "Resume accepted for processing"
}

### 3.3 Resume Parsing
- Method: POST
- Path: /api/v1/resumes/{resume_id}/parse
- Success status: 202 Accepted

Purpose:
Request extraction of resume text and structured information such as skills, education, and work experience.

Example response:
{
  "resume_id": "resume_123",
  "job_id": "job_124",
  "status": "queued"
}

### 3.4 Resume Scoring
- Method: POST
- Path: /api/v1/resumes/{resume_id}/score
- Content-Type: application/json
- Required field: job_description

Example request:
{
  "job_description": "Python, SQL, Power BI, and data analysis experience"
}

Success status: 202 Accepted

Example response:
{
  "resume_id": "resume_123",
  "job_id": "job_125",
  "status": "queued"
}

The completed scoring result may include a match score, matched skills, missing skills, and scoring explanation. Scores must follow the existing ATS scoring implementation.

### 3.5 Candidate Shortlisting
- Method: POST
- Path: /api/v1/shortlists
- Content-Type: application/json

Example request:
{
  "candidate_ids": ["resume_123", "resume_124"],
  "job_description": "Python and SQL data analyst",
  "minimum_score": 70
}

Success status: 202 Accepted

Purpose:
Request ranking and shortlisting of candidates against a job description. The minimum score is a configurable screening threshold, not an automatic hiring decision.

### 3.6 Job Status
- Method: GET
- Path: /api/v1/jobs/{job_id}
- Success status: 200 OK

Example response:
{
  "job_id": "job_123",
  "status": "queued",
  "result": null,
  "error": null
}

Supported statuses:
- queued
- running
- completed
- failed

### 3.7 Job Result
- Method: GET
- Path: /api/v1/jobs/{job_id}/result
- Purpose: Retrieve the result of a completed job.
- Success status: 200 OK
- If the job is still running: 409 Conflict

## 4. Error Response Contract

All API errors should return a consistent JSON structure.

Example:
{
  "error": {
    "code": "INVALID_FILE_TYPE",
    "message": "Only PDF and DOCX files are supported",
    "request_id": "req_123"
  }
}

Expected HTTP status codes:
- 400 Bad Request: invalid request data
- 401 Unauthorized: missing or invalid authentication
- 403 Forbidden: insufficient permission
- 404 Not Found: resource does not exist
- 409 Conflict: operation cannot be performed in the current state
- 413 Payload Too Large: file exceeds the configured limit
- 415 Unsupported Media Type: unsupported file type
- 422 Unprocessable Entity: validation failure
- 429 Too Many Requests: rate limit exceeded
- 500 Internal Server Error: unexpected server error
- 503 Service Unavailable: service temporarily unavailable

## 5. Asynchronous Processing
Long-running parsing, scoring, and ranking operations should return a job ID instead of keeping the request open until processing finishes.

The client can poll GET /api/v1/jobs/{job_id} to check progress. A completed job makes its result available through the job-result endpoint.

The current implementation must clearly distinguish an API design from a production job queue. Persistent storage, worker processes, retries, and queue infrastructure must be configured before claiming production-grade asynchronous execution.

## 6. Logging Standards
- Use Python's standard logging framework.
- Assign a request ID to each API request.
- Log request method, endpoint, response status, duration, and job ID where applicable.
- Log unexpected exceptions with stack traces.
- Never log passwords, API keys, full resume contents, or unnecessary personal information.
- Do not return internal stack traces to API clients.

## 7. Security
- Require authentication for protected endpoints in production.
- Enforce file size and file type limits.
- Validate all user inputs.
- Store uploaded resumes securely.
- Apply access controls to candidate records and job results.
- Define retention and deletion policies for personal data.

## 8. Acceptance Criteria
- All required endpoints are documented.
- Request and response contracts are defined.
- Job states and error responses are standardized.
- Logging and security expectations are documented.
- API implementation and tests are maintained separately from this specification.