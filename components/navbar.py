import streamlit as st

def show_navbar():
    st.markdown("""
    <style>
    .nav-container {
        background-color: #f8f9fa;
        padding: 0.8rem 2rem;
        border-bottom: 1px solid #dee2e6;
    }
    .nav-container a {
        margin-right: 20px;
        text-decoration: none;
        color: #2C3E50;
        font-weight: bold;
    }
    </style>
    <div class="nav-container">
        <a href="/">Home</a>
        <a href="/About">About</a>
        <a href="/Product">Products</a>
        <a href="/Contact">Contact</a>
        <a href="/AdminTest">Admin</a>
    </div>
    """, unsafe_allow_html=True)
