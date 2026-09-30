# Zecpath AI - AI Data Storage Structure

## 1. Purpose

This document defines how AI-generated data is stored and organized
within the Zecpath AI recruitment platform.

The storage design supports the complete AI recruitment lifecycle,
from resume upload to interview evaluation and final hiring decisions.

---

## 2. Storage Overview

Zecpath AI uses different storage formats depending on the type of data.

| Data Type | Storage Format | Storage Location |
|---|---|---|
| Resumes | PDF / DOCX | data/resumes/ |
| Extracted Resume Data | Text / JSON | data/extracted/ |
| Parsed Profiles | JSON | data/parsed_profiles/ |
| Job Descriptions | JSON | data/job_descriptions/ |
| ATS Scores | JSON | data/ats_scores/ |
| Screening Reports | JSON | data/screening_reports/ |
| Interview Results | JSON | data/interview_results/ |
| Structured Data | JSON | data/structured/ |

---

## 3. Resume Storage

Original candidate resumes are stored in their original file format.

Supported formats:

- PDF
- DOCX

Location:

    data/resumes/

Example:

    candidate_CAND-001_resume.pdf

The original resume is preserved so that the extracted and
AI-generated data can be traced back to the source document.

---

## 4. Extracted Resume Data

Text and information extracted from the original resume are stored
for further processing.

Location:

    data/extracted/

The extracted data is used as input for the resume parser.

Flow:

    Resume
       |
       v
    Extraction
       |
       v
    Extracted Data
       |
       v
    Resume Parser

---

## 5. Parsed Profile Storage

The resume parser converts extracted resume information into a
structured candidate profile.

Format:

    JSON

Location:

    data/parsed_profiles/

Example fields:

- candidate_id
- job_id
- model_version
- timestamp
- name
- email
- phone
- education
- skills
- experience

Example file:

    parsed_profile_sample.json

---

## 6. ATS Score Storage

The ATS engine compares the candidate profile with the job
description and generates a matching score.

Format:

    JSON

Location:

    data/ats_scores/

Example fields:

- candidate_id
- job_id
- model_version
- timestamp
- overall_score
- skills_match
- education_match
- experience_match
- matched_skills
- missing_skills
- recommendation

Flow:

    Parsed Profile + Job Description
                  |
                  v
              ATS Engine
                  |
                  v
              ATS Score

---

## 7. Screening Report Storage

The screening AI evaluates the candidate after ATS screening.

Format:

    JSON

Location:

    data/screening_reports/

Example fields:

- candidate_id
- job_id
- model_version
- timestamp
- screening status
- screening score
- communication score
- technical score
- experience relevance
- strengths
- concerns
- recommendation

---

## 8. Interview Result Storage

Interview AI results are stored for each candidate and job.

Format:

    JSON

Location:

    data/interview_results/

Example fields:

- candidate_id
- job_id
- model_version
- timestamp
- interview status
- overall score
- technical score
- communication score
- problem solving score
- strengths
- areas for improvement
- recommendation

---

## 9. Common Metadata

All AI-generated records should contain common metadata.

### Candidate ID

Uniquely identifies the candidate.

Example:

    CAND-001

### Job ID

Uniquely identifies the job associated with the candidate.

Example:

    JOB-001

### Model Version

Identifies the AI model or processing version that generated
the result.

Examples:

    resume-parser-v1.0
    ats-scorer-v1.0
    screening-ai-v1.0
    interview-ai-v1.0

### Timestamp

Records when the AI result was generated.

Example:

    2026-09-30T17:30:00Z

---

## 10. Data Relationships

The main data relationship is:

    Candidate
        |
        v
    Resume
        |
        v
    Extracted Data
        |
        v
    Parsed Profile
        |
        +----------------+
        |                |
        v                v
    Job Description    Candidate Profile
             \          /
              \        /
               v      v
                ATS Score
                    |
                    v
             Screening Report
                    |
                    v
             Interview Result
                    |
                    v
             Hiring Decision

Candidate ID and Job ID connect the records throughout
the pipeline.

---

## 11. Data Lifecycle

The AI data lifecycle begins when a candidate uploads a resume.

1. Resume is uploaded.
2. Original resume is stored.
3. Resume text is extracted.
4. Candidate profile is parsed.
5. Parsed profile is matched with the job description.
6. ATS score is generated.
7. Screening report is generated.
8. Interview is conducted.
9. Interview result is stored.
10. Data is used for the final hiring decision.

---

## 12. Data Versioning

AI-generated data should record the model version used to
produce the result.

Example:

    ats-scorer-v1.0

When the AI model is improved, a new version should be created.

Example:

    ats-scorer-v1.1

Previous results should remain available for traceability and
comparison.

---

## 13. Retraining Dataset

Selected historical AI data can be used to create datasets
for future model improvement.

Potential training data includes:

- Parsed candidate profiles
- ATS scores
- Screening results
- Interview results
- Final hiring outcomes

Training datasets should maintain candidate and job relationships
where appropriate and follow the required data protection rules.

Dataset versions should be identifiable.

Example:

    recruitment_dataset_v1
    recruitment_dataset_v2

---

## 14. Storage Structure

The final Day 7 storage structure is:

    data/
    ├── resumes/
    ├── extracted/
    ├── structured/
    ├── job_descriptions/
    ├── parsed_profiles/
    ├── ats_scores/
    ├── screening_reports/
    └── interview_results/

This structure separates original documents, processed data,
and AI-generated results.

---

## 15. Summary

The Zecpath AI storage design provides a structured way to
store candidate information throughout the recruitment pipeline.

Each AI-generated record contains common metadata such as:

- Candidate ID
- Job ID
- Model version
- Timestamp

This allows the platform to maintain traceability, support
versioning, and prepare historical data for future AI model
improvement.