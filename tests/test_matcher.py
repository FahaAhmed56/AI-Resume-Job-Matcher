import pytest
from app.matcher import calculate_match

def test_good_match_has_high_score():
    r = calculate_match("Python machine learning FastAPI SQL Git Docker", "Python machine learning engineer using FastAPI SQL Git Docker")
    assert r.match_score > 70
    assert "python" in r.matched_skills and "docker" in r.matched_skills

def test_missing_skill_is_reported():
    r = calculate_match("Python and SQL developer", "Python developer with SQL and Docker experience")
    assert "docker" in r.missing_skills

def test_empty_resume_rejected():
    with pytest.raises(ValueError): calculate_match("", "Python developer")

def test_empty_job_rejected():
    with pytest.raises(ValueError): calculate_match("Python developer", "")
