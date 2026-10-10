# Day 17 — ATS Accuracy Metrics

## 1. Objective

To evaluate the current Zecpath AI ATS scoring baseline and identify the additional validation required before reporting accuracy metrics.

## 2. Test Execution Metrics

| Metric | Result |
|---|---:|
| Total test cases executed | 10 |
| Scoring jobs completed | 10 |
| Scoring job completion rate | 100% |
| Highest observed match score | 62.86% |
| Lowest observed match score | 8.82% |

**Note:** The 100% completion rate refers only to successful completion of the 10 scoring jobs. It does not represent ATS accuracy.

## 3. Match Score Results

| Test Case | Match Score |
|---|---:|
| TC01 | 45.65% |
| TC02 | 37.50% |
| TC03 | 8.82% |
| TC04 | 62.86% |
| TC05 | 15.56% |
| TC06 | 38.24% |
| TC07 | 18.60% |
| TC08 | 10.26% |
| TC09 | 45.00% |
| TC10 | 15.38% |

## 4. Validation Status

| Evaluation Metric | Status |
|---|---|
| API execution completion rate | Measured |
| Resume-job relevance correctness | Requires manual review |
| Precision | Not yet calculated |
| Recall | Not yet calculated |
| F1-score | Not yet calculated |
| Validated ATS accuracy | Not yet established |

## 5. Why Further Validation Is Required

The current scoring method is `temporary_keyword_overlap_baseline`.

Keyword overlap may count common words as matches, miss equivalent skill names, and fail to understand context or experience level. Therefore, the match score must not be treated as a verified probability of candidate suitability.

## 6. Next Evaluation Steps

1. Manually review each resume against its corresponding job description.
2. Label each resume-job pair as relevant or not relevant using documented criteria.
3. Compare the manual labels with the system's predictions using a defined score threshold.
4. Calculate precision, recall, and F1-score from the verified labels and predictions.
5. Document false positives, false negatives, and improvement opportunities.

## 7. Conclusion

The initial API execution tests are complete, but the ATS matching quality has not yet been validated. Manual relevance assessment and prediction evaluation are required before reporting accuracy metrics.
