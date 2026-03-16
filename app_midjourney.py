import streamlit as st
import random
import io

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Midjourney Prompt Generator", page_icon="👑", layout="wide")

st.title("👑 The Master Production Edition (Minimal & Clean)")
st.markdown("---")

# --- ตัวแปรคงที่ (Constants) ---
ENV_GROUPS = {
    "CORPORATE": ["bright modern office interior", "minimalist executive boardroom", "high-tech startup workspace", "organized professional center"],
    "HEALTHCARE": ["clean minimalist clinic", "high-end wellness center interior", "modern medical research lab"],
    "WELLNESS": ["peaceful sunlit yoga studio", "tranquil meditation room", "serene garden area", "wellness retreat interior"],
    "OUTDOOR": ["scenic mountain pass", "golden hour beach", "lush park", "nature trail", "remote landscape"],
    "LIFESTYLE": ["cozy artisanal cafe", "modern minimalist living room", "stylish home kitchen", "urban rooftop terrace"]
}

ethnicities = ["diverse", "Asian", "Caucasian", "Hispanic", "Middle Eastern", "Black", "mixed-race"]
ages = ["young adult", "middle-aged", "senior"]
genders = ["man", "woman", "person"]
angles = ["eye-level shot", "medium shot", "slight high angle", "wide angle shot"]
action_stories = ["working focused on a project", "collaborating with a team", "showing success on screen", "engaged in deep discussion", "mentoring with a smile", "making a decisive gesture"]
lenses = ["shot on 35mm lens, f/8.0", "shot on 50mm lens, f/2.8", "shot on 85mm lens, f/1.8"]

# สไตล์หลักบังคับตายตัว (เน้นงาน Commercial Stock)
fixed_style = "high-end commercial stock photography, authentic, clean composition, negative space for text, photorealistic, blurred background, --style raw --v 7"

