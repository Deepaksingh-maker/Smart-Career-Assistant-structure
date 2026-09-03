import streamlit as st

def flow(items):
    st.markdown('<div class="flow">' + ''.join(f'<span>{item}</span><b>→</b>' if index < len(items) - 1 else f'<span>{item}</span>' for index, item in enumerate(items)) + '</div>', unsafe_allow_html=True)

def architecture():
    st.graphviz_chart('''digraph { rankdir=TB; graph [bgcolor="transparent", pad="0.2"]; node [shape=box, style="rounded,filled", fontname="Arial", color="#cbd5e1", fillcolor="#ffffff"]; edge [color="#0f766e", penwidth=2]; user [label="User", fillcolor="#ccfbf1"]; frontend [label="Next.js / React"]; backend [label="FastAPI"]; ai [label="AI Agent Layer", fillcolor="#fef3c7"]; agents [label="Resume • Interview • Portfolio\nRoadmap • Career Analysis", shape=note]; data [label="PostgreSQL • Redis • Qdrant", fillcolor="#e0e7ff"]; apis [label="External AI APIs", fillcolor="#fce7f3"]; user -> frontend -> backend -> ai -> data; ai -> agents [dir=both]; ai -> apis [dir=both]; }''')

def er_diagram():
    st.graphviz_chart('''digraph { rankdir=LR; graph [bgcolor="transparent"]; node [shape=box, style="rounded,filled", fontname="Arial", fillcolor="#ffffff", color="#cbd5e1"]; edge [color="#0f766e", penwidth=1.5]; users [label="USERS", fillcolor="#ccfbf1"]; resumes [label="RESUMES"]; analysis [label="RESUME_ANALYSIS"]; interviews [label="INTERVIEWS"]; questions [label="INTERVIEW_QUESTIONS"]; portfolios [label="PORTFOLIOS"]; roadmaps [label="CAREER_ROADMAPS"]; tasks [label="LEARNING_TASKS"]; skills [label="SKILLS"]; user_skills [label="USER_SKILLS"]; analytics [label="ANALYTICS"]; users -> resumes; resumes -> analysis; users -> interviews; interviews -> questions; users -> portfolios; users -> roadmaps; roadmaps -> tasks; users -> user_skills; user_skills -> skills; users -> analytics; }''')