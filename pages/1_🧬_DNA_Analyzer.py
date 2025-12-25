import streamlit as st
from Bio.Seq import Seq

# 1. Configuration (Must be the first command)
st.set_page_config(page_title="Germiverse Lab", page_icon="🧬", layout="centered")

# 2. Custom CSS to hide Streamlit branding (Optional but looks cleaner)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. The App Layout
st.title("🧬 DNA Analysis Tool")
st.markdown("### Paste your raw sequence below:")

# 4. Input
seq_input = st.text_area("Sequence (ATGC...)", height=150)

# 5. Logic
if st.button("🚀 Analyze Sequence"):
    if seq_input:
        # Clean the input
        clean_seq = seq_input.replace("\n", "").replace(" ", "").upper()
        
        # Check for invalid characters
        if not all(c in "ATGCN" for c in clean_seq):
            st.error("⚠️ Error: Invalid characters detected. Please use only A, T, G, C, N.")
        else:
            dna = Seq(clean_seq)
            
            # Calculations
            gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
            rna = dna.transcribe()
            protein = dna.translate()

            # Display Results
            st.success("Analysis Complete!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Length", f"{len(dna)} bp")
            with col2:
                st.metric("GC Content", f"{gc:.2f}%")

            st.subheader("📝 Transcribed RNA")
            st.code(str(rna))

            st.subheader("🥩 Protein Translation")
            st.code(str(protein))
    else:
        st.warning("Please enter a DNA sequence first.")
