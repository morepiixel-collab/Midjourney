import streamlit as st
import random
import io
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Midjourney Stock Photo Pro", page_icon="📸", layout="wide")

st.title("👑 The Master Production: 100% Perfection Guaranteed")
st.markdown("---")

# 🌟 1. ข้อมูลสถานที่และแสง (Smart Environment & Lighting Mapping)
ENV_DATA = {
    "CORPORATE": {
        "locs": ["modern bright office interior", "minimalist executive boardroom", "high-tech startup workspace"],
        "lights": ["Clean Office Light", "Professional Studio Light", "Soft Diffused Light"]
    },
    "HEALTHCARE": {
        "locs": ["clean minimalist clinic", "premium wellness center", "modern medical lab"],
        "lights": ["Bright Clinical Light", "Clean White Light", "Soft Natural Light"]
    },
    "WELLNESS": {
        "locs": ["peaceful sunlit yoga studio", "tranquil meditation room", "serene indoor zen garden"],
        "lights": ["Soft Natural Light", "Dreamy Diffused Light", "Warm Window Light"]
    },
    "OUTDOOR": {
        "locs": ["scenic mountain pass", "golden hour beach", "lush green national park", "sunny hiking trail"],
        "lights": ["Golden Hour Sunlight", "Bright Natural Daylight", "Soft Morning Light"]
    },
    "LIFESTYLE": {
        "locs": ["cozy artisanal cafe", "modern minimalist living room", "urban rooftop terrace"],
        "lights": ["Warm Ambient Light", "Soft Natural Light", "Bright & Airy Light"]
    },
    "CYBER_TECH": {
        "locs": ["futuristic server room", "neon-lit data center", "high-tech control room"],
        "lights": ["Modern Neon Accent", "Cinematic Dark Lighting", "High-Contrast Tech Lighting"]
    },
    "ECO_SUSTAINABILITY": {
        "locs": ["sustainable green building interior", "lush indoor vertical garden", "solar panel field"],
        "lights": ["Bright Natural Sunlight", "Soft Morning Light"]
    },
    "EDUCATION": {
        "locs": ["modern university classroom", "bright digital learning hub", "quiet modern library"],
        "lights": ["Bright Room Lighting", "Soft Natural Light"]
    },
    "ECOMMERCE_LOGISTICS": {
        "locs": ["automated modern warehouse", "clean distribution center", "bright packaging facility"],
        "lights": ["Bright Industrial Light", "Clean Fluorescent Light"]
    },
    "FOOD_DIET": {
        "locs": ["bright modern home kitchen", "rustic wooden dining table", "organic food market stall"],
        "lights": ["Warm Window Light", "Soft Directional Light"]
    }
}

# 🌟 2. ท่าทางและสิ่งของ (Subject & Objects)
ACTION_DATA = {
    "CORPORATE": "collaborating with team members",
    "HEALTHCARE": "reviewing health information",
    "WELLNESS": "practicing mindfulness and relaxation",
    "OUTDOOR": "enjoying the natural environment",
    "LIFESTYLE": "relaxing in a modern setting",
    "CYBER_TECH": "interacting with digital data",
    "ECO_SUSTAINABILITY": "examining eco-friendly elements",
    "EDUCATION": "focusing on learning and study",
    "ECOMMERCE_LOGISTICS": "managing logistics operations",
    "FOOD_DIET": "preparing healthy organic food"
}

OBJECT_GROUPS = {
    "CORPORATE": "modern tech gadgets, coffee cup, and organized documents",
    "HEALTHCARE": "medical instruments and digital health charts",
    "WELLNESS": "essential oil bottles, yoga mat, and zen stones",
    "OUTDOOR": "hiking gear, camera, and outdoor map",
    "LIFESTYLE": "stylish magazine, ceramic cup, and houseplant",
    "CYBER_TECH": "circuit boards and futuristic smart devices",
    "ECO_SUSTAINABILITY": "biodegradable materials and small growing plant",
    "EDUCATION": "academic notebooks, laptop, and premium pen",
    "ECOMMERCE_LOGISTICS": "delivery boxes and barcode scanner",
    "FOOD_DIET": "fresh organic vegetables and wooden utensils"
}

ethnicities = ["Asian", "Caucasian", "Hispanic", "Middle Eastern", "Black", "mixed-race", "South Asian"]
ages = ["young adult", "middle-aged", "senior"]
genders = ["man", "woman"]

