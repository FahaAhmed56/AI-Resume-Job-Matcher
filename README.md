# 🤖 AI Resume & Job Matcher

An explainable AI/NLP application that compares a resume with a job description and produces a match score, matched skills, missing skills, and text-similarity insights.

## Features
- TF-IDF + cosine-similarity NLP matching
- Skill extraction and explainable skill-gap analysis
- Weighted final score: 70% text similarity + 30% skill overlap
- Streamlit interactive dashboard
- FastAPI REST API with Swagger docs
- CLI prediction mode
- Unit tests and GitHub Actions CI
- No API key or paid service required

## How it works
1. Normalize resume and job text.
2. Extract known technical/professional skills.
3. Convert both documents to TF-IDF vectors.
4. Calculate cosine similarity.
5. Calculate required-skill overlap.
6. Combine both signals into an explainable score.

## Structure
```text
ai-resume-job-matcher/
├── app/                 # ML/NLP engine
├── api/                 # FastAPI service
├── tests/               # Pytest tests
├── data/                # Demo inputs
├── streamlit_app.py     # Web dashboard
├── predict.py           # CLI
├── requirements.txt
└── README.md
```

## Run on Windows
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Run the API
```powershell
uvicorn api.main:app --reload
```
Then open `http://127.0.0.1:8000/docs`.

## CLI
```powershell
python predict.py --resume data/sample_resume.txt --job data/sample_job.txt
```

## Tests
```powershell
pytest -q
```

## Example API JSON
```json
{
  "resume": "Python developer with machine learning, SQL and FastAPI experience.",
  "job_description": "Looking for a Python ML engineer with FastAPI, SQL and Docker."
}
```

## Portfolio value
This demonstrates NLP, feature extraction, similarity-based ML, explainable AI, Python architecture, REST APIs, Streamlit, testing, and CI/CD.

## Future improvements
Embeddings/Sentence Transformers, PDF/DOCX parsing, NER for education and experience, personalized skill recommendations, learned ranking models, and job-board integrations.

> This is a decision-support/demo project, not an automated hiring system.

## License
MIT
