# pages/Contact.py

import streamlit as st
import smtplib
from email.mime.text import MIMEText
from components.navbar import show_navbar
from components.footer import show_footer

show_navbar()

st.title("📬 Contact Us")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Send")

    if submitted:
        try:
            smtp_user = st.secrets["email"]
            smtp_pass = st.secrets["smtp_key"]

            msg = MIMEText(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
            msg["Subject"] = f"Contact Form - DevStackHQ"
            msg["From"] = smtp_user
            msg["To"] = "contact@devstackhq.com"

            server = smtplib.SMTP("smtp.mailersend.net", 587)
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
            server.quit()

            st.success("Message sent successfully!")
        except Exception as e:
            st.error(f"Failed to send message: {e}")

show_footer()
