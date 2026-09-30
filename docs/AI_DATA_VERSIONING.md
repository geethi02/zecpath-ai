# Zecpath AI - AI Data Versioning and Retraining

## 1. Purpose

This document defines how Zecpath AI manages AI model versions,
AI-generated results, and datasets used for future model improvement.

The purpose is to maintain traceability between AI results and
the model version that generated them.

---

## 2. Model Versioning

Each AI component should have a unique model version.

Examples:

    resume-parser-v1.0
    ats-scorer-v1.0
    screening-ai-v1.0
    interview-ai-v1.0

When a model is updated, a new version is created.

Example:

    ats-scorer-v1.0
    ats-scorer-v1.1
    ats-scorer-v2.0

Previous model versions should not be overwritten.

---

## 3. Why Versioning Is Required

Model versioning allows Zecpath AI to:

- Identify which model produced a result
- Track changes between model versions
- Compare results from different versions
- Maintain historical AI results
- Support future model improvement

Each AI-generated record should store the model version in its
metadata.

---

## 4. AI Result Versioning

AI-generated results should retain their original model version.

Example:

```json
{
  "candidate_id": "CAND-001",
  "job_id": "JOB-001",
  "model_version": "ats-scorer-v1.0",
  "timestamp": "2026-09-30T17:30:00Z"
}