import json
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from section_classifier.resume_section_classifier import (
    detect_section_heading,
)

def evaluate_section_accuracy():
    """
    Evaluate section heading detection using the labeled dataset.
    """

    file_path = "data/section_labeled/resume_section_labels.json"

    with open(file_path, "r", encoding="utf-8") as file:
        labeled_data = json.load(file)

    total = 0
    correct = 0

    print("Resume Section Detection Accuracy")
    print("-" * 50)

    for item in labeled_data:

        expected_section = item["section"]

        # The labeled samples contain section labels rather than
        # raw headings, so use representative headings for evaluation.
        heading_map = {
            "professional_summary": "Professional Summary",
            "skills": "Skills",
            "work_experience": "Work Experience",
            "education": "Education",
            "certifications": "Certifications",
            "projects": "Projects",
        }

        heading = heading_map.get(expected_section)

        if heading is None:
            continue

        predicted_section = detect_section_heading(heading)

        total += 1

        if predicted_section == expected_section:
            correct += 1

        print(
            f"Expected: {expected_section:<20} "
            f"Predicted: {predicted_section}"
        )

    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0

    print("-" * 50)
    print(f"Correct predictions: {correct}")
    print(f"Total predictions:   {total}")
    print(f"Accuracy:            {accuracy:.2f}%")


if __name__ == "__main__":
    evaluate_section_accuracy()