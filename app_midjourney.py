import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Midjourney Stock Pro", page_icon="👑", layout="wide")

st.title("👑 The Master Production Edition (Photorealistic Stock 100%)")
st.markdown("---")

# 🌟 1. ข้อมูลสถานที่ (Environment)
ENV_GROUPS = {
    "CORPORATE": ["modern bright office interior", "minimalist executive boardroom", "high-end startup workspace", "glass-walled conference room"],
    "HEALTHCARE": ["clean minimalist clinic", "premium wellness center", "modern medical lab", "bright hospital corridor"],
    "WELLNESS": ["peaceful sunlit yoga studio", "tranquil meditation room", "serene indoor zen garden", "minimalist calm room"],
    "OUTDOOR": ["scenic mountain pass", "golden hour beach", "lush green national park", "sunny hiking trail"],
    "LIFESTYLE": ["cozy artisanal cafe", "modern minimalist living room", "urban rooftop terrace", "sunlit home office"],
    "CYBER_TECH": ["futuristic server room", "neon-lit data center", "high-tech control room", "advanced robotics lab"],
    "ECO_SUSTAINABILITY": ["sustainable green building interior", "lush indoor vertical garden", "solar panel field", "eco-friendly greenhouse"],
    "EDUCATION": ["modern university classroom", "bright digital learning hub", "quiet modern library", "interactive e-learning studio"],
    "ECOMMERCE_LOGISTICS": ["automated modern warehouse", "clean distribution center", "bright packaging facility", "logistics control center"],
    "FOOD_DIET": ["bright modern home kitchen", "rustic wooden dining table", "organic food market stall", "cozy dining room"]
}

# 🌟 2. ท่าทางแบบสุ่ม
ACTION_GROUPS = {
    "CORPORATE": ["collaborating enthusiastically", "analyzing complex data", "leading a strategic business meeting"],
    "HEALTHCARE": ["reviewing patient medical records", "showing a caring professional smile", "examining health data"],
    "WELLNESS": ["practicing deep mindfulness", "sitting in a relaxed zen posture", "enjoying a peaceful mindful moment"],
    "OUTDOOR": ["admiring the expansive scenic view", "walking purposefully", "enjoying the fresh natural air"],
    "LIFESTYLE": ["enjoying a warm cup of coffee", "scrolling thoughtfully on a smartphone", "relaxing comfortably"],
    "CYBER_TECH": ["typing rapidly on a glowing keyboard", "analyzing complex digital interfaces", "working intensely on software code"],
    "ECO_SUSTAINABILITY": ["inspecting green plants carefully", "holding eco-friendly materials", "examining environmental data metrics"],
    "EDUCATION": ["taking detailed academic notes", "reading a book attentively", "focusing intensely on e-learning materials"],
    "ECOMMERCE_LOGISTICS": ["scanning inventory barcodes", "organizing delivery packages", "checking logistics data"],
    "FOOD_DIET": ["preparing fresh healthy ingredients", "choosing organic vegetables carefully", "enjoying a nutritious balanced meal"]
}

# 🌟 3. สิ่งของแบบสุ่ม (ภาพไม่มีคน)
OBJECT_GROUPS = {
    "CORPORATE": ["modern tech gadgets, a coffee cup, and organized corporate documents", "minimalist desk accessories and a digital tablet"],
    "HEALTHCARE": ["clean medical instruments, health charts, and supplements", "a stethoscope alongside a digital health tablet"],
    "WELLNESS": ["essential oil bottles, a neatly rolled yoga mat, and smooth zen stones", "a gratitude journal, herbal tea cup, and bamboo elements"],
    "OUTDOOR": ["a vintage compass, an outdoor trail map, and hiking gear", "travel essentials, a digital camera, and a reusable water bottle"],
    "LIFESTYLE": ["a stylish lifestyle magazine, sunglasses, and a ceramic coffee cup", "minimalist home decor items and a small potted houseplant"],
    "CYBER_TECH": ["advanced circuit boards, glowing fiber optic cables, and tech hardware", "cybersecurity conceptual elements and smart devices"],
    "ECO_SUSTAINABILITY": ["biodegradable packaging materials and fresh green leaves", "recycled paper products and a small growing plant"],
    "EDUCATION": ["open academic textbooks, highlighters, and a modern laptop", "neatly stacked notebooks, a premium pen, and digital learning tools"],
    "ECOMMERCE_LOGISTICS": ["sturdy cardboard boxes, shipping labels, and a barcode scanner", "premium product packaging and a logistics tracking tablet"],
    "FOOD_DIET": ["fresh organic vegetables and rustic wooden cooking utensils", "colorful healthy ingredients, superfood seeds, and fresh fruits"]
}

