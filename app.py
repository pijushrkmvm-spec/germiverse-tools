import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Germiverse Tools",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Header
st.title("🔬 Germiverse Bio-Suite")
st.markdown("### Advanced Computational Tools for Biologists")
st.markdown("---")

# 3. Introduction
st.info("👋 Welcome! Select a tool from the sidebar to begin your analysis.")

# 4. Tool Cards (Using Columns for layout)
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

# 5. Footer / Resources
st.markdown("#### 📚 Quick Resources")
st.markdown("""
* **NCBI BLAST:** [blast.ncbi.nlm.nih.gov](https://blast.ncbi.nlm.nih.gov/)
* **UniProt:** [uniprot.org](https://www.uniprot.org/)
* **PDB:** [rcsb.org](https://www.rcsb.org/)
""")

# 6. Sidebar Info
st.sidebar.success("Select a tool above 👆")
st.sidebar.markdown("---")
st.sidebar.markdown("Developed for **Germiverse**")
