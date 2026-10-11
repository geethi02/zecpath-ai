import json
import re
from pathlib import Path

# Folders
resume_folder = Path("data/structured")
jd_file = Path("data/job_descriptions/data_analyst.txt")


def normalize_text(text):
    """Convert text to lowercase and remove unnecessary characters."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


# Important skills/keywords for this Data Analyst JD
keywords = [
    "sql",
    "python",
    "power bi",
    "excel",
    "data cleaning",
    "data analysis",
    "data visualization",
    "statistics",
    "eda",
    "kpi",
    "dashboard",
    "reporting",
    "data validation",
    "exploratory analysis",
]


# Read Job Description
jd_text = jd_file.read_text(encoding="utf-8")
jd_text = normalize_text(jd_text)


# Find all structured resumes
resume_files = list(resume_folder.glob("*.json"))

results = []


for resume_file in resume_files:

    # Read JSON
    data = json.loads(
        resume_file.read_text(encoding="utf-8")
    )

    # Combine important resume fields
    resume_text = " ".join([
        data.get("summary", ""),
        " ".join(data.get("education", [])),
        " ".join(data.get("experience", [])),
        " ".join(data.get("skills", [])),
        " ".join(data.get("projects", [])),
        " ".join(data.get("certifications", [])),
    ])

    resume_text = normalize_text(resume_text)

    matched_keywords = []

    for keyword in keywords:
        if keyword in resume_text:
            matched_keywords.append(keyword)

    score = (
        len(matched_keywords) / len(keywords)
    ) * 100

    results.append({
        "resume": resume_file.stem,
        "match_score": round(score, 2),
        "matched_keywords": matched_keywords
    })


# Sort by match score
results.sort(
    key=lambda x: x["match_score"],
    reverse=True
)


# Display results
print("\n===== RESUME MATCHING RESULTS =====\n")

for rank, result in enumerate(results, start=1):

    print(
        f"{rank}. {result['resume']} "
        f"→ {result['match_score']}%"
    )

    print(
        "   Matched:",
        ", ".join(result["matched_keywords"])
    )

    print()


print("===================================")