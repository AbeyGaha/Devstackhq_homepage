import streamlit as st

def show_footer():
    st.markdown("---")
    st.markdown("""
    <div style='text-align:center; color:#666; padding: 20px;'>
        <p style='font-size: 16px; font-weight: bold;'>© 2025 DevStackHQ. All rights reserved.</p>
        <div style='margin: 15px 0;'>
            <a href='/Shipping_Policy' style='margin: 0 15px; text-decoration:none; color:#666; font-size: 14px;'>Shipping Policy</a> | 
            <a href='/Terms_Conditions' style='margin: 0 15px; text-decoration:none; color:#666; font-size: 14px;'>Terms & Conditions</a> | 
            <a href='/Cancellations_Refund' style='margin: 0 15px; text-decoration:none; color:#666; font-size: 14px;'>Cancellations & Refund</a> | 
            <a href='/Contact_Us' style='margin: 0 15px; text-decoration:none; color:#666; font-size: 14px;'>Contact Us</a>
        </div>
        <p style='font-size: 14px;'>
            Need help? <a href='mailto:support@devstackhq.com' style='color: #FF4B4B;'>Contact our support team</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
