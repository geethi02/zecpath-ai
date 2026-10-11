# Zecpath AI — ATS Technical Documentation

## 1. Project Overview

Zecpath AI is an Applicant Tracking System (ATS) project designed to process resumes, extract candidate information, compare candidate profiles with job descriptions, and support candidate ranking.

The system uses modular Python components so that individual processing stages can be maintained and improved independently.

## 2. Main Objectives

- Extract text from PDF and DOCX resumes.
- Parse job descriptions.
- Identify candidate skills.
- Structure education and work experience information.
- Match resumes with job requirements.
- Calculate candidate relevance scores.
- Rank candidates for further review.
- Support fairness-related checks and score normalization.

## 3. System Modules

| Module | Responsibility |
|---|---|
| `parsers/` | Resume extraction, text processing, and job description parsing |
| `skill_extraction/` | Skill dictionary and skill extraction |
| `education_parsing/` | Education information and relevance processing |
| `experience_parsing/` | Work experience parsing and relevance |
| `semantic_matching/` | Embedding generation, semantic similarity, and matching thresholds |
| `ats_scoring/` | ATS scoring configuration and candidate score calculation |
| `candidate_ranking/` | Candidate ranking and shortlisting |
| `fairness_normalization/` | Resume normalization and fairness-related evaluation |
| `ats_api/` | API entry points and API specification |
| `src/` | Resume parsing, structuring, and matching scripts |
| `tests/` | Automated tests |
| `docs/` | Technical documentation and project reports |

## 4. Resume Processing Workflow

1. Receive a resume file.
2. Extract text from the supported PDF or DOCX format.
3. Clean the extracted text.
4. Identify skills and relevant candidate information.
5. Parse education and work experience.
6. Compare candidate information with job requirements.
7. Calculate matching or relevance scores.
8. Rank candidates when the ranking workflow is invoked.
9. Review results and investigate errors where necessary.

The exact execution order depends on the entry point and integration between modules.

## 5. Technologies

- Python
- `pypdf` for PDF text extraction
- `python-docx` for DOCX text extraction
- Regular expressions for text cleaning
- `pytest` for automated testing

Semantic matching components may use embedding models and related libraries configured in the project.

## 6. Input and Output

### Inputs
- Resume files in PDF or DOCX format
- Job descriptions
- Skill dictionary and scoring configuration

### Outputs
Depending on the script or module used, outputs may include:
- Extracted resume text
- Structured candidate information
- Extracted skills
- Similarity and relevance scores
- Candidate ranking results

## 7. Error Handling

- Unsupported resume formats should be rejected with a clear error.
- Extraction failures should be logged or reported to the caller.
- Missing or noisy text should be handled carefully.
- Invalid inputs should be investigated before scores are used for decisions.

## 8. Testing

Run the automated tests from the project root:

```powershell
$env:PYTHONPATH = (Get-Location).Path
pytest -q
```

The test suite should be run after changes to extraction, parsing, scoring, or ranking components.

## 9. Limitations

- Extracted text quality depends on the source document.
- Scoring results require validation against manually reviewed examples.
- A matching score should not be treated as a hiring decision.
- Performance and reliability should be tested under realistic workloads before production deployment.
- Fairness-related modules require appropriate evaluation and review.

## 10. Maintenance Guidelines

- Keep each module focused on its defined responsibility.
- Update tests when changing existing behaviour.
- Document changes to scoring logic and configuration.
- Avoid committing temporary files, local secrets,