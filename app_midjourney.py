import streamlit as st
import random

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Background Master Pro: Holiday Edition", page_icon="🖼️", layout="wide")

# --- 🔧 6 โมดูลหลัก (อัปเดตหมวดเทศกาล) ---
SCENE_LIST = [
    "modern office hallway", 
    "glass corridor", 
    "startup workspace", 
    "meeting room", 
    "city view through office glass",
    "luxury hotel lobby decorated for Christmas",
    "modern office entrance with Lunar New Year decor",
    "high-end restaurant interior for Valentine's",
    "minimalist startup lounge with festive decorations",
    "urban rooftop terrace with summer sunset view"
]

LIGHTING_LIST = [
    "natural side lighting", 
    "morning warm light", 
    "sunset golden light", 
    "cool office light", 
    "night artificial glow",
    "festive warm bokeh lighting",
    "red and gold ambient glow",
    "soft romantic diffused light",
    "vibrant high-contrast summer sun"
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
    "dark moody",
    "festive vibrant",
    "clean airy minimalist"
]

USE_CASE_LIST = [
    "minimal clean composition", 
    "strong leading lines", 
    "wide banner composition", 
    "vertical ad layout"
]

# --- UI Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=200, step=10, value=50)
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=1)
    st.markdown("---")
    st.subheader("🛡️ Pure Photography Mode")
    # บล็อกงานวาด และงานที่มีคน เพื่อให้ได้ Background คลีนๆ
    negative_prompt = st.text_area(
        "Negative Prompt (--no)", 
        value="vector, 3d, illustration, cartoon, render, text, watermark, logo, signatures, people, person, face, hand", 
        height=100
    )

# --- UI พื้นที่หลัก ---
st.title("🖼️ Commercial Background Engine (Holiday Ready)")
st.markdown("เน้นเจนฉากหลังสำหรับงานโฆษณาที่มี **Copy Space** และรองรับเทศกาลต่างๆ")
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    scene = st.selectbox("1. SCENE (เพิ่มหมวดเทศกาล)", ["Auto (สุ่ม)"] + SCENE_LIST)
    lighting = st.selectbox("2. LIGHTING (เพิ่มแสงเทศกาล)", ["Auto (สุ่ม)"] + LIGHTING_LIST)
with col2:
    depth = st.selectbox("3. DEPTH (ความเบลอ)", ["Auto (สุ่ม)"] + DEPTH_LIST)
    composition = st.selectbox("4. COMPOSITION (พื้นที่ว่าง)", ["Auto (สุ่ม)"] + COMPOSITION_LIST)
with col3:
    mood = st.selectbox("5. MOOD / TONE", ["Auto (สุ่ม)"] + MOOD_TONE_LIST)
    use_case = st.selectbox("6. USE-CASE", ["Auto (สุ่ม)"] + USE_CASE_LIST)

# --- ปุ่มประมวลผล ---
if st.button("🚀 Generate Holiday-Ready Backgrounds", use_container_width=True):
    prompts = []
    
    for i in range(prompt_count):
        sel_scene = random.choice(SCENE_LIST) if scene == "Auto (สุ่ม)" else scene
        sel_light = random.choice(LIGHTING_LIST) if lighting == "Auto (สุ่ม)" else lighting
        sel_depth = random.choice(DEPTH_LIST) if depth == "Auto (สุ่ม)" else depth
        sel_comp = random.choice(COMPOSITION_LIST) if composition == "Auto (สุ่ม)" else composition
        sel_mood = random.choice(MOOD_TONE_LIST) if mood == "Auto (สุ่ม)" else mood
        sel_use = random.choice(USE_CASE_LIST) if use_case == "Auto (สุ่ม)" else use_case

        # บังคับความเป็น Commercial Background
        base_core = "empty commercial background for product placement, high-end stock photography, photorealistic"
        
        prompt_elements = [
            base_core,
            sel_scene,
            sel_light,
            sel_depth,
            sel_comp,
            f"{sel_mood} mood",
            sel_use,
            "extremely high resolution, sharp focus on surface"
        ]
        
        clean_base = ", ".join(prompt_elements)
        stylize_value = random.randint(150, 300) # เพิ่มค่า Stylize เล็กน้อยสำหรับงานแนวเทศกาล
        
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
        if negative_prompt:
            final_prompt += f" --no {negative_prompt.strip()}"
            
        prompts.append(final_prompt)
        
    st.session_state['prompts'] = prompts
    st.success(f"✅ เจนเรียบร้อย {prompt_count} Prompts (พร้อมสำหรับโปรเจกต์ 1K USD)")

if 'prompts' in st.session_state:
    st.markdown("### 👀 ตัวอย่าง Prompt สำหรับนำไปใช้งาน")
    for p in st.session_state['prompts'][:5]:
        st.code(p, language="text")
        
    prompt_text = "\n".join(st.session_state['prompts'])
    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ .txt", 
        data=prompt_text, 
        file_name="holiday_bg_prompts.txt", 
        mime="text/plain",
        use_container_width=True
    )
