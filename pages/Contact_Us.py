import streamlit as st

st.set_page_config(page_title="Contact Us - DevStackHQ", page_icon="📞")

st.markdown("# 📞 Contact Us")
st.markdown("### We'd love to hear from you!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### 📧 Active Email Addresses
    
    **Technical Support:** support@devstackhq.com  
    *Available 24/7 for technical issues*
    
    **Sales & Business:** sales@devstackhq.com  
    *For product inquiries and partnerships*
    
    **General Inquiries:** contact@devstackhq.com  
    *For general questions and information*
    
    **Privacy & Legal:** privacy@devstackhq.com  
    *For data protection and privacy concerns*
    
    #### 📞 Phone Support
    **Customer Support:** +91-9873171180 
    **Business Inquiries:** +91-9540342222
    
    #### 🏢 Office Address
    DevStackHQ Solutions  
    SD-121, Sector-45, Noida  
    Gautam Budh Nagar, UP-201303  
    India
    """)

with col2:
    st.markdown("#### 📝 Contact Form")
    with st.form("contact_form"):
        name = st.text_input("Full Name*")
        email = st.text_input("Email Address*")
        subject = st.selectbox("Subject*", 
            ["General Inquiry", "Technical Support", "Sales", "Partnership", "Privacy Concern", "Other"])
        message = st.text_area("Message*", height=150)
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you! Your message has been sent successfully. We'll respond within 24 hours.")
            else:
                st.error("❌ Please fill all required fields.")

st.markdown("""
### 🕒 Business Hours
- **Monday - Friday:** 9:00 AM - 6:00 PM IST
- **Saturday:** 10:00 AM - 2:00 PM IST  
- **Sunday:** Closed

### ⚡ Emergency Technical Support
For critical system issues, our technical support is available 24/7 via:
- **Email:** support@devstackhq.com
- **Phone:** +91-9873171180 (24/7)

### 🔒 Response Time Commitment
- **Technical Support:** Within 2 hours (24/7)
- **Sales Inquiries:** Within 4 business hours  
- **General Questions:** Within 24 hours
- **Privacy Concerns:** Within 48 hours
""")
