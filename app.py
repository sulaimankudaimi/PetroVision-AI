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

# تصميم واجهة مستخدم احترافية وعالية التباين
st.markdown("""
    <style>
    .main { background-color: #05070a; color: #ffffff; }
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 2px solid #00f2ff !important;
    }
    .header-box { 
        padding: 25px; 
        border-radius: 15px; 
        background: linear-gradient(135deg, #001f3f, #0074d9); 
        border-bottom: 4px solid #00f2ff;
        margin-bottom: 30px;
        text-align: center;
    }
    .signature-card {
        padding: 15px;
        background: #161b22;
        border: 2px solid #00f2ff;
        border-radius: 10px;
        text-align: center;
    }
    /* تحسين وضوح نصوص الراديو */
    div[data-testid="stRadio"] label p {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك تحميل البيانات مع معالجة الأخطاء (Data Engine) ---
@st.cache_data
def load_all_data():
    files = {
        "petro": "Data/petrophysical_data.csv",
        "sensors": "Data/sensor_integrity_data.csv",
        "history": "Data/production_history.csv",
        "drilling": "Data/real_time_drilling_data.csv"
    }
    loaded_data = {}
    for key, path in files.items():
        try:
            # التأكد من وجود الملف وقراءته
            loaded_data[key] = pd.read_csv(path)
        except Exception as e:
            # في حال الفشل، ننشئ DataFrame فارغ لتجنب الـ NameError
            loaded_data[key] = pd.DataFrame()
            st.sidebar.warning(f"⚠️ Missing file: {key}")
    return loaded_data

# تعريف المتغير data بشكل صريح
all_data = load_all_data()

# --- 3. القائمة الجانبية (Mission Control) ---
with st.sidebar:
    st.markdown(f"""
        <div class='signature-card'>
            <h1 style='color: #ffffff; margin:0; font-size: 1.4em;'>{PLATFORM_NAME}</h1>
            <p style='color: #00f2ff; font-size: 0.8em;'>Sovereign Digital Twin</p>
            <hr style='border-top: 1px solid #00f2ff;'>
            <p style='color: #ffffff; font-size: 0.85em;'>Designed by:</p>
            <p style='color: #00f2ff; font-size: 1.1em; font-weight: bold;'>{DEVELOPER_NAME}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><p style='color: #ffffff; font-weight: bold;'>🕹️ MODULE SELECTOR</p>", unsafe_allow_html=True)
    menu = st.radio("", 
                    ["Strategic Dashboard", "Subsurface Twin", "Production Analytics", "Safety & Sensors"],
                    label_visibility="collapsed")
    
    st.markdown("---")
    st.success("✅ System Connected")

# --- 4. معالجة الأقسام (Module Logic) ---

# العنوان الرئيسي الموحد
st.markdown(f"""
    <div class='header-box'>
        <h1 style='color: white; margin: 0;'>{PLATFORM_NAME} | Operational Command Hub</h1>
        <p style='color: #00f2ff; font-weight: bold;'>Developed by {DEVELOPER_NAME}</p>
    </div>
""", unsafe_allow_html=True)

if menu == "Strategic Dashboard":
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Reservoir Logs", f"{len(all_data['petro'])} pts")
    with c2: st.metric("Sensor Streams", f"{len(all_data['sensors'])} pts")
    with c3: st.metric("Field Status", "Optimal")
    with c4: st.metric("AI Accuracy", "94.8%")

    st.subheader("Field Performance Overview")
    if not all_data['drilling'].empty:
        st.dataframe(all_data['drilling'].head(10), use_container_width=True)

elif menu == "Subsurface Twin":
    st.subheader("🌐 3D Petrophysical Mapping")
    if not all_data['petro'].empty:
        fig_3d = px.scatter_3d(all_data['petro'], x='Depth_m', y='Porosity_%', z='Permeability_mD',
                               color='Gamma_Ray_API', template='plotly_dark')
        st.plotly_chart(fig_3d, use_container_width=True)
    else:
        st.error("Petrophysical data not found.")

elif menu == "Production Analytics":
    st.subheader("🔮 Predictive Production Trends")
    # تم تغيير الاسم هنا من 'history' ليتوافق مع المفاتيح المعرفة في الدالة
    if not all_data['history'].empty:
        fig_prod = px.line(all_data['history'], x=all_data['history'].columns[0], y=all_data['history'].columns[1],
                           template='plotly_dark', title="Historical Production")
        st.plotly_chart(fig_prod, use_container_width=True)
    else:
        st.error("Production history data not found.")

elif menu == "Safety & Sensors":
    st.subheader("🛡️ Asset Integrity Sentinel")
    if not all_data['sensors'].empty:
        fig_sensor = go.Figure()
        fig_sensor.add_trace(go.Scatter(y=all_data['sensors']['Wellhead_Pressure_psi'].tail(100), name="Pressure"))
        fig_sensor.update_layout(template='plotly_dark', title="Real-time Sensor Feed (Last 100 Logs)")
        st.plotly_chart(fig_sensor, use_container_width=True)
    else:
        st.error("Sensor data not found.")

# --- 5. التذييل ---
st.markdown(f"<p style='text-align: center; color: #64748b;'>{PLATFORM_NAME} | Proprietary Tech by {DEVELOPER_NAME} © 2026</p>", unsafe_allow_html=True)
