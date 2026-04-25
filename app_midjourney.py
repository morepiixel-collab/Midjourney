import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Background Master Pro: Ultimate Edition", page_icon="👑", layout="wide")

# ==========================================
# 🔧 1. ข้อมูลโมดูล SCENE (แบ่ง 3 โหมด)
# ==========================================

# --- 🏢 โหมด 1: NORMAL (Corporate & Everyday Life) ---
SCENE_NORMAL = [
    "modern office hallway", "glass corridor", "startup workspace", 
    "meeting room", "city view through office glass", "minimalist desk surface",
    "clean architectural background", "abstract corporate space",
    "modern minimalist classroom with empty desks",
    "bright university library with bookshelves in background",
    "quiet school corridor with lockers and soft sunlight",
    "minimalist serene bedroom with soft morning light on bed",
    "clean modern bathroom with marble surfaces and white towels",
    "bright airy minimalist kitchen with clean countertops",
    "sunlit home office with a clean wooden desk setup",
    "modern supermarket aisle with blurred products on shelves",
    "minimalist gym interior with clean wooden floors",
    "bright artisanal bakery window display area"
]

# --- 🎄 โหมด 2: HOLIDAY (Seasonal Podiums เรียงตามเดือน) ---
SCENE_HOLIDAY = [
    "[Jan] New Year's Day celebratory background",
    "[Jan-Feb] Lunar New Year traditional red and gold background",
    "[Jan-Feb] premium red and gold lacquer podium for Lunar New Year product display",
    "[Feb] Valentine's Day romantic high-end restaurant interior",
    "[Feb] romantic frosted pink glass podium for Valentine's Day skincare ads",
    "[Mar] St. Patrick's Day green festive background",
    "[Mar] Holi Festival vibrant colorful background",
    "[Mar-Apr] Easter pastel spring background",
    "[Apr] Songkran Festival bright summer background",
    "[Apr] smooth white marble podium with soft water ripples for Songkran summer theme",
    "[Apr-May] Sakura Season peaceful spring background",
    "[May] Mother's Day warm elegant background",
    "[May-Jun] Dragon Boat Festival traditional Asian background",
    "[Jun] Father's Day masculine elegant background",
    "[Jul] Summer Vacation festive sunny background",
    "[Aug-Sep] Back to School modern educational background",
    "[Sep-Oct] Mid-Autumn Festival elegant night background",
    "[Oct] Halloween spooky but elegant setup",
    "[Oct-Nov] Diwali glowing lights festive background",
    "[Oct-Nov] luxury dark obsidian platform with glowing diya lamps for Diwali concept",
    "[Nov] Thanksgiving warm autumn harvest background",
    "[Nov] matte white geometric steps decorated with subtle autumn leaves for Thanksgiving",
    "[Nov] Black Friday / Cyber Monday retail shopping background",
    "[Nov] Loy Krathong beautiful night river background",
    "[Dec] Christmas luxury hotel lobby with tree",
    "[Dec] minimalist stone pedestal surrounded by elegant Christmas pine and soft bokeh",
    "[Dec] New Year's Eve glamorous countdown party background"
]

# --- 💎 โหมด 3: PREMIUM (High-End Product Mockup) ---
SCENE_PREMIUM = [
    "smooth water surface with gentle ripples and a floating natural stone podium",
    "pastel plaster arches and geometric steps with soft botanical shadows",
    "frosted acrylic cylinder podium with subtle light reflections",
    "white marble pedestal surrounded by delicate floating white silk cloth",
    "brutalist raw concrete block with sharp harsh sunlight and graphic shadows",
    "sleek brushed metal circular podium in a dark minimalist tech environment",
    "matte black geometric platform with subtle minimalist edge lighting",
    "black obsidian podium with subtle gold accents in a dark moody studio",
    "dark emerald velvet draped elegantly over a presentation pedestal",
    "wabi-sabi style textured clay podium with minimal dried foliage",
    "rich walnut wood slice serving as a premium rustic display stand",
    "terrazzo stone platform with soft dappled sunlight filtering through leaves",
    "marble counter in premium anti-aging wellness clinic",
    "bright clean energy showroom with large bright windows",
    "premium minimalist skincare laboratory counter"
]

