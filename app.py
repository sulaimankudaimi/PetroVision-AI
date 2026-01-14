import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# --- 1. إعدادات الهوية البصرية ---
st.set_page_config(
    page_title="OmniField AI | Eng. Sulaiman Kudaimi",
    page_icon="🌐",
    layout="wide"
)

# تصميم واجهة المستخدم (Custom CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stSidebar { background-color: #1a1c24; border-right: 2px solid #3b82f6; }
    .header-box { 
        padding: 25px; 
        border-radius: 12px; 
        background: linear-gradient(135deg, #1e3a8a, #3b82f6); 
        color: white; 
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .footer-text { text-align: center; color: #94a3b8; padding: 20px; font-size: 0.85em; }
    .signature { color: #60a5fa; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. القائمة الجانبية (Mission Control) ---
with st.sidebar:
    st.markdown(f"""
        <div style='text-align: center; padding: 15px; border-radius: 15px; background: #0f172a; border: 2px solid #3b82f6;'>
            <h1 style='color: white; margin:0; font-size: 1.5em;'>OmniField AI</h1>
            <p style='color: #60a5fa; font-size: 0.8em; margin-bottom:10px;'>Integrated Digital Twin Platform</p>
            <hr style='border-top: 1px solid #334155;'>
            <p style='color: #94a3b8; font-size: 0.85em;'>Developed & Designed by:</p>
            <p style='color: white; font-size: 1em; font-weight: bold;'>Eng. Sulaiman Kudaimi</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    menu = st.radio("MAIN CONTROL CENTER", 
                    ["Strategic Dashboard", "Subsurface (Reservoir)", "Surface (Production)", "Safety & Integrity"])
    
    st.markdown("---")
    st.markdown("🌐 **System Status:** <span style='color:#10b981'>Online</span>", unsafe_allow_html=True)
    st.info("Version: Global Release 2.0")

# --- 3. محتويات المنصة ---

if menu == "Strategic Dashboard":
    st.markdown(f"""
        <div class='header-box'>
            <h1>Executive Strategic Overview</h1>
            <p>Global Insights Managed by <span class='signature'>Eng. Sulaiman Kudaimi</span></p>
        </div>
    """, unsafe_allow_html=True)
    
    # مؤشرات الأداء الرئيسية (KPIs)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Avg Reservoir Pressure", "3,120 psi", "-2.1%")
    with c2: st.metric("Total Field Production", "4,520 bpd", "+5.4%")
    with c3: st.metric("HSE Compliance", "100%", "No Alarms")
    with c4: st.metric("AI Prediction Accuracy", "94.8%", "High")

    # تحليل مدمج
    st.subheader("Inter-Dependency Dynamics")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Production', 'Pressure', 'Safety Index'])
    st.line_chart(chart_data)

elif menu == "Subsurface (Reservoir)":
    st.title("🌐 Subsurface Digital Twin")
    st.write("3D Spatial Analysis & Pressure Mapping")
    # محاكاة المكمن ثلاثي الأبعاد
    grid_x, grid_y = np.mgrid[0:100:20j, 0:100:20j]
    grid_z = np.sin(grid_x/10) * np.cos(grid_y/10)
    fig = go.Figure(data=[go.Surface(z=grid_z, colorscale='RdYlBu')])
    fig.update_layout(template='plotly_dark', height=650)
    st.plotly_chart(fig, use_container_width=True, theme=None)

elif menu == "Surface (Production)":
    st.title("🔮 Production Forecasting Twin")
    st.write("AI-Driven Decline Curve Analysis (DCA)")
    timeline = np.arange(2020, 2035)
    prod = 5000 * np.exp(-0.06 * (timeline - 2020))
    fig_prod = go.Figure(data=[go.Scatter(x=timeline, y=prod, mode='lines+markers', line=dict(color='#10b981', width=3))])
    fig_prod.update_layout(template='plotly_dark', title="Long-term Production Forecast")
    st.plotly_chart(fig_prod, use_container_width=True)

elif menu == "Safety & Integrity":
    st.title("🛡️ HSE & Asset Integrity Twin")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Asset Health Monitoring")
        st.write("Vibration Sensor: **Stable**")
        st.write("Corrosion Rate: **0.02 mm/year**")
    with col2:
        st.warning("Emergency Shutdown (ESD) Systems")
        st.write("Pressure Relief Valves: **Operational**")
        st.progress(100)

# --- 4. التذييل (Footer) ---
st.markdown(f"""
    <div class='footer-text'>
        <hr>
        OmniField AI Platform | Proprietary System Designed & Developed by <b>Eng. Sulaiman Kudaimi</b><br>
        Digital Transformation in Oil & Gas | 2026 Release
    </div>
""", unsafe_allow_html=True)