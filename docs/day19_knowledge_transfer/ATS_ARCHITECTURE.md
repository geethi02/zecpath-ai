
# Zecpath AI — ATS Architecture Diagram

## 1. High-Level Architecture

```mermaid
flowchart TD
    A[Resume PDF or DOCX] --> B[Resume Text Extraction]
    J[Job Description] --> K[Job Description Parser]

    B --> C[Text Cleaning]
    C --> D[Skill Extraction]
    C --> E[Education Parsing]
    C --> F[Experience Parsing]

    D --> G[Candidate Information]
    E --> G
    F --> G

    K --> H[Job Requirements]
    G --> I[Semantic Matching and Scoring]
    H --> I

    I --> L[Candidate Ranking]
    L --> M[Shortlisting Results]
    M --> N[Human Review]

    O[Fairness and Score Normalization] -. Review or integration as configured .-> I
</mermaid>
```

## 2. Architecture Notes

- Resume extraction supports PDF and DOCX files.
- Text cleaning prepares extracted content for downstream processing.
- Skill, education, and experience modules identify candidate information.
- Job description parsing prepares job requirements.
- Matching and scoring compare candidate information against job requirements.
- Ranking modules can order candidates based on available scores.
- Fairness-related components require verification of their actual integration before being considered part of the live scoring path.
- Human review remains necessary; scores should not independently determine hiring outcomes.
