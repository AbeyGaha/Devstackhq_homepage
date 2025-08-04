import streamlit as st

def show_footer():
    st.markdown("""
    <hr style="margin-top: 3rem;">
    <div style='text-align: center; color: gray; font-size: 14px;'>
        &copy; 2025 DevStackHQ. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
