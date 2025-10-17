# pages/About.py

import streamlit as st
from components.navbar import show_navbar
from components.footer import show_footer
from PIL import Image
import os

# ---- Navbar ----
show_navbar()

# ---- Page Title ----
st.title("📖 About DevStackHQ")

# ---- Hero / Intro Section ----
st.markdown("""
**DevStackHQ** is your all-in-one ecosystem for cutting-edge developer tools.  
We accelerate productivity by providing seamless solutions for CI/CD, deployment, monitoring, and AI-assisted development workflows.  
Our mission: **Empower developers to focus on building, not managing infrastructure.**
""")

# ---- Optional Banner Image ----
banner_path = os.path.join("assets", "about_banner.png")
if os.path.exists(banner_path):
    banner_img = Image.open(banner_path)
    st.image(banner_img, use_column_width=True)

# ---- What We Offer ----
st.subheader("🎯 What We Offer")
st.markdown("""
- 🚀 **Developer-centric Tools:** From repository management to AI-driven insights, everything built with developers in mind.
- 🔐 **Secure & Scalable:** Our micro SaaS applications are designed to scale while maintaining high security standards.
- 🧪 **Test & Experiment:** On-demand environments and sandboxes for testing and deploying your tools.
- 🌐 **Cross-platform Integration:** Works seamlessly across cloud, local, and hybrid setups.
- 📊 **Analytics & Insights:** Actionable metrics and visualizations to understand your workflows and productivity.
- 💡 **AI Assistance:** Integrated AI-powered suggestions, automation, and code insights.
""")

# ---- Our Philosophy ----
st.subheader("💡 Our Philosophy")
st.markdown("""
We believe in **developer-first design**:  
Tools should remove friction, not add it. Every feature, every workflow, every integration is carefully crafted to make developers more efficient and creative.  

**Built with ❤️ by developers, for developers.**
""")

# ---- Team / Credits ----
st.subheader("👩‍💻 Meet the Team")
st.markdown("""
- **Abhinav Chauhan** – Founder & Lead Developer  
- **AI & Cloud Experts** – Building the DevStackHQ platform  
- **Community Contributors** – Feedback-driven improvements from our user base  
""")

# ---- Footer ----
show_footer()
