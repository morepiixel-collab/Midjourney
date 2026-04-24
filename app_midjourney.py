import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Background Master Pro: Ultimate Edition", page_icon="👑", layout="wide")

# --- 🔧 ข้อมูลโมดูล (แยก 3 หมวด: ปกติ, เทศกาล, ไฮเอนด์) ---

# 1. SCENE (โหมดปกติ - Corporate & Mass)
SCENE_NORMAL = [
    "modern office hallway", "glass corridor", "startup workspace", 
    "meeting room", "city view through office glass", "minimalist desk surface",
    "clean architectural background", "abstract corporate space"
]

# 2. SCENE (โหมดเทศกาล)
SCENE_HOLIDAY = [
    "[Jan-Feb] Lunar New Year traditional red and gold background",
    "[Feb] Valentine's Day romantic high-end restaurant interior",
    "[Apr] Songkran Festival bright summer background",
    "[Oct] Halloween spooky but elegant setup",
    "[Nov] Black Friday / Cyber Monday retail shopping background",
    "[Dec] Christmas luxury hotel lobby with tree"
] # ตัดมาเฉพาะตัวท็อปเพื่อความกระชับ

# 3. SCENE (โหมด 💎 Premium Product & Hyper-Niche) - โคตรของโคตรทำเงิน
SCENE_PREMIUM = [
    "minimalist natural stone podium for product display",
    "premium marble pedestal with soft shadows",
    "rustic wooden block on elegant neutral background",
    "sleek frosted glass display stand",
    "geometric matte white display platforms",
    "marble counter in premium anti-aging wellness clinic",
    "bright clean energy showroom with large bright windows",
    "luxury spa reception desk with organic textures",
    "high-tech minimalist electric vehicle display area",
    "premium minimalist skincare laboratory counter",
    "modern sustainable architecture lobby with indoor plants"
]

# LIGHTING (แยกตามโหมด)
LIGHTING_NORMAL = ["natural side lighting", "morning warm light", "sunset golden light", "cool office light"]
LIGHTING_HOLIDAY = ["festive warm bokeh lighting", "red and gold ambient glow", "soft romantic diffused light"]
LIGHTING_PREMIUM = [
    "soft diffused studio lighting", 
    "high-end commercial lighting setup", 
    "dramatic spotlight with soft falloff", 
    "window light passing through sheer curtains",
    "clean bright shadowless lighting"
]

# โมดูลที่ใช้ร่วมกัน
DEPTH_LIST = ["heavy blur background", "medium depth of field", "light blur (semi sharp)"]
COMPOSITION_LIST = ["copy space left", "copy space right", "copy space center", "top copy space (vertical)", "empty space for product placement"]
MOOD_TONE_LIST = ["neutral corporate", "blue tech tone", "warm realistic", "clean airy minimalist", "earthy organic tones", "luxurious elegant tones"]
USE_CASE_LIST = ["minimal clean composition", "strong leading lines", "macro close-up texture", "wide banner composition"]

# --- UI Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=200, step=10, value=50)
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=1)
    st.markdown("---")
    st.subheader("🛡️ Pure Photography Mode")
    negative_prompt = st.text_area(
        "Negative Prompt (--no)", 
        value="vector, 3d, illustration, cartoon, render, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box", 
        height=100
    )
    st.info("💡 เพิ่มคำว่า 'product, bottle, box' ลงไปในโหมดพรีเมียม เพื่อกันไม่ให้ AI วางสินค้าปลอมๆ ลงไปบนแท่น เราต้องการแค่ 'แท่นเปล่าๆ' ให้ลูกค้าเอาไปแต่งต่อเอง")

# --- UI พื้นที่หลัก ---
st.title("👑 Commercial Background Engine")
st.markdown("ระบบปั่น Prompt สายฉากหลังโฆษณา ครอบคลุมตั้งแต่งาน Mass ไปจนถึงงาน Premium Mockup")
st.markdown("---")

# 🌟 ปุ่มสลับโหมดหลัก 🌟
st.subheader("🎯 เลือกโหมดการทำงาน (Work Mode)")
work_mode = st.radio(
    "สลับชุดข้อมูลอัตโนมัติ:", 
    [
        "🏢 โหมดปกติ (Corporate & Mass)", 
        "🎄 โหมดเทศกาล (Holidays & Seasonal)", 
        "💎 โหมด Premium Product (Podium & High-End)"
    ],
    horizontal=True
)

st.markdown("---")

# โหลดข้อมูลตามโหมดที่เลือก
if "พรีเมียม" in work_mode or "Premium" in work_mode:
    current_scenes = SCENE_PREMIUM
    current_lights = LIGHTING_PREMIUM
elif "เทศกาล" in work_mode:
    current_scenes = SCENE_HOLIDAY
    current_lights = LIGHTING_HOLIDAY
else:
    current_scenes = SCENE_NORMAL
    current_lights = LIGHTING_NORMAL

st.subheader("📍 กำหนดโครงสร้าง (Modules)")
col1, col2, col3 = st.columns(3)
with col1:
    scene = st.selectbox("1. SCENE (สถานที่/แท่นวาง)", ["Auto (สุ่ม)"] + current_scenes)
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
        # สุ่มค่า
        sel_scene_raw = random.choice(current_scenes) if scene == "Auto (สุ่ม)" else scene
        sel_scene = re.sub(r'\[.*?\]\s*', '', sel_scene_raw).strip() # ตัดวงเล็บเดือนออก
        
        sel_light = random.choice(current_lights) if lighting == "Auto (สุ่ม)" else lighting
        sel_depth = random.choice(DEPTH_LIST) if depth == "Auto (สุ่ม)" else depth
        sel_comp = random.choice(COMPOSITION_LIST) if composition == "Auto (สุ่ม)" else composition
        sel_mood = random.choice(MOOD_TONE_LIST) if mood == "Auto (สุ่ม)" else mood
        sel_use = random.choice(USE_CASE_LIST) if use_case == "Auto (สุ่ม)" else use_case

        # ปรับ Base Core ให้คมขึ้นสำหรับงานพรีเมียม
        if "Premium" in work_mode:
            base_core = "empty product mockup background, photorealistic still life photography, extreme high-end commercial asset"
        else:
            base_core = "empty commercial background for product placement, high-end stock photography, photorealistic"
        
        prompt_elements = [base_core, sel_scene, sel_light, sel_depth, sel_comp, f"{sel_mood} mood", sel_use]
        
        clean_base = ", ".join(prompt_elements)
        
        # ปรับ Stylize
        if "Premium" in work_mode:
            stylize_value = random.randint(50, 150) # โหมดนี้ต้องการความ "จริง" สูงสุด ไม่ต้องให้ AI ปรุงแต่งเยอะ (Stylize ต่ำลง)
        elif "เทศกาล" in work_mode:
            stylize_value = random.randint(150, 300)
        else:
            stylize_value = random.randint(100, 250)
        
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
        if negative_prompt:
            final_prompt += f" --no {negative_prompt.strip()}"
            
        prompts.append(final_prompt)
        
    st.session_state['prompts'] = prompts
    st.success(f"✅ เจนเรียบร้อย {prompt_count} Prompts สำหรับโหมด {work_mode.split(' ')[1]}")

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
