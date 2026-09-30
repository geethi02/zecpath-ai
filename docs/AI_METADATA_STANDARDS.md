# Zecpath AI - AI Metadata Standards

## 1. Purpose

This document defines the standard metadata fields used across
Zecpath AI data and AI-generated results.

The metadata allows candidate data, job data, AI models, and
processing events to be connected and traced throughout the
recruitment pipeline.

---

## 2. Standard Metadata Fields

Every AI-generated record should contain the following fields:

| Field | Description | Example |
|---|---|---|
| candidate_id | Unique identifier for the candidate | CAND-001 |
| job_id | Unique identifier for the job | JOB-001 |
| model_version | Version of the AI model used | ats-scorer-v1.0 |
| timestamp | Date and time when the result was generated | 2026-09-30T17:30:00Z |

---

## 3. Candidate ID

### Definition

Candidate ID uniquely identifies a candidate within the Zecpath
AI recruitment platform.

### Format

    CAND-XXX

### Example

    CAND-001

### Usage

Candidate ID should remain consistent across all stages of the
recruitment process.

Example:

    Resume
       |
       v
    Parsed Profile
       |
       v
    ATS Score
       |
       v
    Screening Report
       |
       v
    Interview Result

All records for the same candidate use the same Candidate ID.

---

## 4. Job ID

### Definition

Job ID uniquely identifies a job or job posting.

### Format

    JOB-XXX

### Example

    JOB-001

### Usage

Job ID connects candidate evaluation results to the specific
job for which the candidate is being evaluated.

A candidate may be associated with multiple jobs, so the Job ID
must be stored with AI evaluation results.

---

## 5. Model Version

### Definition

Model Version identifies the version of the AI model or AI
processing component that generated a result.

### Format

    <component>-v<version>

### Examples

    resume-parser-v1.0
    ats-scorer-v1.0
    screening-ai-v1.0
    interview-ai-v1.0

### Purpose

Model versioning allows Zecpath AI to identify which AI version
produced a specific result.

If the model is updated, a new version should be assigned.

Example:

    ats-scorer-v1.0
    ats-scorer-v1.1
    ats-scorer-v2.0

Previous results should retain their original model version.

---

## 6. Timestamp

### Definition

Timestamp records when an AI result or processing event was
generated.

### Format

ISO 8601 UTC format.

### Example

    2026-09-30T17:30:00Z

### Purpose

Timestamp allows the system to determine when data was created,
processed, or updated.

Using UTC helps maintain consistent timestamps across different
locations and systems.

---

## 7. Metadata Example

A typical AI-generated record can contain:

```json
{
  "candidate_id": "CAND-001",
  "job_id": "JOB-001",
  "model_version": "ats-scorer-v1.0",
  "timestamp": "2026-09-30T17:30:00Z"
}