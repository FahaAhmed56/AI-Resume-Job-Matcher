from fastapi import FastAPI, HTTPException
from app.matcher import calculate_match
from app.schemas import MatchRequest, MatchResponse

app = FastAPI(title="AI Resume & Job Matcher API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "AI Resume & Job Matcher API", "docs": "/docs", "endpoint": "POST /match"}

@app.post("/match", response_model=MatchResponse)
def match_resume(request: MatchRequest):
    try:
        result = calculate_match(request.resume, request.job_description)
        return MatchResponse(match_score=result.match_score, text_similarity=result.text_similarity,
                              skill_match=result.skill_match, matched_skills=result.matched_skills,
                              missing_skills=result.missing_skills)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
