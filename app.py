import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# --- 1. إعدادات الهوية والوضوح ---
PLATFORM_NAME = "PetroVision AI"
DEVELOPER_NAME = "Eng. Sulaiman Kudaimi"

st.set_page_config(page_title=f"{PLATFORM_NAME} | {DEVELOPER_NAME}", layout="wide")

# تصميم واجهة مستخدم احترافية
st.markdown("""
    <style>
    .main { background-color: #05070a; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 2px solid #00f2ff !important; }
    .header-box { padding: 25px; border-radius: 15px; background: linear-gradient(135deg, #001f3f, #0074d9); border-bottom: 4px solid #00f2ff; margin-bottom: 30px; text-align: center; }
    .signature-card { padding: 15px; background: #161b22; border: 2px solid #00f2ff; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك تحميل البيانات ---
@st.cache_data
def load_all_data():
    files = {"petro": "Data/petrophysical_data.csv", "sensors": "Data/sensor_integrity_data.csv", 
             "history": "Data/production_history.csv", "drilling": "Data/real_time_drilling_data.csv"}
    loaded_data = {}
    for key, path in files.items():
        try: loaded_data[key] = pd.read_csv(path)
        except: loaded_data[key] = pd.DataFrame()
    return loaded_data

all_data = load_all_data()

# --- 3. القائمة الجانبية ---
with st.sidebar:
    st.markdown(f"<div class='signature-card'><h1 style='color:white; margin:0; font-size:1.4em;'>{PLATFORM_NAME}</h1><p style='color:#00f2ff; font-size:0.8em;'>Sovereign Digital Twin</p><hr style='border-top:1px solid #00f2ff;'><p style='color:white; font-size:0.85em;'>Designed by:</p><p style='color:#00f2ff; font-size:1.1em; font-weight:bold;'>{DEVELOPER_NAME}</p></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    menu = st.radio("DASHBOARD SELECTOR", ["Strategic Dashboard", "Subsurface Twin (3D Field)", "Production Analytics", "Safety & Sensors"])

# العنوان الرئيسي
st.markdown(f"<div class='header-box'><h1 style='color:white; margin:0;'>{PLATFORM_NAME} | Operational Command Hub</h1><p style='color:#00f2ff; font-weight:bold;'>Developed by {DEVELOPER_NAME}</p></div>", unsafe_allow_html=True)

# --- 4. المنطق البرمجي للأقسام ---

if menu == "Subsurface Twin (3D Field)":
    st.subheader("🌐 3D Integrated Reservoir Field Model")
    
    # توليد تضاريس متموجة (السطح المكمني)
    x = np.linspace(-100, 100, 50)
    y = np.linspace(-100, 100, 50)
    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = -2500 + (np.sin(x_grid/20) * 40 + np.cos(y_grid/20) * 40) # سطح متموج

    fig = go.Figure()

    # 1. إضافة السطح المتموج الملون
    fig.add_trace(go.Surface(
        x=x, y=y, z=z_grid,
        colorscale='Spectral', # ألوان متباينة جداً (أحمر، أصفر، أخضر، أزرق)
        colorbar=dict(title="Depth (m)", thickness=20),
        name="Reservoir Top"
    ))

    # 2. إضافة 5 آبار موزعة (Well-A to Well-E)
    well_locations = [
        {'name': 'Well-A', 'x': -60, 'y': -60},
        {'name': 'Well-B', 'x': 60, 'y': -60},
        {'name': 'Well-C', 'x': 0, 'y': 0},
        {'name': 'Well-D', 'x': -60, 'y': 60},
        {'name': 'Well-E', 'x': 60, 'y': 60},
    ]

    for well in well_locations:
        # رسم عمود البئر (من السطح الافتراضي 0 إلى عمق المكمن)
        fig.add_trace(go.Scatter3d(
            x=[well['x'], well['x']], 
            y=[well['y'], well['y']], 
            z=[0, -2500],
            mode='lines+markers',
            line=dict(color='white', width=6),
            marker=dict(size=4, color='red'),
            name=well['name']
        ))
        # إضافة نص فوق كل بئر
        fig.add_trace(go.Scatter3d(
            x=[well['x']], y=[well['y']], z=[50],
            mode='text',
            text=[well['name']],
            textfont=dict(color='yellow', size=12),
            showlegend=False
        ))

    fig.update_layout(
        template='plotly_dark',
        scene=dict(
            xaxis_title='East (m)', yaxis_title='North (m)', zaxis_title='Depth (m)',
            zaxis=dict(range=[-3000, 500]), # ضبط المدى لظهور الآبار
            aspectratio=dict(x=1, y=1, z=0.6)
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=700
    )
    st.plotly_chart(fig, use_container_width=True)
    st.info("The model displays 5 active wells penetrating the primary reservoir formation. Colors indicate depth variation (Spectral Mapping).")

# بقية الأقسام (يمكنك تركها كما هي أو إضافة لمساتك)
elif menu == "Strategic Dashboard":
    st.write("Overview Stats...")
