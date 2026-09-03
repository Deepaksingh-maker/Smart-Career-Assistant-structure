import pandas as pd
import streamlit as st

def searchable_table(rows, columns, key, placeholder="Search records"):
    query = st.text_input(placeholder, key=key).lower()
    frame = pd.DataFrame(rows, columns=columns)
    if query:
        frame = frame[frame.astype(str).apply(lambda row: row.str.lower().str.contains(query).any(), axis=1)]
    st.dataframe(frame, use_container_width=True, hide_index=True)
    st.caption(f"Showing {len(frame)} of {len(rows)} records")