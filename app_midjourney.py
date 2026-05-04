import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit ---
st.set_page_config(page_title="COMMERCIAL PROMPT ENGINE: ELITE", page_icon="💎", layout="wide")

# ==========================================
# 🧬 1. Master DNA Database (Purged all "Product/Mockup" keywords + New Everyday Locations)
# ==========================================

# 🏢 1.1 DNA โหมด NORMAL (เพิ่ม Healthcare และ Retail)
DNA_NORMAL = {
    "💼 Corporate & Workspace": {
        "scenes": ["blank solid geometric plinth in a blurred modern office lobby", "empty matte display block with a clean architectural background", "bare rectangular pedestal in a minimalist glass corridor environment"],
        "lights": ["natural clean office side-lighting", "crisp professional workspace daylight"],
        "cameras": ["shot on Hasselblad, zoomed out wide shot", "wide angle commercial photography lens, level perspective"],
        "uis": ["heavy bottom composition with massive empty headroom for web banners", "zoomed out rule of thirds with vast negative space"],
        "colors": ["neutral corporate blue and professional grey tones", "clean bright commercial color palette"],
        "stylize_range": (100, 180)
    },
    "🏫 Education & School": {
        "scenes": ["empty wooden display cylinder in a soft-focus library background", "bare stone pedestal with a blurred minimalist classroom backdrop", "blank geometric platform in a quiet bright university hallway"],
        "lights": ["bright soft morning window lighting", "diffused educational environment light"],
        "cameras": ["50mm prime lens, slightly high angle to show bare top surface", "clean documentary commercial style, wide shot"],
        "uis": ["heavy bottom layout with vast empty top negative space", "zoomed out asymmetric placement with massive copy space"],
        "colors": ["warm inviting natural wood tones", "clean bright primary educational colors"],
        "stylize_range": (100, 180)
    },
    "🏠 Home & Daily Life": {
        "scenes": ["blank marble plinth in a blurred bright minimalist kitchen", "bare ceramic display block with a dreamy soft-focus bathroom background", "empty solid platform in a clean airy sunlit room environment"],
        "lights": ["soft morning home interior lighting", "clean bright window daylight"],
        "cameras": ["35mm lens, zoomed out lifestyle framing", "85mm lens, looking slightly down at 45 degree angle"],
        "uis": ["heavy bottom composition with massive empty headroom", "clean centered placement with extreme negative space at the top half"],
        "colors": ["warm comforting home tones", "fresh bright morning colors"],
        "stylize_range": (80, 150)
    },
    "🏥 Healthcare & Medical (โรงพยาบาล/คลินิก)": {
        "scenes": ["blank sterile white exhibition plinth in a blurred clean hospital corridor", "empty presentation block with a bright modern clinic background", "bare geometric pedestal in a soft-focus medical facility"],
        "lights": ["bright crisp clinical daylight", "clean shadowless hospital ambient lighting"],
        "cameras": ["shot on 50mm lens, zoomed out wide shot", "sharp commercial photography, level perspective"],
        "uis": ["heavy bottom composition with massive empty headroom", "zoomed out centered layout with vast negative space"],
        "colors": ["sterile pure white and soft clinical blue tones", "clean reassuring healthcare color palette"],
        "stylize_range": (80, 150)
    },
    "🛍️ Retail & Shopping Mall (ห้างสรรพสินค้า)": {
        "scenes": ["blank exhibition display plinth in a blurred bright shopping mall atrium", "empty presentation pedestal with blurred retail store lights in the background", "bare solid geometric block in a modern commercial complex"],
        "lights": ["bright dynamic mall interior lighting", "soft diffused commercial retail lighting"],
        "cameras": ["35mm lens, zoomed out wide shot", "slightly high angle commercial photography"],
        "uis": ["heavy bottom layout with vast empty top negative space", "zoomed out asymmetric placement with massive copy space"],
        "colors": ["vibrant commercial lighting tones", "clean bright modern mall color palette"],
        "stylize_range": (100, 180)
    }
}

