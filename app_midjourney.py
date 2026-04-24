import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Background Master Pro: Ultimate Edition", page_icon="👑", layout="wide")

# ==========================================
# 🔧 ข้อมูลโมดูล (อัปเดต Everyday Life & Corporate)
# ==========================================

# --- 1. โหมดปกติ (Corporate & Everyday Life) - ครอบคลุมชีวิตประจำวัน ---
SCENE_NORMAL = [
    # --- 🏢 Corporate & Work ---
    "modern office hallway", "glass corridor", "startup workspace", 
    "meeting room", "city view through office glass", "minimalist desk surface",
    "clean architectural background", "abstract corporate space",
    # --- 🏫 Education (โรงเรียน/สถานศึกษา) ---
    "modern minimalist classroom with empty desks",
    "bright university library with bookshelves in background",
    "quiet school corridor with lockers and soft sunlight",
    "clean lecture hall interior with wooden textures",
    "minimalist study nook with a large window view",
    # --- 🏠 Home & Residential (บ้าน/ชีวิตส่วนตัว) ---
    "minimalist serene bedroom with soft morning light on bed", # ห้องนอน
    "clean modern bathroom with marble surfaces and white towels", # ห้องน้ำ
    "bright airy minimalist kitchen with clean countertops", # ห้องครัว
    "cozy living room with neutral-colored sofa and soft textures", # ห้องนั่งเล่น
    "organized laundry room with minimalist wooden shelves", # ห้องซักรีด
    "sunlit home office with a clean wooden desk setup", # มุมทำงานในบ้าน
    "minimalist pantry with neatly organized glass jars", # ห้องเก็บของ/ตู้กับข้าว
    # --- 🛒 Public & Daily Life (สถานที่สาธารณะ) ---
    "modern supermarket aisle with blurred products on shelves", # ซูเปอร์มาร์เก็ต
    "minimalist gym interior with clean wooden floors", # ฟิตเนส
    "urban bus stop with clean modern glass and metal", # ป้ายรถเมล์
    "modern train station platform with blurred city background", # สถานีรถไฟ
    "minimalist white-walled gallery or museum space", # แกลเลอรี
    "bright artisanal bakery window display area" # ร้านเบเกอรี่
]

LIGHTING_NORMAL = [
    "natural side lighting", "morning warm light", "sunset golden light", 
    "cool office light", "night artificial glow", "soft diffused daylight through windows"
]

# --- 2. โหมดเทศกาล (Holidays & Seasonal) ---
SCENE_HOLIDAY = [
    "[Jan] New Year's Day celebratory background",
    "[Jan-Feb] Lunar New Year traditional red and gold background",
    "[Feb] Valentine's Day romantic high-end restaurant interior",
    "[Apr] Songkran Festival bright summer background",
    "[Oct] Halloween spooky but elegant setup",
    "[Dec] Christmas luxury hotel lobby with tree"
]
LIGHTING_HOLIDAY = [
    "festive warm bokeh lighting", "red and gold ambient glow", 
    "soft romantic diffused light", "vibrant high-contrast summer sun"
]

# --- 3. โหมด 💎 Premium Product & High-End ---
SCENE_PREMIUM = [
    "smooth water surface with gentle ripples and a floating natural stone podium",
    "pastel plaster arches and geometric steps with soft botanical shadows",
    "frosted acrylic cylinder podium with subtle light reflections",
    "white marble pedestal surrounded by delicate floating white silk cloth",
    "brutalist raw concrete block with sharp harsh sunlight and graphic shadows",
    "sleek brushed metal circular podium in a dark minimalist tech environment",
    "matte black geometric platform with subtle minimalist edge lighting",
    "black obsidian podium with subtle gold accents in a dark moody studio",
    "wabi-sabi style textured clay podium with minimal dried foliage",
    "rich walnut wood slice serving as a premium rustic display stand",
    "terrazzo stone platform with soft dappled sunlight filtering through leaves",
    "marble counter in premium anti-aging wellness clinic",
    "bright clean energy showroom with large bright windows"
]
LIGHTING_PREMIUM = [
    "soft diffused studio lighting", 
    "high-end commercial lighting setup", 
    "dramatic spotlight with soft falloff", 
    "window light passing through sheer curtains",
    "clean bright shadowless lighting"
]

# --- โมดูลที่ใช้ร่วมกัน ---
DEPTH_LIST = ["heavy blur background", "medium depth of field", "light blur (semi sharp)"]
COMPOSITION_LIST = ["copy space left", "copy space right", "copy space center", "top copy space (vertical)", "empty space for product placement"]
MOOD_TONE_LIST = ["neutral corporate", "blue tech tone", "warm realistic", "clean airy minimalist", "earthy organic tones", "luxurious elegant tones"]
USE_CASE_LIST = ["minimal clean composition", "strong leading lines", "macro close-up texture", "wide banner composition", "vertical ad layout"]

# ==========================================
# ⚙️ UI Sidebar
# ==========================================
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

# ==========================================
# 🖼️ UI พื้นที่หลัก
# ==========================================
st.title("👑 Commercial Background Engine")
st.markdown("ระบบปั่น Prompt สายฉากหลัง ครอบคลุมตั้งแต่ Everyday Life ไปจนถึงงาน Premium Mockup")
st.markdown("---")

st.subheader("🎯 เลือกโหมดการทำงาน (Work Mode)")
work_mode = st.radio(
    "สลับชุดข้อมูลอัตโนมัติ:", 
    [
        "🏢 โหมดปกติ (Corporate & Everyday Life)", 
        "🎄 โหมดเทศกาล (Holidays & Seasonal)", 
        "💎 โหมด Premium Product (Podium & High-End)"
    ],
    horizontal=True
)

st.markdown("---")

if "Premium" in work_mode or "พรีเมียม" in work_mode:
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

if st.button("🚀 รันระบบ (Generate Prompts)", use_container_width=True):
    prompts = []
    for i in range(prompt_count):
        sel_scene_raw = random.choice(current_scenes) if scene == "Auto (สุ่ม)" else scene
        sel_scene = re.sub(r'\[.*?\]\s*', '', sel_scene_raw).strip()
        sel_light = random.choice(current_lights) if lighting == "Auto (สุ่ม)" else lighting
        sel_depth = random.choice(DEPTH_LIST) if depth == "Auto (สุ่ม)" else depth
        sel_comp = random.choice(COMPOSITION_LIST) if composition == "Auto (สุ่ม)" else composition
        sel_mood = random.choice(MOOD_TONE_LIST) if mood == "Auto (สุ่ม)" else mood
        sel_use = random.choice(USE_CASE_LIST) if use_case == "Auto (สุ่ม)" else use_case

        if "Premium" in work_mode or "พรีเมียม" in work_mode:
            base_core = "empty product mockup background, photorealistic still life photography, extreme high-end commercial asset"
        else:
            base_core = "empty commercial background for product placement, high-end stock photography, photorealistic"
        
        prompt_elements = [base_core, sel_scene, sel_light, sel_depth, sel_comp, f"{sel_mood} mood", sel_use]
        clean_base = ", ".join(prompt_elements)
        
        stylize_value = random.randint(50, 150) if "Premium" in work_mode else random.randint(100, 250)
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
    st.download_button(label="💾 ดาวน์โหลดไฟล์ .txt", data=prompt_text, file_name="mj_ultimate_prompts.txt", mime="text/plain", use_container_width=True)
