import streamlit as st
import random
import io

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Midjourney Stock Pro", page_icon="👑", layout="wide")

st.title("👑 The Master Production Edition (Ultimate Stock Contributor)")
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

# 🌟 2. ท่าทางแบบสุ่ม (กรณีไม่ใช้ Preset)
ACTION_GROUPS = {
    "CORPORATE": ["collaborating enthusiastically with colleagues", "analyzing complex data on a laptop", "leading a strategic business meeting"],
    "HEALTHCARE": ["reviewing patient medical records", "showing a caring professional smile", "examining health data thoughtfully"],
    "WELLNESS": ["practicing deep mindfulness", "sitting in a relaxed zen posture", "enjoying a peaceful mindful moment"],
    "OUTDOOR": ["admiring the expansive scenic view", "walking purposefully along the path", "enjoying the fresh natural air"],
    "LIFESTYLE": ["enjoying a warm cup of coffee", "scrolling thoughtfully on a smartphone", "relaxing comfortably on a sofa"],
    "CYBER_TECH": ["typing rapidly on a glowing keyboard", "analyzing complex digital interfaces", "working intensely on software code"],
    "ECO_SUSTAINABILITY": ["inspecting green plants carefully", "holding eco-friendly materials", "examining environmental data metrics"],
    "EDUCATION": ["taking detailed academic notes", "reading a book attentively", "focusing intensely on e-learning materials"],
    "ECOMMERCE_LOGISTICS": ["scanning inventory barcodes", "organizing delivery packages", "checking logistics data on a tablet"],
    "FOOD_DIET": ["preparing fresh healthy ingredients", "choosing organic vegetables carefully", "enjoying a nutritious balanced meal"]
}

# 🌟 3. สิ่งของแบบสุ่ม (กรณีไม่มีมนุษย์ และไม่ได้พิมพ์ Manual)
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

ethnicities = ["diverse", "Asian", "Caucasian", "Hispanic", "Middle Eastern", "Black", "mixed-race"]
ages = ["young adult", "middle-aged", "senior"]
genders = ["man", "woman", "person"]
angles = ["eye-level shot", "medium shot", "slight high angle"]

# --- UI Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 [กลุ่มที่ 1] ไอเดียและรูปแบบ (Subject)")
    idea_manual = st.text_input("ไอเดียหลัก (Manual Entry)", value="", help="พิมพ์คีย์เวิร์ดหลักที่ต้องการ")
    
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
        "--- 💼 10. Corporate Leadership ---", "[10.1 Business] executive presentation", "[10.2 Business] shaking hands deal",
        "--- 🎓 11. E-Learning ---", "[11.1 Edu] online lecture on laptop", "[11.2 Edu] notes during masterclass",
        "--- 🚚 12. E-Commerce & Logistics ---", "[12.1 Ecom] clicking Buy Now phone", "[12.2 Ecom] receiving delivery box",
        "--- 🥗 13. Healthy Food & Diet ---", "[13.1 Food] preparing salad kitchen", "[13.2 Food] drinking green detox smoothie"
    ]
    ready_idea = st.selectbox("สถานการณ์สำเร็จรูป (Preset)", ready_ideas_list)
    include_human = st.radio("มีมนุษย์ (Include Human)", ["Yes", "No"], horizontal=True)

