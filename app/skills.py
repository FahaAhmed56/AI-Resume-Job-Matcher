import re

SKILLS = [
    "python", "java", "javascript", "typescript", "c++", "c#", "go", "rust",
    "react", "next.js", "node.js", "express", "django", "flask", "fastapi",
    "streamlit", "flutter", "dart", "html", "css", "tailwind", "bootstrap",
    "sql", "mysql", "postgresql", "mongodb", "redis", "firebase",
    "machine learning", "deep learning", "natural language processing", "nlp",
    "computer vision", "artificial intelligence", "ai", "scikit-learn", "pandas",
    "numpy", "pytorch", "tensorflow", "transformers", "hugging face", "llm", "rag",
    "openai", "git", "github", "docker", "kubernetes", "aws", "azure", "gcp",
    "rest api", "graphql", "linux", "ci/cd", "power bi", "tableau", "data analysis",
    "data visualization", "statistics", "excel", "agile", "scrum", "testing", "pytest"
]

def extract_skills(text: str) -> list[str]:
    normalized = text.lower()
    return [s for s in SKILLS if re.search(rf"(?<!\w){re.escape(s)}(?!\w)", normalized)]
