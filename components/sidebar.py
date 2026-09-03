import streamlit as st

def render():
    with st.sidebar:
        st.markdown("<div class='brand-mark'>SCA</div>", unsafe_allow_html=True)
        st.markdown("# Smart Career Assistant")
        st.caption("CAPSTONE DOCUMENTATION / 2026")
        st.divider()
        return st.radio("Navigate", ["Overview", "SDLC", "Feasibility Study", "Requirements", "Data Dictionary"], label_visibility="collapsed")
