import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# --- 1. إعدادات الهوية والوضوح العالي ---
PLATFORM_NAME = "PetroVision AI"
DEVELOPER_NAME = "Eng. Sulaiman Kudaimi"

st.set_page_config(
    page_title=f"{PLATFORM_NAME} | {DEVELOPER_NAME}",
    page_icon="💎",
    layout="wide"
)

# تصميم واجهة مستخدم محسنة للوضوح (Super Clarity CSS)
st.markdown("""
    <style>
    /* تحسين الخلفية العامة */
    .main { background-color: #05070a; color: #ffffff; }
    
    /* جعل القائمة الجانبية واضحة جداً */
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 2px solid #00f2ff !important;
    }
    
    /* وضوح نصوص العناوين في القائمة الجانبية */
    .css-17l6nlh, .css-12ttj6m, .st-ae {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
    }

    /* العنوان الرئيسي (Header) */
    .header-box { 
        padding: 30px; 
        border-radius: 15px; 
        background: linear-gradient(135deg, #001f3f, #0074d9); 
        border-bottom: 4px solid #00f2ff;
        margin-bottom: 35px;
        box-shadow: 0 10px 30px rgba(0,242,255,0.2);
    }
    
    /* وضوح نصوص الراديو بوكس في القائمة الجانبية */
    div[data-testid="stRadio"] label p {
        color: #00f2ff !important; /* لون فوسفوري واضح */
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }

    /* توقيع المطور في القائمة الجانبية */
    .signature-card {
        padding: 20px;
        background: #161b22;
        border: 2px solid #00f2ff;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. القائمة الجانبية المحدثة (High-Visibility Sidebar) ---
with st.sidebar:
    st.markdown(f"""
        <div class='signature-card'>
            <h1 style='color: #ffffff; margin:0; font-size: 1.5em; text-shadow: 2px 2px #000;'>{PLATFORM_NAME}</h1>
            <p style='color: #00f2ff; font-size: 0.9em; font-weight: bold;'>Digital Twin Engine</p>
            <hr style='border-top: 2px solid #00f2ff; opacity: 0.5;'>
            <p style='color: #ffffff; font-size: 0.85em;'>Architected & Developed by:</p>
            <p style='color: #00f2ff; font-size: 1.1em; font-weight: bold;'>{DEVELOPER_NAME}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    # استخدام العنوان الملون هنا بدلاً من الراديو العادي لزيادة الوضوح
    st.markdown("<p style='color: #ffffff; font-weight: bold; font-size: 1.2em;'>🕹️ DASHBOARD SELECTOR</p>", unsafe_allow_html=True)
    menu = st.radio("", 
                    ["Strategic Dashboard", "Subsurface (10k Petrophysics)", "Production (History & AI)", "Safety (10k Sensors)"],
                    label_visibility="collapsed")
    
    st.markdown("---")
    st.success("✅ System Online")

# --- 3. العنوان الرئيسي (Header) ---
st.markdown(f"""
    <div class='header-box'>
        <h1 style='color: white; margin: 0; font-size: 2.5em;'>{PLATFORM_NAME} | Operational Command Hub</h1>
        <p style='color: #00f2ff; font-size: 1.2em; font-weight: bold;'>Integrated Field Intelligence System - Designed by {DEVELOPER_NAME}</p>
    </div>
""", unsafe_allow_html=True)

# (تكملة بقية الكود الخاص بالـ Tabs والبيانات كما هي)

# --- 4. معالجة الأقسام (Module Logic) ---

if menu == "Strategic Dashboard":
    st.markdown(f"<div class='header-box'><h1>Global Operations Summary</h1><p>Integrated KPIs Managed by <b>{DEVELOPER_NAME}</b></p></div>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Subsurface Logs", f"{len(data['petro'])} pts")
    with c2: st.metric("Live Sensor Feeds", f"{len(data['sensors'])} pts")
    with c3: st.metric("Avg Pressure", "3120 psi", "-15")
    with c4: st.metric("System Uptime", "99.9%")

    # عرض عينة من البيانات الضخمة
    st.subheader("Real-time Drilling Data Stream")
    st.dataframe(data['drilling'].head(100), use_container_width=True)

elif menu == "Subsurface (10k Petrophysics)":
    st.title("🌐 Advanced Subsurface Analytics")
    if not data['petro'].empty:
        col_a, col_b = st.columns([1, 2])
        with col_a:
            st.write("**Cross-Plot: Porosity vs Permeability**")
            fig_cross = px.scatter(data['petro'], x='Porosity_%', y='Permeability_mD', 
                                   color='Gamma_Ray_API', template='plotly_dark')
            st.plotly_chart(fig_cross, use_container_width=True)
        with col_b:
            st.write("**3D Structural Property Mapping**")
            fig_3d = go.Figure(data=[go.Scatter3d(
                x=data['petro']['Depth_m'], y=data['petro']['Porosity_%'], z=data['petro']['Permeability_mD'],
                mode='markers', marker=dict(size=2, color=data['petro']['Gamma_Ray_API'], colorscale='Viridis')
            )])
            fig_3d.update_layout(template='plotly_dark', margin=dict(l=0, r=0, b=0, t=0))
            st.plotly_chart(fig_3d, use_container_width=True)

elif menu == "Production (History & AI)":
    st.title("🔮 Production Forecasting Engine")
    if not data['history'].empty:
        fig_hist = px.line(data['history'], x=data['history'].columns[0], y=data['history'].columns[1], 
                           title="Historical Production Trend", template='plotly_dark')
        st.plotly_chart(fig_hist, use_container_width=True)
    
    st.info("AI Analysis: Based on current trends, EUR is expected to increase by 4.2% with optimized drawdown.")

elif menu == "Safety (10k Sensors)":
    st.title("🛡️ HSE & Integrity Sentinel")
    if not data['sensors'].empty:
        st.write("**Real-time Vibration & Pressure Stream (10,000 Logs)**")
        # عرض آخر 500 نقطة لضمان سرعة الأداء
        fig_sensors = go.Figure()
        fig_sensors.add_trace(go.Scatter(y=data['sensors']['Wellhead_Pressure_psi'].tail(500), name="Pressure"))
        fig_sensors.add_trace(go.Scatter(y=data['sensors']['Vibration_Level_mm_s'].tail(500), name="Vibration", yaxis="y2"))
        fig_sensors.update_layout(
            template='plotly_dark',
            yaxis2=dict(title="Vibration", overlaying="y", side="right"),
            title="High-Frequency Monitoring Window"
        )
        st.plotly_chart(fig_sensors, use_container_width=True)

# --- 5. التذييل ---
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #64748b;'>Proprietary Big Data Platform | Developed & Architected by <b>{DEVELOPER_NAME}</b></p>", unsafe_allow_html=True)
