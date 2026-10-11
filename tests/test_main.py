
from parsers.resume_extractor import clean_text


def test_zecpath_system():
    assert True


def test_clean_text_removes_extra_spaces():
    assert clean_text("  Geethika   K  ") == "Geethika K"


def test_clean_text_removes_excessive_blank_lines():
    assert clean_text("Skills: Python\n\n\n\nExperience: 2 years") == (
        "Skills: Python\nExperience: 2 years"
    )


def test_clean_text_normalizes_bullets():
    assert clean_text("• Python\n▪ SQL") == "- Python\n- SQL"


def test_clean_text_handles_windows_line_endings():
    assert clean_text("Python\t\tSQL\r\nPower BI") == "Python SQL\nPower BI"
