import streamlit as st
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd
import altair as alt

# 1. Page Config
st.set_page_config(page_title="Protein Tool", page_icon="🥩")

st.title("🥩 Protein Physicochemical Analyzer")
st.markdown("Calculate molecular weight, instability index, and amino acid composition.")

# 2. Input
seq_input = st.text_area("Enter Protein Sequence (Single letter code):", height=150, placeholder="MVLSPADKTNVKAAWGKVGAHAGEYGAE...")

# 3. Logic
if st.button("Analyze Protein"):
    if seq_input:
        # Clean input (Remove whitespace, newlines, and ensure upper case)
        clean_seq = "".join(seq_input.split()).upper()
        
        # Check for non-protein characters
        valid_aas = set("ACDEFGHIKLMNPQRSTVWY")
        if not set(clean_seq).issubset(valid_aas):
            st.error("⚠️ Error: Invalid characters detected. Please use standard amino acid codes.")
        else:
            # Run Analysis
            analysed_seq = ProteinAnalysis(clean_seq)
            
            # --- METRICS ROW ---
            st.success("Analysis Complete!")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                mw = analysed_seq.molecular_weight()
                st.metric("Molecular Weight", f"{mw/1000:.2f} kDa")
            
            with col2:
                # Isoelectric Point
                pi = analysed_seq.isoelectric_point()
                st.metric("Isoelectric Point (pI)", f"{pi:.2f}")
                
            with col3:
                # Instability Index (>40 is unstable)
                instability = analysed_seq.instability_index()
                status = "Stable" if instability <= 40 else "Unstable"
                st.metric("Stability", status, delta=f"{instability:.2f}", delta_color="inverse")

            st.markdown("---")

            # --- AMINO ACID COMPOSITION CHART ---
            st.subheader("🧬 Amino Acid Composition")
            
            # Get count and prepare data for chart
            aa_count = analysed_seq.count_amino_acids()
            df = pd.DataFrame(list(aa_count.items()), columns=["Amino Acid", "Count"])
            
            # Create Bar Chart using Altair (Built-in to Streamlit)
            chart = alt.Chart(df).mark_bar().encode(
                x='Amino Acid',
                y='Count',
                color='Amino Acid',
                tooltip=['Amino Acid', 'Count']
            ).interactive()
            
            st.altair_chart(chart, use_container_width=True)

            # --- EXTRA DETAILS ---
            with st.expander("See Molar Extinction Coefficient"):
                sec_struct = analysed_seq.secondary_structure_fraction()
                epsilon = analysed_seq.molar_extinction_coefficient()
                st.write(f"**Reduced (cysteines):** {epsilon[0]}")
                st.write(f"**Oxidized (cystines):** {epsilon[1]}")
                
    else:
        st.warning("Please enter a protein sequence.")
