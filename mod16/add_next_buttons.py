import os
import glob
import re

base_dir = r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16"
html_files = glob.glob(os.path.join(base_dir, "q*", "templates", "**", "*.html"), recursive=True)

apps = ['q1', 'q2', 'q3', 'q4', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q19']

def get_next_app(current_app):
    try:
        idx = apps.index(current_app)
        if idx + 1 < len(apps):
            return "/" + apps[idx + 1] + "/"
        else:
            return "/" # loop back to launcher if it's the last one
    except ValueError:
        return "/"

count = 0

for path in html_files:
    # determine current app from path (e.g. \q1\templates\...)
    parts = path.split(os.sep)
    current_app = None
    for p in parts:
        if p.startswith('q') and p[1:].isdigit():
            current_app = p
            break
            
    if not current_app:
        continue
        
    next_url = get_next_app(current_app)
    
    next_button_html = f"""
<a href="{next_url}" style="position: fixed; bottom: 20px; right: 20px; z-index: 9999; text-decoration: none; padding: 10px 20px; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); border-radius: 30px; color: #fff; font-family: sans-serif; font-weight: 600; font-size: 14px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; align-items: center; gap: 8px;">
    Next App
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M1 8a.5.5 1 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/></svg>
</a>
"""

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid duplicate injection
    if "Next App" not in content and "<body" in content.lower():
        # Inject right after opening <body> tag
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + next_button_html, content, count=1, flags=re.IGNORECASE)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        
print(f"Injected 'Next App' button into {count} files.")
