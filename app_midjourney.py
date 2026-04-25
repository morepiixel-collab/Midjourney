import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Commercial Engine: GOD MODE", page_icon="⚡", layout="wide")

# ==========================================
# 📂 1. ฐานข้อมูล SCENE แบบแยกหมวดหมู่ (Dictionary)
# ==========================================

# --- 🏢 โหมด 1: NORMAL (Everyday Commercial) ---
SCENE_NORMAL_DICT = {
    "💼 Corporate & Workspace": [
        "modern office hallway", "glass corridor", "startup workspace", 
        "meeting room", "minimalist desk surface", "clean architectural background"
    ],
    "🏫 Education": [
        "modern minimalist classroom with empty desks", "quiet school corridor with soft sunlight",
        "bright university library with bookshelves in background"
    ],
    "🏠 Home & Daily Life": [
        "clean modern bathroom with marble surfaces and white towels",
        "bright airy minimalist kitchen with clean countertops",
        "modern supermarket aisle with blurred products on shelves",
        "bright artisanal bakery window display area"
    ]
}

# --- 🎄 โหมด 2: HOLIDAY (Seasonal Podiums) ---
SCENE_HOLIDAY_DICT = {
    "🧧 Jan-Feb (New Year & Valentine)": [
        "[Jan] New Year's Day celebratory background",
        "[Jan-Feb] premium red and gold lacquer podium for Lunar New Year product display",
        "[Feb] romantic frosted pink glass podium for Valentine's Day skincare ads"
    ],
    "💦 Apr (Songkran & Spring)": [
        "[Apr] smooth white marble podium with soft water ripples for Songkran summer theme",
        "[Apr-May] Sakura Season peaceful spring background"
    ],
    "🎃 Oct-Nov (Halloween & Diwali & Black Friday)": [
        "[Oct] Halloween spooky but elegant setup",
        "[Oct-Nov] luxury dark obsidian platform with glowing diya lamps for Diwali concept",
        "[Nov] matte white geometric steps decorated with subtle autumn leaves for Thanksgiving",
        "[Nov] Black Friday retail shopping background"
    ],
    "🎄 Dec (Christmas & Countdown)": [
        "[Dec] minimalist stone pedestal surrounded by elegant Christmas pine and soft bokeh",
        "[Dec] Christmas luxury hotel lobby with tree",
        "[Dec] New Year's Eve glamorous countdown party background"
    ]
}

# --- 💎 โหมด 3: PREMIUM (The 12 Pillars of Commercial Mockup) ---
SCENE_PREMIUM_DICT = {
    "🧴 Skincare & Hydration": [
        "frosted glass cylinder podium emerging from crystal clear rippling water",
        "minimalist natural stone pedestal surrounded by dynamic clear water splashes",
        "smooth water surface with gentle ripples and a floating acrylic display block"
    ],
    "🥼 Clinical & Dermocosmetics": [
        "sterile white marble podium in a bright minimalist skincare laboratory",
        "premium brushed stainless steel medical pedestal in a clean white environment",
        "minimalist white geometric steps in a pristine anti-aging clinic setting"
    ],
    "💎 High-End Luxury": [
        "black obsidian podium with subtle gold marble veins in a dark moody studio",
        "presentation pedestal elegantly draped in flowing dark emerald velvet",
        "white marble display stand surrounded by delicate floating white silk cloth"
    ],
    "🌿 Organic & Wellness": [
        "wabi-sabi style textured clay podium with minimal organic dried foliage",
        "premium terrazzo stone platform with soft dappled sunlight filtering through leaves",
        "rough natural sandstone pedestal set against a clean warm beige background"
    ],
    "💻 Tech & Men's Grooming": [
        "brutalist raw concrete block with sharp harsh sunlight and graphic shadows",
        "sleek brushed gunmetal circular podium in a dark minimalist tech environment",
        "matte black geometric platform with subtle minimalist edge lighting"
    ],
    "🍭 Gen-Z & Pop Cosmetics": [
        "pastel pink geometric acrylic display blocks with playful sharp shadows",
        "minimalist matte colorful arches and steps with soft studio lighting",
        "translucent holographic glass podium in a bright airy studio"
    ],
    "☕ Edibles & Supplements": [
        "rich rustic walnut wood slice serving as a premium display stand",
        "dark rough slate stone podium with subtle warm natural lighting",
        "clean white kitchen marble countertop podium with soft morning light"
    ],
    "🏋️‍♂️ Fitness & Sports Nutrition": [
        "matte black rubberized texture podium in a moody athletic gym environment",
        "perforated dark steel industrial pedestal with subtle cool rim lighting"
    ],
    "👶 Baby & Maternity": [
        "soft pure cotton draped over a gentle rounded podium in bright airy light",
        "smooth matte ceramic pastel podium resting on soft white fluffy cloud-like textures"
    ],
    "♻️ Eco-Sustainability": [
        "premium compressed recycled paper block serving as a sustainable product podium",
        "raw packed earth pedestal with natural green moss accents and dappled sunlight"
    ],
    "🔮 Ethereal & Abstract": [
        "floating crystal prism podium creating subtle rainbow light refractions",
        "abstract curved alabaster stone pedestal in a surreal minimalist white space"
    ],
    "🛁 Bathroom Shelf": [
        "clean minimalist bathroom shelf with soft natural window light and subtle steam",
        "luxury vanity counter with marble surfaces and subtle bokeh reflections"
    ]
}

