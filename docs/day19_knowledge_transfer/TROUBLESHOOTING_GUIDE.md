# Zecpath AI ATS — Troubleshooting Guide

## 1. Purpose

This guide helps developers identify and resolve common issues when running, testing, or maintaining the ATS project.

## 2. Python Module Import Errors

### Error
`ModuleNotFoundError: No module named 'parsers'`

### Possible solution
Run commands from the project root directory:

```powershell
$env:PYTHONPATH = (Get-Location).Path
pytest -q
```

Ensure the required package folder exists and contains `__init__.py` where appropriate.

## 3. Unsupported Resume Format

### Error
`ValueError: Unsupported file type: .txt`

### Explanation
The resume extractor currently supports PDF and DOCX files.

### Solution
Use a supported file format. If another format is required, implement and test a dedicated extraction method before adding it to the supported formats.

## 4. PDF Text Extraction Problems

### Possible symptoms
- Empty extracted text
- Missing words
- Incorrect reading order
- Unusual symbols

### Troubleshooting
1. Confirm that the PDF opens correctly.
2. Check whether the PDF contains selectable text or scanned images.
3. Test extraction with `pypdf`.
4. Inspect the extracted text before cleaning.
5. Check the output of `clean_text()`.

Scanned PDFs may require OCR, which is not confirmed as part of the current extraction workflow.

## 5. DOCX Extraction Problems

### Possible symptoms
- Missing text
- Missing table content
- Unexpected line breaks

### Troubleshooting
1. Confirm the file is a valid DOCX document.
2. Check whether relevant content is stored in paragraphs or tables.
3. Inspect the extracted output.
4. Add test cases for any newly supported document structures.

The current DOCX extractor reads document paragraphs. Table extraction should be verified or implemented if needed.

## 6. Noisy Resume Text

### Symptoms
- Extra spaces
- Excessive blank lines
- Inconsistent bullet characters

### Troubleshooting
1. Inspect the raw extracted text.
2. Run the text-cleaning function.
3. Verify that meaningful words and line boundaries remain.
4. Add a regression test for every discovered cleaning issue.

Avoid aggressive cleaning that removes useful resume information.

## 7. Unexpected ATS Scores

### Symptoms
- A mismatched candidate receives a high score.
- A relevant candidate receives a low score.
- Candidate ranking seems incorrect.

### Troubleshooting
1. Inspect the resume and job-description text.
2. Check extracted skills and requirements.
3. Review the scoring configuration and implementation.
4. Check score normalization and ranking order.
5. Compare results against manually reviewed test cases.

The temporary keyword-overlap baseline is not a validated measure of hiring suitability.

## 8. Test Failures

### Recommended command

```powershell
$env:PYTHONPATH = (Get-Location).Path
pytest -q
```

### Troubleshooting
- Read the complete failure message.
- Identify the failing test and relevant function.
- Fix the underlying issue rather than deleting the test.
- Rerun the failing test and then the full test suite.

## 9. Git Problems

### Check repository status

```powershell
git status
```

### Review changed files

```powershell
git diff
```

Before committing, verify that the intended source files and documentation are included. Avoid committing local secrets, candidate personal information, temporary logs, or generated cache files.

## 10. Production Readiness Notes

Successful unit tests and a small local benchmark do not establish production readiness. Additional validation may be needed for memory usage, concurrent requests, response time, malformed files, and real-world resume formats.

## 11. Support Information

When reporting a problem, include:
- The command that was executed
- The complete error message
- The affected module or file
- The input type, without sharing confidential candidate data
- The test result before and after the change