# 🎄 1.2 DNA โหมด HOLIDAY
DNA_HOLIDAY = {
    "🧧 Jan-Feb (New Year & Valentine)": {
        "scenes": ["blank crimson lacquer display plinth surrounded by subtle gold bokeh", "empty frosted pink glass plinth strictly devoid of any objects", "bare red and gold exhibition block with festive atmosphere"],
        "lights": ["warm festive ambient glow", "soft romantic diffused studio lighting"],
        "cameras": ["85mm lens, zoomed out full body shot of the plinth", "medium format photography, slightly high angle"],
        "uis": ["heavy bottom composition with wide empty copy space", "zoomed out centered layout for festive typography"],
        "colors": ["auspicious crimson red and metallic gold", "soft romantic pink and elegant rose gold"],
        "stylize_range": (150, 250)
    },
    "💦 Apr (Songkran & Spring)": {
        "scenes": ["empty white marble plinth with soft water ripples, no props", "bare stone plinth surrounded by falling Sakura petals in the background", "blank solid platform with refreshing summer vibe"],
        "lights": ["vibrant high-contrast summer sun", "soft peaceful spring daylight"],
        "cameras": ["fast shutter speed, looking slightly down at 45 degree angle", "dreamy soft focus wide lens"],
        "uis": ["dynamic layout with massive empty headroom", "zoomed out centered calm composition"],
        "colors": ["refreshing cyan and summer blue", "soft pastel pink and pure white"],
        "stylize_range": (100, 200)
    },
    "🎃 Oct-Nov (Halloween & Black Friday)": {
        "scenes": ["bare matte white display steps with subtle autumn leaves in background", "blank dark obsidian platform for tech presentation", "empty sleek geometric plinth for Black Friday sale"],
        "lights": ["moody evening light", "dramatic cinematic spotlighting"],
        "cameras": ["high contrast wide shot", "sharp focus, low angle heroic perspective"],
        "uis": ["heavy bottom placement with dramatic negative space above", "zoomed out extreme negative space on the left"],
        "colors": ["warm autumn orange and brown", "stealth black with bold red accents"],
        "stylize_range": (150, 300)
    },
    "🎄 Dec (Christmas & Year End)": {
        "scenes": ["empty stone pedestal surrounded by blurred Christmas pine bokeh", "blank luxury display plinth with subtle festive decor in the distance", "bare solid geometric block with winter atmosphere"],
        "lights": ["festive warm bokeh lighting", "cozy winter window light"],
        "cameras": ["50mm lens, zoomed out wide shot", "slightly high angle commercial photography"],
        "uis": ["heavy bottom placement with massive empty headroom for holiday text", "zoomed out perfectly balanced negative space"],
        "colors": ["pine green, warm gold, and crisp snow white", "classic winter wonderland tones"],
        "stylize_range": (150, 250)
    }
}

