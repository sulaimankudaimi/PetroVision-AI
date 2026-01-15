import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# --- 1. الإعدادات والوضوح ---
PLATFORM_NAME = "PetroVision AI"
DEVELOPER_NAME = "Eng. Sulaiman Kudaimi"

st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# CSS محسن للتباين والوضوح العالي
st.markdown("""
    <style>
    .main { background-color: #05070a; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #00f2ff !important; }
    .st-emotion-cache-16idsys p { color: white !important; font-weight: bold; }
    .header-box { padding: 25px; border-radius: 15px; background: #111827; border: 2px solid #00f2ff; text-align: center; margin-bottom: 25px; }
    .alert-text { background-color: #ff0000; color: white; padding: 5px 15px; border-radius: 5px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. القائمة الجانبية ---
with st.sidebar:
    st.markdown(f"<h1 style='color:#00f2ff; text-align:center;'>{PLATFORM_NAME}</h1>", unsafe_allow_html=True)
    menu = st.radio("OPERATIONAL MODULES", ["Strategic Overview", "3D Reservoir Twin", "AI Production Forecast", "HSE & Safety Control"])
    st.markdown("---")
    st.write(f"Developed by: **{DEVELOPER_NAME}**")

# --- 3. معالجة الواجهات ---

if menu == "AI Production Forecast":
    st.markdown("<div class='header-box'><h1>🔮 AI Production Forecasting Hub</h1></div>", unsafe_allow_html=True)
    
    # بارامترات التحكم بالتنبؤ (التفاعلية)
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        years = st.slider("Prediction Horizon (Years)", 1, 5, 3)
        initial_rate = st.number_input("Initial Production (bpd)", 1000, 10000, 5000)
    with col_p2:
        decline_rate = st.slider("Annual Decline Rate (%)", 1, 30, 10)
    
    # معادلة الهبوط الأسي (Exponential Decline)
    months = np.arange(0, years * 12)
    # q = qi * e^(-di * t)
    prediction = initial_rate * np.exp(-(decline_rate/100) * (months/12))
    
    fig_ai = go.Figure()
    fig_ai.add_trace(go.Scatter(x=months, y=prediction, name="Predicted Flow Rate", 
                                line=dict(color='#00f2ff', width=4), fill='tozeroy'))
    
    fig_ai.update_layout(
        template='plotly_dark',
        title="Predictive Production Curve (Dynamic Arps Model)",
        xaxis_title="Timeline (Months)",
        yaxis_title="Oil Production (bpd)",
        hovermode="x unified"
    )
    st.plotly_chart(fig_ai, use_container_width=True)
    
    # مؤشرات ذكية
    st.info(f"💡 Estimated Cumulative Production for {years} years: **{int(prediction.sum() * 30):,} Barrels**")

elif menu == "HSE & Safety Control":
    st.markdown("<div class='header-box'><h1>🛡️ HSE & Asset Integrity Sentinel</h1></div>", unsafe_allow_html=True)
    
    # تحسين عرض الحساسات (وضوح فائق)
    st.markdown("<span class='alert-text'>CRITICAL MONITORING: HIGH-PRESSURE ZONE</span>", unsafe_allow_html=True)
    
    # توليد بيانات حساسات واقعية (مع ضجيج بسيط)
    time_steps = np.arange(100)
    pressure = 2800 + np.random.normal(0, 15, 100)
    limit = [3000] * 100 # خط حد الأمان
    
    fig_safety = go.Figure()
    fig_safety.add_trace(go.Scatter(x=time_steps, y=pressure, name="Wellhead Pressure", line=dict(color='#00f2ff', width=2)))
    fig_safety.add_trace(go.Scatter(x=time_steps, y=limit, name="Safety Limit", line=dict(color='red', dash='dash')))
    
    fig_safety.update_layout(
        template='plotly_dark',
        xaxis_title="Time (Last 100 Minutes)",
        yaxis_title="Pressure (psi)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_safety, use_container_width=True)
    
    # لوحة مؤشرات السلامة
    c1, c2, c3 = st.columns(3)
    c1.metric("Max Pressure Recorded", f"{int(pressure.max())} psi", "Safe")
    c2.metric("Vibration Status", "Normal", "0.2 mm/s")
    c3.metric("Alarm Status", "Clear", "No Leaks")

# (بقية الأقسام تتبع نفس المنطق المطور)
# --- 4. معالجة الصفحات والمحتوى ---

# العنوان الرئيسي الموحد
st.markdown(f"""
    <div class='header-box'>
        <h1>{PLATFORM_NAME} | Operational Command Hub</h1>
        <p style='color: #00f2ff; font-weight: bold; font-size: 1.2em;'>Next-Gen Oilfield Management by {DEVELOPER_NAME}</p>
    </div>
""", unsafe_allow_html=True)

if menu == "📖 Quick Start Guide":
    st.header("Welcome to PetroVision AI")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown("""
        <div class='guide-card'>
            <h3 style='color:#00f2ff;'>1. Analyze Status</h3>
            <p>Go to <b>Strategic Dashboard</b> to view real-time KPIs and general field health.</p>
        </div>
        <div class='guide-card'>
            <h3 style='color:#00f2ff;'>2. Explore Subsurface</h3>
            <p>Use the <b>3D Twin</b> to visualize reservoir topography and well placements.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_g2:
        st.markdown("""
        <div class='guide-card'>
            <h3 style='color:#00f2ff;'>3. Predict Future</h3>
            <p>The <b>AI Forecast</b> uses machine learning to estimate production for the next 365 days.</p>
        </div>
        <div class='guide-card'>
            <h3 style='color:#00f2ff;'>4. Custom Data</h3>
            <p>Use the <b>Data Gateway</b> in the sidebar to upload your own field's CSV files.</p>
        </div>
        """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/oil-rig.png", width=200)

elif menu == "📊 Strategic Dashboard":
    st.subheader("Field Key Performance Indicators")
    k1, k2, k3 = st.columns(3)
    k1.metric("Current Production", f"{int(active_df.iloc[-1,1])} bpd", "+5%")
    k2.metric("Reservoir Pressure", "3120 psi", "-12")
    k3.metric("System Safety", "100%", "Secure")
    st.line_chart(active_df.iloc[:, 1].tail(50))

elif menu == "🌐 3D Reservoir Twin":
    st.subheader("3D Interactive Field Mapping")
    x, y = np.linspace(-50, 50, 40), np.linspace(-50, 50, 40)
    X, Y = np.meshgrid(x, y)
    Z = -2000 - (0.08 * X**2 + 0.08 * Y**2) + (np.cos(X/10) * 30)
    
    fig = go.Figure(data=[go.Surface(z=Z, x=x, y=y, colorscale='Jet')])
    # إضافة الآبار
    well_locs = [(-25,-25), (25,-25), (0,0), (-25,25), (25,25)]
    for wx, wy in well_locs:
        fig.add_trace(go.Scatter3d(x=[wx, wx], y=[wy, wy], z=[0, -2200], mode='lines', line=dict(color='white', width=7)))
        fig.add_trace(go.Scatter3d(x=[wx], y=[wy], z=[0], mode='markers', marker=dict(color='red', size=6)))
    
    fig.update_layout(template='plotly_dark', height=700, margin=dict(l=0,r=0,b=0,t=0))
    st.plotly_chart(fig, use_container_width=True)

elif menu == "🔮 AI Production Forecast":
    st.subheader("Machine Learning Decline Curve Analysis")
    df = active_df.copy()
    X = np.arange(len(df)).reshape(-1, 1)
    y = df.iloc[:, 1]
    model = LinearRegression().fit(X, y)
    future = np.arange(len(df), len(df)+365).reshape(-1, 1)
    pred = model.predict(future)
    
    fig_ai = go.Figure()
    fig_ai.add_trace(go.Scatter(y=y, name="History", line=dict(color="#00f2ff")))
    fig_ai.add_trace(go.Scatter(x=np.arange(len(df), len(df)+365), y=pred, name="AI Forecast", line=dict(dash='dash', color='red')))
    fig_ai.update_layout(template='plotly_dark', title="Predicted vs Historical Production")
    st.plotly_chart(fig_ai, use_container_width=True)

elif menu == "🛡️ HSE & Sensors":
    st.subheader("Asset Integrity Sentinel")
    st.warning("Monitoring High-Pressure Critical Zones")
    # محاكاة بيانات حساسات
    sensor_data = np.random.normal(2800, 20, 100)
    st.area_chart(sensor_data)

# --- 5. التذييل ---
st.markdown("---")
st.markdown(f"<p style='text-align:center; color:#64748b;'>{PLATFORM_NAME} | Proprietary Tech by {DEVELOPER_NAME} © 2026</p>", unsafe_allow_html=True)
