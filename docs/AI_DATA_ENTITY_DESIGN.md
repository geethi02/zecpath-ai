# AI Data Entity Design

## 1. Purpose

This document defines the standard data entities used in the
resume screening and job matching system.

The goal is to convert unstructured resumes and job descriptions
into structured data that can be processed by matching algorithms
and AI systems.

---

## 2. Candidate Profile

A Candidate Profile represents a job applicant.

### Fields

- name
- location
- email
- phone
- summary
- education
- experience
- skills
- projects
- certifications

### Example

```json
{
    "name": "Candidate Name",
    "location": "Bengaluru",
    "email": "candidate@email.com",
    "phone": "+91-XXXXXXXXXX",
    "summary": "Data Analyst with experience in reporting and analytics.",
    "education": [],
    "experience": [],
    "skills": [],
    "projects": [],
    "certifications": []
}