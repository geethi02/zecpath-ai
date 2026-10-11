# Day 15 – Fairness, Normalization & Bias Reduction

## Objective

Improve fairness, reduce dependence on non-essential personal information,
and standardize resume evaluation.

## 1. Resume Normalization

The Resume Normalizer converts resume content into a standard structure:

- Summary
- Skills
- Experience
- Education
- Projects
- Certifications

Text formatting is cleaned so that resumes with different formatting
can be processed consistently.

## 2. Score Normalization

The Score Normalizer converts candidate scores into a standard 0–100 range.

Min-max normalization is used to standardize scores within a candidate
score group.

## 3. Personal Attribute Masking

The Attribute Masker removes or masks non-essential personal attributes
before evaluation.

The system can mask:

- Name
- Email
- Phone number
- Date of birth
- Gender
- Address

This helps the scoring process focus more on job-relevant information.

## 4. Bias Indicator Evaluation

The Bias Evaluator checks whether potentially sensitive or non-essential
personal attributes are present in resume content.

Detected indicators can trigger a recommendation to apply attribute masking.

## 5. Fairness Report

The Fairness Report combines:

- Resume standardization
- Bias indicator detection
- Attribute masking status

It produces a recruiter-friendly summary of the fairness checks.

## 6. Fair Scoring Improvements

The Day 15 improvements help make evaluation more consistent by:

- Standardizing resume structure
- Reducing reliance on personal attributes
- Normalizing numerical scores
- Detecting potential bias indicators
- Keeping evaluation focused on job-relevant information

## Important Limitation

These mechanisms reduce some identifiable sources of bias, but they do not
prove that the ATS is completely unbiased.

Fairness should be evaluated using representative candidate datasets,
group-level outcome analysis, and periodic monitoring.