# 💎 1.3 DNA โหมด PREMIUM
DNA_PREMIUM = {
    "🧴 Skincare & Hydration": {
        "scenes": ["blank frosted glass cylinder plinth emerging from rippling water", "empty natural stone pedestal surrounded by dynamic clear water splashes in background", "bare solid plinth for cosmetics presentation"],
        "lights": ["soft diffused studio lighting", "clean shadowless e-commerce lighting"],
        "cameras": ["100mm macro lens, looking slightly down at 45 degree angle", "85mm lens, zoomed out wide shot"],
        "uis": ["heavy bottom composition with massive empty headroom", "zoomed out centered placement with extreme negative space at the top half"],
        "colors": ["clinical cyan and stark white tones", "refreshing aquatic blue and pure white"],
        "stylize_range": (80, 160)
    },
    "💎 High-End Luxury": {
        "scenes": ["blank black obsidian plinth with subtle gold veins", "bare exhibition plinth draped in flowing dark emerald velvet", "empty solid marble pedestal in an abstract luxury space"],
        "lights": ["dramatic elegant spotlighting", "moody studio lighting with gold reflections"],
        "cameras": ["shot on 85mm f/1.4, wide framing", "high-end editorial slightly high angle shot"],
        "uis": ["zoomed out centered minimalist composition", "heavy bottom layout with elegant top negative space for typography"],
        "colors": ["luxurious rich emerald and gold tones", "deep burgundy and polished brass accents"],
        "stylize_range": (100, 180)
    },
    "🌿 Organic & Wellness": {
        "scenes": ["blank textured clay plinth with minimal dried foliage in background", "bare terrazzo stone platform with blurred moss accents", "empty solid wood block in a soft sunlit space"],
        "lights": ["soft dappled sunlight", "warm morning golden hour light"],
        "cameras": ["Kodak Portra 400 simulation, zoomed out", "50mm lens, slightly high angle natural documentary style"],
        "uis": ["heavy bottom composition with balanced negative space", "zoomed out vast empty space for organic branding"],
        "colors": ["earthy organic neutral tones", "warm beige and muted sage green"],
        "stylize_range": (20, 70)
    },
    "💻 Tech & Men's Grooming": {
        "scenes": ["bare brutalist raw concrete block with graphic shadows", "empty sleek brushed gunmetal circular plinth in a dark tech environment", "blank carbon fiber pedestal"],
        "lights": ["dramatic editorial hard spotlight with sharp shadows", "minimalist neon edge lighting"],
        "cameras": ["shot on Hasselblad, low angle heroic perspective", "sharp digital medium format, zoomed out"],
        "uis": ["heavy bottom composition with massive empty space above", "zoomed out extreme negative space for tech specifications"],
        "colors": ["charcoal and matte black tones with subtle silver", "dark moody cyber tones with one accent color"],
        "stylize_range": (150, 250)
    },
    "🚗 Automotive & Parts": {
        "scenes": ["empty high-tech carbon fiber display platform in a modern dark garage", "blank brushed aluminum circular plinth with industrial asphalt texture", "bare forged steel pedestal with sharp geometric lines"],
        "lights": ["dramatic hard edge lighting to highlight metallic curves", "cool blue industrial studio lighting"],
        "cameras": ["shot on Hasselblad, low angle heroic wide shot", "wide angle 24mm lens, zoomed out for grand scale"],
        "uis": ["heavy bottom layout with massive headroom", "zoomed out extreme negative space for automotive brand name"],
        "colors": ["metallic silver and deep charcoal blacks", "high-contrast racing red and black"],
        "stylize_range": (180, 280)
    },
    "🐾 Pet Food & Pet Care": {
        "scenes": ["bare rustic light oak wooden plinth on a clean sunlit floor", "empty matte ceramic pedestal surrounded by blurred organic ingredients", "blank minimalist wooden block in a bright airy room"],
        "lights": ["warm natural morning sunlight", "soft airy high-key studio lighting"],
        "cameras": ["low angle pet-eye view shot, wide framing", "looking slightly down at 45 degree angle"],
        "uis": ["heavy bottom composition with top copy space", "zoomed out wide empty space on the right"],
        "colors": ["warm earthy browns and leafy greens", "vibrant friendly orange and teal"],
        "stylize_range": (60, 130)
    },
    "🍭 Gen-Z & Pop Cosmetics": {
        "scenes": ["blank pastel pink geometric acrylic display blocks", "empty minimalist matte colorful arches and steps"],
        "lights": ["bright high-key studio lighting", "playful colored gel lighting setup"],
        "cameras": ["crisp commercial wide shot", "slightly high angle flash photography style"],
        "uis": ["zoomed out dynamic asymmetrical layout", "heavy bottom placement with vast negative space"],
        "colors": ["vibrant high-contrast complementary colors", "soft pastel holographic and neon tones"],
        "stylize_range": (250, 450)
    },
    "☕ Edibles & Supplements": {
        "scenes": ["bare rich rustic walnut wood slice serving as a premium display plinth", "empty dark rough slate stone pedestal with subtle warm natural lighting"],
        "lights": ["warm appetizing directional light", "soft morning sunlight"],
        "cameras": ["looking slightly down at 45 degree angle, wide framing", "food photography style zoomed out"],
        "uis": ["heavy bottom composition with top copy space", "zoomed out wide side copy space for nutritional info"],
        "colors": ["warm rich earthy tones", "fresh morning natural colors"],
        "stylize_range": (70, 140)
    },
    "🏋️‍♂️ Fitness & Sports Nutrition": {
        "scenes": ["empty matte black rubberized texture plinth in a moody athletic gym environment", "bare perforated dark steel industrial pedestal with cool rim lighting"],
        "lights": ["dramatic high-contrast gym lighting", "cool industrial rim lighting"],
        "cameras": ["low angle heroic perspective, zoomed out", "gritty wide shot film look"],
        "uis": ["heavy bottom composition with massive headroom", "zoomed out extreme negative space"],
        "colors": ["stealth black with neon accents", "cool steel gray and electric blue"],
        "stylize_range": (100, 200)
    },
    "👶 Baby & Maternity": {
        "scenes": ["blank soft pure cotton draped over a gentle rounded plinth", "empty smooth matte ceramic pastel pedestal resting on soft white fluffy textures"],
        "lights": ["ultra-soft diffused airy lighting", "gentle morning window light"],
        "cameras": ["shot on 50mm, slightly high angle soft focus", "dreamy pastel zoomed out wide shot"],
        "uis": ["heavy bottom composition with massive soft negative space", "zoomed out centered layout with vast headroom"],
        "colors": ["pure warm white and soft cream", "delicate baby blue and pastel pink"],
        "stylize_range": (50, 120)
    },
    "♻️ Eco-Sustainability": {
        "scenes": ["empty premium compressed recycled paper block serving as a sustainable exhibition plinth", "bare raw packed earth pedestal with natural green moss accents"],
        "lights": ["clean natural daylight", "soft dappled forest lighting"],
        "cameras": ["slightly high angle documentary style", "wide framing medium format"],
        "uis": ["heavy bottom placement with massive empty headroom", "zoomed out vast negative space for eco messaging"],
        "colors": ["raw natural brown and muted green", "clean off-white and earth tones"],
        "stylize_range": (20, 80)
    },
    "🔮 Ethereal & Abstract": {
        "scenes": ["blank floating crystal prism plinth creating subtle rainbow light refractions", "empty abstract curved alabaster stone pedestal in a surreal minimalist white space"],
        "lights": ["ethereal glowing ambient light", "sharp directional light creating prism refractions"],
        "cameras": ["zoomed out high-fashion photography", "dreamy slightly high angle lens"],
        "uis": ["heavy bottom composition with vast negative space", "zoomed out extreme headroom for high-end design"],
        "colors": ["iridescent pearl and holographic tones", "pure surreal white with subtle color shifts"],
        "stylize_range": (300, 600)
    },
    "🛁 Bathroom Shelf": {
        "scenes": ["empty clean minimalist bathroom shelf with soft natural window light and subtle steam", "bare luxury vanity counter with marble surfaces and subtle bokeh reflections"],
        "lights": ["soft morning bathroom window light", "clean spa-like ambient lighting"],
        "cameras": ["zoomed out lifestyle still-life photography", "looking slightly down at 45 degree angle"],
        "uis": ["heavy bottom composition with massive headroom", "zoomed out clean centered layout with top copy space"],
        "colors": ["refreshing spa aqua and white", "warm comforting cream and beige"],
        "stylize_range": (70, 130)
    }
}