# ==========================================
# 📷 2. ข้อมูลโมดูลระดับ PRO
# ==========================================
LIGHTING_PRO = [
    "soft diffused studio lighting", 
    "dramatic editorial hard spotlight with sharp shadows",
    "window light passing through sheer curtains",
    "clean bright shadowless e-commerce lighting"
]

CAMERA_LENS_LIST = [
    "shot on Hasselblad medium format, highly detailed",
    "shot on 100mm macro lens, sharp focus on surface texture",
    "Kodak Portra 400 film stock simulation, subtle film grain",
    "85mm lens, creamy bokeh background, professional depth of field"
]

UI_LAYOUT_LIST = [
    "wide empty copy space on the left for typography",
    "wide empty copy space on the right for UI elements",
    "centered product placement with negative space at the top",
    "lower third empty space for ad copy and buttons",
    "perfectly balanced negative space for magazine layout"
]

COLOR_PSYCHOLOGY_LIST = [
    "clinical cyan and stark white tones",
    "charcoal and matte black tones",
    "earthy organic neutral tones",
    "luxurious rich emerald and gold tones",
    "soft pastel holographic tones",
    "vibrant high-contrast complementary colors"
]

# ==========================================
# ⚡ 3. UI: Master Controller (โหมดทำงาน)
# ==========================================
st.title("⚡ Commercial Engine: GOD MODE")
st.markdown("ระบบผลิต Prompt โฆษณาระดับ Art Director (แยกหมวดอุตสาหกรรม + UI Layout + Medium Format)")
st.markdown("---")

st.subheader("🎯 ขั้นตอนที่ 1: เลือกโหมดการทำงานหลัก")
work_mode = st.radio(
    "ระบบจะปรับค่า Aspect Ratio และฐานข้อมูลอัตโนมัติ:", 
    [
        "🏢 โหมดปกติ (Corporate & Everyday)", 
        "🎄 โหมดเทศกาล (Seasonal Podiums)", 
        "💎 โหมด Premium Product (Podium & High-End)"
    ],
    horizontal=True,
    index=2
)

# ดึง Dictionary ตามโหมดที่เลือก
if "Premium" in work_mode or "พรีเมียม" in work_mode:
    current_dict = SCENE_PREMIUM_DICT
    default_ar_index = 0 # 16:9 
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, octane render, unreal engine, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"
elif "เทศกาล" in work_mode:
    current_dict = SCENE_HOLIDAY_DICT
    default_ar_index = 1 # 3:2 
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"
else:
    current_dict = SCENE_NORMAL_DICT
    default_ar_index = 1 # 3:2 
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, text, watermark, logo, signatures"

st.markdown("---")

# ==========================================
# 🏭 4. UI: Industry Selector (อัปเกรด God Mode)
# ==========================================
st.subheader("🏭 ขั้นตอนที่ 2: เลือกหมวดอุตสาหกรรมเป้าหมาย (Industry)")
industry_options = ["🌟 รวมทุกหมวด (All)"] + list(current_dict.keys())
selected_industry = st.selectbox("เลือกอุตสาหกรรม (เพื่อคัดกรองสถานที่และแท่นวาง):", industry_options)

# เตรียม List ของ Scene ตามอุตสาหกรรมที่เลือก
if selected_industry == "🌟 รวมทุกหมวด (All)":
    # นำ Scene ทุกหมวดย่อยมารวมกันเป็น List เดียว
    available_scenes = [scene for sublist in current_dict.values() for scene in sublist]
