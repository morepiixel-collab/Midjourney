import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Commercial Master Engine: Pro-Max", page_icon="👑", layout="wide")

# ==========================================
# 🔧 1. ข้อมูลโมดูล SCENE (ปรับปรุงล่าสุดตามเทรนด์)
# ==========================================

# --- 🏢 โหมด 1: NORMAL (Everyday Commercial) ---
SCENE_NORMAL = [
    "modern office hallway", "glass corridor", "startup workspace", 
    "meeting room", "minimalist desk surface", "clean architectural background",
    "modern minimalist classroom with empty desks", "quiet school corridor with soft sunlight",
    "clean modern bathroom with marble surfaces and white towels",
    "bright airy minimalist kitchen with clean countertops",
    "modern supermarket aisle with blurred products on shelves",
    "bright artisanal bakery window display area"
]

# --- 🎄 โหมด 2: HOLIDAY (Seasonal Podiums) ---
SCENE_HOLIDAY = [
    "[Jan-Feb] premium red and gold lacquer podium for Lunar New Year product display",
    "[Feb] romantic frosted pink glass podium for Valentine's Day skincare ads",
    "[Apr] smooth white marble podium with soft water ripples for Songkran summer theme",
    "[Oct-Nov] luxury dark obsidian platform with glowing diya lamps for Diwali concept",
    "[Nov] matte white geometric steps decorated with subtle autumn leaves for Thanksgiving",
    "[Dec] minimalist stone pedestal surrounded by elegant Christmas pine and soft bokeh"
]

# --- 💎 โหมด 3: PREMIUM (Hyper-Specific & Liquid Texture) ---
SCENE_PREMIUM = [
    # สาย Texture & Liquid (เทรนด์ใหม่มาแรง)
    "frosted glass podium emerging from crystal clear rippling water",
    "minimalist stone pedestal surrounded by dynamic clear water splashes",
    # สาย Bathroom & Vanity
    "clean minimalist bathroom shelf with soft natural window light",
    "luxury vanity counter with marble surfaces and subtle bokeh reflections",
    # สาย Luxury & Tech
    "brutalist raw concrete block with sharp harsh sunlight and graphic shadows",
    "sleek brushed metal circular podium in a dark minimalist tech environment",
    "black obsidian podium with subtle gold accents in a dark moody studio",
    # สาย Sustainable Luxury
    "wabi-sabi style textured clay podium with organic dried foliage and soft light",
    "premium recycled stone platform with natural moss accents and dappled sunlight"
]

# ==========================================
# 📷 2. ข้อมูลโมดูลระดับ PRO (อัปเกรดใหม่)
# ==========================================

# แสงระดับตากล้องนิตยสาร
LIGHTING_PRO = [
    "soft diffused studio lighting", 
    "dramatic editorial hard spotlight with sharp shadows",
    "window light passing through sheer curtains",
    "clean bright shadowless e-commerce lighting"
]

# เลนส์และฟิล์ม (ฆ่าความปลอมของ AI)
CAMERA_LENS_LIST = [
    "shot on Hasselblad medium format, highly detailed",
    "shot on 100mm macro lens, sharp focus on surface texture",
    "Kodak Portra 400 film stock simulation, subtle film grain",
    "85mm lens, creamy bokeh background, professional depth of field"
]

# การจัดเลย์เอาต์เผื่อ UI / Ads
UI_LAYOUT_LIST = [
    "wide empty copy space on the left for typography",
    "wide empty copy space on the right for UI elements",
    "centered product placement with negative space at the top",
    "lower third empty space for ad copy and buttons",
    "perfectly balanced negative space for magazine layout"
]

# จิตวิทยาสี (Color Psychology)
COLOR_PSYCHOLOGY_LIST = [
    "clinical cyan and stark white tones (Skincare)",
    "charcoal and matte black tones (Men's grooming & Tech)",
    "earthy organic neutral tones (Sustainable & Wellness)",
    "luxurious rich emerald and gold tones (High-end Jewelry)",
    "soft pastel holographic tones (Gen-Z Beauty)"
]

# ==========================================
# 👑 3. UI: Master Controller
# ==========================================
st.title("👑 Commercial Master Engine: Pro-Max")
st.markdown("ระบบผลิต Prompt ระดับ High-End Commercial (เจาะลึก Lens, Film Stock และ UI Layout)")
st.markdown("---")

st.subheader("🎯 เลือกโหมดการทำงาน (Work Mode)")
work_mode = st.radio(
    "ระบบปรับค่า Aspect Ratio และ Negative Prompt อัตโนมัติ:", 
    [
        "🏢 โหมดปกติ (Corporate & Everyday Life)", 
        "🎄 โหมดเทศกาล (Seasonal Podiums)", 
        "💎 โหมด Premium Product (Podium & High-End)"
    ],
    horizontal=True,
    index=2
)
st.markdown("---")

