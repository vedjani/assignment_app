import os
import glob
import re

base_dir = r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16"
html_files = glob.glob(os.path.join(base_dir, "q*", "**", "*.html"), recursive=True)

spidey_theme = """
<!-- SPIDEY THEME INJECT -->
<style>
    :root {
        --spidey-red: #D92525;
        --spidey-blue: #0A2463;
        --spidey-dark: #070b14;
        --spidey-light: #e2e8f0;
    }
    body {
        background-color: var(--spidey-dark) !important;
        color: var(--spidey-light) !important;
        font-family: 'Oswald', sans-serif, system-ui !important;
        background-image: 
            radial-gradient(circle at 10% 10%, rgba(217, 37, 37, 0.15) 0%, transparent 50%),
            repeating-linear-gradient(45deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 1px, transparent 1px, transparent 20px) !important;
    }
    h1, h2, h3 { 
        font-family: 'Bangers', cursive, impact !important; 
        color: var(--spidey-red) !important; 
        letter-spacing: 2px !important;
        text-shadow: 2px 2px 0 var(--spidey-blue) !important;
        margin-bottom: 1rem !important;
    }
    a { color: #00f0ff !important; text-decoration: none !important; }
    a:hover { color: var(--spidey-red) !important; text-decoration: underline !important; }

    /* Tables */
    table { width: 100%; border-collapse: collapse; margin-bottom: 2rem; background: rgba(10, 36, 99, 0.4) !important; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important; color: white !important;}
    th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); }
    th { background-color: var(--spidey-blue) !important; color: white !important; font-weight: bold; text-transform: uppercase; font-family: 'Oswald', sans-serif; letter-spacing: 1px; }
    tr:hover { background-color: rgba(217, 37, 37, 0.3) !important; }

    /* Forms */
    form { margin-bottom: 2rem; background: rgba(0,0,0,0.3); padding: 20px; border-radius: 12px; border: 1px solid var(--spidey-blue); }
    label { font-weight: bold; margin-bottom: 5px; display: block; color: var(--spidey-light) !important; font-family: 'Oswald', sans-serif; letter-spacing: 1px; }
    input[type="text"], input[type="number"], input[type="email"], input[type="password"], select, textarea {
        width: 100%; max-width: 500px; padding: 12px; margin: 8px 0 20px 0;
        background: rgba(255,255,255,0.05) !important; color: white !important;
        border: 2px solid var(--spidey-blue) !important; border-radius: 4px; font-family: inherit;
    }
    input:focus, select:focus, textarea:focus { border-color: var(--spidey-red) !important; outline: none; box-shadow: 0 0 8px rgba(217, 37, 37, 0.8) !important; }

    /* Buttons */
    button, input[type="submit"], .btn {
        background: var(--spidey-red) !important; color: white !important; border: none !important;
        padding: 12px 25px !important; font-size: 1.1rem !important; font-weight: bold !important; cursor: pointer;
        border-radius: 4px !important; text-transform: uppercase !important; font-family: 'Oswald', sans-serif !important; letter-spacing: 1px;
        box-shadow: 4px 4px 0 var(--spidey-blue) !important; transition: all 0.2s !important; display: inline-block; text-align: center; margin-top: 10px;
    }
    button:hover, input[type="submit"], .btn:hover {
        transform: translateY(-2px) !important; box-shadow: 6px 6px 0 var(--spidey-blue) !important; background: #ff1a1a !important;
    }
</style>
<!-- END SPIDEY THEME -->
"""

count = 0
for path in html_files:
    # Exclude main launcher
    if r"templates\index.html" in path and not re.search(r"q\d+", path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "SPIDEY THEME INJECT" not in content:
        if "</head>" in content.lower():
            content = re.sub(r'(</head>)', spidey_theme + r'\n\1', content, count=1, flags=re.IGNORECASE)
        elif "<body" in content.lower():
            content = re.sub(r'(<body[^>]*>)', spidey_theme + r'\n\1', content, count=1, flags=re.IGNORECASE)
        else:
            content = spidey_theme + "\n" + content
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Fixed injection applied to {count} sub-app templates.")
