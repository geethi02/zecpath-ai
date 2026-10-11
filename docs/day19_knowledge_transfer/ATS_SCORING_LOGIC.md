# Zecpath AI — ATS Scoring Logic

## 1. Purpose

The ATS scoring component evaluates how closely a candidate's resume matches a job description. The resulting score can help organize candidates for further review.

A score is a matching indicator, not a hiring decision.

## 2. Scoring Components

The project contains modules for the following areas:

- **Skill matching:** Identifies skills in candidate resumes and compares them with job requirements.
- **Experience relevance:** Evaluates work experience against relevant requirements.
- **Education relevance:** Processes academic information and its relevance.
- **Semantic matching:** Uses text embeddings and similarity methods to estimate how closely candidate information relates to job requirements.
- **Candidate scoring:** Combines scoring logic according to the implementation and configuration.
- **Candidate ranking:** Uses available scores to order candidates.

The exact contribution of each component must be confirmed by inspecting the implemented scoring functions and configuration.

## 3. Scoring Workflow

1. Extract and clean the resume text.
2. Parse the job description.
3. Extract candidate skills, education, and experience.
4. Prepare the candidate and job information for matching.
5. Calculate the scores supported by the configured scoring modules.
6. Apply the implemented score-combination logic, if configured.
7. Pass available scores to the ranking component.
8. Review the results before making decisions.

## 4. Interpreting Scores

A higher score may indicate a closer match under the configured scoring method. It does not guarantee that a candidate is qualified or will perform well.

Scores from different scoring methods should not be compared directly unless their scales and meanings have been validated.

## 5. Baseline ATS Scoring Results

The Day 17 baseline evaluation used 10 test cases. The scoring method was recorded as `temporary_keyword_overlap_baseline`.

Observed scores included:

| Test case | Scenario | Score |
|---|---|---:|
| TC01 | Entry-Level Data Analyst | 45.65% |
| TC02 | Junior Python Developer | 37.50% |
| TC03 | HR Executive | 8.82% |
| TC04 | Sales Executive | 62.86% |
| TC05 | Graduate Data Analyst mismatch | 15.56% |
| TC06 | Data Analyst mismatch | 38.24% |
| TC07 | Senior Data Analyst | 18.60% |
| TC08 | Senior HR Manager | 10.26% |
| TC09 | BI Analyst | 45.00% |
| TC10 | ML Engineer | 15.38% |

These results are baseline observations, not proof of ATS accuracy. In particular, the relatively high score for the Sales Executive test case demonstrates why scores need to be evaluated against the actual job requirements and manually reviewed labels.

## 6. Validation Requirements

Before using scores for consequential decisions:

- Create manually reviewed resume–job-description match labels.
- Test relevant matches and mismatches.
- Investigate false positives and false negatives.
- Measure appropriate evaluation metrics.
- Check score behaviour across different resume formats.
- Review fairness and potential sources of bias.
- Record scoring configuration and version changes.

Precision, recall, and accuracy should not be reported as validated metrics until the required ground-truth labels and evaluation procedure exist.

## 7. Troubleshooting

### Unexpectedly high scores
Check generic keywords, duplicate terms, and whether the scoring method accounts for job-specific requirements.

### Unexpectedly low scores
Check text extraction quality, skill dictionary coverage, missing job-description fields, and the score normalization method.

### Candidates appear in an unexpected order
Inspect the ranking input, sorting direction, missing scores, and tie-breaking behaviour.

### Scores change after a code update
Compare configuration versions, input text, preprocessing, and scoring functions.

## 8. Responsible Use

- Treat scores as decision-support information.
- Do not automatically reject candidates based only on a score.
- Review extracted information for errors.
- Protect candidate data.
- Document limitations and investigate potential bias.

## 9. Maintenance

Whenever scoring logic changes, update this document, add or update tests, and record the effect of the change on a fixed evaluation dataset.
