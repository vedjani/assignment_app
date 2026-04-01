import os
import glob

base_dir = r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16"
html_files = glob.glob(os.path.join(base_dir, "q*", "templates", "**", "*.html"), recursive=True)

old_html = """<a href="/" style="position: fixed; top: 20px; left: 20px; z-index: 9999; text-decoration: none; padding: 10px 20px; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); border-radius: 30px; color: #fff; font-family: sans-serif; font-weight: 600; font-size: 14px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; align-items: center; gap: 8px;">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M15 8a.5.5 1 0 1-.5.5H2.707l3.147 3.146a.5.5 0 0 1-.708.708l-4-4a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 7.5H14.5A.5.5 0 0 1 15 8z"/></svg>
    Back to Launcher
</a>"""

new_html = """<a href="/" style="position: fixed; top: 20px; left: 20px; z-index: 9999; text-decoration: none; padding: 8px 16px; background: transparent; border: 1px solid rgba(0,0,0,0.2); border-radius: 30px; color: #000; font-family: sans-serif; font-weight: 800; font-size: 14px; text-shadow: 0 0 3px rgba(255,255,255,1); transition: all 0.3s ease; display: flex; align-items: center; gap: 8px;">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M15 8a.5.5 1 0 1-.5.5H2.707l3.147 3.146a.5.5 0 0 1-.708.708l-4-4a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 7.5H14.5A.5.5 0 0 1 15 8z"/></svg>
    Back
</a>"""

count = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_html in content:
        content = content.replace(old_html, new_html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated back button to be transparent in {count} files.")
