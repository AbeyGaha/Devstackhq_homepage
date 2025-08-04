# pages/About.py

import streamlit as st
from components.navbar import show_navbar
from components.footer import show_footer

show_navbar()

st.title("📖 About DevStackHQ")
st.write("""
DevStackHQ is your go-to platform for developer tools that accelerate productivity.

From CI/CD pipelines to seamless deployment and monitoring, we aim to build tools that reduce friction in the development lifecycle.

### What We Offer
- 🚀 Developer-centric tools
- 🔐 Secure and scalable micro SaaS applications
- 🧪 On-demand test benches for your tools

Built with ❤️ by developers, for developers.
""")

show_footer()
