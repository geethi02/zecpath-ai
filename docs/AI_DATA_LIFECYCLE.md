# Zecpath AI - AI Data Lifecycle

## 1. Purpose

This document defines the lifecycle of AI data in the Zecpath AI
recruitment platform.

The lifecycle describes how candidate data moves from resume upload
through AI processing and finally to the hiring decision.

---

## 2. AI Data Lifecycle Overview

The complete lifecycle is:

Resume Upload
      |
      v
Resume Storage
      |
      v
Resume Extraction
      |
      v
Profile Parsing
      |
      v
ATS Evaluation
      |
      v
AI Screening
      |
      v
AI Interview
      |
      v
Technical / Machine Evaluation
      |
      v
Final AI Decision
      |
      v
Hiring Decision

---

## 3. Stage 1 - Resume Upload

The candidate submits a resume through the Zecpath AI platform.

Supported resume formats include:

- PDF
- DOCX

The original resume is stored without changing the source file.

Storage location:

    data/resumes/

A unique Candidate ID is assigned to the candidate.

---

## 4. Stage 2 - Resume Extraction

The resume extraction component reads the uploaded resume and
extracts useful text and information.

The extracted information is stored for further processing.

Storage location:

    data/extracted/

Flow:

    Resume
       |
       v
    Resume Extractor
       |
       v
    Extracted Data

---

## 5. Stage 3 - Profile Parsing

The extracted resume information is processed by the resume parser.

The parser creates a structured candidate profile containing
information such as:

- Personal information
- Education
- Skills
- Experience

The structured profile is stored as JSON.

Storage location:

    data/parsed_profiles/

Each profile contains standard metadata:

- Candidate ID
- Job ID
- Model Version
- Timestamp

---

## 6. Stage 4 - ATS Evaluation

The ATS engine compares the parsed candidate profile with the
job description.

The ATS engine evaluates areas such as:

- Skills
- Education
- Experience

The resulting ATS score is stored as structured JSON data.

Storage location:

    data/ats_scores/

Flow:

    Parsed Profile
          +
    Job Description
          |
          v
      ATS Engine
          |
          v
      ATS Score

---

## 7. Stage 5 - AI Screening

Candidates who continue through the recruitment process are
processed by the AI screening component.

The screening system generates a screening result containing
scores, strengths, concerns, and a recommendation.

Storage location:

    data/screening_reports/

The screening result includes:

- Candidate ID
- Job ID
- Model Version
- Timestamp
- Screening Score
- Evaluation results
- Recommendation

---

## 8. Stage 6 - AI Interview

The candidate proceeds to the AI interview stage.

The interview system evaluates areas such as:

- Technical knowledge
- Communication
- Problem solving

The interview result is stored as structured JSON data.

Storage location:

    data/interview_results/

---

## 9. Stage 7 - Technical / Machine Evaluation

The candidate may proceed to technical or machine-based evaluation.

The evaluation result can be associated with the same Candidate ID
and Job ID used throughout the recruitment pipeline.

Evaluation results can be stored and connected with previous
screening and interview results.

---

## 10. Stage 8 - Final AI Decision

The available evaluation data is used by the final decision component.

Relevant information may include:

- ATS score
- Screening result
- Interview result
- Technical evaluation
- Machine test result

The final decision data is associated with the candidate and job.

---

## 11. Stage 9 - Hiring Decision

The final stage produces the recruitment outcome.

Possible outcomes include:

- Selected
- Rejected
- Further review

The final outcome should remain associated with:

- Candidate ID
- Job ID
- Timestamp

This allows the recruitment process to remain traceable.

---

## 12. Data Traceability

The same Candidate ID and Job ID connect data across the pipeline.

Example:

    CAND-001
       |
       +-- Resume
       |
       +-- Parsed Profile
       |
       +-- ATS Score
       |
       +-- Screening Report
       |
       +-- Interview Result
       |
       +-- Final Decision

This provides a continuous data trail for each candidate.

---

## 13. Data Lifecycle Summary

The Zecpath AI data lifecycle follows this sequence:

1. Resume is uploaded.
2. Original resume is stored.
3. Resume text is extracted.
4. Candidate profile is parsed.
5. Candidate is evaluated against the job description.
6. ATS score is generated.
7. AI screening is performed.
8. Interview results are generated.
9. Technical or machine evaluation is performed.
10. Final decision is generated.
11. Hiring outcome is recorded.

The lifecycle ensures that AI-generated information remains
connected throughout the recruitment process.