# --- UI Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 [กลุ่มที่ 1] ไอเดียและรูปแบบ (Subject)")
    idea_manual = st.text_input("ไอเดียหลัก (Manual Entry)", value="", help="พิมพ์คีย์เวิร์ดหลัก")
    
    ready_ideas_list = [
        "Auto (ให้ AI สุ่ม)", 
        "--- 📊 1. Business Micro-Situations ---", "[1.1 Business] employee burnout at desk", "[1.2 Business] manager giving feedback to employee", "[1.3 Business] business team meeting",
        "--- 🤝 2. AI + Human Interaction ---", "[2.1 AI] human using AI assistant hologram", "[2.2 AI] AI chatbot customer service",
        "--- 💻 3. Modern Work Lifestyle ---", "[3.1 Work] remote worker video meeting", "[3.2 Work] freelancer home office setup", "[3.3 Work] digital nomad working cafe",
        "--- 🔒 4. Cybersecurity & Data ---", "[4.1 Cyber] hacker silhouette computer screen", "[4.2 Cyber] digital data protection shield",
        "--- 💰 5. Finance, Startup & ESG ---", "[5.1 Fin/ESG] fintech mobile payment", "[5.2 Fin/ESG] startup growth chart",
        "--- 🏥 6. High-Demand Healthcare ---", "[6.1 Health] doctor consulting patient", "[6.2 Health] telemedicine online doctor",
        "--- 🌍 8. Sustainability & Eco ---", "[8.1 Eco] holding small plant", "[8.2 Eco] charging electric vehicle",
        "--- 🧘‍♀️ 9. Mental Health & Wellness ---", "[9.1 Wellness] meditating peaceful room", "[9.2 Wellness] writing gratitude journal",
        "--- 💼 10. Corporate Leadership ---", "[10.1 Business] executive presentation", "[10.2 Business] shaking hands deal",
        "--- 🚚 12. E-Commerce & Logistics ---", "[12.1 Ecom] clicking Buy Now phone", "[12.2 Ecom] receiving delivery box",
        "--- 🥗 13. Healthy Food & Diet ---", "[13.1 Food] preparing salad kitchen", "[13.2 Food] diverse family cooking dinner together"
    ]
    ready_idea = st.selectbox("สถานการณ์สำเร็จรูป (Preset)", ready_ideas_list)
    include_human = st.radio("มีมนุษย์ (Include Human)", ["Yes", "No"], horizontal=True)

with col2:
    st.subheader("💎 [กลุ่มที่ 2] การจัดองค์ประกอบ (Composition)")
    copy_space = st.selectbox("พื้นที่ว่าง (Copy Space)", [
        "Auto (ให้ AI จัดวางเอง)",
        "subject on the right, wide empty copy space on the left",
        "subject on the left, wide empty copy space on the right",
        "centered subject, wide negative space around",
        "subject at the bottom, wide empty copy space at the top"
    ])
    
    niche_insights = st.selectbox("เจาะจงตลาด (Niche)", ["Auto (ให้ AI สุ่ม)", "Eco-friendly", "Inclusive Health", "Sustainable Fashion", "Green Tech", "Sustainability", "Digital Nomad", "Mental Health", "Cybersecurity", "CSR", "Corporate Data"])
    
    color_palette = st.selectbox("โทนสี (Color)", ["Auto (ให้ AI สุ่ม)", "Natural & True-to-life", "Bright & Airy", "Neutral & Clean", "Warm & Inviting", "Cool & Professional", "Vibrant & Punchy", "Muted & Earthy"])
    
    lighting_style = st.selectbox("สไตล์แสง (Lighting)", ["Auto (ให้ AI สุ่ม)", "Soft Natural Light", "Professional Studio Light", "Golden Hour Sunlight", "Modern Neon Accent", "Clean Office Light", "Dreamy Diffused Light"])

st.markdown("---")

col3, col4 = st.columns(2)
with col3:
    st.subheader("🎬 [กลุ่มที่ 3] การตั้งค่า")
    aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "9:16", "1:1"], index=0)
with col4:
    st.subheader("⚙️ [กลุ่มที่ 4] ข้อจำกัด")
    prompt_count = st.number_input("จำนวน Prompts", min_value=10, max_value=200, step=10, value=50)
    negative_prompt = st.text_input("สิ่งที่ไม่ต้องการ (--no)", value="text, watermark, logo, ugly, deformed, blurry eyes, low quality")

