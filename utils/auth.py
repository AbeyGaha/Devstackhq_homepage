# utils/auth.py

import streamlit as st

def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["admin_password"]:
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Admin Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Admin Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Incorrect password")
        return False
    else:
        return True
