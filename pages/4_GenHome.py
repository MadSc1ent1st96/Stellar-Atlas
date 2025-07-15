import streamlit as st

from utils import setup_page
setup_page()

st.title("🌟 Stellar Evolution Atlas")
st.markdown("### Visualizing the Lives of Stars")

st.markdown("""
Welcome to the **Stellar Evolution Atlas** — a personal astrophysics project by **Aniket Mishra** *(BS-MS, IISER Kolkata)* that simulates and visualizes how stars evolve over time.

Leveraging tools like **MESA**, **FFmpeg**, **bash scripting**, and **Streamlit**, this project models stellar life cycles from pre-main-sequence to red giant phases for stars of varying masses and metallicities.

---

### 🧭 Explore the Atlas

- 🔭 **[Atlas](/Atlas)** — View stellar evolution plots and animations  
- 📘 **[Project Report](/Project_Report)** — Read the full scientific report  
- 👤 **[About Project](/About_Project)** — Learn about the background, tools, and author  

Use the **sidebar** or navigation tabs to get started.

---

### 🚀 Project Objectives

- Simulate stellar evolution using a range of masses and metallicities
- Build an interactive web atlas for plots, data, and videos
- Compare simulations with observational data (e.g., Gaia DR3)
- Share results for public learning, outreach, and scientific utility

---

### 📂 Data Access

The complete dataset (~1200 simulations) is hosted on Zenodo:  
📎 [View Dataset on Zenodo](https://doi.org/10.5281/zenodo.15571157)

---

> _"To understand stars is to glimpse the engines of the universe."_ ✨

""")

st.success("📌 Tip: Use the sidebar on the left to explore each section.")
