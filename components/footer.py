import streamlit as st

def footer():
    st.markdown("""
    <footer class="footer">
        <p style="font-size: 16px; font-weight: bold;">© 2025 DevStackHQ. All rights reserved.</p>
        <div class="footer-links">
            <a href="shipping-policy.html">Shipping Policy</a> | 
            <a href="terms-conditions.html">Terms & Conditions</a> | 
            <a href="cancellations-refund.html">Cancellations & Refund</a> | 
            <a href="contact.html">Contact Us</a>
        </div>
        <p style="font-size: 14px; margin-top: 1rem;">
            Need help? <a href="mailto:support@devstackhq.com" style="color: #FF4B4B;">Contact our support team</a>
        </p>
    </footer>

    <style>
    .footer {
        text-align: center;
        color: #666;
        padding: 20px;
        margin-top: 3rem;
        border-top: 1px solid #dee2e6;
    }
    .footer-links {
        margin: 15px 0;
    }
    .footer-links a {
        margin: 0 15px;
        text-decoration: none;
        color: #666;
        font-size: 14px;
        transition: color 0.3s ease;
    }
    .footer-links a:hover {
        color: #667eea;
    }
    </style>
    """, unsafe_allow_html=True)
