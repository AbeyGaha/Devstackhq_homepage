import streamlit as st
import smtplib
from email.mime.text import MIMEText

# -------- Email Sender Function --------
def send_email(name, email, subject, message):
    config = st.secrets["email"]
    contact = st.secrets["contact_form"]

    msg = MIMEText(
        f"New Contact Form Submission\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}"
    )
    msg["Subject"] = f"📩 New Message from {name}: {subject}"
    msg["From"] = config["sender"]
    msg["To"] = contact["recipient"]

    with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as server:
        if config.get("use_tls", True):
            server.starttls()
        server.login(config["sender"], config["password"])
        server.send_message(msg)

# -------- Streamlit Page --------
def contact_us_page():
    st.set_page_config(page_title="Contact Us - DevStackHQ", layout="wide")

    st.markdown("""
    <style>
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    :root {
        --primary: #667eea; --secondary: #764ba2; --accent: #FF4B4B;
        --light: #f8f9fa; --dark: #343a40;
    }
    body { background-color: #f5f5f5; color: #333; line-height: 1.6; }
    .main-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        color: white; padding: 20px; border-radius: 10px;
        text-align: center; margin: 20px 0;
    }
    .main-header h1 { font-size: 36px; margin: 0; }
    .content-section {
        background: white; padding: 2rem; border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 2rem;
    }
    .section-title { color: var(--dark); margin-bottom: 1.5rem;
        border-left: 4px solid var(--primary); padding-left: 1rem; }
    .contact-item { margin-bottom: 1rem; padding: 1rem;
        background: var(--light); border-radius: 8px; }
    .submit-btn {
        background: var(--accent); color: white; border: none;
        padding: 1rem 2rem; border-radius: 5px; cursor: pointer;
        font-size: 1rem; font-weight: bold;
    }
    .submit-btn:hover { background: #e53c3c; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-header"><h1>📞 Contact Us</h1><p>We\'d love to hear from you!</p></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📧 Active Email Addresses")
        st.info("**Technical Support:** support@devstackhq.com\n\nAvailable 24/7 for technical issues.")
        st.info("**Sales & Business:** sales@devstackhq.com\n\nFor product inquiries and partnerships.")
        st.info("**General Inquiries:** contact@devstackhq.com\n\nFor general questions and information.")
        st.info("**Privacy & Legal:** privacy@devstackhq.com\n\nFor data protection and privacy concerns.")
        st.markdown("### 📞 Phone Support")
        st.success("Customer Support: +91-9873171180\n\nBusiness Inquiries: +91-9540342222")
        st.markdown("### 🏢 Office Address")
        st.markdown("DevStackHQ Solutions  \nSD-121, Sector-45, Noida  \nGautam Budh Nagar, UP-201303  \nIndia")

    with col2:
        st.markdown("### 📝 Contact Form")
        with st.form("contact_form"):
            name = st.text_input("Full Name *")
            email = st.text_input("Email Address *")
            subject = st.selectbox("Subject *", ["", "General Inquiry", "Technical Support", "Sales", "Partnership", "Privacy Concern", "Other"])
            message = st.text_area("Message *")
            submitted = st.form_submit_button("Send Message")

            if submitted:
                if name and email and subject and message:
                    try:
                        send_email(name, email, subject, message)
                        st.success("✅ Thank you! Your message has been sent successfully. We'll respond within 24 hours.")
                    except Exception as e:
                        st.error(f"❌ Failed to send message: {e}")
                else:
                    st.error("❌ Please fill all required fields.")

    st.markdown("### 🕒 Business Hours")
    st.write("""
    - **Monday - Friday:** 9:00 AM - 6:00 PM IST  
    - **Saturday:** 10:00 AM - 2:00 PM IST  
    - **Sunday:** Closed
    """)

    st.markdown("### ⚡ Emergency Technical Support")
    st.warning("For critical system issues, our technical support is available 24/7:\n\n📧 support@devstackhq.com | 📞 +91-9873171180")

    st.markdown("### 🔒 Response Time Commitment")
    st.write("""
    - **Technical Support:** Within 2 hours (24/7)  
    - **Sales Inquiries:** Within 4 business hours  
    - **General Questions:** Within 24 hours  
    - **Privacy Concerns:** Within 48 hours
    """)

# Run if standalone
if __name__ == "__main__":
    contact_us_page()
