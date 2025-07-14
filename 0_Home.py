import streamlit as st

# st.set_page_config(page_title="Home", layout="centered")

from utils import setup_page
setup_page()

st.title("🌟 Stellar Evolution Atlas")
st.markdown("### Visualizing the Lives of Stars")

st.markdown("""
Welcome to the **Stellar Evolution Atlas**, a personal astrophysics project by  
**Aniket Mishra** (BS-MS, IISER Kolkata) that simulates and visualizes how stars live, evolve, and die.

Using tools like **MESA**, **FFMPEG**, **Bash Scripting** and **Streamlit**, this project archives the life cycles of stars with different masses — from Sun-like stars to massive giants.

You can explore:
- 🔭 The [Atlas](./Atlas) — view stellar models, graphs, and evolution videos
- 👨‍🚀 [About Project](./About_Project) — learn more about the project and me
- 📘 [Project Report](./Project_Report) — access the full PDF report

---

### 🚀 Goals of the Project

- Simulate stellar evolution across mass ranges
- Build an accessible interface for data, videos, and metadata
- Compare simulated outputs with real astrophysical data
- Host the Atlas for peer learning and outreach


""")

st.success("Use the sidebar to explore the Site")