else:
    # ดึงมาเฉพาะหมวดที่เลือก
    available_scenes = current_dict[selected_industry]

st.markdown("---")

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
    st.info("⚡ **God Mode Active:** ระบบ Auto จะดึงข้อมูลเฉพาะอุตสาหกรรมที่คุณเลือกเท่านั้น ไม่ผสมมั่ว")

# ==========================================
# 📍 6. โครงสร้างโมดูล
# ==========================================
st.subheader("📍 ขั้นตอนที่ 3: กำหนดโครงสร้าง (Pro Modules)")
col1, col2, col3 = st.columns(3)
with col1:
    scene = st.selectbox("1. SCENE (แท่นวางที่ผ่านการคัดกรองแล้ว)", ["Auto (สุ่ม)"] + available_scenes)
    lighting = st.selectbox("2. LIGHTING (แสงแมกกาซีน)", ["Auto (สุ่ม)"] + LIGHTING_PRO)
with col2:
    camera = st.selectbox("3. CAMERA & LENS (กล้อง/ฟิล์ม)", ["Auto (สุ่ม)"] + CAMERA_LENS_LIST)
    ui_layout = st.selectbox("4. UI LAYOUT (เผื่อปุ่ม/Text)", ["Auto (สุ่ม)"] + UI_LAYOUT_LIST)
with col3:
    color_psych = st.selectbox("5. COLOR PSYCHOLOGY (จิตวิทยาสี)", ["Auto (สุ่ม)"] + COLOR_PSYCHOLOGY_LIST)

# ==========================================
# 🚀 7. ระบบประมวลผล
# ==========================================
if st.button("🚀 Generate GOD MODE Prompts", use_container_width=True):
    prompts = []
    for i in range(prompt_count):
        # ระบบสุ่ม Scene อัจฉริยะ (สุ่มเฉพาะใน available_scenes)
        sel_scene_raw = random.choice(available_scenes) if scene == "Auto (สุ่ม)" else scene
        sel_scene = re.sub(r'\[.*?\]\s*', '', sel_scene_raw).strip() # ตัดเดือนออกเผื่อเป็นหมวดเทศกาล
        
        sel_light = random.choice(LIGHTING_PRO) if lighting == "Auto (สุ่ม)" else lighting
        sel_cam = random.choice(CAMERA_LENS_LIST) if camera == "Auto (สุ่ม)" else camera
        sel_ui = random.choice(UI_LAYOUT_LIST) if ui_layout == "Auto (สุ่ม)" else ui_layout
        sel_color = random.choice(COLOR_PSYCHOLOGY_LIST) if color_psych == "Auto (สุ่ม)" else color_psych

        # ฐาน Prompt
        base_core = "empty product mockup background, extreme high-end commercial asset, photography award winner"
        
        prompt_elements = [base_core, sel_scene, sel_light, sel_cam, sel_color, sel_ui]
        clean_base = ", ".join(prompt_elements)
        
        # Stylize ต่ำเสมอ เพื่อรักษาความดิบสมจริง
        stylize_value = random.randint(50, 100) if "Premium" in work_mode else random.randint(100, 200)
        
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
        if negative_prompt:
            final_prompt += f" --no {negative_prompt.strip()}"
        prompts.append(final_prompt)
        
    st.session_state['prompts'] = prompts
    st.success(f"✅ เจนเรียบร้อย {prompt_count} Prompts (หมวด: {selected_industry})")

if 'prompts' in st.session_state:
    st.markdown("### 👀 Preview Prompts")
    for p in st.session_state['prompts'][:5]:
        st.code(p, language="text")
    prompt_text = "\n".join(st.session_state['prompts'])
    
    # ตั้งชื่อไฟล์ดาวน์โหลดให้ฉลาดขึ้น ตามอุตสาหกรรมที่เลือก
    safe_filename_mode = work_mode.split(' ')[0]
    safe_filename_ind = selected_industry.split(' ')[1] if selected_industry != "🌟 รวมทุกหมวด (All)" else "All_Industries"
    file_name = f"mj_{safe_filename_mode}_{safe_filename_ind}_prompts.txt"
    
    st.download_button(label=f"💾 ดาวน์โหลดไฟล์ .txt ({file_name})", data=prompt_text, file_name=file_name, mime="text/plain", use_container_width=True)
