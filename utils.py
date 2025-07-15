import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Home | Stellar Evolution Atlas",
        layout="centered",
        initial_sidebar_state="auto"
    )
    with st.sidebar:
        #st.image("assets/logo.png", width=150)  # Remove if no logo
        st.markdown("## 🔭 Navigation")
        st.markdown("Use the menu on the left to explore different views.")