# ==========================================
# 🧠 4. Auto-Default Logic
# ==========================================
if "Premium" in work_mode or "พรีเมียม" in work_mode:
    current_scenes = SCENE_PREMIUM
    default_ar_index = 0 # 16:9 
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, octane render, unreal engine, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"
elif "เทศกาล" in work_mode:
    current_scenes = SCENE_HOLIDAY
    default_ar_index = 1 # 3:2 
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"
else:
    current_scenes = SCENE_NORMAL
    default_ar_index = 1 # 3:2 
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, text, watermark, logo, signatures"

# ==========================================
# ⚙️ 5. UI Sidebar
# ==========================================
with st.sidebar:
    st.header("⚙️ Settings")
    prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=500, step=10, value=50)
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=default_ar_index)
    
    st.markdown("---")
    st.subheader("🛡️ Strict Photo Mode")
    negative_prompt = st.text_area("Negative Prompt (--no)", value=default_neg_prompt, height=140)

    st.markdown("---")
    st.subheader("📌 คัมภีร์ Pro-Max")
    with st.expander("📖 อ่านเคล็ดลับการเจน", expanded=True):
        st.markdown("""
        **1. ฆ่า AI ด้วย Lens:** ระบบฝังคำว่า Hasselblad, Kodak Portra ไว้ เพื่อให้ได้ Texture ภาพถ่ายจริง
        
        **2. UI-Driven Layout:** เลย์เอาต์ถูกออกแบบมาให้เผื่อที่วาง "ปุ่มกด" หรือ "Text" ซื้อไปทำโฆษณาได้ทันที
        
        **3. แนวตั้งมาแรง (9:16 / 4:5):** ตลาด Reels/TikTok กำลังโต อย่าลืมเจนสัดส่วนแนวตั้ง
        """)

# ==========================================
# 📍 6. โครงสร้างโมดูล
# ==========================================
st.subheader("📍 กำหนดโครงสร้าง (Pro Modules)")
col1, col2, col3 = st.columns(3)
with col1:
    scene = st.selectbox("1. SCENE (แท่นวาง)", ["Auto (สุ่ม)"] + current_scenes)
    lighting = st.selectbox("2. LIGHTING (แสงแมกกาซีน)", ["Auto (สุ่ม)"] + LIGHTING_PRO)
with col2:
    camera = st.selectbox("3. CAMERA & LENS (กล้อง/ฟิล์ม)", ["Auto (สุ่ม)"] + CAMERA_LENS_LIST)
    ui_layout = st.selectbox("4. UI LAYOUT (เผื่อปุ่ม/Text)", ["Auto (สุ่ม)"] + UI_LAYOUT_LIST)
with col3:
    color_psych = st.selectbox("5. COLOR PSYCHOLOGY (จิตวิทยาสี)", ["Auto (สุ่ม)"] + COLOR_PSYCHOLOGY_LIST)

# ==========================================
# 🚀 7. ระบบประมวลผล
# ==========================================
if st.button("🚀 Generate PRO Prompts", use_container_width=True):
    prompts = []
    for i in range(prompt_count):
        sel_scene_raw = random.choice(current_scenes) if scene == "Auto (สุ่ม)" else scene
        sel_scene = re.sub(r'\[.*?\]\s*', '', sel_scene_raw).strip() 
        sel_light = random.choice(LIGHTING_PRO) if lighting == "Auto (สุ่ม)" else lighting
        sel_cam = random.choice(CAMERA_LENS_LIST) if camera == "Auto (สุ่ม)" else camera
        sel_ui = random.choice(UI_LAYOUT_LIST) if ui_layout == "Auto (สุ่ม)" else ui_layout
        sel_color = random.choice(COLOR_PSYCHOLOGY_LIST) if color_psych == "Auto (สุ่ม)" else color_psych

        # ฐาน Prompt ที่โหดที่สุด
        base_core = "empty product mockup background, extreme high-end commercial asset, photography award winner"
        
        prompt_elements = [base_core, sel_scene, sel_light, sel_cam, sel_color, sel_ui]
        clean_base = ", ".join(prompt_elements)
        
        # Stylize ต่ำเสมอ เพื่อรักษาความดิบสมจริงของเลนส์และฟิล์ม
        stylize_value = random.randint(50, 100) if "Premium" in work_mode else random.randint(100, 200)
        
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
        if negative_prompt:
            final_prompt += f" --no {negative_prompt.strip()}"
        prompts.append(final_prompt)
        
    st.session_state['prompts'] = prompts
    st.success(f"✅ เจนเรียบร้อย {prompt_count} Prompts (Pro-Max Edition)")

if 'prompts' in st.session_state:
    st.markdown("### 👀 Preview Prompts")
    for p in st.session_state['prompts'][:5]:
        st.code(p, language="text")
    prompt_text = "\n".join(st.session_state['prompts'])
    st.download_button(label="💾 ดาวน์โหลดไฟล์ .txt", data=prompt_text, file_name="mj_promax_prompts.txt", mime="text/plain", use_container_width=True)
