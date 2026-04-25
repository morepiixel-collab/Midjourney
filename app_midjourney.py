import streamlit as st
import random
import re

# --- ตั้งค่าหน้าเว็บ Streamlit (ต้องอยู่บนสุดเสมอ) ---
st.set_page_config(page_title="OMEGA GOD MODE: 2-in-1 Engine", page_icon="⚡", layout="wide")

# ==========================================
# 🎛️ MASTER SWITCH: ปุ่มสลับหน้าต่างทำงาน
# ==========================================
st.sidebar.title("🎛️ Master Switch")
app_mode = st.sidebar.radio(
    "เลือกเครื่องมือที่คุณต้องการใช้งาน:",
    ["🏛️ เครื่องจักรสร้างแท่นวาง (Podiums)", "⚪ เครื่องจักรสร้างฉากขาว (Isolated)"]
)
st.sidebar.markdown("---")


# ==========================================================================================
# 🟩 ส่วนที่ 1: โค้ดสำหรับ "เครื่องจักรสร้างแท่นวาง" (โค้ดดั้งเดิมของคุณ 100% ไม่มีปรับลอจิก)
# ==========================================================================================
if app_mode == "🏛️ เครื่องจักรสร้างแท่นวาง (Podiums)":

    # 🏢 1.1 DNA โหมด NORMAL (Everyday Commercial)
    DNA_NORMAL = {
        "💼 Corporate & Workspace": {
            "scenes": ["modern office hallway", "glass corridor", "startup workspace", "meeting room", "minimalist desk surface", "clean architectural background"],
            "lights": ["natural side lighting", "cool clean office daylight"],
            "cameras": ["standard architectural photography lens", "crisp wide angle commercial shot"],
            "uis": ["wide banner composition for web headers", "standard rule of thirds composition"],
            "colors": ["neutral corporate blue and gray tones", "clean bright everyday color palette"],
            "stylize_range": (100, 180)
        },
        "🏫 Education & School": {
            "scenes": ["modern minimalist classroom with empty desks", "quiet school corridor with soft sunlight", "bright university library with bookshelves"],
            "lights": ["bright morning classroom lighting", "soft diffused window light"],
            "cameras": ["50mm lens natural perspective", "clean documentary style"],
            "uis": ["centered layout with top copy space", "wide empty space on the left"],
            "colors": ["warm inviting wood tones and crisp white", "bright educational primary colors"],
            "stylize_range": (100, 180)
        },
        "🏠 Home & Daily Life": {
            "scenes": ["clean modern bathroom with marble surfaces", "bright airy minimalist kitchen with clean countertops", "modern supermarket aisle with blurred products"],
            "lights": ["soft morning home lighting", "bright clean kitchen daylight"],
            "cameras": ["lifestyle product photography style", "35mm lens for natural room feel"],
            "uis": ["natural asymmetric composition", "side copy space for lifestyle text"],
            "colors": ["warm comforting home tones", "fresh morning natural colors"],
            "stylize_range": (80, 150)
        }
    }

    # 🎄 1.2 DNA โหมด HOLIDAY (Seasonal Podiums)
    DNA_HOLIDAY = {
        "🧧 Jan-Feb (New Year & Valentine)": {
            "scenes": ["[Jan-Feb] premium red and gold lacquer podium for Lunar New Year", "[Feb] romantic frosted pink glass podium for Valentine's Day"],
            "lights": ["warm festive ambient glow", "soft romantic diffused light"],
            "cameras": ["85mm lens, professional depth of field", "shot on medium format, highly detailed"],
            "uis": ["wide empty copy space for festive promotions", "centered layout for seasonal greeting"],
            "colors": ["auspicious crimson red and metallic gold", "soft romantic pink and elegant rose gold"],
            "stylize_range": (150, 250)
        },
        "💦 Apr (Songkran & Spring)": {
            "scenes": ["[Apr] smooth white marble podium with soft water ripples for Songkran summer theme", "minimalist stone pedestal with Sakura petals falling"],
            "lights": ["vibrant high-contrast summer sun", "soft peaceful spring daylight"],
            "cameras": ["fast shutter speed to freeze water ripples", "dreamy soft focus lens"],
            "uis": ["dynamic layout with splash space", "centered calm composition"],
            "colors": ["refreshing cyan and summer blue", "soft pastel pink and pure white"],
            "stylize_range": (100, 200)
        },
        "🎃 Oct-Nov (Halloween & Diwali & Black Friday)": {
            "scenes": ["[Oct] matte white geometric steps decorated with subtle autumn leaves", "[Oct-Nov] luxury dark obsidian platform with glowing diya lamps", "[Nov] dark sleek podium for Black Friday tech sale"],
            "lights": ["moody autumn evening light", "glowing ambient fire light"],
            "cameras": ["high contrast cinematic style", "sharp commercial focus"],
            "uis": ["lower third empty space for sale text", "dramatic negative space on the left"],
            "colors": ["warm autumn orange and brown", "stealth black with bold red sale accents"],
            "stylize_range": (150, 300)
        },
        "🎄 Dec (Christmas & Year End)": {
            "scenes": ["[Dec] minimalist stone pedestal surrounded by elegant Christmas pine and soft bokeh", "[Dec] luxury hotel lobby display podium with subtle festive decor"],
            "lights": ["festive warm bokeh lighting", "cozy winter window light"],
            "cameras": ["50mm lens, creamy holiday lights bokeh", "crisp commercial photography"],
            "uis": ["lower third empty space for holiday sale text", "perfectly balanced negative space"],
            "colors": ["pine green, warm gold, and crisp snow white", "classic winter wonderland tones"],
            "stylize_range": (150, 250)
        }
    }

    # 💎 1.3 DNA โหมด PREMIUM (14 อุตสาหกรรม ครบ 100%)
    DNA_PREMIUM = {
        "🧴 Skincare & Hydration": {
            "scenes": ["frosted glass cylinder podium emerging from crystal clear rippling water", "minimalist natural stone pedestal surrounded by dynamic clear water splashes"],
            "lights": ["soft diffused studio lighting", "clean bright shadowless e-commerce lighting"],
            "cameras": ["shot on 100mm macro lens, sharp focus on water droplets", "85mm lens, creamy bokeh background"],
            "uis": ["wide empty copy space on the left for cosmetics typography", "centered product placement with clean negative space"],
            "colors": ["clinical cyan and stark white tones", "refreshing aquatic blue and pure white"],
            "stylize_range": (80, 160)
        },
        "🥼 Clinical & Dermocosmetics": {
            "scenes": ["sterile white marble podium in a bright minimalist skincare laboratory", "premium brushed stainless steel medical pedestal in a clean white environment"],
            "lights": ["bright crisp clinical lighting", "clean shadowless lighting setup"],
            "cameras": ["sharp digital medium format", "100mm macro for clinical precision"],
            "uis": ["clean minimalist layout with ample negative space", "side copy space for scientific claims"],
            "colors": ["sterile stark white and subtle clinical blue", "minimalist pure white with silver accents"],
            "stylize_range": (40, 90)
        },
        "💎 High-End Luxury": {
            "scenes": ["black obsidian podium with subtle gold marble veins", "presentation pedestal elegantly draped in flowing dark emerald velvet"],
            "lights": ["dramatic elegant spotlighting with soft falloff", "moody studio lighting with gold reflections"],
            "cameras": ["shot on 85mm f/1.4, luxurious creamy bokeh", "high-end editorial fashion photography style"],
            "uis": ["centered minimalist composition", "elegant top negative space for serif typography"],
            "colors": ["luxurious rich emerald and gold tones", "deep burgundy and polished brass accents"],
            "stylize_range": (100, 180)
        },
        "🌿 Organic & Wellness": {
            "scenes": ["wabi-sabi style textured clay podium with minimal organic dried foliage", "premium terrazzo stone platform with moss accents"],
            "lights": ["soft dappled sunlight filtering through leaves", "warm morning golden hour lighting"],
            "cameras": ["Kodak Portra 400 film stock simulation, subtle film grain", "shot on 50mm lens, natural documentary style"],
            "uis": ["perfectly balanced negative space for magazine layout", "top copy space for organic brand messaging"],
            "colors": ["earthy organic neutral tones", "warm beige, terracotta, and muted sage green"],
            "stylize_range": (20, 70)
        },
        "💻 Tech & Men's Grooming": {
            "scenes": ["brutalist raw concrete block with graphic shadows", "sleek brushed gunmetal circular podium in a dark tech environment"],
            "lights": ["dramatic editorial hard spotlight with sharp shadows", "minimalist neon edge lighting"],
            "cameras": ["shot on Hasselblad medium format, extreme high contrast", "sharp digital medium format"],
            "uis": ["wide empty copy space on the right for tech specifications", "lower third empty space for UI buttons"],
            "colors": ["charcoal and matte black tones with subtle silver", "dark moody cyber tones with one accent color"],
            "stylize_range": (150, 250)
        },
        "🚗 Automotive & Parts": {
            "scenes": ["high-tech carbon fiber display platform in a modern dark garage", "brushed aluminum circular podium with industrial asphalt texture", "forged steel pedestal with sharp geometric lines"],
            "lights": ["dramatic hard edge lighting to highlight metallic curves", "cool blue industrial studio lighting"],
            "cameras": ["shot on Hasselblad medium format, extreme detail on metal texture", "wide angle 24mm lens for heroic scale"],
            "uis": ["side copy space for technical specifications", "lower third space for automotive brand name"],
            "colors": ["metallic silver and deep charcoal blacks", "high-contrast racing red and black"],
            "stylize_range": (180, 280)
        },
        "🐾 Pet Food & Pet Care": {
            "scenes": ["rustic light oak wooden podium on a clean sunlit kitchen floor", "matte ceramic pedestal surrounded by fresh organic ingredients", "minimalist wooden stand in a bright airy living room"],
            "lights": ["warm natural morning sunlight", "soft airy high-key studio lighting"],
            "cameras": ["low angle pet-eye view shot on 50mm lens", "shot on 85mm, soft natural depth of field"],
            "uis": ["top copy space for pet brand logo", "wide empty space on the right for nutrition facts"],
            "colors": ["warm earthy browns and leafy greens", "vibrant friendly orange and teal"],
            "stylize_range": (60, 130)
        },
        "🍭 Gen-Z & Pop Cosmetics": {
            "scenes": ["pastel pink geometric acrylic display blocks", "minimalist matte colorful arches and steps"],
            "lights": ["bright high-key studio lighting", "playful colored gel lighting setup"],
            "cameras": ["crisp commercial digital photography", "flash photography style with distinct shadows"],
            "uis": ["dynamic asymmetrical layout with copy space", "bold center placement with framing elements"],
            "colors": ["vibrant high-contrast complementary colors", "soft pastel holographic and neon tones"],
            "stylize_range": (250, 450)
        },
        "☕ Edibles & Supplements": {
            "scenes": ["rich rustic walnut wood slice serving as a premium display stand", "dark rough slate stone podium with subtle warm natural lighting"],
            "lights": ["warm appetizing directional light", "soft morning sunlight"],
            "cameras": ["shot on 85mm lens, shallow depth of field", "food photography style, macro details"],
            "uis": ["centered composition with top copy space", "wide side copy space for nutritional info"],
            "colors": ["warm rich earthy tones", "fresh morning natural colors"],
            "stylize_range": (70, 140)
        },
        "🏋️‍♂️ Fitness & Sports Nutrition": {
            "scenes": ["matte black rubberized texture podium in a moody athletic gym environment", "perforated dark steel industrial pedestal with cool rim lighting"],
            "lights": ["dramatic high-contrast gym lighting", "cool industrial rim lighting"],
            "cameras": ["wide angle heroic perspective", "gritty film look with high contrast"],
            "uis": ["bold typography layout with side copy space", "centered heroic product placement"],
            "colors": ["stealth black with neon accents", "cool steel gray and electric blue"],
            "stylize_range": (100, 200)
        },
        "👶 Baby & Maternity": {
            "scenes": ["soft pure cotton draped over a gentle rounded podium", "smooth matte ceramic pastel podium resting on soft white fluffy cloud-like textures"],
            "lights": ["ultra-soft diffused airy lighting", "gentle morning window light"],
            "cameras": ["shot on 50mm, soft glowing highlights", "dreamy pastel photography style"],
            "uis": ["generous soft negative space all around", "gentle curved layout with side text space"],
            "colors": ["pure warm white and soft cream", "delicate baby blue and pastel pink"],
            "stylize_range": (50, 120)
        },
        "♻️ Eco-Sustainability": {
            "scenes": ["premium compressed recycled paper block serving as a sustainable product podium", "raw packed earth pedestal with natural green moss accents"],
            "lights": ["clean natural daylight", "soft dappled forest lighting"],
            "cameras": ["raw unedited photography style", "documentary style medium format"],
            "uis": ["minimalist clean layout for eco messaging", "wide empty space on the left"],
            "colors": ["raw natural brown and muted green", "clean off-white and earth tones"],
            "stylize_range": (20, 80)
        },
        "🔮 Ethereal & Abstract": {
            "scenes": ["floating crystal prism podium creating subtle rainbow light refractions", "abstract curved alabaster stone pedestal in a surreal minimalist white space"],
            "lights": ["ethereal glowing ambient light", "sharp directional light creating prism refractions"],
            "cameras": ["artistic high-fashion photography", "dreamy soft focus lens"],
            "uis": ["vast negative space for high-end design", "unconventional asymmetrical layout"],
            "colors": ["iridescent pearl and holographic tones", "pure surreal white with subtle color shifts"],
            "stylize_range": (300, 600)
        },
        "🛁 Bathroom Shelf": {
            "scenes": ["clean minimalist bathroom shelf with soft natural window light and subtle steam", "luxury vanity counter with marble surfaces and subtle bokeh reflections"],
            "lights": ["soft morning bathroom window light", "clean spa-like ambient lighting"],
            "cameras": ["lifestyle product photography style", "85mm lens for intimate product focus"],
            "uis": ["side copy space for personal care routine text", "clean centered layout"],
            "colors": ["refreshing spa aqua and white", "warm comforting cream and beige"],
            "stylize_range": (70, 130)
        }
    }

    # ==========================================
    # ⚡ UI: โหมดแท่นวาง
    # ==========================================
    st.title("⚡ OMEGA GOD MODE: Commercial Engine")
    st.markdown("ระบบผลิต Prompt โหมดแท่นวางสินค้า (Podiums)")
    st.markdown("---")

    st.subheader("🎯 ขั้นตอนที่ 1: เลือกโหมดการทำงานหลัก")
    work_mode = st.radio(
        "ระบบจะดึงฐานข้อมูลอุตสาหกรรมตามโหมดที่คุณเลือก:", 
        [
            "🏢 โหมดปกติ (Corporate & Everyday)", 
            "🎄 โหมดเทศกาล (Seasonal Podiums)", 
            "💎 โหมด Premium Product (Podium & High-End)"
        ],
        horizontal=True,
        index=2
    )

    if "Premium" in work_mode or "พรีเมียม" in work_mode:
        current_dna_dict = DNA_PREMIUM
        mode_th = "โหมดพรีเมียม"
        mode_name = "Premium"
        default_ar_index = 0 # 16:9
        default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, octane render, unreal engine, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"
    elif "เทศกาล" in work_mode:
        current_dna_dict = DNA_HOLIDAY
        mode_th = "โหมดเทศกาล"
        mode_name = "Holiday"
        default_ar_index = 1 # 3:2
        default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, text, watermark, logo, signatures, people, person, face, hand, product, bottle, box"
    else:
        current_dna_dict = DNA_NORMAL
        mode_th = "โหมดปกติ"
        mode_name = "Normal"
        default_ar_index = 1 # 3:2
        default_neg_prompt = "vector, 3d, illustration, cartoon, render, cgi, text, watermark, logo, signatures"

    st.markdown("---")

    st.subheader(f"🏭 ขั้นตอนที่ 2: เลือกอุตสาหกรรมเป้าหมาย (ใน{mode_th})")
    industry_options = ["🌟 สุ่มผสมทุกหมวด (All in this mode)"] + list(current_dna_dict.keys())
    selected_industry = st.selectbox("เลือกอุตสาหกรรมที่ต้องการเจาะตลาด:", industry_options)

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
        
        if any(x in selected_industry for x in ["Tech", "Automotive", "Skincare", "Luxury"]):
            default_ar_index = 0 
        elif any(x in selected_industry for x in ["Corporate", "Pet Food", "Baby"]):
            default_ar_index = 1 
        else:
            default_ar_index = 1 

    with st.sidebar:
        st.header("⚙️ Settings")
        prompt_count = st.number_input("จำนวน Prompts", min_value=1, max_value=500, step=10, value=50)
        aspect_ratio = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["16:9", "3:2", "1:1", "4:5", "9:16"], index=default_ar_index)
        
        st.markdown("---")
        st.subheader("🛡️ Strict Photo Mode")
        negative_prompt = st.text_area("Negative Prompt", value=default_neg_prompt, height=140)
        
        st.markdown("---")
        if selected_industry != "🌟 สุ่มผสมทุกหมวด (All in this mode)":
            st.success(f"🎚️ **Stylize Range (--s):** {s_min} - {s_max}")
        else:
            st.info("🎚️ **Stylize Range (--s):** 80 - 200 (Mode: All)")

    st.subheader("📍 ขั้นตอนที่ 3: กำหนดโครงสร้าง (Filtered DNA Modules)")
    col1, col2, col3 = st.columns(3)
    with col1:
        scene = st.selectbox("1. SCENE (แท่นวาง)", ["Auto (สุ่มตาม DNA)"] + available_scenes)
        lighting = st.selectbox("2. LIGHTING (แสง)", ["Auto (สุ่มตาม DNA)"] + available_lights)
    with col2:
        camera = st.selectbox("3. CAMERA & LENS (กล้อง)", ["Auto (สุ่มตาม DNA)"] + available_cameras)
        ui_layout = st.selectbox("4. UI LAYOUT (เลย์เอาต์)", ["Auto (สุ่มตาม DNA)"] + available_uis)
    with col3:
        color_psych = st.selectbox("5. COLOR PSYCHOLOGY (สี)", ["Auto (สุ่มตาม DNA)"] + available_colors)

    if st.button("🚀 Generate PERFECT Prompts", use_container_width=True):
        prompts = []
        for i in range(prompt_count):
            sel_scene_raw = random.choice(available_scenes) if scene == "Auto (สุ่มตาม DNA)" else scene
            sel_scene = re.sub(r'\[.*?\]\s*', '', sel_scene_raw).strip()
            sel_light = random.choice(available_lights) if lighting == "Auto (สุ่มตาม DNA)" else lighting
            sel_cam = random.choice(available_cameras) if camera == "Auto (สุ่มตาม DNA)" else camera
            sel_ui = random.choice(available_uis) if ui_layout == "Auto (สุ่มตาม DNA)" else ui_layout
            sel_color = random.choice(available_colors) if color_psych == "Auto (สุ่มตาม DNA)" else color_psych

            if mode_name in ["Premium", "Holiday"]:
                base_core = "empty product mockup background, extreme high-end commercial asset, photography award winner"
            else:
                base_core = "empty commercial background, high-end stock photography"
                
            prompt_elements = [base_core, sel_scene, sel_light, sel_cam, sel_color, sel_ui]
            clean_base = ", ".join(prompt_elements)
            
            stylize_value = random.randint(s_min, s_max)
            
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
        
        safe_industry = re.sub(r'[^a-zA-Z0-9]+', '_', selected_industry).strip('_') if "🌟" not in selected_industry else "All"
        file_name = f"mj_DNA_{mode_name}_{safe_industry}_prompts.txt"
        st.download_button(label="💾 ดาวน์โหลดไฟล์ .txt", data=prompt_text, file_name=file_name, mime="text/plain", use_container_width=True)


