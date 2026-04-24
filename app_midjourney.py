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
    # Corporate & Work
    "modern office hallway", "glass corridor", "startup workspace", 
    "meeting room", "city view through office glass", "minimalist desk surface",
    # Education 
    "modern minimalist classroom with empty desks",
    "bright university library with bookshelves in background",
    "quiet school corridor with lockers and soft sunlight",
    # Home & Residential
    "minimalist serene bedroom with soft morning light on bed",
    "clean modern bathroom with marble surfaces and white towels",
    "bright airy minimalist kitchen with clean countertops",
    "sunlit home office with a clean wooden desk setup",
    # Public & Daily Life
    "modern supermarket aisle with blurred products on shelves",
    "minimalist gym interior with clean wooden floors",
    "bright artisanal bakery window display area"
]

# --- 🎄 โหมด 2: HOLIDAY (Festivals & Seasonal Podiums เรียงตามเดือน) ---
SCENE_HOLIDAY = [
    # --- มกราคม (January) ---
    "[Jan] New Year's Day celebratory background",
    "[Jan-Feb] Lunar New Year traditional red and gold background",
    "[Jan-Feb] premium red and gold lacquer podium for Lunar New Year product display",
    
    # --- กุมภาพันธ์ (February) ---
    "[Feb] Valentine's Day romantic high-end restaurant interior",
    "[Feb] romantic frosted pink glass podium for Valentine's Day skincare ads",
    
    # --- มีนาคม (March) ---
    "[Mar] St. Patrick's Day green festive background",
    "[Mar] Holi Festival vibrant colorful background",
    "[Mar-Apr] Easter pastel spring background",
    
    # --- เมษายน (April) ---
    "[Apr] Songkran Festival bright summer background",
    "[Apr] smooth white marble podium with soft water ripples for Songkran summer theme",
    "[Apr-May] Sakura Season peaceful spring background",
    
    # --- พฤษภาคม (May) ---
    "[May] Mother's Day warm elegant background",
    "[May-Jun] Dragon Boat Festival traditional Asian background",
    
    # --- มิถุนายน (June) ---
    "[Jun] Father's Day masculine elegant background",
    
    # --- กรกฎาคม (July) ---
    "[Jul] Summer Vacation festive sunny background",
    
    # --- สิงหาคม (August) ---
    "[Aug-Sep] Back to School modern educational background",
    
    # --- กันยายน (September) ---
    "[Sep-Oct] Mid-Autumn Festival elegant night background",
    
    # --- ตุลาคม (October) ---
    "[Oct] Halloween spooky but elegant setup",
    "[Oct-Nov] Diwali glowing lights festive background",
    "[Oct-Nov] luxury dark obsidian platform with glowing diya lamps for Diwali concept",
    
    # --- พฤศจิกายน (November) ---
    "[Nov] Thanksgiving warm autumn harvest background",
    "[Nov] matte white geometric steps decorated with subtle autumn leaves for Thanksgiving",
    "[Nov] Black Friday / Cyber Monday retail shopping background",
    "[Nov] Loy Krathong beautiful night river background",
    
    # --- ธันวาคม (December) ---
    "[Dec] Christmas luxury hotel lobby with tree",
    "[Dec] minimalist stone pedestal surrounded by elegant Christmas pine and soft bokeh",
    "[Dec] New Year's Eve glamorous countdown party background"
]

# --- 💎 โหมด 3: PREMIUM (High-End Product Mockup) ---
SCENE_PREMIUM = [
    # Skincare & Cosmetics
    "smooth water surface with gentle ripples and a floating natural stone podium",
    "pastel plaster arches and geometric steps with soft botanical shadows",
    "frosted acrylic cylinder podium with subtle light reflections",
    "white marble pedestal surrounded by delicate floating white silk cloth",
    # Tech & Men's Grooming
    "brutalist raw concrete block with sharp harsh sunlight and graphic shadows",
    "sleek brushed metal circular podium in a dark minimalist tech environment",
    "matte black geometric platform with subtle minimalist edge lighting",
    # Luxury & Wellness
    "black obsidian podium with subtle gold accents in a dark moody studio",
    "wabi-sabi style textured clay podium with minimal dried foliage",
    "terrazzo stone platform with soft dappled sunlight filtering through leaves",
    # Premium Environments
    "marble counter in premium anti-aging wellness clinic",
    "bright clean energy showroom with large bright windows",
    "premium minimalist skincare laboratory counter"
]

# ==========================================
# 💡 2. ข้อมูลโมดูลอื่นๆ (Lighting, Depth, Tone)
# ==========================================

LIGHTING_NORMAL = ["natural side lighting", "morning warm light", "sunset golden light", "cool office light", "soft diffused daylight through windows"]
LIGHTING_HOLIDAY = ["festive warm bokeh lighting", "red and gold ambient glow", "soft romantic diffused light", "vibrant high-contrast summer sun"]
LIGHTING_PREMIUM = ["soft diffused studio lighting", "high-end commercial lighting setup", "dramatic spotlight with soft falloff", "clean bright shadowless lighting"]

DEPTH_LIST = ["heavy blur background", "medium depth of field", "light blur (semi sharp)"]
COMPOSITION_LIST = ["copy space left", "copy space right", "copy space center", "top copy space (vertical)", "empty space for product placement"]
MOOD_TONE_LIST = ["neutral corporate", "blue tech tone", "warm realistic", "clean airy minimalist", "earthy organic tones", "luxurious elegant tones", "festive vibrant", "dark moody"]
USE_CASE_LIST = ["minimal clean composition", "strong leading lines", "macro close-up texture", "wide banner composition", "vertical ad layout"]