ethnicities = ["Asian", "Caucasian", "Hispanic", "Middle Eastern", "Black", "mixed-race", "South Asian"]
ages = ["young adult", "middle-aged", "senior"]
genders = ["man", "woman"] 

# --- UI Layout (ปรับปรุงใหม่ตาม Flow 1 -> 2 -> 3) ---

st.subheader("1️⃣ กำหนดเนื้อหาภาพ (Subject & Story)")
col1, col2, col3 = st.columns(3)

with col1:
    idea_manual = st.text_input("ไอเดียหลัก (Manual Entry)", value="", help="พิมพ์คีย์เวิร์ดหลักที่ต้องการ")
    
    ready_ideas_list = [
        "Auto (ให้ AI สุ่ม)", 
        "--- 📊 1. Business Micro-Situations ---", "[1.1 Business] employee burnout at desk", "[1.2 Business] manager giving feedback to employee", "[1.3 Business] business team meeting",
        "--- 🤝 2. AI + Human Interaction ---", "[2.1 AI] human using AI assistant hologram", "[2.2 AI] AI chatbot customer service",
        "--- 💻 3. Modern Work Lifestyle ---", "[3.1 Work] remote worker video meeting", "[3.2 Work] freelancer home office setup", "[3.3 Work] digital nomad working cafe",
        "--- 🔒 4. Cybersecurity & Data ---", "[4.1 Cyber] hacker silhouette computer screen", "[4.2 Cyber] digital data protection shield",
        "--- 💰 5. Finance, Startup & ESG ---", "[5.1 Fin/ESG] fintech mobile payment", "[5.2 Fin/ESG] startup growth chart",
        "--- 🏥 6. High-Demand Healthcare ---", "[6.1 Health] doctor consulting patient", "[6.2 Health] telemedicine online doctor",
        "--- 🤖 7. Future Tech (General) ---", "[7.1 Tech] transparent holographic interface", "[7.2 Tech] VR headset data visualization",
        "--- 🌍 8. Sustainability & Eco ---", "[8.1 Eco] holding small plant", "[8.2 Eco] charging electric vehicle",
        "--- 🧘‍♀️ 9. Mental Health & Wellness ---", "[9.1 Wellness] meditating peaceful room", "[9.2 Wellness] writing gratitude journal",
        "--- 💼 10. Corporate Leadership ---", "[10.1 Business] executive presentation", "[10.2 Business] shaking hands deal",
        "--- 🎓 11. E-Learning ---", "[11.1 Edu] online lecture on laptop", "[11.2 Edu] notes during masterclass",
        "--- 🚚 12. E-Commerce & Logistics ---", "[12.1 Ecom] clicking Buy Now phone", "[12.2 Ecom] receiving delivery box",
        "--- 🥗 13. Healthy Food & Diet ---", "[13.1 Food] preparing salad kitchen", "[13.2 Food] diverse family cooking dinner together", "[13.3 Food] young couple cooking together"
    ]
    ready_idea = st.selectbox("สถานการณ์สำเร็จรูป (Preset)", ready_ideas_list)

with col2:
    include_human = st.radio("มีมนุษย์ (Include Human)", ["Yes", "No"], horizontal=True)
    demo_control = st.selectbox("ล็อกเชื้อชาติ/อายุ (Demographics)", [
        "Auto (ให้ AI สุ่ม)", "Asian Only", "Caucasian Only", "Black Only", "Seniors Only", "Young Adults Only"
    ])