# --- ข้อมูล Lighting, Depth, Tone ---
LIGHTING_NORMAL = ["natural side lighting", "morning warm light", "sunset golden light", "cool office light", "soft diffused daylight through windows"]
LIGHTING_HOLIDAY = ["festive warm bokeh lighting", "red and gold ambient glow", "soft romantic diffused light", "vibrant high-contrast summer sun"]
LIGHTING_PREMIUM = ["soft diffused studio lighting", "high-end commercial lighting setup", "dramatic spotlight with soft falloff", "clean bright shadowless lighting"]

DEPTH_LIST = ["heavy blur background", "medium depth of field", "light blur (semi sharp)"]
COMPOSITION_LIST = ["copy space left", "copy space right", "copy space center", "top copy space (vertical)", "empty space for product placement"]
MOOD_TONE_LIST = ["neutral corporate", "blue tech tone", "warm realistic", "clean airy minimalist", "earthy organic tones", "luxurious elegant tones", "festive vibrant", "dark moody"]
USE_CASE_LIST = ["minimal clean composition", "strong leading lines", "macro close-up texture", "wide banner composition", "vertical ad layout"]

# ==========================================
# 👑 2. UI: Master Controller (ต้องอยู่บนสุดเพื่อควบคุม Sidebar)
# ==========================================
st.title("👑 Commercial Background Engine")
st.markdown("ระบบผลิต Prompt ฉากหลังโฆษณา สำหรับโปรเจกต์รายได้ $1,000/เดือน")
st.markdown("---")

st.subheader("🎯 เลือกโหมดการทำงาน (Work Mode)")
work_mode = st.radio(
    "ระบบจะปรับค่า Default ของสัดส่วนภาพและ Negative Prompt ให้อัตโนมัติตามโหมดที่เลือก:", 
    [
        "🏢 โหมดปกติ (Corporate & Everyday Life)", 
        "🎄 โหมดเทศกาล (Seasonal & Holiday Podiums)", 
        "💎 โหมด Premium Product (Podium & High-End)"
    ],
    horizontal=True,
    index=2 # ล็อกให้เปิดแอปมาเจอโหมด Premium เป็นค่าเริ่มต้นเลย
)

st.markdown("---")

# ==========================================
# 🧠 3. Auto-Default Logic (ปรับค่าอัตโนมัติตามโหมด)
# ==========================================
if "Premium" in work_mode or "พรีเมียม" in work_mode:
    current_scenes, current_lights = SCENE_PREMIUM, LIGHTING_PREMIUM
    default_ar_index = 0 # 16:9 เหมาะกับโฆษณา Banner ที่สุด
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"
    mode_hint = "💡 ล็อกคำว่า 'product, bottle, box' ไว้ เพื่อบังคับให้ได้แท่นเปล่า 100%"
elif "เทศกาล" in work_mode:
    current_scenes, current_lights = SCENE_HOLIDAY, LIGHTING_HOLIDAY
    default_ar_index = 1 # 3:2 ครอบจักรวาล
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, text, watermark, logo, signatures, people, person, face, hand"
    mode_hint = "💡 กันคนและมือออกไป แต่ยอมให้มีสิ่งของตกแต่งเทศกาลได้"
else:
    current_scenes, current_lights = SCENE_NORMAL, LIGHTING_NORMAL
    default_ar_index = 1 # 3:2 ครอบจักรวาล
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, text, watermark, logo, signatures"
    mode_hint = "💡 โหมดปกติ (ไม่ได้บล็อกคนหรือสิ่งของ เผื่อเจนภาพซูเปอร์มาร์เก็ตหรือห้องเรียน)"

