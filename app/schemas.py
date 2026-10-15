from pydantic import BaseModel, Field

class MatchRequest(BaseModel):
    resume: str = Field(..., min_length=10)
    job_description: str = Field(..., min_length=10)

class MatchResponse(BaseModel):
    match_score: float
    text_similarity: float
    skill_match: float
    matched_skills: list[str]
    missing_skills: list[str]
