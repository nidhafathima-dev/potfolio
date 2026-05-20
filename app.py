import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- 🚀 PORTFOLIO CONFIGURATION 🚀 ---
# Edit these variables to update your portfolio text
GREETING = "HI, I'M NIDHA"
HERO_PARA = "“A jack of all trades, master of none — and so what? I am happy as I am.”"
ATTRIBUTES = ["DESIGNER", "ENGINEER", "READER", "WRITER"]
ABOUT_ME = "I am a first-year engineering student who is entirely new to the tech world but driven by curiosity and a strong desire to learn. I enjoy exploring creative spaces, especially designing posters and working with Figma, which allows me to express my ideas visually. Aside from technology and design, I am an avid reader who loves discovering new perspectives and ideas through books. I also enjoy solving real-world problems and designing impactful solutions, believing that even small ideas can create meaningful change. I believe in learning step by step, growing through experience, and exploring different fields with an open and curious mind."

# Paths to your images (in assets/ folder)
HERO_IMAGE_PATH = "/Users/nidhafathima/.gemini/antigravity/brain/2fc9ca7f-90e2-4d73-9d96-36133232143a/media__1775285859504.png"
ENG_TICKER_PATH = "assets/ticker_engineering.png"
READ_TICKER_PATH = "assets/ticker_reading.png"
TICKER_1 = "assets/ticker_1.jpg"
TICKER_2 = "assets/ticker_2.jpg"
TICKER_3 = "assets/ticker_3.jpg"
TICKER_4 = "assets/ticker_4.jpg"
TICKER_5 = "assets/ticker_5.jpg"
ABOUT_1 = "assets/about_1.png"
ABOUT_2 = "assets/about_2.png"
ABOUT_3 = "assets/about_3.png"
ABOUT_4 = "assets/about_4.png"
DESIGN_HACKWAVE = "assets/design_hackwave.jpg"
DESIGN_KILIYE = "assets/design_kiliye.jpg"
DESIGN_THEYYAM = "assets/design_theyyam.jpg"
DESIGN_STRANGER_THINGS = "assets/design_stranger_things.jpg"
DESIGN_BMW = "assets/design_bmw.jpg"
DESIGN_MADMAX = "assets/design_madmax.jpg"
DESIGN_FIGHTCLUB = "assets/design_fightclub.jpg"
DESIGN_PREMAM = "assets/design_premam.jpg"
DESIGN_COVER = "assets/design_cover.jpg"

# --- 🎨 THEME COLORS 🎨 ---
THEME_BLUE = "#151345"
THEME_BLACK = "#000000"
THEME_TEXT = "#ffffff"
THEME_TEXT_SECONDARY = "#a0a0b8"

# Page Configuration
st.set_page_config(page_title="Nidha | Portfolio", page_icon="🎨", layout="wide")