# ==========================================
# 🎛️ MASTER SWITCH
# ==========================================
st.sidebar.title("🎛️ Master Switch")
app_mode = st.sidebar.radio(
    "เลือกเครื่องมือที่คุณต้องการใช้งาน:",
    ["🏛️ เครื่องจักรสร้างแท่นวาง (Podiums)", "⚪ เครื่องจักรสร้างฉากขาว (Isolated)"]
)
st.sidebar.markdown("---")

# ==========================================
# 🏛️ MODE: PODIUMS
# ==========================================
if app_mode == "🏛️ เครื่องจักรสร้างแท่นวาง (Podiums)":
    
    st.title("🏛️ ELITE PODIUM ENGINE: V8.1 Ready")
    st.markdown("ระบบผลิตงาน Mockup ระดับโฆษณา: **คุมมุมกล้องและพื้นที่ว่าง ป้องกัน AI สร้างสินค้าปลอม**")
    st.markdown("---")

    st.subheader("🎯 ขั้นตอนที่ 1: เลือกโหมดการทำงานหลัก")
    work_mode = st.radio(
        "ฐานข้อมูลอุตสาหกรรม:", 
        ["🏢 โหมดปกติ (Corporate & Everyday)", "🎄 โหมดเทศกาล (Seasonal Podiums)", "💎 โหมด Premium Product (Podium & High-End)"],
        horizontal=True, index=0
    )

    if "Premium" in work_mode: current_dna_dict = DNA_PREMIUM; mode_th = "โหมดพรีเมียม"
    elif "เทศกาล" in work_mode: current_dna_dict = DNA_HOLIDAY; mode_th = "โหมดเทศกาล"
    else: current_dna_dict = DNA_NORMAL; mode_th = "โหมดปกติ"

    st.subheader(f"🏭 ขั้นตอนที่ 2: เลือกอุตสาหกรรมเป้าหมาย ({mode_th})")
    industry_options = ["🌟 สุ่มผสมทุกหมวด (All in this mode)"] + list(current_dna_dict.keys())
    selected_industry = st.selectbox("เลือกอุตสาหกรรม:", industry_options)

    if selected_industry == "🌟 สุ่มผสมทุกหมวด (All in this mode)":
        available_scenes = list(set([item for sublist in [dna["scenes"] for dna in current_dna_dict.values()] for item in sublist]))
        available_lights = list(set([item for sublist in [dna["lights"] for dna in current_dna_dict.values()] for item in sublist]))
        available_cameras = list(set([item for sublist in [dna["cameras"] for dna in current_dna_dict.values()] for item in sublist]))
        available_uis = list(set([item for sublist in [dna["uis"] for dna in current_dna_dict.values()] for item in sublist]))
        available_colors = list(set([item for sublist in [dna["colors"] for dna in current_dna_dict.values()] for item in sublist]))
        s_min, s_max = (80, 200)
    else:
        dna = current_dna_dict[selected_industry]
        available_scenes, available_lights = dna["scenes"], dna["lights"]
        available_cameras, available_uis, available_colors = dna["cameras"], dna["uis"], dna["colors"]
        s_min, s_max = dna["stylize_range"]

    with st.sidebar:
        st.header("⚙️ Global Settings")
        mj_version = st.selectbox("Midjourney Version (--v)", ["8.1", "8.0", "7", "6.1", "6.0"], index=0)
        if mj_version in ["8.1", "8.0"]:
            st.warning(f"⚠️ V{mj_version} ไม่รองรับ --no ระบบจะใช้การบีบบังคับคำศัพท์ (Positive Enforcement) แทนเพื่อให้แท่นว่างเปล่า")
        
        prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=500, step=10, value=50)
        
        st.markdown("---")
        st.subheader("🖼️ Aspect Ratio (สัดส่วนภาพ)")
        is_random_ar = st.checkbox("🎲 สุ่มสัดส่วนภาพอัตโนมัติ (คละกัน)", value=True)
        
        if is_random_ar:
            st.info("ระบบจะสุ่มสัดส่วน 3:2, 16:9, 4:5, 1:1, 9:16 ให้คละกัน")
            aspect_ratio = "Auto"
        else:
            aspect_ratio = st.selectbox("เลือกล็อกสัดส่วนภาพแบบตายตัว:", ["3:2", "4:5", "1:1", "16:9", "9:16"], index=0)
        
        st.markdown("---")
        st.subheader("🛡️ Strict Photo Mode")
        negative_prompt = st.text_area("Negative Prompt (เฉพาะ V7 ลงไป)", value="plants, candles, books, flowers, clutter, people, signatures, text, watermark, objects, items", height=140)
        
        st.markdown("---")
        if selected_industry != "🌟 สุ่มผสมทุกหมวด (All in this mode)":
            st.success(f"🎚️ **Stylize Range (--s):** {s_min} - {s_max}")
        else:
            st.info("🎚️ **Stylize Range (--s):** 80 - 200 (Mode: All)")

    st.subheader("📍 ขั้นตอนที่ 3: กำหนดโครงสร้าง")
    col1, col2, col3 = st.columns(3)
    with col1:
        scene = st.selectbox("1. SCENE (แท่นวาง)", ["Auto (สุ่มตาม DNA)"] + available_scenes)
        lighting = st.selectbox("2. LIGHTING (แสง)", ["Auto (สุ่มตาม DNA)"] + available_lights)
    with col2:
        camera = st.selectbox("3. CAMERA & LENS (กล้อง)", ["Auto (สุ่มตาม DNA)"] + available_cameras)
        ui_layout = st.selectbox("4. UI LAYOUT (พื้นที่ว่าง)", ["Auto (สุ่มตาม DNA)"] + available_uis)
    with col3:
        color_psych = st.selectbox("5. COLOR PSYCHOLOGY (สี)", ["Auto (สุ่มตาม DNA)"] + available_colors)

    if st.button("🚀 Generate PERFECT Podiums", use_container_width=True):
        prompts = []
        ar_choices = ["3:2", "4:5", "1:1", "16:9", "9:16"]
        
        for i in range(prompt_count):
            sel_scene = random.choice(available_scenes) if scene == "Auto (สุ่มตาม DNA)" else scene
            sel_light = random.choice(available_lights) if lighting == "Auto (สุ่มตาม DNA)" else lighting
            sel_cam = random.choice(available_cameras) if camera == "Auto (สุ่มตาม DNA)" else camera
            sel_ui = random.choice(available_uis) if ui_layout == "Auto (สุ่มตาม DNA)" else ui_layout
            sel_color = random.choice(available_colors) if color_psych == "Auto (สุ่มตาม DNA)" else color_psych

            # Base Core ตัดคำว่า Product / Mockup ทิ้งทั้งหมด
            base_core = "blank exhibition display background, extreme high-end commercial asset, photography award winner, completely clear uninterrupted flat top surface, pure geometric presentation plinth, devoid of any objects or decor"
            
            prompt_elements = [base_core, sel_scene, sel_light, sel_cam, sel_color, sel_ui]
            clean_base = ", ".join(prompt_elements)
            stylize_value = random.randint(s_min, s_max)
            
            sel_ar = random.choice(ar_choices) if is_random_ar else aspect_ratio
            
            final_prompt = f"{clean_base}"
            if negative_prompt and mj_version not in ["8.1", "8.0"]:
                final_prompt += f" --no {negative_prompt.strip()}"
                
            final_prompt += f" --ar {sel_ar} --s {stylize_value} --style raw --v {mj_version}"
            prompts.append(final_prompt)
            
        st.session_state['prompts'] = prompts
        st.success(f"✅ เจนเรียบร้อย {prompt_count} Prompts (โหมดสุ่มสัดส่วน: {'เปิด' if is_random_ar else 'ปิด'})")

    if 'prompts' in st.session_state:
        st.markdown("### 👀 Preview Prompts")
        for p in st.session_state['prompts'][:5]: st.code(p, language="text")
        
        prompt_text = "\n\n".join(st.session_state['prompts'])
        st.download_button(label="💾 ดาวน์โหลดไฟล์ .txt", data=prompt_text, file_name=f"podium_v{mj_version}.txt", mime="text/plain", use_container_width=True)

