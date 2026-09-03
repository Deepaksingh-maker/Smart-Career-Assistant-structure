import streamlit as st

def metric_row(items):
    columns = st.columns(len(items))
    for column, (label, value) in zip(columns, items):
        column.metric(label, value)

def phase_card(phase):
    with st.expander(f"{phase['icon']}  {phase['name']}", expanded=phase["name"] == "Planning"):
        st.markdown(f"**Objective**  \n{phase['objective']}")
        left, right = st.columns(2)
        with left:
            st.markdown("**Activities**")
            st.markdown("\n".join(f"- {item}" for item in phase["activities"]))
            st.markdown(f"**Inputs**  \n{phase['inputs']}")
        with right:
            st.markdown("**Outputs**")
            st.markdown("\n".join(f"- {item}" for item in phase["outputs"]))
            st.markdown(f"**Deliverable**  \n{phase['deliverable']}")
        st.info(f"**Dependencies:** {phase['dependencies']}  \n**Definition of Done:** {phase['done']}")