# ==========================================================================================
# ⚪ ส่วนที่ 2: โค้ดสำหรับ "เครื่องจักรสร้างฉากขาว (ISOLATED)" (ทำงานแยกเป็นเอกเทศ ไม่กวนของเดิม)
# ==========================================================================================
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

    st.title("⚪ ISOLATED MASTER ENGINE")
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
        prompt_count_iso = st.number_input("จำนวน Prompts", min_value=1, max_value=500, step=10, value=50, key="iso_count")
        aspect_ratio_iso = st.selectbox("สัดส่วนภาพ (Aspect Ratio)", ["1:1", "16:9", "3:2", "4:5", "9:16"], index=0, key="iso_ar")
        st.markdown("---")
        negative_prompt_iso = st.text_area("Negative Prompt (โหมดกันเงา)", value=strict_isolated_neg_prompt, height=180, key="iso_neg")
        st.markdown("---")
        st.success(f"🎚️ **Stylize Range (--s):** {s_min_iso} - {s_max_iso}")

    st.subheader("📍 ขั้นตอนที่ 2: กำหนดโครงสร้าง (Isolated Elements)")
    col1, col2 = st.columns(2)
    with col1:
        # --- อัปเดต: เรียงลำดับตัวเลือก "พิมพ์กำหนดเอง" ให้อยู่ต่อจาก "Auto (สุ่ม)" ทันที ---
        subject_options = ["Auto (สุ่ม)", "✏️ พิมพ์กำหนดเอง (Custom Input)"] + available_subjects
        subject = st.selectbox("1. SUBJECT (วัตถุเป้าหมาย)", subject_options, key="iso_sub")
        
        # --- แสดงช่องพิมพ์ข้อความถ้าเลือก "พิมพ์กำหนดเอง" ---
        custom_subject = ""
        if subject == "✏️ พิมพ์กำหนดเอง (Custom Input)":
            custom_subject = st.text_input("📝 พิมพ์ชื่อวัตถุ (ภาษาอังกฤษ):", placeholder="เช่น isolated fresh red strawberry", key="iso_custom")

        dynamic = st.selectbox("2. DYNAMIC ACTION (การลอย)", ["Auto (สุ่ม)"] + available_dynamics, key="iso_dyn")
    with col2:
        lighting = st.selectbox("3. LIGHTING (แสงและขอบ)", ["Auto (สุ่ม)"] + available_lights, key="iso_light")
        camera = st.selectbox("4. CAMERA & LENS (กล้อง)", ["Auto (สุ่ม)"] + available_cameras, key="iso_cam")

    if st.button("🚀 Generate ISOLATED Prompts", use_container_width=True, key="iso_btn"):
        prompts_iso = []
        for i in range(prompt_count_iso):
            
            # --- ลอจิกดึงค่า Subject สำหรับแบบพิมพ์เอง ---
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
            
            final_prompt_iso = f"/imagine prompt: {clean_base_iso} --ar {aspect_ratio_iso} --s {stylize_value_iso} --style raw --v 7"
            if negative_prompt_iso:
                final_prompt_iso += f" --no {negative_prompt_iso.strip()}"
            prompts_iso.append(final_prompt_iso)
            
        st.session_state['prompts_isolated'] = prompts_iso
        st.success(f"✅ เจนเรียบร้อย {prompt_count_iso} Prompts (หมวด: {selected_industry_iso})")

    if 'prompts_isolated' in st.session_state:
        st.markdown("### 👀 Preview Prompts (Isolated)")
        for p in st.session_state['prompts_isolated'][:5]:
            st.code(p, language="text")
        prompt_text_iso = "\n".join(st.session_state['prompts_isolated'])
        
        safe_industry_iso = re.sub(r'[^a-zA-Z0-9]+', '_', selected_industry_iso).strip('_') if "🌟" not in selected_industry_iso else "All"
        file_name_iso = f"mj_ISOLATED_{safe_industry_iso}_prompts.txt"
        st.download_button(label="💾 ดาวน์โหลดไฟล์ .txt", data=prompt_text_iso, file_name=file_name_iso, mime="text/plain", use_container_width=True, key="iso_dl")
