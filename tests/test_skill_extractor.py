from skill_extraction.skill_extractor import SkillExtractor


def test_exact_skills():
    extractor = SkillExtractor()

    text = "I have experience in Python, SQL and Power BI."

    result = extractor.extract_skills(text)

    skill_names = [skill["name"] for skill in result]

    assert "Python" in skill_names
    assert "SQL" in skill_names
    assert "Power BI" in skill_names


def test_skill_variations():
    extractor = SkillExtractor()

    text = "Experience with Python, PowerBI, ReactJS and NodeJS."

    result = extractor.extract_skills(text)

    skill_names = [skill["name"] for skill in result]

    assert "Python" in skill_names
    assert "Power BI" in skill_names
    assert "React" in skill_names
    assert "Node.js" in skill_names


def test_mern_stack():
    extractor = SkillExtractor()

    text = "Developed applications using MERN stack."

    result = extractor.extract_skills(text)

    skill_names = [skill["name"] for skill in result]

    assert "MongoDB" in skill_names
    assert "Express.js" in skill_names
    assert "React" in skill_names
    assert "Node.js" in skill_names


def test_business_and_creative_skills():
    extractor = SkillExtractor()

    text = """
    Strong communication and problem solving skills.
    Experience in content writing and graphic design.
    """

    result = extractor.extract_skills(text)

    skill_names = [skill["name"] for skill in result]

    assert "Communication" in skill_names
    assert "Problem Solving" in skill_names
    assert "Content Writing" in skill_names
    assert "Graphic Design" in skill_names


def test_duplicate_skills():
    extractor = SkillExtractor()

    text = "Python Python Python and PYTHON."

    result = extractor.extract_skills(text)

    skill_names = [skill["name"] for skill in result]

    assert skill_names.count("Python") == 1


def test_no_skills():
    extractor = SkillExtractor()

    text = "I am a hardworking and motivated person."

    result = extractor.extract_skills(text)

    assert result == []