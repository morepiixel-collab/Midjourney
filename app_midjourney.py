import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="Midjourney Stock Pro", page_icon="👑", layout="wide")

st.title("👑 The Master Production Edition (Adobe Stock Optimized)")
st.markdown("---")

# 🌟 1. ข้อมูลสถานที่ (Environment) แบบเต็ม 100%
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

# 🌟 2. ท่าทางแบบสุ่ม แบบเต็ม 100%
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

# 🌟 3. สิ่งของแบบสุ่ม (ภาพไม่มีคน) แบบเต็ม 100%
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

ethnicities_list = ["Asian", "Caucasian", "Hispanic", "Middle Eastern", "Black", "mixed-race", "South Asian"]
ages_list = ["young adult", "middle-aged", "senior"]
genders_list = ["man", "woman"] 

# --- UI Layout ---
st.subheader("1️⃣ กำหนดเนื้อหาภาพ (Subject & Story)")
col1, col2, col3 = st.columns(3)

with col1:
    idea_manual = st.text_input("ไอเดียหลัก (Manual Entry)", help="เช่น business meeting, eating salad")
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
    ready_idea = st.selectbox("สถานการณ์สำเร็จรูป", ready_ideas_list)

with col2:
    include_human = st.radio("มีมนุษย์ในภาพไหม?", ["Yes", "No"], horizontal=True)
    demo_control = st.selectbox("ล็อกกลุ่มคน (Demographics)", [
        "Auto (สุ่มทั้งหมด)", "Asian Only", "Caucasian Only", "Black Only", "Seniors Only", "Young Adults Only"
    ])

with col3:
    emotion_control = st.selectbox("อารมณ์ภาพ (Emotion)", [
        "Auto (สุ่มตามสถานการณ์)", "Candid & Authentic Smile", "Deeply Focused & Serious", "Relaxed & Calm", "Excited & Enthusiastic"
    ])
    camera_angle = st.selectbox("มุมกล้อง (Camera Angle)", [
        "Auto (ให้ AI จัดการ)", "Eye-level shot", "High angle / Top-down", "Low angle / Hero shot", "Over-the-shoulder shot"
    ])

st.markdown("---")
st.subheader("2️⃣ องค์ประกอบและสไตล์ (Composition & Vibe)")
col4, col5, col6, col_niche = st.columns(4) # เพิ่มคอลัมน์ Niche คืนมา

with col4:
    copy_space = st.selectbox("พื้นที่ว่าง (Copy Space)", [
        "Auto (สุ่มจัดวาง)", "Wide empty copy space on the left", "Wide empty copy space on the right"
    ])
with col5:
    color_palette = st.selectbox("โทนสี (Color)", [
        "Auto (สุ่ม)", "Natural & True-to-life", "Bright & Airy", "Warm & Inviting", "Cool & Professional"
    ])
with col6:
    lighting_style = st.selectbox("สไตล์แสง (Lighting)", [
        "Auto (สุ่ม)", "Soft Natural Light", "Golden Hour Sunlight", "Professional Studio Light", "Clean Office Light"
    ])
with col_niche:
    niche_list = ["Auto (ไม่ระบุ)", "Eco-friendly", "Inclusive Health", "Sustainable Fashion", "Green Tech", "Sustainability", "Digital Nomad", "Mental Health", "Cybersecurity", "CSR", "Corporate Data"]
    niche_insights = st.selectbox("เจาะจงตลาด (Niche)", niche_list)

st.markdown("---")
# ซ่อนตั้งค่าเชิงลึก
with st.expander("⚙️ ตั้งค่าไฟล์และขั้นสูง (Advanced Settings)"):
    col7, col8 = st.columns(2)
    with col7:
        aspect_ratio = st.selectbox("สัดส่วนภาพ", ["16:9", "9:16", "1:1", "4:3"], index=0)
        prompt_count = st.number_input("จำนวน Prompts ที่ต้องการ", min_value=5, max_value=200, step=5, value=30)
    with col8:
        negative_prompt = st.text_area("สิ่งที่ไม่ต้องการ (--no)", value="text, watermark, logo, signatures, ugly, deformed, bad anatomy, illustration, 3d, vector, artificial, plastic skin")

st.markdown("---")

