import streamlit as st

st.set_page_config(page_title="Contact Us - DevStackHQ", page_icon="📞")

st.markdown("# 📞 Contact Us")
st.markdown("### We'd love to hear from you!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### 📧 Email
    **General Inquiries:** contact@devstackhq.com  
    **Support:** support@devstackhq.com  
    **Sales:** sales@devstackhq.com
    
    #### 📞 Phone
    **Customer Support:** +91-XXXXXXXXXX  
    **Business Inquiries:** +91-XXXXXXXXXX
    
    #### 🏢 Office Address
    DevStackHQ Solutions  
    SD-121,Sector-45,Noida
    Gautam Budh Nagar UP-
    201303
    """)

with col2:
    st.markdown("#### 📝 Contact Form")
    with st.form("contact_form"):
        name = st.text_input("Full Name*")
        email = st.text_input("Email Address*")
        subject = st.selectbox("Subject*", 
            ["General Inquiry", "Technical Support", "Sales", "Partnership", "Other"])
        message = st.text_area("Message*", height=150)
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you! Your message has been sent successfully.")
            else:
                st.error("❌ Please fill all required fields.")

st.markdown("""
### 🕒 Business Hours
- **Monday - Friday:** 9:00 AM - 6:00 PM IST
- **Saturday:** 10:00 AM - 2:00 PM IST  
- **Sunday:** Closed

### ⚡ Emergency Support
For critical system issues, our emergency support is available 24/7.
""")
