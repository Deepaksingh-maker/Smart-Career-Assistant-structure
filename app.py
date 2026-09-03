import pandas as pd
import plotly.express as px
import streamlit as st
from components.cards import metric_row, phase_card
from components.diagrams import architecture, er_diagram, flow
from components.sidebar import render
from components.tables import searchable_table
from data.data_dictionary import TABLES
from data.feasibility import COSTS, SCHEDULE, TECHNICAL
from data.requirements import FUNCTIONAL, NON_FUNCTIONAL, TRACEABILITY
from data.sdlc import DEVELOPMENT_MODULES, SDLC_PHASES

st.set_page_config(page_title="Smart Career Assistant | Documentation", page_icon="✦", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --ink:#17212b; --muted:#64748b; --teal:#0f766e; --mint:#ccfbf1; --line:#dbe5e2; --paper:#f7faf9; }
.stApp { background:var(--paper); color:var(--ink); font-family:'DM Sans', sans-serif; }
h1,h2,h3 { font-family:'Space Grotesk', sans-serif; letter-spacing:0; }
h1 { font-size:2.5rem; } h2 { margin-top:1.5rem; }
[data-testid="stSidebar"] { background:#173f3b; }
[data-testid="stSidebar"] * { color:#ecfdf5; }
.brand-mark { width:44px; height:44px; display:grid; place-items:center; background:#fbbf24; color:#173f3b; font-family:'Space Grotesk'; font-weight:700; border-radius:10px; margin-bottom:1rem; }
.eyebrow { color:var(--teal); font-weight:700; letter-spacing:.12em; font-size:.75rem; text-transform:uppercase; }
.hero { border-bottom:1px solid var(--line); padding:1rem 0 2rem; margin-bottom:1.5rem; }
.hero p { color:var(--muted); font-size:1.1rem; }
.flow { display:flex; align-items:center; gap:.5rem; overflow-x:auto; padding:1.25rem 0 1.75rem; }
.flow span { white-space:nowrap; background:white; border:1px solid var(--line); padding:.65rem .85rem; border-radius:6px; font-weight:600; }
.flow b { color:var(--teal); }
.stMetric { background:white; border:1px solid var(--line); border-radius:6px; padding:.75rem; }
div[data-testid="stExpander"] { background:white; border:1px solid var(--line); border-radius:6px; margin-bottom:.5rem; }
</style>
""", unsafe_allow_html=True)

page = render()
if page == "Overview":
    st.markdown("<div class='hero'><div class='eyebrow'>Capstone project / documentation viewer</div><h1>Smart Career Assistant</h1><p>AI-Powered Career Development Platform</p></div>", unsafe_allow_html=True)
    metric_row([("SDLC phases", "8"), ("Feasibility areas", "5"), ("Functional reqs", "16"), ("Non-functional", "10"), ("Database tables", "11"), ("Core modules", "7+")])
    st.subheader("Project at a glance")
    left, right = st.columns([1.2, 1])
    with left:
        st.markdown("### A structured path from idea to operation")
        st.write("A faculty-friendly view of the engineering decisions, requirements, architecture, and data model behind the Smart Career Assistant.")
        flow(["Planning", "Feasibility", "Requirements", "Design", "Development", "Testing", "Deployment", "Maintenance"])
    with right:
        st.markdown("### Project profile")
        profile = {"Project type": "Capstone project", "Architecture": "AI + Web Application", "Frontend": "Next.js + React", "Backend": "FastAPI", "Database": "PostgreSQL", "AI": "Multi-Agent AI"}
        st.dataframe(pd.DataFrame(profile.items(), columns=["Attribute", "Decision"]), hide_index=True, use_container_width=True)
    st.subheader("Development flow")
    chart = pd.DataFrame({"Phase": [p["name"] for p in SDLC_PHASES], "Sequence": range(1, 9), "Status": ["Defined"] * 8})
    st.plotly_chart(px.bar(chart, x="Phase", y="Sequence", color="Status", color_discrete_sequence=["#0f766e"], title="SDLC phases documented in sequence"), use_container_width=True, config={"displayModeBar": False})
elif page == "SDLC":
    st.markdown("<div class='eyebrow'>01 / Engineering lifecycle</div><h1>Software Development Life Cycle</h1>", unsafe_allow_html=True)
    flow([p["name"] for p in SDLC_PHASES])
    for phase in SDLC_PHASES: phase_card(phase)
    st.subheader("System architecture")
    architecture()
    st.subheader("Development modules")
    st.dataframe(pd.DataFrame(DEVELOPMENT_MODULES, columns=["Module", "Objective"]), hide_index=True, use_container_width=True)
    st.subheader("Testing workflow")
    flow(["Unit Test", "Integration Test", "API Test", "System Test", "UAT", "Bug Fix", "Regression Test"])
elif page == "Feasibility Study":
    st.markdown("<div class='eyebrow'>02 / Decision support</div><h1>Feasibility Study</h1>", unsafe_allow_html=True)
    st.write("Feasibility determines whether the project can realistically be developed with available time, skills, technology, and budget.")
    tabs = st.tabs(["Technical", "Economic", "Operational", "Schedule", "Legal & Security"])
    with tabs[0]: st.dataframe(pd.DataFrame(TECHNICAL), hide_index=True, use_container_width=True); st.info("Technically feasible. Required hardware, software, skills, and AI/API dependencies remain configurable.")
    with tabs[1]:
        cost_frame = pd.DataFrame(COSTS); st.dataframe(cost_frame.drop(columns="Value"), hide_index=True, use_container_width=True); st.plotly_chart(px.bar(cost_frame, x="Category", y="Value", color="Type", title="Estimated cost categories (configurable)"), use_container_width=True, config={"displayModeBar": False}); st.info("Economically feasible for a student capstone if free/student tiers are used during development. Costs are estimates, not commitments.")
    with tabs[2]: st.markdown("**User workflow**"); flow(["Register", "Create Profile", "Upload Resume", "Analyze Resume", "Practice Interview", "Identify Skill Gaps", "Generate Roadmap", "Track Skills", "Build Portfolio", "View Analytics"]); st.info("Operationally feasible. The workflow is designed for guided, self-service use with minimal training.")
    with tabs[3]:
        st.data_editor(pd.DataFrame({"Phase": SCHEDULE, "Duration": ["To be defined"] * len(SCHEDULE)}), hide_index=True, use_container_width=True, num_rows="fixed"); st.caption("Schedule durations are intentionally configurable; no fixed project duration is assumed.")
    with tabs[4]: st.markdown("**Controls to implement:** personal information handling, resume and upload protection, authentication and authorization, encryption, secure API keys, HTTPS, deletion workflows, and privacy review."); st.info("Feasible if appropriate security and privacy controls are implemented.")
elif page == "Requirements":
    st.markdown("<div class='eyebrow'>03 / Product contract</div><h1>Requirements</h1>", unsafe_allow_html=True)
    tabs = st.tabs(["Functional", "Non-functional", "Traceability"])
    with tabs[0]: searchable_table(FUNCTIONAL, ["ID", "Category", "Requirement"], "functional_search")
    with tabs[1]:
        selected = st.multiselect("Filter categories", sorted({item[1] for item in NON_FUNCTIONAL}), default=[]); rows = [item for item in NON_FUNCTIONAL if not selected or item[1] in selected]; searchable_table(rows, ["ID", "Category", "Requirement"], "nfr_search")
    with tabs[2]: searchable_table(TRACEABILITY, ["Requirement", "Module", "Database Table", "SDLC Phase", "Testing Type"], "trace_search")
else:
    st.markdown("<div class='eyebrow'>04 / Persistence model</div><h1>Data Dictionary</h1>", unsafe_allow_html=True)
    st.caption("Database: PostgreSQL")
    table_name = st.selectbox("Select a table", list(TABLES))
    table = TABLES[table_name]; st.markdown(f"### `{table_name}`"); st.write(table["purpose"]); metric_row([("Primary key", table["pk"]), ("Foreign keys", table["fks"])])
    st.dataframe(pd.DataFrame(table["fields"], columns=["Field Name", "Data Type", "Size", "Key", "Nullable", "Default", "Description"]), hide_index=True, use_container_width=True)
    with st.expander("View relationship diagram"): er_diagram()