# ==========================================
# ⚙️ 4. UI Sidebar (รับค่าที่อัปเดตแล้วจาก Master Controller)
# ==========================================
with st.sidebar:
    st.header("⚙️ Settings")
    prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=500, step=10, value=50)
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=default_ar_index)
    
    st.markdown("---")
    st.subheader("🛡️ Quality Control")
    negative_prompt = st.text_area("Negative Prompt (--no)", value=default_neg_prompt, height=120)
    st.info(mode_hint)

    st.markdown("---")
    st.subheader("📌 คัมภีร์ 1,000 เหรียญ")
    with st.expander("📖 เปิดอ่านเคล็ดลับสายสต็อก", expanded=True):
        st.markdown("""
        **1. กฎ 3 เดือน (The 90-Day Rule):**
        อัปโหลดภาพเทศกาลล่วงหน้า 3 เดือนเสมอ (เช่น สงกรานต์ ส่งตั้งแต่ ม.ค.)
        
        **2. สัดส่วนภาพ (AR Strategy):**
        - `3:2` = เซฟสุด ขายได้กว้าง
        - `16:9` = สายโฆษณา Banner เว็บไซต์
        - `4:5` = สาย Social Media Ads
        *เทคนิค:* 1 Idea ควรแตกให้ครบทั้ง 3 สัดส่วน
        
        **3. โฟกัส "พื้นที่ใช้งาน":**
        ลูกค้าซื้อภาพไปทำงานต่อ Copy Space ต้องชัดเจน
        
        **4. SEO Metadata:**
        คุมความยาว Title (ชื่อภาพ) ให้อยู่ที่ **150 - 190 ตัวอักษร** ดัน SEO ได้แรงที่สุด
        """)

# ==========================================
# 📍 5. โครงสร้างโมดูลและการเจนภาพ
# ==========================================
st.subheader("📍 กำหนดโครงสร้างโมดูล (Modules)")
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

if st.button("🚀 Generate Master Prompts", use_container_width=True):
    prompts = []
    for i in range(prompt_count):
        sel_scene_raw = random.choice(current_scenes) if scene == "Auto (สุ่ม)" else scene
        sel_scene = re.sub(r'\[.*?\]\s*', '', sel_scene_raw).strip() 
        sel_light = random.choice(current_lights) if lighting == "Auto (สุ่ม)" else lighting
        sel_depth = random.choice(DEPTH_LIST) if depth == "Auto (สุ่ม)" else depth
        sel_comp = random.choice(COMPOSITION_LIST) if composition == "Auto (สุ่ม)" else composition
        sel_mood = random.choice(MOOD_TONE_LIST) if mood == "Auto (สุ่ม)" else mood
        sel_use = random.choice(USE_CASE_LIST) if use_case == "Auto (สุ่ม)" else use_case

        if "Premium" in work_mode or "พรีเมียม" in work_mode or ("เทศกาล" in work_mode and "podium" in sel_scene.lower()):
            base_core = "empty product mockup background, photorealistic still life photography, extreme high-end commercial asset"
        else:
            base_core = "empty commercial background for product placement, high-end stock photography, photorealistic"
        
        prompt_elements = [base_core, sel_scene, sel_light, sel_depth, sel_comp, f"{sel_mood} mood", sel_use]
        clean_base = ", ".join(prompt_elements)
        
        stylize_value = random.randint(50, 150) if "Premium" in work_mode else random.randint(150, 300) if "เทศกาล" in work_mode else random.randint(100, 250)
        
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
        if negative_prompt:
            final_prompt += f" --no {negative_prompt.strip()}"
        prompts.append(final_prompt)
        
    st.session_state['prompts'] = prompts
    st.success(f"✅ เจนเรียบร้อย {prompt_count} Prompts")

if 'prompts' in st.session_state:
    st.markdown("### 👀 Preview Prompts")
    for p in st.session_state['prompts'][:5]:
        st.code(p, language="text")
    prompt_text = "\n".join(st.session_state['prompts'])
    st.download_button(label="💾 ดาวน์โหลดไฟล์ .txt", data=prompt_text, file_name="mj_ultimate_prompts.txt", mime="text/plain", use_container_width=True)
