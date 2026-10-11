# Zecpath AI ATS — Developer Guide

## 1. Introduction

This guide explains how to set up, test, and maintain the Zecpath AI Applicant Tracking System (ATS) project.

The project contains separate modules for resume extraction, skill extraction, education and experience parsing, semantic matching, scoring, candidate ranking, and fairness-related processing.

## 2. Prerequisites

- Python installed on your system
- Git
- Visual Studio Code or another Python editor
- Project dependencies installed from `requirements.txt`, if available

## 3. Open the Project

Open the project directory:

`C:\Users\DELL\Desktop\zecpath-ai`

Open a PowerShell terminal at the project root.

## 4. Set Up the Python Import Path

For the current PowerShell session, run:

```powershell
$env:PYTHONPATH = (Get-Location).Path
```

This allows Python to locate project modules when running commands from the project root.

The setting is temporary and must be repeated in a new terminal session.

## 5. Install Dependencies

If the project has a `requirements.txt` file, create and activate a virtual environment if appropriate, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, follow your organization's approved environment setup process. Do not change system execution policies without understanding the implications.

## 6. Project Structure

| Directory | Purpose |
|---|---|
| `parsers/` | Resume extraction and job description parsing |
| `skill_extraction/` | Skill extraction |
| `education_parsing/` | Education parsing and relevance |
| `experience_parsing/` | Experience parsing and relevance |
| `semantic_matching/` | Embeddings and semantic similarity |
| `ats_scoring/` | Candidate scoring |
| `candidate_ranking/` | Candidate ranking and shortlisting |
| `fairness_normalization/` | Fairness-related processing |
| `ats_api/` | API-related code and specifications |
| `src/` | Processing and matching scripts |
| `tests/` | Automated tests |
| `docs/` | Documentation and reports |

## 7. Run Automated Tests

From the project root, run:

```powershell
$env:PYTHONPATH = (Get-Location).Path
pytest -q
```

Check the output and resolve failures before committing code changes.

## 8. Resume Extraction

The resume extractor supports PDF and DOCX files.

Relevant file:

`parsers/resume_extractor.py`

The main operations include extracting document text, cleaning text, and processing resumes.

Before changing extraction logic, add test cases for the affected formats and edge cases.

## 9. Making Changes Safely

1. Identify the module responsible for the required behaviour.
2. Inspect the existing implementation and tests.
3. Make a focused change.
4. Run the relevant tests.
5. Run the full test suite.
6. Compare outputs before and after the change.
7. Update the technical documentation if behaviour or interfaces change.
8. Review the Git diff before committing.

## 10. Extending the ATS

Examples of future improvements include:

- Adding OCR for scanned resumes
- Improving extraction from tables and multi-column layouts
- Expanding the skill dictionary
- Validating scoring against manually labelled examples
- Improving error reporting
- Measuring memory usage and concurrent processing performance
- Adding API integration tests where applicable

New features should include tests and documentation.

## 11. Scoring and Ranking Guidance

Scoring and ranking should support human review rather than replace it.

Before modifying scoring:
- Inspect the actual scoring formula and configuration.
- Document any changes to score ranges or weights.
- Test relevant and mismatched resume–job-description pairs.
- Review unexpected scores and ranking results.
- Evaluate potential bias and limitations.

Do not describe unvalidated scores as proven ATS accuracy.

## 12. Git Workflow

Check changed files:

```powershell
git status
```

Review the diff:

```powershell
git diff
```

Stage only intended files:

```powershell
git add <file-or-folder>
```

Commit with a descriptive message:

```powershell
git commit -m "Describe the change"
```

Push the branch:

```powershell
git push origin main
```

Do not commit secrets, private candidate data, or temporary files.

## 13. Troubleshooting

For common errors and diagnostic steps, refer to `TROUBLESHOOTING_GUIDE.md` in this directory.

## 14. Current Limitations

This guide describes the intended development workflow. Verify actual dependencies, API behaviour, model configuration, and module integration against the repository before extending or deploying the system.

Successful unit tests do not by themselves establish production readiness.
