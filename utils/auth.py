import streamlit as st

DEMO_USER = {"email": "admin@devstackhq.com", "password": "devstack123"}

def login_ui():
    st.sidebar.subheader("Sign in")
    email = st.sidebar.text_input("Email")
    pwd = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Sign in"):
        if email == DEMO_USER["email"] and pwd == DEMO_USER["password"]:
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.sidebar.error("Invalid credentials")

def logout():
    st.session_state.logged_in = False
    st.experimental_rerun()

def require_login(func):
    def wrapped(*args, **kwargs):
        if not st.session_state.get("logged_in", False):
            st.warning("Please log in.")
            return
        return func(*args, **kwargs)
    return wrapped
