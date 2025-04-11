
import streamlit as st
from proposal_logic import generate_proposal

st.set_page_config(page_title="Momar AI Proposal Generator", layout="centered")

st.title("📄 Momar AI-Powered Sales Proposal Tool")
st.markdown("Auto-generate a tailored product proposal for any client situation.")

with st.form("proposal_form"):
    client_type = st.text_input("Client Type (e.g., Food Processing, Automotive)")
    issue = st.text_area("Maintenance Issue or Challenge")
    product = st.text_input("Recommended Product")
    usage_notes = st.text_area("Usage Instructions & Precautions")
    submitted = st.form_submit_button("Generate Proposal")

if submitted:
    proposal = generate_proposal(client_type, issue, product, usage_notes)
    st.markdown("---")
    st.markdown(proposal)