# --- ปุ่มประมวลผล ---
if st.button("🚀 Generate Stock Prompts", use_container_width=True):
    
    main_idea = idea_manual.strip()
    ready_text = ""
    is_preset_used = False
    
    if ready_idea != "Auto (ให้ AI สุ่ม)" and not ready_idea.startswith("---"):
        ready_text = ready_idea.split("] ")[1] if "]" in ready_idea else ready_idea
        is_preset_used = True

    clean_preset_text = ready_text
    if include_human == "No" and is_preset_used:
        remove_words = r'\b(human|employee|manager|doctor|patient|person|people|freelancer|worker|family|couple)\b'
        clean_preset_text = re.sub(remove_words, 'workspace elements', ready_text, flags=re.IGNORECASE).strip()
        clean_preset_text = re.sub(r'\s+', ' ', clean_preset_text)

    if is_preset_used and main_idea:
        active_subject = f"{clean_preset_text}, {main_idea}"
    elif is_preset_used:
        active_subject = f"{clean_preset_text}"
    elif main_idea:
        active_subject = f"{main_idea}"
    else:
        active_subject = ""

    group_keywords = ['team', 'family', 'couple', 'parents', 'meeting', 'collaboration', 'group']
    is_group = any(kw in active_subject.lower() for kw in group_keywords)

    # 🌟 กู้คืนระบบตรวจจับ Environment ที่สมบูรณ์แบบ
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

    niche_text = f"{niche_insights} concept" if niche_insights != "Auto (ไม่ระบุ)" else ""
    
    prompts = []
    
    for i in range(prompt_count):
        raw_location = random.choice(ENV_GROUPS.get(target_env, ENV_GROUPS["CORPORATE"]))
        stylize_value = random.randint(100, 250)
        
        prompt_tags = []
        
        # 🌟 ลอจิก Framing + Bokeh อย่างหนักแน่น
        if include_human == "Yes":
            framing_choice = random.choice([
                ("wide shot", "shot on Sony A7R IV, 35mm lens, f/5.6", ""), 
                ("medium shot", "shot on Canon EOS R5, 50mm lens, f/2.8", "shallow depth of field, blurred background"), 
                ("close-up portrait", "shot on Fujifilm GFX 100, 85mm lens, f/1.2", "beautiful bokeh, blurred background, extreme shallow depth of field")
            ])
            framing = framing_choice[0]
            lens_spec = framing_choice[1]
            bokeh_effect = framing_choice[2]

            # จัดการ Demographics
            if demo_control == "Asian Only": selected_eth, selected_age = "Asian", random.choice(ages_list)
            elif demo_control == "Caucasian Only": selected_eth, selected_age = "Caucasian", random.choice(ages_list)
            elif demo_control == "Black Only": selected_eth, selected_age = "Black", random.choice(ages_list)
            elif demo_control == "Seniors Only": selected_eth, selected_age = random.choice(ethnicities_list), "senior"
            elif demo_control == "Young Adults Only": selected_eth, selected_age = random.choice(ethnicities_list), "young adult"
            else: selected_eth, selected_age = random.choice(ethnicities_list), random.choice(ages_list)

            demo_str = f"a {selected_age} {selected_eth} {random.choice(genders_list)}"
            if is_group:
                demo_str = f"a diverse group of {selected_age} people"

            # จัดการอารมณ์ (Emotion)
            emotion_str = emotion_control if emotion_control != "Auto (สุ่มตามสถานการณ์)" else random.choice(["candid and authentic", "natural subtle smile", "deeply focused"])
            
            action_str = f"engaged in {active_subject}" if active_subject else random.choice(ACTION_GROUPS.get(target_env, ACTION_GROUPS["CORPORATE"]))
            
            prompt_tags.append(f"{framing} of {demo_str}")
            prompt_tags.append(f"{action_str}, showing a {emotion_str} expression")

        else:
            obj_focus = f"everyday objects related to '{active_subject}'" if active_subject else random.choice(OBJECT_GROUPS.get(target_env, OBJECT_GROUPS["CORPORATE"]))
            prompt_tags.append(f"flat lay photography, top-down overhead view of {obj_focus}")
            lens_spec = "shot on Sony A7R IV, 35mm lens, f/8.0, sharp focus across entire layout"
            bokeh_effect = ""

        # Niche
        if niche_text: prompt_tags.append(niche_text)

        # มุมกล้อง และ Copy Space
        if camera_angle != "Auto (ให้ AI จัดการ)": prompt_tags.append(camera_angle)
        if copy_space != "Auto (สุ่มจัดวาง)": prompt_tags.append(copy_space)
        
        prompt_tags.append(f"set in a {raw_location}")
        if bokeh_effect: prompt_tags.append(bokeh_effect)
        
        # สี และ แสง
        if color_palette != "Auto (สุ่ม)": prompt_tags.append(f"using a {color_palette} color palette")
        if lighting_style != "Auto (สุ่ม)": prompt_tags.append(f"lit by {lighting_style}")

        # ล็อกมาตรฐาน Stock Photo
        prompt_tags.append(lens_spec)
        prompt_tags.append("high-end commercial stock photography, highly detailed, photorealistic, authentic candid moment")

        clean_tags = [p for p in prompt_tags if p]
        clean_base = ", ".join(clean_tags)
        
        # ฝังพารามิเตอร์หลัก (ล็อก --style raw และ 16:9 ตามกระบวนการ)
        final_prompt = f"/imagine prompt: {clean_base} --ar {aspect_ratio} --s {stylize_value} --style raw --v 7"
            
        if negative_prompt.strip():
            final_prompt += f" --no {negative_prompt.strip()}"
            
        prompts.append(final_prompt)

    prompt_text = "\n".join(prompts)
    
    st.success(f"✅ สร้างสำเร็จ {prompt_count} Prompts!")
    
    st.markdown("### 👀 ตัวอย่าง Prompts")
    for p in prompts[:3]: 
        st.code(p, language="text")

    st.download_button(
        label="💾 ดาวน์โหลดไฟล์ Text",
        data=prompt_text,
        file_name="adobe_stock_prompts.txt",
        mime="text/plain",
        use_container_width=True
    )
