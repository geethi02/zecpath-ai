# Zecpath AI - Resume Section Taxonomy

## 1. Purpose

This document defines the major resume sections that will be
identified by the Resume Section Segmentation module.

The section classifier will use these categories to organize
extracted resume text into meaningful blocks for downstream AI
processing.

---

## 2. Supported Resume Sections

The initial classifier will identify the following sections:

1. Skills
2. Work Experience
3. Education
4. Certifications
5. Projects

---

## 3. Skills

### Description

Contains technical skills, programming languages, tools,
technologies, databases, frameworks, and other professional skills.

### Common headings

- Skills
- Technical Skills
- Skills & Technologies
- Technical Expertise
- Core Skills
- Key Skills
- Technologies

### Example

    SKILLS

    Python
    SQL
    Power BI
    Excel
    Pandas
    NumPy

---

## 4. Work Experience

### Description

Contains professional employment history, internships, traineeships,
and other work-related experience.

### Common headings

- Work Experience
- Experience
- Professional Experience
- Employment History
- Career History
- Work History

### Example

    WORK EXPERIENCE

    Data Analyst
    ABC Company
    2025 - 2026

    Analyzed business data and created dashboards.

---

## 5. Education

### Description

Contains academic qualifications such as degrees, diplomas,
universities, colleges, and academic achievements.

### Common headings

- Education
- Educational Qualifications
- Academic Background
- Academic Qualifications
- Education Background

### Example

    EDUCATION

    MSc Data Science and Analytics
    Jain University

    BSc Mathematics
    Kannur University

---

## 6. Certifications

### Description

Contains professional certifications, online certifications,
training certificates, and completed certification programs.

### Common headings

- Certifications
- Certificates
- Professional Certifications
- Courses & Certifications
- Certifications & Training

### Example

    CERTIFICATIONS

    Python for Data Science
    Power BI Data Analyst
    SQL Certification

---

## 7. Projects

### Description

Contains academic, personal, professional, or portfolio projects.

### Common headings

- Projects
- Academic Projects
- Personal Projects
- Key Projects
- Project Experience
- Projects & Research

### Example

    PROJECTS

    Sales Analytics Dashboard

    Developed a Power BI dashboard to analyze sales
    performance and business KPIs.

---

## 8. Section Heading Variations

Resume section headings may appear in different formats.

Examples:

    WORK EXPERIENCE
    Work Experience
    Work experience:
    Professional Experience
    EXPERIENCE

The classifier should normalize heading text before classification.

Example:

    "WORK EXPERIENCE:" 
            |
            v
    normalized heading
            |
            v
    work_experience

---

## 9. Target Section Labels

The classifier will use standardized labels:

| Resume Section | Standard Label |
|---|---|
| Skills | skills |
| Work Experience | work_experience |
| Education | education |
| Certifications | certifications |
| Projects | projects |

---

## 10. Missing Sections

A resume may not contain every section.

For example, a resume may contain:

- Skills
- Education
- Projects

but no Certifications section.

The classifier should not create an empty section unless required
by the downstream data schema.

---

## 11. Section Detection Approach

The Resume Section Segmentation module will use two approaches:

### Rule-Based Detection

Rules will identify sections using:

- Known section headings
- Heading variations
- Keywords
- Text patterns
- Formatting cues when available

### NLP-Based Detection

NLP techniques may be used when:

- A heading is missing
- A heading is unusual
- The section content is ambiguous
- Resume formatting makes rule-based detection difficult

---

## 12. Output

Each extracted text block should be assigned a section label.

Example:

    {
      "section": "skills",
      "text": "Python, SQL, Power BI, Excel"
    }

Another example:

    {
      "section": "education",
      "text": "MSc Data Science and Analytics - Jain University"
    }

---

## 13. Future Considerations

The classifier should be designed so additional sections can be
added later.

Possible future sections include:

- Summary
- Objective
- Achievements
- Publications
- Awards
- Languages
- Interests
- References

These sections are outside the initial Day 8 classification scope.