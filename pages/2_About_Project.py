import streamlit as st

from utils import setup_page
setup_page()

# st.set_page_config(page_title="About Project")

st.title("👨‍🚀 About Project")

st.markdown("""
Hi, I'm **Aniket Mishra** — a 3rd-year BS-MS student at IISER Kolkata,  
passionate about stars among other things. This is a project site, to know more about me visit my [Personal Website](https://madsc1ent1st96.github.io/)

This project, *Stellar Evolution Atlas*, is an effort to archive and visualize 
the life stories of stars through MESA simulations.

The primary focus is on understanding stellar behavior through **Hertzsprung–Russell** (HR) diagrams by varying stellar **mass** and **metallicity**. Alongside HR diagrams, this study explores key evolutionary indicators such as **core temperature versus core density** (Tc vs 𝜌c), **age versus radius**, **age versus luminosity**, and **central hydrogen fraction versus time**. These visualizations and analyses collectively provide insights into the internal structure, fusion processes, and life cycles of stars. A detailed explanation of the methodology, results, and interpretation is available in the **project report**.

---

### The project database is uploaded at Zenodo.
### Access it here

---

### 🔧 Tools I Used for this project:
- **MESA** (Modules for Experiments in Stellar Astrophysics) [*Stellar evolution simulation*]
- Astrophysics textbooks like *Prialnik* and *Carroll & Ostlie*
- **Python + Streamlit** [*Interface*]
- **FFMPEG** [*Video generation*]
- **Matplotlib**, **pandas**, **JSON** for *data visualization*
- **Numpy**, **Mesa_reader** and **above tools** for *plotting*
- **Bash Scripting** for *automation* 


---

### 📬 Contact Me:
- **Email**: mas23ms096@iiserkol.ac.in
- **Alt. Email**: aniket.mishra200510@gmail.com
- **GitHub**: [github.com/MadSc1ent1st96](https://github.com/MadSc1ent1st96)

""")
