from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .skills import extract_skills

@dataclass
class MatchResult:
    match_score: float
    text_similarity: float
    skill_match: float
    matched_skills: list[str]
    missing_skills: list[str]

def _clean(text: str) -> str:
    return " ".join(text.lower().strip().split())

def calculate_match(resume: str, job_description: str) -> MatchResult:
    if not resume.strip():
        raise ValueError("Resume text cannot be empty.")
    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")
    resume_clean, job_clean = _clean(resume), _clean(job_description)
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), sublinear_tf=True)
    matrix = vectorizer.fit_transform([resume_clean, job_clean])
    text_similarity = float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100
    resume_skills, job_skills = set(extract_skills(resume)), set(extract_skills(job_description))
    matched, missing = sorted(resume_skills & job_skills), sorted(job_skills - resume_skills)
    skill_match = (len(matched) / len(job_skills) * 100) if job_skills else text_similarity
    final_score = 0.70 * text_similarity + 0.30 * skill_match
    return MatchResult(round(final_score, 2), round(text_similarity, 2), round(skill_match, 2), matched, missing)