# ==========================================
# ⚪ MODE: ISOLATED (ฉากขาว)
# ==========================================
elif app_mode == "⚪ เครื่องจักรสร้างฉากขาว (Isolated)":
    
    DNA_ISOLATED = {
        "💦 Liquid & Splash (น้ำและของเหลว)": {
            "subjects": ["crystal clear pure water splash", "dynamic milky lotion texture explosion", "translucent cosmetic serum droplet falling"],
            "dynamics": ["frozen in mid-air", "high-speed dynamic splash", "elegant anti-gravity flow", "exploding outward"],
            "lights": ["clean shadowless e-commerce lighting with bright reflections", "cool bright studio strobe lighting"],
            "cameras": ["shot on 100mm macro lens, ultra-sharp focus on droplets", "fast shutter speed photography simulation"],
            "stylize_range": (40, 90)
        },
        "🌿 Botanical & Nature (พฤกษศาสตร์และธรรมชาติ)": {
            "subjects": ["fresh green tea leaves and natural herbs", "delicate petals of sakura and pink roses", "detailed autumn leaves with organic textures"],
            "dynamics": ["levitating gracefully", "falling gently", "suspended in mid-air", "swirling dynamic composition"],
            "lights": ["soft diffused shadowless light with subtle rim light", "clean natural daylight simulation on pure white"],
            "cameras": ["shot on Hasselblad medium format, extreme texture detail", "85mm lens crisp edge-to-edge sharpness"],
            "stylize_range": (30, 80)
        },
        "☕ Food & Ingredients (อาหารและวัตถุดิบ)": {
            "subjects": ["roasted coffee beans and fine powder", "chopped fresh fruits like mango and kiwi", "colorful aromatic spices and herbs"],
            "dynamics": ["explosive burst outward", "levitating in a chaotic but balanced arrangement", "dynamic flying composition"],
            "lights": ["crisp shadowless strobe with strong rim light to separate edges", "bright appetizing even lighting"],
            "cameras": ["food photography macro style, extreme sharpness", "focus stacked macro photography"],
            "stylize_range": (50, 100)
        },
        "💻 Tech & Exploded Views (ชิ้นส่วนไอที)": {
            "subjects": ["modern smartphone internal components", "premium noise-cancelling wireless earbuds", "mechanical watch gears and metallic parts"],
            "dynamics": ["precise exploded view diagram style", "levitating separated parts", "dynamic anti-gravity tech composition"],
            "lights": ["cool industrial shadowless lighting with sharp highlights", "perfect studio strobe with metallic reflection control"],
            "cameras": ["technical product photography style", "extreme detailed medium format"],
            "stylize_range": (100, 200)
        },
        "💊 Cosmetics & Pills (เวชสำอางและยา)": {
            "subjects": ["transparent gel capsules and vitamins", "premium skincare glass dropper bottles", "smeared textures of thick facial cream"],
            "dynamics": ["floating elegantly", "arranged in a dynamic levitating pattern", "suspended with a gentle splash"],
            "lights": ["clinical bright shadowless light", "pure white studio wrap-around lighting"],
            "cameras": ["100mm macro for clinical precision", "sharp digital medium format"],
            "stylize_range": (40, 90)
        },
        "📦 Packaging Mockups (กล่องและบรรจุภัณฑ์)": {
            "subjects": ["blank matte cardboard shipping box", "empty frosted glass cosmetic jar", "minimalist white squeeze tube"],
            "dynamics": ["levitating at a dynamic 45-degree angle", "floating weightlessly", "suspended symmetrically"],
            "lights": ["soft shadowless lighting with strong edge definition", "clean e-commerce product lighting"],
            "cameras": ["standard 50mm commercial product lens", "perfectly sharp product photography"],
            "stylize_range": (60, 120)
        }
    }

    st.title("⚪ ISOLATED MASTER ENGINE: V8.1")
    st.markdown("ระบบผลิตงาน High-Volume: สร้างภาพวัตถุไดคัทฉากขาวบริสุทธิ์ (#FFFFFF) ไร้เงา 100%")
    st.markdown("---")

    st.subheader("🏭 ขั้นตอนที่ 1: เลือกหมวดหมู่วัตถุเป้าหมาย (Isolated Subject)")
    industry_options_iso = ["🌟 สุ่มผสมทุกหมวด (All Isolated)"] + list(DNA_ISOLATED.keys())
    selected_industry_iso = st.selectbox("เลือกประเภทของวัตถุ:", industry_options_iso)

    if selected_industry_iso == "🌟 สุ่มผสมทุกหมวด (All Isolated)":
        available_subjects = list(set([item for sublist in [dna["subjects"] for dna in DNA_ISOLATED.values()] for item in sublist]))
        available_dynamics = list(set([item for sublist in [dna["dynamics"] for dna in DNA_ISOLATED.values()] for item in sublist]))
        available_lights = list(set([item for sublist in [dna["lights"] for dna in DNA_ISOLATED.values()] for item in sublist]))
        available_cameras = list(set([item for sublist in [dna["cameras"] for dna in DNA_ISOLATED.values()] for item in sublist]))
        s_min_iso, s_max_iso = (40, 120)
    else:
        dna_iso = DNA_ISOLATED[selected_industry_iso]
        available_subjects, available_dynamics = dna_iso["subjects"], dna_iso["dynamics"]
        available_lights, available_cameras = dna_iso["lights"], dna_iso["cameras"]
        s_min_iso, s_max_iso = dna_iso["stylize_range"]

    strict_isolated_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, shadow, drop shadow, reflection, gradient, floor, surface, table, pedestal, podium, colored background, off-white, grey background, watermark, text, logo"

    with st.sidebar:
        st.header("⚙️ Settings (Isolated)")
        mj_version_iso = st.selectbox("Midjourney Version (--v)", ["8.1", "8.0", "7", "6.1", "6.0"], index=0, key="iso_ver")
        
        if mj_version_iso in ["8.1", "8.0"]:
            st.warning(f"⚠️ V{mj_version_iso} ยังไม่รองรับระบบ Negative Prompt ระบบจะละเว้นให้อัตโนมัติชั่วคราวนะครับ")
            
        prompt_count_iso = st.number_input("จำนวน Prompts", min_value=1, max_value=500, step=10, value=50, key="iso_count")
        
        st.markdown("---")
        st.subheader("🖼️ Aspect Ratio (สัดส่วนภาพ)")
        is_random_ar_iso = st.checkbox("🎲 สุ่มสัดส่วนภาพอัตโนมัติ (คละกัน)", value=True, key="iso_rand_ar")
        
        if is_random_ar_iso:
            st.info("ระบบจะสุ่มสัดส่วน 1:1, 4:5, 3:2, 16:9, 9:16 ให้คละกัน")
            aspect_ratio_iso = "Auto"
        else:
            aspect_ratio_iso = st.selectbox("เลือกล็อกสัดส่วนภาพแบบตายตัว:", ["1:1", "4:5", "3:2", "16:9", "9:16"], index=0, key="iso_ar_sel")

        st.markdown("---")
        negative_prompt_iso = st.text_area("Negative Prompt (โหมดกันเงา)", value=strict_isolated_neg_prompt, height=180, key="iso_neg")
        st.markdown("---")
        st.success(f"🎚️ **Stylize Range (--s):** {s_min_iso} - {s_max_iso}")

    st.subheader("📍 ขั้นตอนที่ 2: กำหนดโครงสร้าง (Isolated Elements)")
    col1, col2 = st.columns(2)
    with col1:
        subject_options = ["Auto (สุ่ม)", "✏️ พิมพ์กำหนดเอง (Custom Input)"] + available_subjects
        subject = st.selectbox("1. SUBJECT (วัตถุเป้าหมาย)", subject_options, key="iso_sub")
        
        custom_subject = ""
        if subject == "✏️ พิมพ์กำหนดเอง (Custom Input)":
            custom_subject = st.text_input("📝 พิมพ์ชื่อวัตถุ (ภาษาอังกฤษ):", placeholder="เช่น isolated fresh red strawberry", key="iso_custom")

        dynamic = st.selectbox("2. DYNAMIC ACTION (การลอย)", ["Auto (สุ่ม)"] + available_dynamics, key="iso_dyn")
    with col2:
        lighting = st.selectbox("3. LIGHTING (แสงและขอบ)", ["Auto (สุ่ม)"] + available_lights, key="iso_light")
        camera = st.selectbox("4. CAMERA & LENS (กล้อง)", ["Auto (สุ่ม)"] + available_cameras, key="iso_cam")

    if st.button("🚀 Generate ISOLATED Prompts", use_container_width=True, key="iso_btn"):
        prompts_iso = []
        ar_choices_iso = ["1:1", "4:5", "3:2", "16:9", "9:16"]
        
        for i in range(prompt_count_iso):
            
            if subject == "✏️ พิมพ์กำหนดเอง (Custom Input)":
                 sel_subj = custom_subject if custom_subject.strip() != "" else "isolated object"
            elif subject == "Auto (สุ่ม)":
                 sel_subj = random.choice(available_subjects)
            else:
                 sel_subj = subject
                 
            sel_dyn = random.choice(available_dynamics) if dynamic == "Auto (สุ่ม)" else dynamic
            sel_light = random.choice(available_lights) if lighting == "Auto (สุ่ม)" else lighting
            sel_cam = random.choice(available_cameras) if camera == "Auto (สุ่ม)" else camera

            base_core_iso = "isolated object, extreme sharp focus on pure white background, absolute #FFFFFF backdrop, completely shadowless, ready for die-cut, premium stock photography object"
            prompt_elements_iso = [base_core_iso, sel_subj, sel_dyn, sel_light, sel_cam]
            clean_base_iso = ", ".join(prompt_elements_iso)
            stylize_value_iso = random.randint(s_min_iso, s_max_iso)
            
            sel_ar_iso = random.choice(ar_choices_iso) if is_random_ar_iso else aspect_ratio_iso
            
            final_prompt_iso = f"{clean_base_iso}"
            if negative_prompt_iso and mj_version_iso not in ["8.1", "8.0"]:
                final_prompt_iso += f" --no {negative_prompt_iso.strip()}"
                
            final_prompt_iso += f" --ar {sel_ar_iso} --s {stylize_value_iso} --style raw --v {mj_version_iso}"
                    
            prompts_iso.append(final_prompt_iso)
            
        st.session_state['prompts_isolated'] = prompts_iso
        st.success(f"✅ เจนเรียบร้อย {prompt_count_iso} Prompts (โหมดสุ่มสัดส่วน: {'เปิด' if is_random_ar_iso else 'ปิด'})")

    if 'prompts_isolated' in st.session_state:
        st.markdown("### 👀 Preview Prompts (Isolated)")
        for p in st.session_state['prompts_isolated'][:5]:
            st.code(p, language="text")
            
        prompt_text_iso = "\n\n".join(st.session_state['prompts_isolated'])
        
        safe_industry_iso = re.sub(r'[^a-zA-Z0-9]+', '_', selected_industry_iso).strip('_') if "🌟" not in selected_industry_iso else "All"
        file_name_iso = f"mj_ISOLATED_{safe_industry_iso}_prompts.txt"
        st.download_button(label="💾 ดาวน์โหลดไฟล์ .txt", data=prompt_text_iso, file_name=file_name_iso, mime="text/plain", use_container_width=True, key="iso_dl")
