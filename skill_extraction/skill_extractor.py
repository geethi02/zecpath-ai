import json
import re
from pathlib import Path


class SkillExtractor:
    """Extract, normalize, and score skills from resume text."""

    def __init__(self, dictionary_path=None):
        if dictionary_path is None:
            dictionary_path = Path(__file__).parent / "skill_dictionary.json"

        self.dictionary_path = Path(dictionary_path)
        self.skill_dictionary = self._load_dictionary()

    def _load_dictionary(self):
        """Load the master skill dictionary."""
        with open(self.dictionary_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _normalize_text(self, text):
        """Normalize text for reliable skill matching."""

        text = text.lower()

        # Normalize common separators
        text = text.replace("-", " ")
        text = text.replace("_", " ")
        text = text.replace(".", "")

        # Normalize multiple spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def _get_skill_entries(self):
        """Return all skills from the dictionary."""

        skills = []

        technical = self.skill_dictionary.get("technical", {})

        for category, entries in technical.items():
            for entry in entries:
                skills.append({
                    "canonical": entry["canonical"],
                    "synonyms": entry["synonyms"],
                    "category": "technical",
                    "subcategory": category
                })

        for entry in self.skill_dictionary.get("business", []):
            skills.append({
                "canonical": entry["canonical"],
                "synonyms": entry["synonyms"],
                "category": "business",
                "subcategory": "business"
            })

        for entry in self.skill_dictionary.get("creative", []):
            skills.append({
                "canonical": entry["canonical"],
                "synonyms": entry["synonyms"],
                "category": "creative",
                "subcategory": "creative"
            })

        return skills

    def extract_skills(self, text):
        """Extract skills from resume text."""

        normalized_text = self._normalize_text(text)
        extracted_skills = []

        # ---------------------------------------------------------
        # 1. Skill stack detection
        # ---------------------------------------------------------

        skill_stacks = self.skill_dictionary.get("skill_stacks", {})

        for stack_name, stack_skills in skill_stacks.items():

            normalized_stack_name = self._normalize_text(stack_name)

            pattern = r"\b" + re.escape(normalized_stack_name) + r"\b"

            if re.search(pattern, normalized_text):

                for skill_name in stack_skills:

                    extracted_skills.append({
                        "name": skill_name,
                        "category": "technical",
                        "subcategory": "skill_stack",
                        "matched_as": stack_name,
                        "confidence": 0.85
                    })

        # ---------------------------------------------------------
        # 2. Individual skill detection
        # ---------------------------------------------------------

        for skill in self._get_skill_entries():

            for synonym in skill["synonyms"]:

                normalized_synonym = self._normalize_text(synonym)

                pattern = r"\b" + re.escape(normalized_synonym) + r"\b"

                if re.search(pattern, normalized_text):

                    if normalized_synonym == self._normalize_text(
                        skill["canonical"]
                    ):
                        confidence = 1.00
                    else:
                        confidence = 0.90

                    extracted_skills.append({
                        "name": skill["canonical"],
                        "category": skill["category"],
                        "subcategory": skill["subcategory"],
                        "matched_as": synonym,
                        "confidence": confidence
                    })

                    break

        return self._deduplicate(extracted_skills)

    def _deduplicate(self, skills):
        """Remove duplicate skills and keep the highest confidence."""

        unique_skills = {}

        for skill in skills:

            key = skill["name"].lower()

            if key not in unique_skills:
                unique_skills[key] = skill

            else:
                if skill["confidence"] > unique_skills[key]["confidence"]:
                    unique_skills[key] = skill

        return list(unique_skills.values())

    def get_structured_output(self, text):
        """Return skills in structured format."""

        skills = self.extract_skills(text)

        technical_count = 0
        business_count = 0
        creative_count = 0

        for skill in skills:

            if skill["category"] == "technical":
                technical_count += 1

            elif skill["category"] == "business":
                business_count += 1

            elif skill["category"] == "creative":
                creative_count += 1

        return {
            "skills": skills,
            "total_skills": len(skills),
            "summary": {
                "technical": technical_count,
                "business": business_count,
                "creative": creative_count
            }
        }


if __name__ == "__main__":

    extractor = SkillExtractor()

    sample_resume = """
    Data Scientist with experience in Python,
    PowerBI, ReactJS, NodeJS, Scikit-learn,
    Num Py and Machine-Learning.
    """

    result = extractor.get_structured_output(sample_resume)

    print(json.dumps(result, indent=2))