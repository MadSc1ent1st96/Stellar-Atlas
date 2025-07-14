import streamlit as st

from utils import setup_page
setup_page()

# st.set_page_config(page_title="Project Report")

st.title("📘 Project Report")
st.markdown("Download and read the full Stellar Atlas PDF below.")

# Download button
with open("assets/Stellar-Atlas-Final-Report.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📥 Download Atlas (PDF)",
                   data=PDFbyte,
                   file_name="Stellar-Atlas-Final-Report.pdf",
                   mime='application/pdf')

# Optionally display inside page
#st.markdown("### 📖 Preview")
#st.markdown("If you're using Chrome, you might be able to view the PDF below:")

#st.markdown("""
#<iframe src="https://docs.google.com/gview?url=https://yourdomain.com/assets/stellar_atlas.pdf&embedded=true" 
#        style="width:100%; height:600px;" frameborder="0"></iframe>
#""", unsafe_allow_html=True)