def get_variety_list(source_list, count):
    shuffled = source_list.copy()
    random.shuffle(shuffled)
    return (shuffled * (count // len(shuffled) + 1))[:count]

# --- UI Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 [กลุ่มที่ 1] ไอเดียและรูปแบบมนุษย์")
    idea_manual = st.text_input("ไอเดียหลัก (Manual Entry)", value="digital nomad lifestyle", help="พิมพ์คีย์เวิร์ดหลักที่ต้องการ หากเลือกสถานการณ์ด้านล่างด้วย ระบบจะนำมารวมกันให้เอง")
    
    ready_ideas_list = [
        "Auto (ให้ AI สุ่ม)", 
        "--- 📊 1. Business Micro-Situations ---", "[1.1 Business] employee burnout at desk", "[1.2 Business] manager giving feedback to employee", 
        "--- 🤝 2. AI + Human Interaction ---", "[2.1 AI] human using AI assistant hologram", "[2.2 AI] AI chatbot customer service",
        "--- 💻 3. Modern Work Lifestyle ---", "[3.1 Work] remote worker video meeting", "[3.2 Work] freelancer home office setup", "[3.3 Work] digital nomad working cafe",
        "--- 🔒 4. Cybersecurity & Data ---", "[4.1 Cyber] hacker silhouette computer screen", "[4.2 Cyber] digital data protection shield",
        "--- 💰 5. Finance, Startup & ESG ---", "[5.1 Fin/ESG] fintech mobile payment", "[5.2 Fin/ESG] startup growth chart",
        "--- 🏥 6. High-Demand Healthcare ---", "[6.1 Health] doctor consulting patient", "[6.2 Health] telemedicine online doctor",
        "--- 🤖 7. Future Tech (General) ---", "[7.1 Tech] transparent holographic interface", "[7.2 Tech] VR headset data visualization",
        "--- 🌍 8. Sustainability & Eco ---", "[8.1 Eco] holding small plant", "[8.2 Eco] charging electric vehicle",
        "--- 🧘‍♀️ 9. Mental Health & Wellness ---", "[9.1 Wellness] meditating peaceful room", "[9.2 Wellness] writing gratitude journal",
        "--- 💼 10. Corporate Leadership ---", "[10.1 Business] executive presentation", "[10.2 Business] shaking hands deal"
    ]
    ready_idea = st.selectbox("สถานการณ์สำเร็จรูป (Preset)", ready_ideas_list)
    include_human = st.radio("มีมนุษย์ (Include Human)", ["Yes", "No"], horizontal=True)

with col2:
    st.subheader("💎 [กลุ่มที่ 2] การเจาะจงตลาด (Niche, Tone & Lighting)")
    niche_list = ["Auto (ให้ AI สุ่ม)", "Nature-Inspired Wellness", "Inclusive Healthcare Solutions", "Sustainable Fashion Trends", "Green Technology Innovation", "Environmental Sustainability", "Digital Nomad Lifestyle", "Mental Health Awareness", "Cybersecurity Best Practices", "Corporate Social Responsibility", "Data-Driven Decision Making"]
    niche_insights = st.selectbox("หัวข้อ Niche Insights", niche_list)
    
    color_palette = st.selectbox("โทนสี (Color Palette)", ["Auto (ให้ AI สุ่ม)", "Modern Blue & White (Corporate/Trust)", "Warm Earth Tones (Wellness/Organic)", "Vibrant & Energetic (Tech/Startup)", "Soft Pastels (Life/Minimalist)", "High-Contrast Black & Gold (Luxury)", "Cool Teal & Grey (Cyber/Future)", "Muted Scandinavian (Home/Style)"])
    
    lighting_style = st.selectbox("สไตล์แสง (Lighting)", ["Auto (ให้ AI สุ่ม)", "Soft Natural Light", "Professional Studio Light", "Golden Hour Sunlight", "Modern Neon Accent", "Clean Office Light", "Dreamy Diffused Light"])

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.subheader("🎬 [กลุ่มที่ 3] การตั้งค่าไฟล์ภาพ")
    col3_1, col3_2 = st.columns(2)
    with col3_1:
        aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "9:16", "1:1"], index=0)
    with col3_2:
        prompt_count = st.number_input("จำนวน Prompts", min_value=10, max_value=200, step=10, value=50)

with col4:
    st.subheader("⚙️ [กลุ่มที่ 4] ข้อจำกัด (Negative Prompt)")
    negative_prompt = st.text_input("สิ่งที่ไม่ต้องการ (--no)", value="text, watermark, logo, signatures, ugly, deformed, bad anatomy")

st.markdown("---")

