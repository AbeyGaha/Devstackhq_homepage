# pages/Products.py
import streamlit as st
from pathlib import Path

ROOT = Path(__file__).parent.parent
ASSETS = ROOT / "assets"

st.set_page_config(page_title="DevStackHQ - Products", layout="centered")

CSS = """
<style>
:root {
  --primary: #667eea;
  --secondary: #764ba2;
  --accent: #FF6B35;
  --light: #f8f9fa;
  --dark: #343a40;
}
body { background: linear-gradient(135deg, var(--primary), var(--secondary)); color: #333; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
.main-header { text-align: center; padding: 3rem 0; color: white; }
.product-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem; margin: 1.5rem 0; }
.product-card { background: white; border-radius: 20px; padding: 1.5rem; box-shadow: 0 15px 35px rgba(0,0,0,0.08); position:relative; overflow:hidden; }
.product-card::before { content:''; position:absolute; top:0; left:0; right:0; height:4px; background: linear-gradient(45deg, var(--accent), var(--primary)); }
.tech-tag { background: linear-gradient(45deg, var(--primary), var(--secondary)); color:white; padding:.35rem .8rem; border-radius:16px; margin-right:.4rem; display:inline-block; font-size:.85rem; }
.status-badge { display:inline-flex; align-items:center; padding:.4rem .8rem; border-radius:20px; background:#d4edda; color:#155724; margin-top:.5rem; }
.url-box { background: var(--light); padding:.8rem 1rem; border-radius:8px; border:1px dashed #e6e6e6; font-family: monospace; word-break:break-all; margin-top:.6rem; }
.btn { background: linear-gradient(45deg, var(--accent), #FF8E53); color:white; padding:.6rem .9rem; border-radius:999px; text-decoration:none; display:inline-block; margin-top:.7rem; }
.quick-access { background:white; padding:1rem; border-radius:12px; box-shadow:0 8px 24px rgba(0,0,0,0.06); margin-top:1.2rem; }
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header"><h1>🚀 DevStackHQ Products</h1><p>Discover powerful AI tools and developer solutions</p></div>', unsafe_allow_html=True)

# Server status block
st.markdown('<div style="max-width:900px;margin:auto"><div style="background:rgba(255,255,255,0.08);padding:1rem;border-radius:12px;color:white;text-align:center"> <h3 style="margin:.25rem 0">🟢 ALL SYSTEMS OPERATIONAL</h3><p style="margin:.25rem 0">SearchPulse Chatbot: Online | AdVisionGenre: Live | Reposcope: Running</p><small>Powered by Groq LPU • Optimized for Performance</small></div></div>', unsafe_allow_html=True)

st.markdown("---")

# Products grid (three cards)
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.markdown('<div class="product-card"><div style="font-size:2rem">🤖</div><h2>SearchPulse Chatbot</h2><p><strong>AI-Powered Conversational Assistant with Creative Tools</strong></p><p>Next-gen AI conversations, file uploads, and creative tools.</p><div style="margin:8px 0"><span class="tech-tag">FastAPI</span><span class="tech-tag">Groq LPU</span><span class="tech-tag">Gradio</span><span class="tech-tag">Python</span></div><div class="status-badge">✅ LIVE ON LINODE</div><div class="url-box">https://advisiongenre.devstackhq.com/chat/</div><a target="_blank" href="https://advisiongenre.devstackhq.com/chat/" class="btn">🚀 Try Free Demo</a></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card"><div style="font-size:2rem">📰</div><h2>AdVisionGenre</h2><p><strong>AI Content Creation & Automated Publishing</strong></p><p>Auto blog generation, WP auto-publish, SEO tools.</p><div style="margin:8px 0"><span class="tech-tag">WordPress API</span><span class="tech-tag">Google Cloud</span><span class="tech-tag">FastAPI</span></div><div class="status-badge">✅ LIVE ON LINODE</div><div class="url-box">https://advisiongenre.devstackhq.com</div><a target="_blank" href="https://advisiongenre.devstackhq.com" class="btn">📖 Read Our Blogs</a></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card"><div style="font-size:2rem">🧠</div><h2>Reposcope</h2><p><strong>Cloud Repository Intelligence Platform</strong></p><p>Streamlit-based repo analysis, cloud deployment automation and dashboards.</p><div style="margin:8px 0"><span class="tech-tag">Streamlit</span><span class="tech-tag">Python</span><span class="tech-tag">Data Viz</span></div><div class="status-badge">✅ LIVE ON STREAMLIT</div><div class="url-box">https://reposcope.streamlit.app</div><a target="_blank" href="https://reposcope.streamlit.app" class="btn">🌐 Launch Platform</a></div>', unsafe_allow_html=True)

st.markdown("---")

st.header("🔗 Quick Access Links")
st.write("- SearchPulse Chatbot — https://advisiongenre.devstackhq.com/chat/")
st.write("- AdVisionGenre — https://advisiongenre.devstackhq.com")
st.write("- Reposcope — https://reposcope.streamlit.app")

st.markdown('<div class="quick-access"><h4 style="margin:0 0 .5rem 0">Quick Access</h4><div style="display:flex;gap:.6rem;flex-wrap:wrap"><a class="btn" href="https://advisiongenre.devstackhq.com/chat/" target="_blank">SearchPulse Chatbot</a><a class="btn" href="https://advisiongenre.devstackhq.com" target="_blank">AdVisionGenre</a><a class="btn" href="https://reposcope.streamlit.app" target="_blank">Reposcope</a></div></div>', unsafe_allow_html=True)

st.markdown("<footer style='text-align:center;margin-top:2rem;color:#fff'>&copy; 2025 DevStackHQ Labs</footer>", unsafe_allow_html=True)
