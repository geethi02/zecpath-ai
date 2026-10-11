
# Zecpath AI - ATS API Integration Flow

## 1. Overview

The ATS API provides an interface between backend applications and the existing resume processing and scoring modules.

## 2. End-to-End Flow

1. A client submits a resume through the upload endpoint.
2. The API validates the file type, size, and request.
3. The system assigns a resume ID and job ID.
4. A processing worker extracts the resume text.
5. Resume parsing and extraction modules produce structured data.
6. The ATS scoring module compares the candidate profile with the job description.
7. Candidate ranking and shortlisting modules evaluate eligible candidates.
8. The system stores the processing status and result.
9. The client checks job status and retrieves the result.
10. The system logs request IDs, processing duration, outcomes, and errors.

## 3. Integration Sequence

Client Application
    |
    v
ATS REST API
    |
    v
Input Validation
    |
    v
Resume Storage and Job Creation
    |
    v
Background Worker
    |
    v
Resume Extraction and Parsing
    |
    v
ATS Scoring
    |
    v
Candidate Ranking and Shortlisting
    |
    v
Result Storage
    |
    v
Job Status and Result API
    |
    v
Client Application

## 4. Asynchronous Job Lifecycle

queued -> running -> completed

queued -> running -> failed

The client receives a job ID and checks its status through the job-status endpoint.

A real background queue, worker, and persistent job store must be implemented before this lifecycle is considered operational.

## 5. Error Handling

- Invalid inputs are rejected before processing.
- Missing resumes or jobs return a not-found response.
- Unsupported files are rejected.
- Unexpected processing errors are logged and return a generic server error.
- Failed jobs record a safe error code and message.

## 6. Observability

Each request should have a request ID. Logs should record the endpoint, status code, duration, and relevant job ID without exposing full resume contents or secrets.

## 7. Security and Privacy

- Protect endpoints with authentication in production.
- Validate uploaded files and enforce size limits.
- Restrict access to resumes and results.
- Protect personal information in storage and logs.
- Define retention and deletion procedures.

## 8. Current Implementation Boundary

This document describes the intended integration architecture. Actual endpoint behavior, background processing, storage, and scoring integration must be verified through implementation and tests.