# Day 17 — ATS Improvement Backlog

## 1. Objective

Document the issues identified during ATS testing and prioritize improvements for future development.

## 2. Improvement Items

| ID | Issue / Improvement | Priority | Status |
|---|---|---|---|
| IMP-01 | Replace temporary keyword-overlap scoring with a more reliable matching approach. | High | Pending |
| IMP-02 | Exclude common words that do not represent skills or qualifications. | High | Pending |
| IMP-03 | Improve skill extraction to recognize relevant technical and non-technical skills. | High | Pending |
| IMP-04 | Support equivalent skill names and common variations. | Medium | Pending |
| IMP-05 | Consider job requirements, experience level, and education when calculating relevance. | High | Pending |
| IMP-06 | Establish manually reviewed resume-job relevance labels for evaluation. | High | Pending |
| IMP-07 | Add automated tests for false positives and false negatives. | High | Pending |
| IMP-08 | Calculate precision, recall, and F1-score after ground-truth validation. | Medium | Pending |
| IMP-09 | Document score interpretation and limitations in API responses. | Medium | Pending |
| IMP-10 | Retest all scenarios after scoring improvements. | Medium | Pending |

## 3. Priority Definitions

- **High:** Important for reliable matching and evaluation.
- **Medium:** Important for improving maintainability, transparency, and future validation.

## 4. Recommended Implementation Order

1. Establish manual relevance labels for the existing test cases.
2. Investigate common-word matches and missing relevant skills.
3. Improve text preprocessing and skill extraction.
4. Update the scoring method and add automated tests.
5. Evaluate the updated model using verified labels.
6. Record the results and rerun the 10 test scenarios.

## 5. Completion Criteria

An improvement should be marked complete only after implementation and appropriate testing. Accuracy metrics should be reported only after evaluation against manually verified labels.

## 6. Conclusion

Day 17 identified limitations in the temporary ATS scoring baseline and documented a prioritized improvement plan. These items are proposed future work and are not yet implemented.
