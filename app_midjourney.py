import streamlit as st
import random

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Background Master Pro", page_icon="🖼️", layout="wide")

# --- 🔧 ข้อมูลโมดูล (แยกหมวด ปกติ vs เทศกาล) ---

# 1. SCENE
SCENE_NORMAL = [
    "modern office hallway", "glass corridor", "startup workspace", 
    "meeting room", "city view through office glass"
]
SCENE_HOLIDAY = [
    "luxury hotel lobby decorated for Christmas", "modern office entrance with Lunar New Year decor",
    "high-end restaurant interior for Valentine's", "minimalist startup lounge with festive decorations",
    "urban rooftop terrace with summer sunset view", "spooky but elegant Halloween setup"
]

# 2. LIGHTING
LIGHTING_NORMAL = [
    "natural side lighting", "morning warm light", "sunset golden light", 
    "cool office light", "night artificial glow"
]
LIGHTING_HOLIDAY = [
    "festive warm bokeh lighting", "red and gold ambient glow", 
    "soft romantic diffused light", "vibrant high-contrast summer sun",
    "moody orange and purple night glow"
]

# โมดูลที่ใช้ร่วมกันได้
DEPTH_LIST = ["heavy blur background", "medium depth of field", "light blur (semi sharp)"]
COMPOSITION_LIST = ["copy space left", "copy space right", "copy space center", "top copy space (vertical)"]
MOOD_TONE_LIST = ["neutral corporate", "blue tech tone", "warm realistic", "dark moody", "festive vibrant", "clean airy minimalist"]
USE_CASE_LIST = ["minimal clean composition", "strong leading lines", "wide banner composition", "vertical ad layout"]

# --- UI Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=200, step=10, value=50)
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=1)
    st.markdown("---")
    st.subheader("🛡️ Pure Photography Mode")
    negative_prompt = st.text_area(
        "Negative Prompt (--no)", 
        value="vector, 3d, illustration, cartoon, render, text, watermark, logo, signatures, people, person, face, hand", 
        height=100
    )

# --- UI พื้นที่หลัก ---
st.title("🖼️ Commercial Background Engine")
st.markdown("ระบบปั่น Prompt สายฉากหลังเว้นพื้นที่ Copy Space")
st.markdown("---")

# 🌟 ปุ่มสลับโหมดหลัก 🌟
st.subheader("🎯 เลือกโหมดการทำงาน (Work Mode)")
work_mode = st.radio(
    "สลับชุดข้อมูลอัตโนมัติ:", 
    ["🏢 โหมดปกติ (Corporate & Business)", "🎄 โหมดเทศกาล (Holidays & Seasonal)"],
    horizontal=True
)
st.markdown("---")

# โหลดข้อมูลตามโหมดที่เลือก
current_scenes = SCENE_HOLIDAY if "เทศกาล" in work_mode else SCENE_NORMAL
current_lights = LIGHTING_HOLIDAY if "เทศกาล" in work_mode else LIGHTING_NORMAL

st.subheader("📍 กำหนดโครงสร้าง (Modules)")
col1, col2, col3 = st.columns(3)
with col1:
    scene = st.selectbox("1. SCENE (สถานที่)", ["Auto (สุ่ม)"] + current_scenes)
    lighting = st.selectbox("2. LIGHTING (แสง)", ["Auto (สุ่ม)"] + current_lights)
with col2:
    depth = st.selectbox("3. DEPTH (ความเบลอ)", ["Auto (สุ่ม)"] + DEPTH_LIST)
    composition = st.selectbox("4. COMPOSITION (พื้นที่ว่าง)", ["Auto (สุ่ม)"] + COMPOSITION_LIST)
with col3:
    mood = st.selectbox("5. MOOD / TONE", ["Auto (สุ่ม)"] + MOOD_TONE_LIST)
    use_case = st.selectbox("6. USE-CASE", ["Auto (สุ่ม)"] + USE_CASE_LIST)

st.markdown("---")

# --- ปุ่มประมวลผล ---
if st.button("🚀 รันระบบ (Generate Prompts)", use_container_width=True):
    prompts = []
    
    for i in range(prompt_count):
        sel_scene = random.choice(current_scenes) if scene == "Auto (สุ่ม)" else scene
        sel_light = random.choice(current_lights) if lighting == "Auto (สุ่ม)" else lighting
        sel_depth = random.choice(DEPTH_LIST) if depth == "Auto (สุ่ม)" else depth
        sel_comp = random.choice(COMPOSITION_LIST) if composition == "Auto (สุ่ม)" else composition
        sel_mood = random.choice(MOOD_TONE_LIST) if mood == "Auto (สุ่ม)" else mood
        sel_use = random.choice(USE_CASE_LIST) if use_case == "Auto (สุ่ม)" else use_case

        base_core = "empty commercial background for product placement, high-end stock photography, photorealistic"
        
        prompt_elements = [base_core, sel_scene, sel_light, sel_depth, sel_comp, f"{sel_mood} mood", sel_use]
        
        clean_base = ", ".join(prompt_elements)
        # ถ้าเป็นเทศกาล ดัน Stylize สูงขึ้นนิดหน่อยให้ภาพดูอลังการขึ้น
        stylize_value = random.randint(150, 300) if "เทศกาล" in work_mode else random.randint(100, 250)
        
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
        if negative_prompt:
            final_prompt += f" --no {negative_prompt.strip()}"
            
        prompts.append(final_prompt)
        
    st.session_state['prompts'] = prompts
    st.success(f"✅ เจนเรียบร้อย {prompt_count} Prompts สำหรับ {work_mode.split(' ')[1]}")

if 'prompts' in st.session_state:
    st.markdown("### 👀 ตัวอย่าง Prompt (5 รายการแรก)")
    for p in st.session_state['prompts'][:5]:
        st.code(p, language="text")
        
    prompt_text = "\n".join(st.session_state['prompts'])
    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ .txt", 
        data=prompt_text, 
        file_name="mj_prompts.txt", 
        mime="text/plain",
        use_container_width=True
    )
