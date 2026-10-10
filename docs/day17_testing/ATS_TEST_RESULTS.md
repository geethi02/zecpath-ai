# Day 17 — ATS Test Results

## 1. Objective

The objective of Day 17 is to test the Zecpath AI ATS system with different job roles and candidate profiles, including entry-level candidates, senior professionals, and mismatched resumes.

## 2. Testing Summary

- Total test cases executed: 10
- Completed scoring jobs: 10
- Testing approach: API-based testing
- Scoring method: `temporary_keyword_overlap_baseline`

## 3. Test Results

| Test Case | Scenario | Match Score | Status |
|---|---|---:|---|
| TC01 | Entry-Level Data Analyst | 45.65% | Completed |
| TC02 | Junior Python Developer | 37.50% | Completed |
| TC03 | HR Executive | 8.82% | Completed |
| TC04 | Sales Executive | 62.86% | Completed |
| TC05 | Graduate Data Analyst — mismatch test | 15.56% | Completed |
| TC06 | Data Analyst — mismatch test | 38.24% | Completed |
| TC07 | Senior Data Analyst | 18.60% | Completed |
| TC08 | Senior HR Manager | 10.26% | Completed |
| TC09 | Business Intelligence Analyst | 45.00% | Completed |
| TC10 | Machine Learning Engineer | 15.38% | Completed |

## 4. Observations

- All 10 scoring jobs completed successfully.
- TC04 recorded the highest match score at 62.86%.
- TC03 recorded the lowest match score at 8.82%.
- The test cases covered technical roles, non-technical roles, entry-level profiles, senior profiles, and mismatched resume scenarios.
- The baseline matching approach may count common words as matches and may fail to recognize relevant skills accurately.
- Match scores represent the current baseline output