import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Commercial Engine: ABSOLUTE GOD MODE", page_icon="⚡", layout="wide")

# ==========================================
# 🧬 1. Master DNA Database (เพิ่มหมวดสัตว์และยานยนต์)
# ==========================================

INDUSTRY_DNA = {
    # ---------------- 💎 สาย PREMIUM ----------------
    "🧴 Skincare & Hydration": {
        "scenes": ["frosted glass cylinder podium emerging from crystal clear rippling water", "minimalist natural stone pedestal surrounded by dynamic clear water splashes"],
        "lights": ["soft diffused studio lighting", "clean bright shadowless e-commerce lighting", "ethereal soft rim lighting"],
        "cameras": ["shot on 100mm macro lens, sharp focus on water droplets", "85mm lens, creamy bokeh background"],
        "uis": ["wide empty copy space on the left for cosmetics typography", "centered product placement with clean negative space"],
        "colors": ["clinical cyan and stark white tones", "refreshing aquatic blue and pure white"]
    },
    "🐾 Pet Food & Pet Care": { # --- เพิ่มใหม่ ---
        "scenes": ["rustic light oak wooden podium on a clean sunlit kitchen floor", "matte ceramic pedestal surrounded by fresh organic ingredients like carrots and greens", "minimalist wooden stand in a bright airy pet-friendly living room"],
        "lights": ["warm natural morning sunlight", "soft airy high-key studio lighting"],
        "cameras": ["low angle pet-eye view shot on 50mm lens", "shot on 85mm, soft natural depth of field"],
        "uis": ["top copy space for pet brand logo", "wide empty space on the right for nutrition facts"],
        "colors": ["warm earthy browns and leafy greens", "soft yellow and cream tones", "vibrant friendly orange and teal"]
    },
    "🚗 Automotive & Parts": { # --- เพิ่มใหม่ ---
        "scenes": ["high-tech carbon fiber display platform in a modern dark garage", "brushed aluminum circular podium with industrial asphalt texture", "forged steel pedestal with sharp geometric lines and metallic surfaces"],
        "lights": ["dramatic hard edge lighting to highlight metallic curves", "cool blue industrial studio lighting with sharp highlights"],
        "cameras": ["shot on Hasselblad medium format, extreme detail on metal texture", "wide angle 24mm lens for heroic scale"],
        "uis": ["side copy space for technical specifications", "lower third space for automotive brand name"],
        "colors": ["metallic silver and deep charcoal blacks", "high-contrast racing red and black", "electric blue and dark slate"]
    },
    "💻 Tech & Men's Grooming": {
        "scenes": ["brutalist raw concrete block with graphic shadows", "sleek brushed gunmetal circular podium in a dark tech environment"],
        "lights": ["dramatic editorial hard spotlight with sharp shadows", "minimalist neon edge lighting"],
        "cameras": ["shot on Hasselblad medium format, extreme high contrast", "sharp digital medium format"],
        "uis": ["wide empty copy space on the right for tech specs", "lower third empty space for UI buttons"],
        "colors": ["charcoal and matte black tones with subtle silver", "dark moody cyber tones"]
    },
    "🌿 Organic & Wellness": {
        "scenes": ["wabi-sabi style textured clay podium with organic dried foliage", "premium terrazzo stone platform with moss accents"],
        "lights": ["soft dappled sunlight filtering through leaves", "warm morning golden hour lighting"],
        "cameras": ["Kodak Portra 400 film stock simulation", "shot on 50mm lens, natural documentary style"],
        "uis": ["balanced negative space for magazine layout", "top copy space for organic branding"],
        "colors": ["earthy organic neutral tones", "warm beige, terracotta, and muted sage green"]
    },
    "💎 High-End Luxury": {
        "scenes": ["black obsidian podium with subtle gold marble veins", "presentation pedestal elegantly draped in flowing dark emerald velvet"],
        "lights": ["dramatic elegant spotlighting with soft falloff", "moody studio lighting with gold reflections"],
        "cameras": ["shot on 85mm f/1.4, luxurious creamy bokeh", "high-end editorial style"],
        "uis": ["centered minimalist composition", "elegant top negative space for serif typography"],
        "colors": ["luxurious rich emerald and gold tones", "deep burgundy and polished brass accents"]
    },
    "🍭 Gen-Z & Pop Cosmetics": {
        "scenes": ["pastel pink geometric acrylic display blocks", "minimalist matte colorful arches and steps"],
        "lights": ["bright high-key studio lighting", "playful colored gel lighting setup"],
        "cameras": ["crisp commercial digital photography", "flash photography style with distinct shadows"],
        "uis": ["dynamic asymmetrical layout", "bold center placement"],
        "colors": ["vibrant high-contrast complementary colors", "soft pastel holographic and neon tones"]
    },
    "🎄 Seasonal & Festive": {
        "scenes": ["premium red and gold lacquer podium", "minimalist stone pedestal with Christmas pine and soft bokeh"],
        "lights": ["warm festive ambient glow", "festive warm bokeh lighting"],
        "cameras": ["85mm lens, professional depth of field", "50mm lens, holiday lights bokeh"],
        "uis": ["wide empty copy space for festive promos", "centered seasonal greeting layout"],
        "colors": ["auspicious red and gold", "pine green, warm gold, and snow white"]
    },
    "💼 Corporate & Daily": {
        "scenes": ["modern office hallway glass corridor", "minimalist desk surface", "clean modern bathroom with marble"],
        "lights": ["natural side lighting", "cool clean office daylight"],
        "cameras": ["standard architectural photography lens", "crisp wide angle commercial shot"],
        "uis": ["wide banner composition for web headers", "standard rule of thirds"],
        "colors": ["neutral corporate blue and gray", "clean bright everyday color palette"]
    }
}