with col2:
    st.subheader("💎 [กลุ่มที่ 2] การจัดองค์ประกอบ (Composition & Style)")
    
    art_medium = st.selectbox("ประเภทของสื่อ (Art Medium)", ["Photorealistic (ภาพถ่ายสมจริง)", "Flat Vector Illustration (เวกเตอร์ 2D)", "3D Render (ภาพ 3D)"])
    
    copy_space_list = [
        "Auto (ให้ AI จัดวางเอง)",
        "Subject positioned on the right, wide empty copy space on the left",
        "Subject positioned on the left, wide empty copy space on the right",
        "Centered subject, wide empty negative space around",
        "Subject at the bottom, wide empty copy space at the top"
    ]
    copy_space = st.selectbox("พื้นที่ว่าง (Copy Space)", copy_space_list)
    
    niche_list = ["Auto (ให้ AI สุ่ม)", "Eco-friendly", "Inclusive Health", "Sustainable Fashion", "Green Tech", "Sustainability", "Digital Nomad", "Mental Health", "Cybersecurity", "CSR", "Corporate Data"]
    niche_insights = st.selectbox("เจาะจงตลาด (Niche)", niche_list)
    
    col2_1, col2_2 = st.columns(2)
    with col2_1:
        color_palette_list = [
            "Auto (ให้ AI สุ่ม)", 
            "Natural & True-to-life", 
            "Bright & Airy", 
            "Neutral & Clean", 
            "Warm & Inviting", 
            "Cool & Professional", 
            "Vibrant & Punchy", 
            "Muted & Earthy"
        ]
        color_palette = st.selectbox("โทนสี (Color)", color_palette_list)
    with col2_2:
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
    
    main_idea = idea_manual.strip()
    ready_text = ""
    is_preset_used = False
    
    if ready_idea != "Auto (ให้ AI สุ่ม)" and not ready_idea.startswith("---"):
        ready_text = ready_idea.split("] ")[1] if "]" in ready_idea else ready_idea
        is_preset_used = True

    active_subject = f"{ready_text}, {main_idea}" if (ready_text and main_idea) else (ready_text or main_idea or "")

    # เช็ค Environment
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
        if any(x in full_context for x in ["cyber", "ai", "tech", "hacker", "data", "server", "code", "software"]): target_env = "CYBER_TECH"
        elif any(x in full_context for x in ["eco", "sustainab", "solar", "green", "farm", "climate"]): target_env = "ECO_SUSTAINABILITY"
        elif any(x in full_context for x in ["school", "class", "study", "learn", "student", "university"]): target_env = "EDUCATION"
        elif any(x in full_context for x in ["delivery", "warehouse", "box", "pack", "logistics", "shipping"]): target_env = "ECOMMERCE_LOGISTICS"
        elif any(x in full_context for x in ["food", "cook", "kitchen", "salad", "diet", "meal", "eat"]): target_env = "FOOD_DIET"
        elif any(x in full_context for x in ["beach", "mountain", "nature", "outdoor", "trail", "sea", "hike"]): target_env = "OUTDOOR"
        elif any(x in full_context for x in ["doctor", "telemedicine", "medical", "health", "hospital", "clinic"]): target_env = "HEALTHCARE"
        elif any(x in full_context for x in ["yoga", "meditation", "wellness", "mental", "mindful"]): target_env = "WELLNESS"
        elif any(x in full_context for x in ["office", "business", "corporate", "bus", "fin", "meeting", "manager"]): target_env = "CORPORATE"

    is_photo = "Photorealistic" in art_medium
    is_vector = "Flat Vector" in art_medium
    is_3d = "3D Render" in art_medium

    niche_text = f"representing {niche_insights} theme" if niche_insights != "Auto (ให้ AI สุ่ม)" else ""
    c_space = copy_space if copy_space != "Auto (ให้ AI จัดวางเอง)" else ""

    prompts = []
    
    for i in range(prompt_count):
        raw_location = random.choice(ENV_GROUPS[target_env])
        final_location = raw_location if is_photo else f"minimalist {raw_location} backdrop"
        stylize_value = random.randint(100, 250)
        
        # จัดการแสง (ปิดการใช้งานแสงโดยสิ้นเชิงถ้าเป็น Vector)
        current_light = ""
        if not is_vector:
            if lighting_style == "Auto (ให้ AI สุ่ม)":
                if target_env == "CORPORATE": current_light = random.choice(["Clean Office Light", "Professional Studio Light"])
                elif target_env == "HEALTHCARE": current_light = random.choice(["Bright Clinical Light", "Clean White Light"])
                elif target_env == "WELLNESS": current_light = random.choice(["Soft Natural Light", "Dreamy Diffused Light"])
                elif target_env == "OUTDOOR": current_light = random.choice(["Golden Hour Sunlight", "Bright Natural Daylight"])
                elif target_env == "CYBER_TECH": current_light = random.choice(["Modern Neon Accent", "Cinematic Dark Lighting"])
                elif target_env == "ECO_SUSTAINABILITY": current_light = random.choice(["Bright Natural Sunlight", "Soft Morning Light"])
                elif target_env == "EDUCATION": current_light = random.choice(["Bright Room Lighting", "Soft Natural Light"])
                elif target_env == "ECOMMERCE_LOGISTICS": current_light = random.choice(["Bright Industrial Light", "Clean Fluorescent Light"])
                elif target_env == "FOOD_DIET": current_light = random.choice(["Warm Window Light", "Soft Directional Light"])
                else: current_light = random.choice(["Warm Ambient Light", "Soft Natural Light"])
            else:
                current_light = lighting_style
            if current_light: current_light = f"lit by {current_light}"

        # จัดการสี
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
        
        # 🌟 ลอจิกไร้ที่ติสำหรับ Subject & Action
        prompt_tags = []
        
        if include_human == "Yes":
            clothes = "modern smart casual"
            if target_env in ["CORPORATE", "CYBER_TECH"]: clothes = "professional business attire"
            elif target_env == "HEALTHCARE": clothes = "medical uniform"
            elif target_env == "ECOMMERCE_LOGISTICS": clothes = "warehouse uniform"
            elif target_env == "FOOD_DIET": clothes = "chef apron"
            elif target_env == "OUTDOOR": clothes = "outdoor activewear"
            
            # รวบรวมท่าทางให้ไวยากรณ์สละสลวย
            if is_preset_used:
                if main_idea:
                    action_str = f"acting out the concept of {ready_text}, conveying {main_idea}"
                else:
                    action_str = f"acting out the concept of {ready_text}"
            else:
                action_str = random.choice(ACTION_GROUPS[target_env])
                if main_idea: 
                    action_str = f"acting out the concept of {main_idea}, {action_str}"
            
            demo_str = f"a {random.choice(ages)} {random.choice(ethnicities)} {random.choice(genders)} dressed in {clothes}"
            
            if is_photo:
                prompt_tags.append(f"{random.choice(angles)} of {demo_str}")
            else:
                prompt_tags.append(f"clean illustration of {demo_str}")
                
            prompt_tags.append(action_str)

        else:
            # 🌟 แก้ไข: ลอจิก Flat Lay ที่ AI เข้าใจ 100%
            if active_subject:
                obj_focus = f"conceptual physical objects representing '{active_subject}'"
            else:
                obj_focus = random.choice(OBJECT_GROUPS[target_env])
            
            if is_photo:
                prompt_tags.append(f"flat lay photography, top-down view of {obj_focus}")
                prompt_tags.append("knolling aesthetic, neatly organized")
            else:
                prompt_tags.append(f"clean minimalist illustration featuring {obj_focus}")

        # เพิ่ม Niche และ Location
        if niche_text: prompt_tags.append(niche_text)
        
        if include_human == "No" and is_photo:
            prompt_tags.append(f"arranged on a flat surface in a {final_location}")
        else:
            prompt_tags.append(f"set in a {final_location}")
            
        # เพิ่มองค์ประกอบศิลป์
        if c_space: prompt_tags.append(c_space)
        if palette_text: prompt_tags.append(palette_text)
        if current_light: prompt_tags.append(current_light)
        
        # 🌟 จัดการเอกลักษณ์ของภาพขั้นสุดยอด (Camera & Style)
        if is_photo:
            if include_human == "Yes":
                prompt_tags.append(f"shot on {random.choice(['35mm lens, f/8.0', '50mm lens, f/2.8', '85mm lens, f/1.8'])}")
                prompt_tags.append("high-end commercial stock photography, photorealistic, blurred background")
            else:
                # Flat lay ต้องคมกริบทั้งภาพ
                prompt_tags.append("shot on 35mm lens, f/8.0")
                prompt_tags.append("high-end commercial stock photography, photorealistic, sharp focus across entire layout")
        elif is_vector:
            prompt_tags.append("clean flat vector illustration, corporate memphis style, minimalist UI/UX aesthetic, solid clean background, no gradients, 2d")
        elif is_3d:
            prompt_tags.append("3D isometric illustration, soft smooth clay render, clean background, octane render, blender")

        # ประกอบเป็นประโยคด้วยเครื่องหมายจุลภาค
        clean_base = ", ".join([p for p in prompt_tags if p])
        
        final_prompt = f"/imagine prompt: {clean_base} --style raw --ar {aspect_ratio} --s {stylize_value} --v 7"
            
        # 🌟 Negative Prompt ที่ปรับตัวตามโหมด
        neg_prompt = negative_prompt.strip()
        if is_vector and not "gradient" in neg_prompt:
            neg_prompt += ", gradient, 3d, realistic, shadow, photographic"
        elif is_3d and not "photo" in neg_prompt:
            neg_prompt += ", photo, 2d, flat vector"
            
        if neg_prompt:
            final_prompt += f" --no {neg_prompt}"
            
        prompts.append(final_prompt)

    # --- เตรียมไฟล์สำหรับดาวน์โหลด ---
    prompt_text = "\n".join(prompts)
    
    st.success(f"✅ สร้างสำเร็จจำนวน {prompt_count} Prompts (ไวยากรณ์สมบูรณ์แบบระดับ Masterpiece!)")
    
    st.markdown("### 👀 ทดสอบนำไปเจน (5 รายการแรก)")
    for p in prompts[:5]:
        st.code(p, language="text")

    text_buffer = io.BytesIO(prompt_text.encode('utf-8'))
    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ .txt สำหรับ Midjourney",
        data=text_buffer,
        file_name="midjourney_master_production.txt",
        mime="text/plain",
        use_container_width=True
    )