# CSS to remove Streamlit's default padding and spacing
st.markdown("""
    <style>
    #root > div:nth-child(1) > div > div > div > div > section > div {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
    .main {
        background-color: #000000;
    }
    header[data-testid="stHeader"] {
        display: none;
    }
    footer {
        display: none;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
        overflow: hidden;
    }
    iframe {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        z-index: 999999;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

def get_base64_image(image_path):
    if os.path.exists(image_path):
        ext = os.path.splitext(image_path)[1].lower()
        mime = "image/png" if ext == ".png" else "image/jpeg"
        with open(image_path, "rb") as img_file:
            return f"data:{mime};base64,{base64.b64encode(img_file.read()).decode()}"
    return ""

# Encode Current Assets
hero_b64 = get_base64_image(HERO_IMAGE_PATH)
eng_ticker_b64 = get_base64_image(ENG_TICKER_PATH)
read_ticker_b64 = get_base64_image(READ_TICKER_PATH)
t1_b64 = get_base64_image(TICKER_1)
t2_b64 = get_base64_image(TICKER_2)
t3_b64 = get_base64_image(TICKER_3)
t4_b64 = get_base64_image(TICKER_4)
t5_b64 = get_base64_image(TICKER_5)
a1_b64 = get_base64_image(ABOUT_1)
a2_b64 = get_base64_image(ABOUT_2)
a3_b64 = get_base64_image(ABOUT_3)
a4_b64 = get_base64_image(ABOUT_4)
hackwave_b64 = get_base64_image(DESIGN_HACKWAVE)
kiliye_b64 = get_base64_image(DESIGN_KILIYE)
theyyam_b64 = get_base64_image(DESIGN_THEYYAM)
stranger_things_b64 = get_base64_image(DESIGN_STRANGER_THINGS)
bmw_b64 = get_base64_image(DESIGN_BMW)
madmax_b64 = get_base64_image(DESIGN_MADMAX)
fightclub_b64 = get_base64_image(DESIGN_FIGHTCLUB)
premam_b64 = get_base64_image(DESIGN_PREMAM)
cover_b64 = get_base64_image(DESIGN_COVER)

# --- PORTFOLIO HTML TEMPLATE ---
attr_spans = "".join([f"<span>{a.upper()}</span>" for a in ATTRIBUTES])

portfolio_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Outfit:wght@300;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: {THEME_TEXT};
            --secondary: {THEME_TEXT_SECONDARY};
            --accent: {THEME_BLUE};
            --bg-dark: {THEME_BLACK};
            --glass: rgba(21, 19, 69, 0.9);
            --border: rgba(255, 255, 255, 0.1);
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }}
        html {{ scroll-behavior: smooth; }}
        body {{
            font-family: 'Inter', sans-serif;
            background: var(--bg-dark);
            color: var(--primary);
            overflow-x: hidden;
            line-height: 1.6;
            width: 100%;
        }}

        h1, h2, h3, h4 {{ font-family: 'Inter', sans-serif; font-weight: 900; text-transform: uppercase; letter-spacing: -0.05em; }}

        .section-heading {{
            font-size: 4rem;
            text-align: center;
            margin-bottom: 2rem;
            opacity: 0.1;
            position: relative;
            top: 10px;
            z-index: 0;
            pointer-events: none;
            color: #fff;
            transition: 0.3s;
        }}

        .section-heading.fill-text {{
            opacity: 1;
            -webkit-text-stroke: 1px rgba(255, 255, 255, 0.8);
            color: transparent;
            --fill-val: 0%;
            background-image: linear-gradient(to top, #fff var(--fill-val), transparent var(--fill-val));
            background-repeat: no-repeat;
            -webkit-background-clip: text;
            background-clip: text;
            pointer-events: auto;
            display: inline-block;
            width: 100%;
        }}

        #navbar {{
            display: flex;
            justify-content: space-evenly;
            padding: 1.5rem 5%;
            width: 100%;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 9999;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-bottom: 1px solid var(--border);
        }}

        #navbar a {{ 
            text-decoration: none; 
            color: #fff; 
            font-weight: 900; 
            text-transform: uppercase; 
            font-size: 0.75rem; 
            letter-spacing: 0.25em; 
            transition: 0.3s;
            opacity: 0.6;
        }}
        #navbar a:hover {{ opacity: 1; }}

        #loader {{ 
            position: fixed; 
            top: 0; 
            left: 0; 
            width: 100%; 
            height: 100%; 
            background: #000; 
            z-index: 20000; 
            display: flex; 
            flex-direction: column;
            justify-content: center; 
            align-items: center; 
            transition: opacity 1s ease-in-out, visibility 1s;
        }}
        .spinner {{ 
            width: 40px; 
            height: 40px; 
            border: 2px solid rgba(255,255,255,0.05); 
            border-top-color: var(--accent); 
            border-radius: 50%; 
            animation: spin 1s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite; 
            margin-bottom: 1rem;
        }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
        .loader-text {{ color: #fff; font-size: 0.7rem; letter-spacing: 0.5em; opacity: 0.5; text-transform: uppercase; }}

        .hero {{
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 2rem;
            padding-top: 100px;
            background: #000;
        }}

        #greeting {{ 
            font-size: 14vw; 
            line-height: 0.8; 
            margin-bottom: -2vw; 
            color: #fff; 
            font-weight: 950;
            width: 100%;
            white-space: nowrap;
            letter-spacing: -0.04em;
            z-index: 1;
            transition: 0.5s;
        }}

        .face-container {{ 
            position: relative; 
            z-index: 2; 
            margin-top: -8vw;
        }}

        .float-wrapper {{
            animation: float 4s ease-in-out infinite;
        }}

        #face-hero {{
            width: 45vw;
            max-width: 650px;
            height: auto;
            object-fit: contain;
            filter: drop-shadow(0 40px 100px rgba(0, 0, 0, 0.9)) drop-shadow(0 10px 20px rgba(255,255,255,0.05));
            transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1), filter 0.5s ease;
            transform-style: preserve-3d;
            will-change: transform;
        }}

        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-30px); }}
        }}

        .hero-paragraph {{ 
            max-width: 600px; 
            font-size: 1.1rem; 
            color: var(--secondary); 
            margin-top: -2rem;
            margin-bottom: 0.5rem; 
            font-style: italic; 
            z-index: 3;
        }}

        .attributes {{ display: flex; gap: 2rem; font-weight: 700; text-transform: lowercase; opacity: 0.6; font-size: 1.2rem; color: var(--secondary); z-index: 3; margin-bottom: 2rem; }}

        #ticker-section {{ padding: 0; background: #000; overflow: hidden; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }}
        .ticker-row {{ display: flex; margin-bottom: 0; width: 200%; }}
        .ticker-content img {{ 
            width: 150px; 
            height: 250px; 
            object-fit: cover; 
            border-radius: 6px; 
            background: #0a0a1a; 
            border: 1px solid var(--border);
            transform: rotate(90deg);
        }}
        .ticker-content {{ display: flex; gap: 0.5rem; animation: move-right 30s linear infinite; padding: 0.5rem 0; }}
        .row-left .ticker-content {{ animation: move-left 30s linear infinite; }}
        @keyframes move-right {{ 0% {{ transform: translateX(-50%); }} 100% {{ transform: translateX(0%); }} }}
        @keyframes move-left {{ 0% {{ transform: translateX(0%); }} 100% {{ transform: translateX(-50%); }} }}
        .ticker-item-wrapper {{ display: flex; align-items: center; justify-content: center; width: 250px; height: 150px; overflow: hidden; }}

        #about {{ min-height: 100vh; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden; padding: 4rem 2rem; background: #000; }}
        .about-content {{ max-width: 800px; text-align: center; z-index: 10; position: relative; }}
        .about-obj {{ 
            position: absolute; 
            z-index: 1; 
            pointer-events: none; 
            transition: transform 1.2s cubic-bezier(0.22, 1, 0.36, 1);
        }}
        
        /* Initial Positions */
        .obj-1 {{ top: 5%; left: 2%; transform: translateX(-200px); }}
        .obj-2 {{ top: 10%; right: 2%; transform: translateX(200px); }}
        .obj-3 {{ bottom: 10%; left: 5%; transform: translateX(-200px); }}
        .obj-4 {{ bottom: 5%; right: 5%; transform: translateX(200px); }}
        
        .about-obj.visible {{ transform: translateX(0); }}

        .obj-bob {{ 
            width: 18vw; 
            max-width: 250px; 
            filter: drop-shadow(0 20px 50px rgba(0,0,0,0.8)); 
            opacity: 0.9;
        }}
        
        /* Specific Idle Tilts */
        .obj-1 img {{ transform: rotate(-15deg); animation: gentle-tilt 8s infinite ease-in-out; }}
        .obj-2 img {{ width: 14vw; max-width: 200px; transform: rotate(12deg); animation: gentle-tilt 10s infinite ease-in-out reverse; }}
        .obj-3 img {{ transform: rotate(10deg); animation: gentle-tilt 7s infinite ease-in-out; }}
        .obj-4 img {{ transform: rotate(-8deg); animation: gentle-tilt 9s infinite ease-in-out reverse; }}
        
        @keyframes gentle-tilt {{ 
            0%, 100% {{ transform: translateY(0) rotate(var(--rot, -10deg)); }} 
            50% {{ transform: translateY(-40px) rotate(var(--rot-mid, -5deg)); }} 
        }}
        
        /* Set individual rotation variables for the animation */
        .obj-1 img {{ --rot: -15deg; --rot-mid: -10deg; }}
        .obj-2 img {{ --rot: 12deg; --rot-mid: 17deg; }}
        .obj-3 img {{ --rot: 10deg; --rot-mid: 15deg; }}
        .obj-4 img {{ --rot: -8deg; --rot-mid: -3deg; }}

        #designs {{ min-height: 100vh; padding: 4rem 2rem; background: #050505; display: flex; flex-direction: column; align-items: center; justify-content: center; border-top: 1px solid var(--border); }}
        .flipbook-container {{ perspective: 1500px; margin-top: 1rem; }}
        .flipbook {{ width: 450px; height: 620px; position: relative; transform-style: preserve-3d; cursor: pointer; }}
        .page {{ position: absolute; width: 100%; height: 100%; background: #111; border: 1px solid var(--border); backface-visibility: hidden; transform-origin: left; transition: transform 1.2s cubic-bezier(0.645, 0.045, 0.355, 1); color: #fff; overflow: hidden; }}
        .page.flipped {{ transform: rotateY(-165deg); }}
        .page.cover {{ background: #000; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0; }}

        #projects {{ min-height: 100vh; padding: 4rem 2rem; background: #000; display: flex; flex-direction: column; justify-content: center; }}
        .stacks-container {{ width: 100%; max-width: 600px; margin: 1rem auto; }}
        .project-tab {{ 
            background: rgba(255, 255, 255, 0.03); 
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1); 
            padding: 2.5rem; 
            border-radius: 24px; 
            display: flex; 
            flex-direction: column;
            align-items: flex-start; 
            gap: 1.5rem; 
            opacity: 0; 
            transform: translateY(40px) rotate(0deg); 
            transition: all 0.6s cubic-bezier(0.22, 1, 0.36, 1); 
            color: #fff; 
            position: relative;
            overflow: hidden;
            box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.02), 0 15px 35px rgba(0,0,0,0.5);
            margin-bottom: -100px;
            cursor: pointer;
        }}
        .project-tab:nth-child(1) {{ z-index: 5; }}
        .project-tab:nth-child(2) {{ z-index: 4; }}
        
        .project-tab.visible:nth-child(1) {{ transform: translateY(0) rotate(-2deg); opacity: 1; }}
        .project-tab.visible:nth-child(2) {{ transform: translateY(0) rotate(1deg); opacity: 1; }}

        .project-tab:hover {{ 
            z-index: 100 !important;
            background: rgba(255, 255, 255, 0.08); 
            border-color: rgba(255, 255, 255, 0.6); 
            transform: translateY(-20px) rotate(0deg) scale(1.05) !important;
            box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 30px rgba(255,255,255,0.1);
        }}
        .project-tab::before {{
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                120deg, 
                transparent, 
                rgba(255, 255, 255, 0.05), 
                transparent
            );
            transition: 0.8s;
        }}
        .project-tab:hover::before {{
            left: 100%;
        }}
        .project-desc {{ font-size: 0.95rem; opacity: 0.6; color: #fff; margin-top: 0.5rem; line-height: 1.6; font-weight: 300; }}
        .project-info h4 {{ font-size: 1.5rem; letter-spacing: 0.05em; }}

        #contact {{ min-height: 100vh; padding: 4rem 2rem; background: #000; color: #fff; text-align: center; border-top: 1px solid var(--border); display: flex; flex-direction: column; align-items: center; justify-content: center; }}
        .social-links {{ display: flex; justify-content: center; gap: 3rem; margin-bottom: 1.5rem; }}
        .social-links a {{ color: #fff; text-decoration: none; font-weight: 900; text-transform: uppercase; font-size: 1.5rem; opacity: 0.6; transition: 0.3s; }}
        .social-links a:hover {{ opacity: 1; color: var(--accent); text-shadow: 0 0 20px var(--accent); }}

        .trail-dot {{ position: absolute; width: 10px; height: 10px; background: #fff; border-radius: 50%; pointer-events: none; opacity: 0.6; filter: blur(4px); animation: fadeOut 1s forwards; z-index: 9999; }}
        @keyframes fadeOut {{ to {{ opacity: 0; transform: scale(3); }} }}

        /* MOBILE RESPONSIVENESS */
        @media (max-width: 768px) {{
            #navbar {{ 
                padding: 1rem; 
                font-size: 0.6rem; 
                gap: 0.5rem; 
                justify-content: center;
                flex-wrap: wrap;
            }}
            #navbar a {{ font-size: 0.6rem; }}
            
            #greeting {{ font-size: 18vw; white-space: normal; line-height: 1; }}
            .face-container {{ margin-top: 0; }}
            #face-hero {{ width: 250px; }}
            .hero-paragraph {{ font-size: 1rem; padding: 0 1rem; }}
            
            .section-heading {{ font-size: 2.5rem; }}
            
            .about-obj {{ width: 20vw; opacity: 0.4 !important; }}
            .obj-1 {{ top: 2%; left: -5%; }}
            .obj-2 {{ top: 5%; right: -5%; width: 18vw; }}
            .obj-3 {{ bottom: 5%; left: -0%; }}
            .obj-4 {{ bottom: 2%; right: -0%; }}
            
            .flipbook-container {{ 
                transform: scale(0.65); 
                margin-top: -50px;
                margin-bottom: -50px;
            }}
            
            .project-tab {{ padding: 1.5rem; }}
            .project-info h4 {{ font-size: 1.1rem; }}
            .project-desc {{ font-size: 0.8rem; }}
            
            .social-links {{ gap: 1rem; flex-wrap: wrap; }}
            .social-links a {{ font-size: 1rem; }}
        }}
    </style>
</head>
<body>
    <div id="loader">
        <div class="spinner"></div>
        <div class="loader-text">Loading Portfolio</div>
    </div>
    <header id="masthead">
        <nav id="navbar">
            <a href="#home">Home</a>
            <a href="#about">About Me</a>
            <a href="#designs">Portfolio</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact Me</a>
        </nav>
        <section id="home" class="hero">
            <h1 id="greeting">{GREETING.upper()}</h1>
            <div class="face-container">
                <div class="float-wrapper">
                    <img src="{hero_b64}" alt="Hero" id="face-hero">
                </div>
            </div>
            <p class="hero-paragraph">{HERO_PARA}</p>
            <div class="attributes">
                {attr_spans}
            </div>
        </section>
    </header>

    <section id="ticker-section">
        <div class="ticker-row row-right">
            <div class="ticker-content">
                <div class="ticker-item-wrapper"><img src="{t3_b64}"></div> <!-- O -->
                <div class="ticker-item-wrapper"><img src="{t1_b64}"></div> <!-- B -->
                <div class="ticker-item-wrapper"><img src="{t4_b64}"></div> <!-- O -->
                <div class="ticker-item-wrapper"><img src="{t2_b64}"></div> <!-- B -->
                <div class="ticker-item-wrapper"><img src="{t5_b64}"></div> <!-- O -->
                <div class="ticker-item-wrapper"><img src="{t1_b64}"></div> <!-- B -->
                <div class="ticker-item-wrapper"><img src="{t3_b64}"></div> <!-- O -->
                <div class="ticker-item-wrapper"><img src="{t2_b64}"></div> <!-- B -->
            </div>
        </div>
        <div class="ticker-row row-left">
            <div class="ticker-content">
                <div class="ticker-item-wrapper"><img src="{t2_b64}"></div> <!-- B -->
                <div class="ticker-item-wrapper"><img src="{t5_b64}"></div> <!-- O -->
                <div class="ticker-item-wrapper"><img src="{t1_b64}"></div> <!-- B -->
                <div class="ticker-item-wrapper"><img src="{t4_b64}"></div> <!-- O -->
                <div class="ticker-item-wrapper"><img src="{t2_b64}"></div> <!-- B -->
                <div class="ticker-item-wrapper"><img src="{t3_b64}"></div> <!-- O -->
                <div class="ticker-item-wrapper"><img src="{t1_b64}"></div> <!-- B -->
                <div class="ticker-item-wrapper"><img src="{t5_b64}"></div> <!-- O -->
            </div>
        </div>
    </section>

    <section id="about">
        <div class="about-obj obj-1"><img src="{a1_b64}" class="obj-bob"></div>
        <div class="about-obj obj-2"><img src="{a2_b64}" class="obj-bob"></div>
        <div class="about-obj obj-3"><img src="{a3_b64}" class="obj-bob"></div>
        <div class="about-obj obj-4"><img src="{a4_b64}" class="obj-bob"></div>
        <div class="about-content">
            <h2 class="section-heading fill-text" id="about-heading">ABOUT ME</h2>
            <p>{ABOUT_ME}</p>
        </div>
    </section>

    <section id="designs">
        <h2 class="section-heading fill-text">DESIGNS</h2>
        <div class="flipbook-container">
            <div class="flipbook" id="flip-book">
                <div class="page cover" style="z-index: 13;"><img src="{cover_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="page" style="z-index: 12;"><img src="{hackwave_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="page" style="z-index: 11;"><img src="{kiliye_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="page" style="z-index: 10;"><img src="{theyyam_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="page" style="z-index: 9;"><img src="{stranger_things_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="page" style="z-index: 8;"><img src="{bmw_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="page" style="z-index: 7;"><img src="{madmax_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="page" style="z-index: 6;"><img src="{fightclub_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
                <div class="page" style="z-index: 5;"><img src="{premam_b64}" style="width:100%; height:100%; object-fit:cover;"></div>
            </div>
        </div>
    </section>

    <section id="projects">
        <h2 class="section-heading fill-text">PROJECTS</h2>
        <div class="stacks-container">
            <div class="project-tab">
                <div class="project-info">
                    <h4>NexaGuard - AI-driven web vulnerability scanner</h4>
                    <p class="project-desc">Vanguard is an AI-powered cybersecurity simulation tool that I built for a hackathon to help developers quickly identify and fix vulnerabilities in their applications. It uses a multi-agent approach, where an Attacker AI simulates potential threats, an Analyzer AI evaluates and ranks the severity of those risks, and a Defender AI provides practical solutions to improve security. Instead of performing real attacks, Vanguard intelligently models possible weaknesses based on the system’s code or architecture and generates a clear, actionable report, making security analysis faster, more accessible, and easier to understand.</p>
                </div>
            </div>
            <div class="project-tab">
                <div class="project-info">
                    <h4>Leaflet - Personalized Reading App</h4>
                    <p class="project-desc">Leaflet is a personalized digital space designed to make reading immersive, accessible, and engaging. It allows users to explore a wide range of books across genres, track their reading progress, and build their own curated library. With features like customizable themes, bookmarking, and smooth navigation, the app creates a comfortable reading experience tailored to individual preferences.</p>
                </div>
            </div>
        </div>
    </section>

    <footer id="contact">
        <h2 class="section-heading fill-text">CONTACT ME</h2>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/nidha-fathima-ms" target="_blank">LinkedIn</a>
            <a href="https://github.com/nidhafathima-dev" target="_blank">GitHub</a>
            <a href="mailto:nidhafathimaabcd@gmail.com?subject=Inquiry from Portfolio">Draft an Email</a>
            <a href="https://www.instagram.com/nxdhaaa_?igsh=MXdyOXM3bGhkcGYyNg==" target="_blank">Instagram</a>
        </div>
        <p style="margin-top: 4rem; opacity: 0.3; font-size: 0.8rem;">© 2026 Nidha</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const hero = document.querySelector('.hero');
            const face = document.getElementById('face-hero');

            if (hero && face) {{
                hero.addEventListener('mousemove', (e) => {{
                    const rect = face.getBoundingClientRect();
                    const centerX = rect.left + rect.width / 2;
                    const centerY = rect.top + rect.height / 2;
                    const mouseX = e.clientX;
                    const mouseY = e.clientY;

                    const moveX = (mouseX - centerX) / 25;
                    const moveY = (mouseY - centerY) / 25;

                    face.style.transform = `translate3d(${{moveX}}px, ${{moveY}}px, 0)`;

                    // Trail dots logic
                    const dot = document.createElement('div');
                    dot.className = 'trail-dot';
                    dot.style.left = e.pageX + 'px';
                    dot.style.top = e.pageY + 'px';
                    document.body.appendChild(dot);
                    setTimeout(() => dot.remove(), 1000);
                }});

                hero.addEventListener('mouseleave', () => {{
                    face.style.transform = `translate3d(0, 0, 0)`;
                }});
            }}

            // Flipbook Logic
            let cur = 0;
            const pages = document.querySelectorAll('.page');
            const flipbook = document.getElementById('flip-book');
            if (flipbook) {{
                flipbook.addEventListener('click', () => {{
                    if(cur < pages.length) {{
                        pages[cur].classList.add('flipped');
                        cur++;
                    }} else {{
                        pages.forEach(p => p.classList.remove('flipped'));
                        cur = 0;
                    }}
                }});
            }}

            // Scroll Effects
            const headings = document.querySelectorAll('.fill-text');
            const tabs = document.querySelectorAll('.project-tab');
            const aboutObjs = document.querySelectorAll('.about-obj');

            const handleScroll = () => {{
                // Text Fill Effect
                headings.forEach(heading => {{
                    const rect = heading.getBoundingClientRect();
                    const winH = window.innerHeight;
                    
                    // Fill based on viewport position
                    let progress = (winH * 0.85 - rect.top) / (winH * 0.5);
                    progress = Math.min(Math.max(progress, 0), 1) * 100;
                    
                    heading.style.setProperty('--fill-val', `${{progress}}%`);
                }});

                // About Objects Visibility (Re-triggerable)
                aboutObjs.forEach(obj => {{
                    const rect = obj.getBoundingClientRect();
                    if(rect.top < window.innerHeight * 0.9 && rect.bottom > 0) {{
                        obj.classList.add('visible');
                    }} else {{
                        obj.classList.remove('visible');
                    }}
                }});

                // Projects Visibility (Re-triggerable)
                tabs.forEach(tab => {{
                    const rect = tab.getBoundingClientRect();
                    if(rect.top < window.innerHeight * 0.85 && rect.bottom > 0) {{
                        tab.classList.add('visible');
                    }} else {{
                        tab.classList.remove('visible');
                    }}
                }});
            }};

            window.addEventListener('scroll', handleScroll);
            handleScroll(); // Initial check

            // Loader Removal
            window.addEventListener('load', () => {{
                const loader = document.getElementById('loader');
                setTimeout(() => {{
                    loader.style.opacity = '0';
                    setTimeout(() => {{
                        loader.style.visibility = 'hidden';
                    }}, 1000);
                }}, 1500);
            }});

            // Smooth Scroll Fix for Nav Links
            const navLinks = document.querySelectorAll('#navbar a');
            navLinks.forEach(link => {{
                link.addEventListener('click', (e) => {{
                    const targetId = link.getAttribute('href').substring(1);
                    const targetElement = document.getElementById(targetId);
                    if (targetElement) {{
                        e.preventDefault();
                        targetElement.scrollIntoView({{ behavior: 'smooth' }});
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>
"""
# Render Portfolio Block
st.markdown("<style>iframe { border: none !important; margin: 0; padding: 0; }</style>", unsafe_allow_html=True)
components.html(portfolio_html, height=1000, scrolling=True)
