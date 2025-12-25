import streamlit as st

# 1. Page Config (MUST be first)
st.set_page_config(
    page_title="Germiverse Tools",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="collapsed" 
)
# Note: "collapsed" on mobile is default. 
# Users must click the arrow (>) at top-left to see the menu.

# 2. Hide Branding (Corrected CSS)
# We removed 'header {visibility: hidden;}' so the Sidebar Arrow stays visible!
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Header
st.title("🔬 Germiverse Bio-Suite")
st.markdown("### Computational Tools for Biologists")
st.markdown("### Best viewed in Desktop, please turn on Desktop Mode if you are using Mobile")
st.markdown("---")

# 4. Introduction
st.info("👋 Welcome! Open the sidebar (top-left >) to select a tool.")

# 5. Tool Cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧬 DNA Analyzer")
    st.write("Perform essential operations on nucleotide sequences.")
    st.markdown("- GC Content Calculation")
    st.markdown("- Transcription (DNA -> RNA)")
    st.markdown("- Translation (DNA -> Protein)")
    
with col2:
    st.markdown("### 🥩 Protein Analyzer")
    st.write("Analyze physicochemical properties of protein sequences.")
    st.markdown("- Molecular Weight")
    st.markdown("- Isoelectric Point (pI)")
    st.markdown("- Amino Acid Composition Charts")

st.markdown("---")

# 6. Resources
st.markdown("#### 📚 Quick Resources")
st.markdown("""
* **NCBI BLAST:** [blast.ncbi.nlm.nih.gov](https://blast.ncbi.nlm.nih.gov/)
* **UniProt:** [uniprot.org](https://www.uniprot.org/)
* **PDB:** [rcsb.org](https://www.rcsb.org/)
""")

# 7. Sidebar Footer
st.sidebar.success("Select a tool above 👆")
st.sidebar.markdown("---")
st.sidebar.markdown("Developed for **Germiverse**")