with col3:
    emotion_control = st.selectbox("อารมณ์/สีหน้า (Emotion)", [
        "Auto (สุ่มตามสถานการณ์)", "Natural warm smile", "Candid & Authentic", "Deeply focused", "Relaxed & Calm", "Excited & Joyful"
    ])
    camera_angle = st.selectbox("มุมกล้อง (Camera Angle)", [
        "Auto (ให้ AI สุ่มมุมกล้อง)", "Eye-level shot", "High angle / Top-down shot", "Low angle / Hero shot", "Over-the-shoulder shot"
    ])

st.markdown("---")
st.subheader("2️⃣ การจัดองค์ประกอบ (Composition & Style)")

col4, col5, col6, col7 = st.columns(4)

with col4:
    copy_space_list = [
        "Auto (ให้ AI จัดวางเอง)",
        "subject positioned on the right, wide empty copy space on the left",
        "subject positioned on the left, wide empty copy space on the right",
        "centered subject, wide empty negative space around",
        "subject at the bottom, wide empty copy space at the top"
    ]
    copy_space = st.selectbox("พื้นที่ว่าง (Copy Space)", copy_space_list)

with col5:
    niche_list = ["Auto (ให้ AI สุ่ม)", "Eco-friendly", "Inclusive Health", "Sustainable Fashion", "Green Tech", "Sustainability", "Digital Nomad", "Mental Health", "Cybersecurity", "CSR", "Corporate Data"]
    niche_insights = st.selectbox("เจาะจงตลาด (Niche)", niche_list)

with col6:
    color_palette_list = [
        "Auto (ให้ AI สุ่ม)", "Natural & True-to-life", "Bright & Airy", "Neutral & Clean", "Warm & Inviting", "Cool & Professional", "Vibrant & Punchy", "Muted & Earthy"
    ]
    color_palette = st.selectbox("โทนสี (Color)", color_palette_list)

with col7:
    lighting_style = st.selectbox("สไตล์แสง (Lighting)", ["Auto (ให้ AI สุ่ม)", "Soft Natural Light", "Professional Studio Light", "Golden Hour Sunlight", "Modern Neon Accent", "Clean Office Light", "Dreamy Diffused Light"])

st.markdown("---")
st.subheader("3️⃣ ตั้งค่าไฟล์และขั้นสูง (Advanced Settings)")

with st.expander("⚙️ เปิดเพื่อตั้งค่า สัดส่วนภาพ, จำนวน, และ Negative Prompt", expanded=False):
    col8, col9 = st.columns(2)
    with col8:
        col8_1, col8_2 = st.columns(2)
        with col8_1:
            aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "9:16", "1:1"], index=0)
        with col8_2:
            prompt_count = st.number_input("จำนวน Prompts", min_value=10, max_value=200, step=10, value=50)
    with col9:
        negative_prompt = st.text_input("สิ่งที่ไม่ต้องการ (--no)", value="text, watermark, logo, signatures, ugly, deformed, bad anatomy, illustration, 3d, vector")

st.markdown("---")

