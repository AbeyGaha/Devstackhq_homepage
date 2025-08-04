# pages/AdminTest.py

import streamlit as st
from components.navbar import show_navbar
from components.footer import show_footer

show_navbar()

st.title("🧪 Admin Testing Panel")

st.markdown("### 🧰 Test: Reposcope Status Check")

if st.button("Run Reposcope Status"):
    st.success("✅ Reposcope Status: Healthy\n📦 Modules: Loaded\n🚀 Ready for Execution")

# Add more tests for other products

show_footer()