# --- ปุ่มประมวลผล ---
if st.button("🚀 Generate Prompts", use_container_width=True):
    
    # รวม Logic ของไอเดีย
    main_idea = idea_manual.strip()
    ready_text = ""
    if ready_idea != "Auto (ให้ AI สุ่ม)" and not ready_idea.startswith("---"):
        ready_text = ready_idea.split("] ")[1] if "]" in ready_idea else ready_idea

    if ready_text and main_idea:
        active_subject = f"{ready_text}, {main_idea}"
    else:
        active_subject = ready_text or main_idea or ""

    # ค้นหา Environment อัตโนมัติจากบริบท
    full_context = (active_subject + " " + niche_insights).lower()
    target_env = "LIFESTYLE"
    if any(x in full_context for x in ["beach", "mountain", "nature", "outdoor", "trail", "nat", "spo", "tra", "bike", "motorbike", "sunset", "glacier", "sea", "hiking", "cycling"]): target_env = "OUTDOOR"
    elif any(x in full_context for x in ["doctor", "telemedicine", "medical", "health", "hospital", "clin", "sci", "treatment"]): target_env = "HEALTHCARE"
    elif any(x in full_context for x in ["yoga", "meditation", "wellness", "mental", "mindful", "parenting"]): target_env = "WELLNESS"
    elif any(x in full_context for x in ["office", "business", "corporate", "bus", "cyber", "fin", "edu", "tec", "meeting", "manager", "work", "entrepreneur"]): target_env = "CORPORATE"

    # กระจายความหลากหลาย
    dist_ethnicities = get_variety_list(ethnicities, prompt_count)
    dist_ages = get_variety_list(ages, prompt_count)
    dist_genders = get_variety_list(genders, prompt_count)
    dist_angles = get_variety_list(angles, prompt_count)
    dist_actions = get_variety_list(action_stories, prompt_count)
    dist_lenses = get_variety_list(lenses, prompt_count)

    niche_text = f"in a {niche_insights} environment" if niche_insights != "Auto (ให้ AI สุ่ม)" else ""
    palette_text = f"using a {color_palette.split(' (')[0]} palette" if color_palette != "Auto (ให้ AI สุ่ม)" else ""

    prompts = []
    for i in range(prompt_count):
        final_location = random.choice(ENV_GROUPS[target_env])
        
        current_light = lighting_style
        if current_light == "Auto (ให้ AI สุ่ม)":
            if target_env == "CORPORATE": current_light = random.choice(["Clean Office Light", "Professional Studio Light"])
            elif target_env == "HEALTHCARE": current_light = "Bright Clinical Light"
            elif target_env == "OUTDOOR": current_light = random.choice(["Golden Hour Sunlight", "Natural Daylight"])
            elif target_env == "WELLNESS": current_light = "Soft Diffused Light"
            else: current_light = random.choice(["Soft Natural Light", "Warm Ambient Light"])
        
        stylize_value = random.randint(100, 250)
        
        if include_human == "Yes":
            clothes = "modern smart casual"
            if target_env == "CORPORATE": clothes = "professional business attire"
            elif target_env == "HEALTHCARE": clothes = "medical uniform"
            elif target_env == "OUTDOOR": clothes = "weather-appropriate outdoor gear"
            subject_part = f"{dist_angles[i]} of a {dist_ages[i]} {dist_ethnicities[i]} {dist_genders[i]} in {clothes}"
            action_part = dist_actions[i]
        else:
            obj_focus = random.choice(["modern tech gadgets", "organized desk setup", "symbolic professional tools"])
            subject_part = f"{dist_angles[i]} of a clean scene featuring {obj_focus}"
            action_part = "with meticulous details and copy space"

        parts = [subject_part, action_part]
        if niche_text: parts.append(niche_text)
        if active_subject: parts.append(active_subject)
        if palette_text: parts.append(palette_text)
        parts.append(f"lit by {current_light}")
        parts.append("clean commercial style")
        
        clean_base = ", ".join([p for p in parts if p])
        
        # จัดการพารามิเตอร์หลัก
        final_prompt = f"/imagine prompt: {clean_base}, at {final_location}, {dist_lenses[i]}, {fixed_style} --ar {aspect_ratio} --s {stylize_value}"
            
        # เพิ่ม Negative Prompt
        if negative_prompt.strip():
            final_prompt += f" --no {negative_prompt.strip()}"
            
        prompts.append(final_prompt)

    # --- เตรียมไฟล์สำหรับดาวน์โหลด ---
    prompt_text = "\n".join(prompts)
    
    st.success(f"✅ สร้างสำเร็จจำนวน {prompt_count} Prompts (พร้อม Negative Prompt)")
    
    st.markdown("### 👀 ทดสอบนำไปเจน (5 รายการแรก)")
    st.info("💡 นำเมาส์ไปชี้ที่มุมขวาบนของกล่องข้อความ จะมีไอคอน 'Copy' ปรากฏขึ้นมาครับ")
    
    for p in prompts[:5]:
        st.code(p, language="text")

    text_buffer = io.BytesIO(prompt_text.encode('utf-8'))
    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ .txt ทั้งหมด",
        data=text_buffer,
        file_name="midjourney_clean_prompts.txt",
        mime="text/plain",
        use_container_width=True
    )
