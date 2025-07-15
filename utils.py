import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Home | Stellar Evolution Atlas",
        layout="centered",
        initial_sidebar_state="auto"
    )
    _center_page_layout()
    with st.sidebar:
        st.markdown("## 🔭 Navigation")
        st.markdown("Use the menu on the left to explore different views.")

def _center_page_layout():
    st.markdown("""
        <style>
        @media (min-width: 768px) {
            .main .block-container {
                max-width: 700px;
                margin-left: auto;
                margin-right: auto;
                padding-top: 2rem;
            }
        }
        </style>
    """, unsafe_allow_html=True)
