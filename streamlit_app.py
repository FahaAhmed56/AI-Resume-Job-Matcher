import streamlit as st
from app.matcher import calculate_match

st.set_page_config(page_title="AI Resume & Job Matcher", page_icon="🤖", layout="wide")
st.title("🤖 AI Resume & Job Matcher")
st.caption("Explainable NLP matching using TF-IDF, cosine similarity, and skill overlap.")

resume_default = """Software Engineering student and Python developer with experience building machine learning applications and REST APIs. Skilled in Python, scikit-learn, pandas, FastAPI, SQL, Git, GitHub, React, and Firebase. Built NLP and predictive analytics projects and enjoy developing practical AI solutions."""
job_default = """We are looking for a Junior AI/ML Engineer with Python experience. The candidate should understand machine learning and NLP, build REST APIs using FastAPI, work with SQL databases, use Git/GitHub, and be comfortable with Docker. Experience with React is a plus."""

c1, c2 = st.columns(2)
with c1:
    resume = st.text_area("📄 Resume", resume_default, height=320)
with c2:
    job = st.text_area("💼 Job Description", job_default, height=320)

if st.button("🚀 Analyze Match", type="primary", use_container_width=True):
    try:
        result = calculate_match(resume, job)
        st.divider(); st.subheader("Match Analysis")
        a, b, c = st.columns(3)
        a.metric("Overall Match", f"{result.match_score:.1f}%")
        b.metric("Text Similarity", f"{result.text_similarity:.1f}%")
        c.metric("Skill Match", f"{result.skill_match:.1f}%")
        st.progress(min(result.match_score / 100, 1.0))
        left, right = st.columns(2)
        with left:
            st.markdown("### ✅ Matched Skills")
            for skill in result.matched_skills or ["None detected"]: st.write(f"• {skill}")
        with right:
            st.markdown("### ⚠️ Missing Skills")
            for skill in result.missing_skills or ["None detected"]: st.write(f"• {skill}")
        st.markdown("### How the score is calculated")
        st.write("70% comes from TF-IDF text similarity and 30% from overlap between detected job and resume skills.")
    except ValueError as exc:
        st.error(str(exc))