# ==========================================
# ⚡ 2. UI: Master Controller
# ==========================================
st.title("⚡ ABSOLUTE GOD MODE: Commercial Engine")
st.markdown("ระบบผลิต Prompt ที่รวมหมวด **'อาหารสัตว์'** และ **'ยานยนต์'** พร้อมล็อก DNA แสง สี กล้อง 100%")
st.markdown("---")

st.subheader("🏭 เลือกหมวดอุตสาหกรรมเป้าหมาย (Industry DNA)")
industry_options = ["🌟 สุ่มผสมทุกหมวด (All Industries)"] + list(INDUSTRY_DNA.keys())
selected_industry = st.selectbox("เลือกอุตสาหกรรมที่ต้องการเจาะตลาด:", industry_options, index=2) # Default ที่ Pet Food เพื่อให้ลองดูหมวดใหม่

# ==========================================
# 🧠 3. DNA Extraction Logic
# ==========================================
if selected_industry == "🌟 สุ่มผสมทุกหมวด (All Industries)":
    available_scenes = list(set([item for sublist in [dna["scenes"] for dna in INDUSTRY_DNA.values()] for item in sublist]))
    available_lights = list(set([item for sublist in [dna["lights"] for dna in INDUSTRY_DNA.values()] for item in sublist]))
    available_cameras = list(set([item for sublist in [dna["cameras"] for dna in INDUSTRY_DNA.values()] for item in sublist]))
    available_uis = list(set([item for sublist in [dna["uis"] for dna in INDUSTRY_DNA.values()] for item in sublist]))
    available_colors = list(set([item for sublist in [dna["colors"] for dna in INDUSTRY_DNA.values()] for item in sublist]))
    default_ar_index = 1
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"
else:
    dna = INDUSTRY_DNA[selected_industry]
    available_scenes, available_lights = dna["scenes"], dna["lights"]
    available_cameras, available_uis, available_colors = dna["cameras"], dna["uis"], dna["colors"]
    
    # ปรับแต่งค่าอัตโนมัติตามอุตสาหกรรม
    if "Automotive" in selected_industry:
        default_ar_index = 0 # 16:9 สำหรับอุปกรณ์รถยนต์
    elif "Pet Food" in selected_industry:
        default_ar_index = 1 # 3:2 สำหรับสินค้าสัตว์เลี้ยงทั่วไป
    else:
        default_ar_index = 0
        
    default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, octane render, unreal engine, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"

# ==========================================
# ⚙️ 4. UI Sidebar
# ==========================================
with st.sidebar:
    st.header("⚙️ Settings")
    prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=500, step=10, value=50)
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=default_ar_index)
    
    st.markdown("---")
    st.subheader("🛡️ Strict Photo Mode")
    negative_prompt = st.text_area("Negative Prompt", value=default_neg_prompt, height=140)
    st.info("💡 ระบบล็อกค่าที่เหมาะสมกับหมวดที่คุณเลือกไว้แล้ว")

# ==========================================
# 📍 5. โครงสร้างโมดูลที่ผ่านการกรอง DNA แล้ว
# ==========================================
st.subheader("📍 กำหนดโครงสร้าง (Filtered Pro Modules)")
col1, col2, col3 = st.columns(3)
with col1:
    scene = st.selectbox("1. SCENE (แท่นวาง)", ["Auto (สุ่มตาม DNA)"] + available_scenes)
    lighting = st.selectbox("2. LIGHTING (แสง)", ["Auto (สุ่มตาม DNA)"] + available_lights)
with col2:
    camera = st.selectbox("3. CAMERA & LENS (กล้อง)", ["Auto (สุ่มตาม DNA)"] + available_cameras)
    ui_layout = st.selectbox("4. UI LAYOUT (เลย์เอาต์)", ["Auto (สุ่มตาม DNA)"] + available_uis)
with col3:
    color_psych = st.selectbox("5. COLOR PSYCHOLOGY (สี)", ["Auto (สุ่มตาม DNA)"] + available_colors)

# ==========================================
# 🚀 6. ระบบประมวลผล
# ==========================================
if st.button("🚀 Generate PERFECT Prompts", use_container_width=True):
    prompts = []
    for i in range(prompt_count):
        sel_scene = random.choice(available_scenes) if scene == "Auto (สุ่มตาม DNA)" else scene
        sel_light = random.choice(available_lights) if lighting == "Auto (สุ่มตาม DNA)" else lighting
        sel_cam = random.choice(available_cameras) if camera == "Auto (สุ่มตาม DNA)" else camera
        sel_ui = random.choice(available_uis) if ui_layout == "Auto (สุ่มตาม DNA)" else ui_layout
        sel_color = random.choice(available_colors) if color_psych == "Auto (สุ่มตาม DNA)" else color_psych

        base_core = "empty product mockup background, extreme high-end commercial asset, photography award winner"
        prompt_elements = [base_core, sel_scene, sel_light, sel_cam, sel_color, sel_ui]
        clean_base = ", ".join(prompt_elements)
        
        # ปรับ Stylize ให้ภาพดูสมจริง (Raw Photography Look)
        stylize_value = random.randint(50, 100)
        
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
    file_name = f"mj_DNA_{selected_industry.replace(' ', '_')}_prompts.txt"
    st.download_button(label="💾 ดาวน์โหลดไฟล์ .txt", data=prompt_text, file_name=file_name, mime="text/plain", use_container_width=True)
