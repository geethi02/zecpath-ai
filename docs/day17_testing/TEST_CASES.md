# Day 17 — ATS Test Cases

## 1. Purpose

To evaluate the Zecpath AI ATS scoring API across different job descriptions and candidate profiles.

## 2. Test Cases

| Test ID | Test Scenario | Expected Behaviour | Actual Result |
|---|---|---|---|
| TC01 | Entry-Level Data Analyst | Score a fresher resume against a data analyst job description. | Completed — 45.65% |
| TC02 | Junior Python Developer | Evaluate Python-related keyword overlap. | Completed — 37.50% |
| TC03 | HR Executive | Evaluate an HR profile against an HR job description. | Completed — 8.82% |
| TC04 | Sales Executive | Evaluate a sales profile against a sales job description. | Completed — 62.86% |
| TC05 | Graduate Data Analyst mismatch test | Check whether an HR resume receives a lower match score against a data analyst job description. | Completed — 15.56% |
| TC06 | Data Analyst mismatch test | Evaluate a mismatched profile against the selected job description. | Completed — 38.24% |
| TC07 | Senior Data Analyst | Test a senior-level job description against the selected candidate profile. | Completed — 18.60% |
| TC08 | Senior HR Manager | Evaluate an HR profile against a senior HR job description. | Completed — 10.26% |
| TC09 | Business Intelligence Analyst | Evaluate keyword overlap for a BI-related role. | Completed — 45.00% |
| TC10 | Machine Learning Engineer | Evaluate a candidate profile against an ML engineering job description. | Completed — 15.38% |

## 3. Test Execution Notes

- All 10 scoring jobs reached the completed status.
- The reported scores are outputs from the current temporary keyword-overlap baseline.
- A completed scoring job confirms execution, not the correctness of the score.
- The expected behaviours describe the intended test purpose; detailed correctness must be checked through manual review.

## 4. Testing Limitations

The current tests do not independently establish precision, recall, or validated ATS accuracy. These metrics require manually verified resume-job relevance labels and a defined pass/fail threshold.
