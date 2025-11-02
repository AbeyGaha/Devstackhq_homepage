import streamlit as st

st.set_page_config(page_title="Privacy Policy | DevStackHQ", page_icon="🔒", layout="wide")

st.markdown("""
<style>
    * {font-family: 'Segoe UI', sans-serif;}
    .main-header {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white; padding: 25px; border-radius: 10px; text-align: center;
    }
    .policy-content {
        background: white; padding: 2rem; border-radius: 10px;
        margin: 2rem 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h2 {color: #333; border-left: 4px solid #667eea; padding-left: 10px;}
    .footer {text-align: center; color: #666; margin-top: 3rem; border-top: 1px solid #ddd; padding-top: 1rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🔒 Privacy Policy</h1>
    <p>Last Updated: January 2025</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="policy-content">
<h2>1. Information We Collect</h2>
<ul>
<li>Name, Contact, and Payment Details (via Razorpay)</li>
<li>Technical Data: IP, browser, device info</li>
<li>Usage Data and Cookies</li>
</ul>

<h2>2. How We Use Data</h2>
<ul>
<li>To deliver services and provide support</li>
<li>Enhance security and prevent fraud</li>
<li>Send updates and marketing (with consent)</li>
</ul>

<h2>3. Data Sharing</h2>
<p>We do not sell personal data. Shared only with:</p>
<ul>
<li>Razorpay for payments</li>
<li>AWS/Google Cloud for hosting</li>
<li>Google Analytics for insights</li>
</ul>

<h2>4. Security</h2>
<ul>
<li>SSL/TLS Encryption</li>
<li>Access Controls & Regular Audits</li>
</ul>

<h2>5. User Rights</h2>
<ul>
<li>Access, Correction, Deletion, Objection, Portability</li>
</ul>

<h2>6. Contact Us</h2>
<p><strong>Email:</strong> privacy@devstackhq.com<br>
<strong>Address:</strong> DevStackHQ Solutions, SD-121, Sector-45, Noida</p>

<p><em>Complies with GDPR and Indian Data Protection Regulations.</em></p>
</div>

<div class="footer">
<p>© 2025 DevStackHQ. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
