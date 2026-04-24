import streamlit as st
import random

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Background Master Pro", page_icon="🖼️", layout="wide")

# --- 🔧 6 โมดูลหลัก (ตามสูตรทำเงิน) ---
SCENE_LIST = [
    "modern office hallway", 
    "glass corridor", 
    "startup workspace", 
    "meeting room", 
    "city view through office glass"
]

LIGHTING_LIST = [
    "natural side lighting", 
    "morning warm light", 
    "sunset golden light", 
    "cool office light", 
    "night artificial glow"
]

DEPTH_LIST = [
    "heavy blur background", 
    "medium depth of field", 
    "light blur (semi sharp)"
]

COMPOSITION_LIST = [
    "copy space left", 
    "copy space right", 
    "copy space center", 
    "top copy space (vertical)"
]

MOOD_TONE_LIST = [
    "neutral corporate", 
    "blue tech tone", 
    "warm realistic", 
    "dark moody"
]

USE_CASE_LIST = [
    "minimal clean composition", 
    "strong leading lines", 
    "wide banner composition", 
    "vertical ad layout"
]

# --- UI Sidebar (ตั้งค่าระบบ) ---
with st.sidebar:
    st.header("⚙️ Settings")
    prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=200, step=10, value=50)
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=1)
    st.markdown("---")
    st.subheader("🛡️ Safety & Quality")
    # ล็อก Vector/3D ตามกฎเดิม และเพิ่ม people/person เพื่อกันภาพติดคน
    negative_prompt = st.text_area(
        "Negative Prompt (--no)", 
        value="vector, 3d, illustration, cartoon, render, text, watermark, logo, signatures, ugly, deformed, people, person", 
        height=100
    )
    st.info("💡 เพิ่มคำว่า 'people, person' ลงใน Negative Prompt เพื่อบังคับให้ได้พื้นหลังว่าง 100%")

# --- UI พื้นที่หลัก (Main Area) ---
st.title("🖼️ Commercial Background Engine")
st.markdown("ระบบปั่น Prompt สายฉากหลัง (Background) เว้นพื้นที่ Copy Space สำหรับงานโฆษณา")
st.markdown("---")

st.subheader("📍 กำหนดโครงสร้าง (Modules)")
st.caption("เลือกเจาะจงทีละค่า หรือปล่อย Auto เพื่อให้ระบบสุ่มสร้าง Variation ให้ไม่ซ้ำกัน")

col1, col2, col3 = st.columns(3)
with col1:
    scene = st.selectbox("1. SCENE (สถานที่)", ["Auto (สุ่ม)"] + SCENE_LIST)
    lighting = st.selectbox("2. LIGHTING (แสง)", ["Auto (สุ่ม)"] + LIGHTING_LIST)
with col2:
    depth = st.selectbox("3. DEPTH (ความเบลอ)", ["Auto (สุ่ม)"] + DEPTH_LIST)
    composition = st.selectbox("4. COMPOSITION (พื้นที่ว่าง)", ["Auto (สุ่ม)"] + COMPOSITION_LIST)
with col3:
    mood = st.selectbox("5. MOOD / TONE (โทนสี)", ["Auto (สุ่ม)"] + MOOD_TONE_LIST)
    use_case = st.selectbox("6. USE-CASE (การจัดวาง)", ["Auto (สุ่ม)"] + USE_CASE_LIST)

st.markdown("---")

# --- ปุ่มประมวลผล ---
if st.button("🚀 รันระบบ (Generate Background Prompts)", use_container_width=True):
    prompts = []
    
    for i in range(prompt_count):
        # ดึงค่า (ถ้าเลือก Auto ให้สุ่มจาก List)
        sel_scene = random.choice(SCENE_LIST) if scene == "Auto (สุ่ม)" else scene
        sel_light = random.choice(LIGHTING_LIST) if lighting == "Auto (สุ่ม)" else lighting
        sel_depth = random.choice(DEPTH_LIST) if depth == "Auto (สุ่ม)" else depth
        sel_comp = random.choice(COMPOSITION_LIST) if composition == "Auto (สุ่ม)" else composition
        sel_mood = random.choice(MOOD_TONE_LIST) if mood == "Auto (สุ่ม)" else mood
        sel_use = random.choice(USE_CASE_LIST) if use_case == "Auto (สุ่ม)" else use_case

        # ฐาน Prompt เพื่อบังคับความเป็นงาน Commercial
        base_core = "empty background for commercial product placement, high-end commercial stock photography, photorealistic"
        
        # ประกอบร่าง Prompt ตามโครงสร้าง 6 โมดูล
        prompt_elements = [
            base_core,
            sel_scene,
            sel_light,
            sel_depth,
            sel_comp,
            f"{sel_mood} mood",
            sel_use
        ]
        
        clean_base = ", ".join(prompt_elements)
        
        # สุ่มค่า Stylize เล็กน้อยเพื่อให้ Midjourney ไม่จำเจ
        stylize_value = random.randint(100, 250)
        
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
        if negative_prompt:
            final_prompt += f" --no {negative_prompt.strip()}"
            
        prompts.append(final_prompt)
        
    # บันทึกลง Session State
    st.session_state['prompts'] = prompts
    st.success(f"✅ สร้างสำเร็จ {prompt_count} Prompts (ฉากหลังสาย Ad-Ready ล้วนๆ)")

# แสดงผลและดาวน์โหลด
if 'prompts' in st.session_state:
    st.markdown("### 👀 Preview Prompts (5 รายการแรก)")
    for p in st.session_state['prompts'][:5]:
        st.code(p, language="text")
        
    prompt_text = "\n".join(st.session_state['prompts'])
    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ Prompts (.txt)", 
        data=prompt_text, 
        file_name="mj_background_prompts.txt", 
        mime="text/plain",
        use_container_width=True
    )
