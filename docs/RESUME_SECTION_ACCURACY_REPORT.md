# Zecpath AI - Resume Section Detection Accuracy Report

## 1. Purpose

This report evaluates the Resume Section Classifier developed
for Day 8 of the Zecpath AI project.

The classifier identifies common resume section headings and
segments resume text into standardized section labels.

---

## 2. Supported Sections

The classifier currently detects the following sections:

| Resume Section | Standard Label |
|---|---|
| Professional Summary | `professional_summary` |
| Skills | `skills` |
| Work Experience | `work_experience` |
| Education | `education` |
| Certifications | `certifications` |
| Projects | `projects` |

---

## 3. Detection Approach

The classifier uses a rule-based approach with a
content-based NLP fallback.

It identifies sections using:

- Common resume section headings
- Heading variations
- Text normalization
- Lowercase conversion
- Punctuation removal
- Whitespace normalization
- Section-specific heading patterns
- Content keywords when a heading is missing

Examples:

```text
SKILLS
Work Experience
EDUCATION:
Professional Summary