# ==========================================
# ⚙️ 3. UI Sidebar (การตั้งค่า)
# ==========================================
with st.sidebar:
    st.header("⚙️ Settings")
    prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=500, step=10, value=50)
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=1)
    st.markdown("---")
    st.subheader("🛡️ Pure Photography Mode")
    negative_prompt = st.text_area(
        "Negative Prompt (--no)", 
        value="vector, 3d, illustration, cartoon, render, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box", 
        height=120
    )
    st.info("💡 คำว่า 'product, bottle, box' ถูกล็อกไว้เพื่อป้องกัน AI ใส่สินค้าปลอมลงบนแท่น เราต้องการขาย 'แท่นเปล่า' ให้ลูกค้าไปแต่งต่อ")

# ==========================================
# 🖼️ 4. UI พื้นที่หลัก (Main Engine)
# ==========================================
st.title("👑 Commercial Background Engine")
st.markdown("ระบบปั่น Prompt สายฉากหลังโฆษณา ครอบคลุมตั้งแต่ Everyday Life, เทศกาล ไปจนถึง Premium Mockup")
st.markdown("---")

# 🎯 เลือกโหมดการทำงาน
st.subheader("🎯 เลือกโหมดการทำงาน (Work Mode)")
work_mode = st.radio(
    "สลับชุดข้อมูลอัตโนมัติ:", 
    [
        "🏢 โหมดปกติ (Corporate & Everyday Life)", 
        "🎄 โหมดเทศกาล (Holidays & Seasonal Podiums)", 
        "💎 โหมด Premium Product (Podium & High-End)"
    ],
    horizontal=True
)

if "เทศกาล" in work_mode:
    st.info("💡 **กฎ 3 เดือน:** ควรเจนภาพและอัปโหลดล่วงหน้าอย่างน้อย 90 วันก่อนถึงเดือนของเทศกาลนั้นๆ เพื่อให้ AI ของ Adobe Stock ทำการ Index ทัน")

st.markdown("---")

# โหลดข้อมูลตามโหมดที่เลือก
if "Premium" in work_mode or "พรีเมียม" in work_mode:
    current_scenes, current_lights = SCENE_PREMIUM, LIGHTING_PREMIUM
elif "เทศกาล" in work_mode:
    current_scenes, current_lights = SCENE_HOLIDAY, LIGHTING_HOLIDAY
else:
    current_scenes, current_lights = SCENE_NORMAL, LIGHTING_NORMAL

# 📍 โครงสร้างโมดูล
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

# ==========================================
# 🚀 5. ระบบประมวลผล (Generation Logic)
# ==========================================
if st.button("🚀 รันระบบ (Generate Prompts)", use_container_width=True):
    prompts = []
    
    for i in range(prompt_count):
        # 5.1 สุ่มและคลีนค่า
        sel_scene_raw = random.choice(current_scenes) if scene == "Auto (สุ่ม)" else scene
        sel_scene = re.sub(r'\[.*?\]\s*', '', sel_scene_raw).strip() # ตัดแท็กเดือน [Jan] ออกเพื่อไม่ให้ Midjourney งง
        
        sel_light = random.choice(current_lights) if lighting == "Auto (สุ่ม)" else lighting
        sel_depth = random.choice(DEPTH_LIST) if depth == "Auto (สุ่ม)" else depth
        sel_comp = random.choice(COMPOSITION_LIST) if composition == "Auto (สุ่ม)" else composition
        sel_mood = random.choice(MOOD_TONE_LIST) if mood == "Auto (สุ่ม)" else mood
        sel_use = random.choice(USE_CASE_LIST) if use_case == "Auto (สุ่ม)" else use_case

        # 5.2 ปรับ Base Core ให้เข้ากับโหมด
        if "Premium" in work_mode or "พรีเมียม" in work_mode or ("เทศกาล" in work_mode and "podium" in sel_scene.lower()):
            base_core = "empty product mockup background, photorealistic still life photography, extreme high-end commercial asset"
        else:
            base_core = "empty commercial background for product placement, high-end stock photography, photorealistic"
        
        prompt_elements = [base_core, sel_scene, sel_light, sel_depth, sel_comp, f"{sel_mood} mood", sel_use]
        clean_base = ", ".join(prompt_elements)
        
        # 5.3 คุม Stylize ตามความเหมาะสมของโหมด
        if "Premium" in work_mode or "พรีเมียม" in work_mode:
            stylize_value = random.randint(50, 150) # เน้นสมจริงสุดๆ ไม่ฟุ้งเฟ้อ
        elif "เทศกาล" in work_mode:
            stylize_value = random.randint(150, 300) # ยอมให้จัดเต็มเรื่องเอฟเฟกต์แสงไฟเทศกาล
        else:
            stylize_value = random.randint(100, 250)
        
        # 5.4 ประกอบร่าง Prompt สุดท้าย
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
        if negative_prompt:
            final_prompt += f" --no {negative_prompt.strip()}"
            
        prompts.append(final_prompt)
        
    st.session_state['prompts'] = prompts
    st.success(f"✅ เจนเรียบร้อย {prompt_count} Prompts สำหรับโหมด {work_mode.split(' ')[1]}")

# ==========================================
# 👀 6. แสดงผลและดาวน์โหลด
# ==========================================
if 'prompts' in st.session_state:
    st.markdown("### 👀 ตัวอย่าง Prompt (5 รายการแรก)")
    for p in st.session_state['prompts'][:5]:
        st.code(p, language="text")
        
    prompt_text = "\n".join(st.session_state['prompts'])
    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ .txt", 
        data=prompt_text, 
        file_name="mj_master_prompts.txt", 
        mime="text/plain",
        use_container_width=True
    )
