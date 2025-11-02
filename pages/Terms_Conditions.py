# pages/Terms_and_Conditions.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Terms & Conditions - DevStackHQ", layout="centered")

CSS = """
<style>
:root{--primary:#667eea;--dark:#343a40;--light:#f8f9fa}
body{font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;background:var(--light);color:#222}
.header{background:linear-gradient(135deg,var(--primary),#764ba2);color:white;padding:1.2rem;border-radius:10px;text-align:center}
.terms{background:white;padding:1.2rem;border-radius:8px;box-shadow:0 8px 20px rgba(0,0,0,0.06);margin-top:1rem}
.term-section{margin-bottom:1rem}
.term-section h3{margin-bottom:.4rem;color:var(--dark)}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="header"><h1>📄 Terms & Conditions</h1><p>Please read these terms carefully before using our services</p></div>', unsafe_allow_html=True)

st.markdown('<div class="terms">', unsafe_allow_html=True)

st.markdown('''
<div class="term-section">
  <h3>1. Acceptance of Terms</h3>
  <p>By accessing and using DevStackHQ services, you accept and agree to be bound by these Terms and Conditions.</p>
</div>

<div class="term-section">
  <h3>2. Services Description</h3>
  <p>DevStackHQ provides:</p>
  <ul>
    <li>Software development tools</li>
    <li>DevOps and CI/CD solutions</li>
    <li>Cloud deployment services</li>
    <li>Digital products and subscriptions</li>
  </ul>
</div>

<div class="term-section">
  <h3>3. User Accounts</h3>
  <ul>
    <li>You must provide accurate registration information</li>
    <li>You are responsible for maintaining account security</li>
    <li>You must be at least 18 years old to create an account</li>
  </ul>
</div>

<div class="term-section">
  <h3>4. Payment Terms</h3>
  <ul>
    <li>All prices are in INR/USD unless specified</li>
    <li>Payments are processed through secure gateways</li>
    <li>Subscription fees are billed in advance</li>
    <li>No refunds for digital products unless specified</li>
  </ul>
</div>

<div class="term-section">
  <h3>5. Intellectual Property</h3>
  <ul>
    <li>All software and content is owned by DevStackHQ</li>
    <li>You receive license to use products as per subscription</li>
    <li>No redistribution or reverse engineering allowed</li>
  </ul>
</div>

<div class="term-section">
  <h3>6. User Responsibilities</h3>
  <ul>
    <li>Use services only for lawful purposes</li>
    <li>No unauthorized access to other accounts</li>
    <li>No distribution of malware or harmful code</li>
    <li>Compliance with all applicable laws</li>
  </ul>
</div>

<div class="term-section">
  <h3>7. Service Modifications</h3>
  <p>We reserve the right to modify or discontinue services, update pricing with 30 days notice, and change features and functionality.</p>
</div>

<div class="term-section">
  <h3>8. Limitation of Liability</h3>
  <p>DevStackHQ shall not be liable for indirect, incidental, or consequential damages, service interruptions beyond our control, or third-party actions or content.</p>
</div>

<div class="term-section">
  <h3>9. Termination</h3>
  <p>We may suspend or terminate accounts for violations, non-payment, or fraudulent activities.</p>
</div>

<div class="term-section">
  <h3>10. Governing Law</h3>
  <p>These terms are governed by Indian law. Disputes shall be resolved in Bangalore courts.</p>
</div>

<div class="term-section">
  <h3>11. Changes to Terms</h3>
  <p>We may update these terms with notice via email or website posting.</p>
</div>

<div class="term-section">
  <h3>12. Contact Information</h3>
  <p>For questions about these terms, contact: legal@devstackhq.com</p>
  <p><em>Effective Date: October 2025</em></p>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<footer style='text-align:center;margin-top:1rem;color:#555'>&copy; 2025 DevStackHQ. All rights reserved.</footer>", unsafe_allow_html=True)
