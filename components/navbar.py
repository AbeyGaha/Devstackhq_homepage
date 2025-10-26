import streamlit as st

def show_navbar():
    st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #f8f9fa;
        border-bottom: 1px solid #dee2e6;
    }
    .nav-links a {
        margin: 0 15px;
        text-decoration: none;
        color: #495057;
        font-weight: 500;
    }
    .nav-links a:hover {
        color: #007bff;
    }
    </style>

    <div class="navbar">
        <div class="nav-logo">
            <strong>DevStackHQ</strong>
        </div>
        <div class="nav-links">
            <a href="/" target="_self">Home</a>
            <a href="/About" target="_self">About</a>
            <a href="/Products" target="_self">Products</a>
            <a href="/Contact_Us" target="_self">Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
