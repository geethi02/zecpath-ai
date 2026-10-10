## Day 17 Priorities

### P0 — Critical

* Remove common words such as "and", "with", and "skills" from skill matching.
* Improve multi-word skill detection, including "object-oriented programming" and "data visualization".
* Match skills against the resume's extracted skills rather than every word in the job description.

### P1 — High

* Add role-specific skill dictionaries for Data Analyst, Python Developer, HR Executive, and Sales Executive roles.
* Evaluate fresh graduate and senior candidate profiles separately.
* Improve handling of equivalent skill names and abbreviations.

### P2 — Medium

* Create manually verified test labels.
* Calculate precision, recall, and F1 score.
* Add regression tests to ensure fixes do not break existing functionality.

### Completion Criteria

The ATS should correctly identify relevant and missing skills, avoid matching ordinary words, and produce metrics based on manually verified test results before its accuracy is claimed.