# --- ปุ่มประมวลผล ---
if st.button("🚀 Generate Prompts", use_container_width=True):
    
    main_idea = idea_manual.strip()
    ready_text = ""
    is_preset_used = False
    
    if ready_idea != "Auto (ให้ AI สุ่ม)" and not ready_idea.startswith("---"):
        ready_text = ready_idea.split("] ")[1] if "]" in ready_idea else ready_idea
        is_preset_used = True

    # 🌟 ระบบลบ "วิญญาณคน" อัตโนมัติ (Sanitize)
    clean_preset_text = ready_text
    if include_human == "No" and is_preset_used:
        remove_words = r'\b(human|employee|manager|doctor|patient|person|people|freelancer|worker|family|couple)\b'
        clean_preset_text = re.sub(remove_words, 'workspace elements', ready_text, flags=re.IGNORECASE).strip()
        clean_preset_text = re.sub(r'\s+', ' ', clean_preset_text)

    # สร้าง Active Subject
    if is_preset_used and main_idea:
        active_subject = f"{clean_preset_text}, {main_idea}"
    elif is_preset_used:
        active_subject = f"{clean_preset_text}"
    elif main_idea:
        active_subject = f"{main_idea}"
    else:
        active_subject = ""

    # ตรวจสอบกลุ่มคน (Group Detection)
    group_keywords = ['team', 'family', 'couple', 'parents', 'meeting', 'collaboration', 'group', 'colleagues']
    is_group = any(kw in active_subject.lower() for kw in group_keywords)

    # เช็ค Environment อัตโนมัติ
    target_env = "LIFESTYLE" 
    if is_preset_used:
        if any(tag in ready_idea for tag in ["[1.", "[10."]): target_env = "CORPORATE"
        elif any(tag in ready_idea for tag in ["[2.", "[4.", "[7."]): target_env = "CYBER_TECH"
        elif any(tag in ready_idea for tag in ["[5.", "[8."]): target_env = "ECO_SUSTAINABILITY"
        elif any(tag in ready_idea for tag in ["[6."]): target_env = "HEALTHCARE"
        elif any(tag in ready_idea for tag in ["[9."]): target_env = "WELLNESS"
        elif any(tag in ready_idea for tag in ["[11."]): target_env = "EDUCATION"
        elif any(tag in ready_idea for tag in ["[12."]): target_env = "ECOMMERCE_LOGISTICS"
        elif any(tag in ready_idea for tag in ["[13."]): target_env = "FOOD_DIET"
        elif any(tag in ready_idea for tag in ["[3."]): target_env = "LIFESTYLE"
    else:
        full_context = (main_idea + " " + niche_insights).lower()
        if any(x in full_context for x in ["cyber", "ai", "tech", "hacker", "data", "server"]): target_env = "CYBER_TECH"
        elif any(x in full_context for x in ["eco", "sustainab", "solar", "green", "farm"]): target_env = "ECO_SUSTAINABILITY"
        elif any(x in full_context for x in ["school", "class", "study", "learn", "student"]): target_env = "EDUCATION"
        elif any(x in full_context for x in ["delivery", "warehouse", "box", "pack", "logistics"]): target_env = "ECOMMERCE_LOGISTICS"
        elif any(x in full_context for x in ["food", "cook", "kitchen", "salad", "diet", "meal"]): target_env = "FOOD_DIET"
        elif any(x in full_context for x in ["beach", "mountain", "nature", "outdoor", "trail"]): target_env = "OUTDOOR"
        elif any(x in full_context for x in ["doctor", "telemedicine", "medical", "health", "hospital"]): target_env = "HEALTHCARE"
        elif any(x in full_context for x in ["yoga", "meditation", "wellness", "mental", "mindful"]): target_env = "WELLNESS"
        elif any(x in full_context for x in ["office", "business", "corporate", "bus", "fin", "meeting"]): target_env = "CORPORATE"

    niche_text = f"{niche_insights} concept" if niche_insights != "Auto (ให้ AI สุ่ม)" else ""
    c_space = copy_space if copy_space != "Auto (ให้ AI จัดวางเอง)" else ""

    prompts = []
    
    for i in range(prompt_count):
        raw_location = random.choice(ENV_GROUPS[target_env])
        stylize_value = random.randint(100, 250)
        
        # 🌟 จัดการสี
        palette_text = ""
        if color_palette == "Auto (ให้ AI สุ่ม)":
            if target_env == "CORPORATE": auto_c = random.choice(["Modern Blue & White", "Cool Teal & Grey", "Neutral & Clean"])
            elif target_env == "HEALTHCARE": auto_c = random.choice(["Clean White & Blue", "Soft Pastels", "Neutral & Clean"])
            elif target_env == "WELLNESS": auto_c = random.choice(["Warm Earth Tones", "Muted & Earthy", "Soft Pastels"])
            elif target_env == "OUTDOOR": auto_c = random.choice(["Natural & True-to-life", "Vibrant & Punchy"])
            elif target_env == "CYBER_TECH": auto_c = random.choice(["Cool Teal & Grey", "High-Contrast Black & Gold"])
            elif target_env == "ECO_SUSTAINABILITY": auto_c = random.choice(["Natural & True-to-life", "Muted & Earthy"])
            elif target_env == "EDUCATION": auto_c = random.choice(["Bright & Airy", "Neutral & Clean"])
            elif target_env == "ECOMMERCE_LOGISTICS": auto_c = random.choice(["Neutral & Clean", "Bright & Airy"])
            elif target_env == "FOOD_DIET": auto_c = random.choice(["Warm & Inviting", "Natural & True-to-life"])
            else: auto_c = random.choice(["Warm & Inviting", "Muted Scandinavian"])
            palette_text = f"using a {auto_c} color palette"
        else:
            palette_text = f"using a {color_palette} color palette"

        prompt_tags = []
        lens_spec = ""
        bokeh_effect = ""
        
        # 🌟 ลอจิก Framing + Lens Physics Synchronization
        if include_human == "Yes":
            if c_space: 
                framing = "wide pulled-back shot"
                lens_spec = "shot on Sony A7R IV, 35mm lens, f/5.6"
            else:
                framing_choice = random.choice([
                    ("wide shot", "shot on Sony A7R IV, 35mm lens, f/5.6", ""), 
                    ("medium shot", "shot on Canon EOS R5, 50mm lens, f/2.8", "shallow depth of field, blurred background"), 
                    ("close-up portrait", "shot on Fujifilm GFX 100, 85mm lens, f/1.2", "beautiful bokeh, blurred background, extreme shallow depth of field")
                ])
                framing = framing_choice[0]
                lens_spec = framing_choice[1]
                bokeh_effect = framing_choice[2]

            clothes = "modern smart casual"
            if target_env in ["CORPORATE", "CYBER_TECH"]: clothes = "professional business attire"
            elif target_env == "HEALTHCARE": clothes = "medical uniform"
            elif target_env == "ECOMMERCE_LOGISTICS": clothes = "warehouse uniform"
            elif target_env == "FOOD_DIET": clothes = "chef apron"
            elif target_env == "OUTDOOR": clothes = "outdoor activewear"
            
            # 🌟 ล็อก Demographics
            if demo_control == "Asian Only": selected_eth, selected_age = "Asian", random.choice(ages)
            elif demo_control == "Caucasian Only": selected_eth, selected_age = "Caucasian", random.choice(ages)
            elif demo_control == "Black Only": selected_eth, selected_age = "Black", random.choice(ages)
            elif demo_control == "Seniors Only": selected_eth, selected_age = random.choice(ethnicities), "senior"
            elif demo_control == "Young Adults Only": selected_eth, selected_age = random.choice(ethnicities), "young adult"
            else: selected_eth, selected_age = random.choice(ethnicities), random.choice(ages)

            sub_lower = active_subject.lower()
            if any(kw in sub_lower for kw in ['couple', 'two people']):
                demo_str = f"a {selected_age} couple dressed in {clothes}"
            elif any(kw in sub_lower for kw in ['family', 'parents']):
                demo_str = f"a diverse family dressed in {clothes}"
            elif is_group:
                demo_str = f"a diverse group of professionals dressed in {clothes}" if target_env == "CORPORATE" else f"a diverse group of people dressed in {clothes}"
            else:
                demo_str = f"a {selected_age} {selected_eth} {random.choice(genders)} dressed in {clothes}"
            
            # 🌟 การกระทำ
            if is_preset_used:
                action_str = f"engaged in {ready_text}"
                if main_idea: action_str += f", portraying {main_idea}"
            else:
                action_str = random.choice(ACTION_GROUPS[target_env])
                if main_idea: action_str += f", illustrating {main_idea}"
            
            # 🌟 ล็อกอารมณ์/สีหน้า (Emotion)
            if emotion_control == "Auto (สุ่มตามสถานการณ์)":
                emotion_str = random.choice(["candid and authentic", "natural subtle smile", "deeply focused"])
            else:
                emotion_str = emotion_control
                
            prompt_tags.append(f"{framing} of {demo_str}")
            prompt_tags.append(f"{action_str}, showing a {emotion_str} expression")

        else:
            # 🌟 Flat Lay Logic แบบสมบูรณ์
            if active_subject:
                obj_focus = f"everyday objects and elements related to '{active_subject}'"
            else:
                obj_focus = random.choice(OBJECT_GROUPS[target_env])
            
            prompt_tags.append(f"flat lay photography, top-down overhead view of {obj_focus}")
            prompt_tags.append("knolling aesthetic, perfectly organized")
            lens_spec = "shot on Sony A7R IV, 35mm lens, f/8.0, sharp focus across entire layout"

        # Niche
        if niche_text: prompt_tags.append(niche_text)
        
        # 🌟 ระบบ มุมกล้อง (Camera Angle)
        if camera_angle != "Auto (ให้ AI สุ่มมุมกล้อง)":
            prompt_tags.append(camera_angle)

        # 🌟 ระบบ Background 
        if include_human == "No":
            prompt_tags.append(f"arranged flat on a surface within a {raw_location}")
        else:
            prompt_tags.append(f"set in a {raw_location}")
            if bokeh_effect: prompt_tags.append(bokeh_effect)
            
        # Composition & Palette
        if c_space: prompt_tags.append(c_space)
        if palette_text: prompt_tags.append(palette_text)
        
        # 🌟 ระบบแสง (Lighting) 
        if lighting_style == "Auto (ให้ AI สุ่ม)":
            if target_env == "CORPORATE": light = random.choice(["Clean Office Light", "Professional Studio Light"])
            elif target_env == "HEALTHCARE": light = random.choice(["Bright Clinical Light", "Clean White Light"])
            elif target_env == "WELLNESS": light = random.choice(["Soft Natural Light", "Dreamy Diffused Light"])
            elif target_env == "OUTDOOR": light = random.choice(["Golden Hour Sunlight", "Bright Natural Daylight"])
            elif target_env == "CYBER_TECH": light = random.choice(["Modern Neon Accent", "Cinematic Dark Lighting"])
            else: light = random.choice(["Warm Ambient Light", "Soft Natural Light"])
            prompt_tags.append(f"lit by {light}")
        elif lighting_style != "Auto (ให้ AI สุ่ม)":
            prompt_tags.append(f"lit by {lighting_style}")

        # 🌟 Camera & Style Suffix (ล็อก Photorealistic)
        prompt_tags.append(lens_spec)
        prompt_tags.append("high-end commercial stock photography, photorealistic")

        clean_tags = [p for p in prompt_tags if p]
        clean_base = ", ".join(clean_tags)
        
        # ประกอบเป็นประโยคสุดท้าย (ฝัง --style raw เป็นค่าเริ่มต้น)
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
            
        # 🌟 Negative Prompt
        neg_prompt = negative_prompt.strip()
        if neg_prompt:
            final_prompt += f" --no {neg_prompt}"
            
        prompts.append(final_prompt)

    # --- เตรียมไฟล์สำหรับดาวน์โหลด ---
    prompt_text = "\n".join(prompts)
    
    st.success(f"✅ สร้างสำเร็จ {prompt_count} Prompts (โค้ดนี้คือ The Masterpiece ไร้จุดบอด 100%!)")
    
    st.markdown("### 👀 ทดสอบนำไปเจน (5 รายการแรก)")
    for p in prompts[:5]:
        st.code(p, language="text")

    # แก้ไขบั๊กการดาวน์โหลดไฟล์โดยใช้ตัวแปร String โดยตรง
    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ .txt สำหรับ Midjourney",
        data=prompt_text,
        file_name="midjourney_master_production.txt",
        mime="text/plain",
        use_container_width=True
    )