# --- ปุ่มประมวลผล ---
if st.button("🚀 Generate Perfect Prompts", use_container_width=True):
    
    # 1. คัดกรองไอเดีย
    main_idea = idea_manual.strip()
    preset_text = ""
    if ready_idea != "Auto (ให้ AI สุ่ม)" and not ready_idea.startswith("---"):
        preset_text = ready_idea.split("] ")[1] if "]" in ready_idea else ready_idea

    # 2. ค้นหา Environment อัตโนมัติ
    target_env = "LIFESTYLE"
    search_str = (preset_text + " " + main_idea + " " + niche_insights).lower()
    if any(x in search_str for x in ["office", "business", "corp", "manager"]): target_env = "CORPORATE"
    elif any(x in search_str for x in ["doctor", "health", "clinic", "medical"]): target_env = "HEALTHCARE"
    elif any(x in search_str for x in ["yoga", "wellness", "mental", "meditat"]): target_env = "WELLNESS"
    elif any(x in search_str for x in ["mountain", "beach", "outdoor", "park", "trail"]): target_env = "OUTDOOR"
    elif any(x in search_str for x in ["cyber", "tech", "data", "hacker", "ai"]): target_env = "CYBER_TECH"
    elif any(x in search_str for x in ["eco", "sustain", "green", "solar"]): target_env = "ECO_SUSTAINABILITY"
    elif any(x in search_str for x in ["edu", "study", "learn", "student"]): target_env = "EDUCATION"
    elif any(x in search_str for x in ["warehouse", "logistics", "delivery", "ecom"]): target_env = "ECOMMERCE_LOGISTICS"
    elif any(x in search_str for x in ["food", "diet", "cook", "kitchen"]): target_env = "FOOD_DIET"

    prompts = []
    
    for i in range(prompt_count):
        # 🌟 สุ่มข้อมูลพื้นฐาน
        ethnicity = random.choice(ethnicities)
        age = random.choice(ages)
        gender = random.choice(genders)
        location = random.choice(ENV_DATA[target_env]["locs"])
        
        # 🌟 ระบบ Smart Lighting & Color
        light = lighting_style if lighting_style != "Auto (ให้ AI สุ่ม)" else random.choice(ENV_DATA[target_env]["lights"])
        color = color_palette if color_palette != "Auto (ให้ AI สุ่ม)" else "Natural & True-to-life"
        
        # 🌟 ระบบ Physics-Accurate Camera & Framing
        if copy_space != "Auto (ให้ AI จัดวางเอง)":
            # กรณีต้องการพื้นที่ว่าง ต้องใช้มุมกว้าง (Wide) และเลนส์คมชัด (f/5.6 - f/8.0)
            framing = "wide pulled-back shot"
            lens_spec = "shot on 35mm lens, f/8.0"
            style_suffix = "high-end commercial stock photography, clear environment details"
            active_copy_space = copy_space
        else:
            # กรณีปกติ สุ่มมุมมอง และจับคู่เลนส์ให้สมบูรณ์แบบ
            choice = random.choice([
                ("medium shot", "shot on 50mm lens, f/2.8", "shallow depth of field, beautifully blurred background"),
                ("close-up portrait", "shot on 85mm lens, f/1.8", "soft bokeh, shallow depth of field"),
                ("eye-level shot", "shot on 35mm lens, f/4.0", "natural depth of field")
            ])
            framing, lens_spec, style_suffix = choice
            active_copy_space = ""

        # 🌟 ระบบ Smart Action (Sanitize)
        if include_human == "Yes":
            # ตรวจสอบว่าเป็นกลุ่มหรือไม่
            is_group = any(kw in (preset_text + " " + main_idea).lower() for kw in ["team", "group", "family", "meeting", "couple"])
            subject = f"a diverse group of people" if is_group else f"a {age} {ethnicity} {gender}"
            
            # รวม Action
            action = preset_text if preset_text else ACTION_DATA[target_env]
            if main_idea: action += f", {main_idea}"
            
            subject_part = f"{framing} of {subject}, engaged in {action}"
        else:
            # 🌟 โหมดไม่มีคน: แก้ไขคำกริยาให้เป็นกลาง
            obj = preset_text if preset_text else OBJECT_GROUPS[target_env]
            if main_idea: obj += f", {main_idea}"
            # ตัดคำกริยาที่ใช้คนออก
            obj = re.sub(r'\b(holding|preparing|clicking|writing|looking|working)\b', '', obj, flags=re.IGNORECASE).strip()
            
            subject_part = f"flat lay photography, top-down view of {obj}, perfectly organized on a surface"
            lens_spec = "shot on 35mm lens, f/8.0"
            style_suffix = "high-end commercial stock photography, sharp focus across entire layout"

        # 🌟 ประกอบร่าง
        final_prompt = f"/imagine prompt: {subject_part}, at {location}, {active_copy_space}, using a {color} color palette, lit by {light}, {lens_spec}, {style_suffix}, photorealistic, --style raw --ar {aspect_ratio} --v 7"
        
        if negative_prompt.strip():
            final_prompt += f" --no {negative_prompt.strip()}"
            
        prompts.append(final_prompt)

    # --- แสดงผล ---
    st.success(f"✅ สมบูรณ์แบบ 100%! สร้างสำเร็จ {prompt_count} Prompts")
    for p in prompts[:5]:
        st.code(p, language="text")

    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ .txt สำหรับ Midjourney",
        data=io.BytesIO("\n".join(prompts).encode('utf-8')),
        file_name="midjourney_stock_perfection.txt",
        mime="text/plain",
        use_container_width=True
    )
