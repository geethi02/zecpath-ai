# Day 17 – ATS Test Cases

## Objective

Validate resume matching across different job roles and experience levels.

## Test Cases

| Test ID | Category       | Job Role                                   | Expected Result                                                                                |
| ------- | -------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| TC01    | Technical      | Entry-Level Data Analyst                   | Relevant Python, SQL, Excel, and Power BI skills should be recognized.                         |
| TC02    | Technical      | Junior Python Developer                    | Python-related skills should be recognized; unrelated skills should not receive undue credit.  |
| TC03    | Non-Technical  | HR Executive                               | HR, recruitment, communication, and coordination experience should be relevant.                |
| TC04    | Non-Technical  | Sales Executive                            | Sales, customer communication, negotiation, and target tracking should be relevant.            |
| TC05    | Fresher        | Graduate Data Analyst                      | Education, projects, internships, and relevant skills should be considered.                    |
| TC06    | Fresher        | Graduate without required technical skills | The system should not report strong relevance when essential skills are missing.               |
| TC07    | Senior Profile | Senior Data Analyst                        | Relevant experience, technical skills, and senior-level responsibilities should be recognized. |
| TC08    | Senior Profile | Senior HR Manager                          | HR leadership and management experience should be considered for the HR role.                  |

## Manual Review

For every test, record:

* Required skills in the job description
* Skills actually present in the resume
* ATS match score and matched/missing skills
* Manual assessment of relevance
* Mismatch or parsing errors

## Evaluation Rule

Do not assume a test passes simply because the API returns HTTP 200. Compare the actual output with the expected result and manual review.
