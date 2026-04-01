import os
import glob
import re

base_dir = r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16"
html_files = glob.glob(os.path.join(base_dir, "q*", "templates", "**", "*.html"), recursive=True)

# Regex to find the previously injected back buttons regardless of their exact styling state
# It matches <a href="/" style="position: fixed; ...> ... </a>
button_pattern = re.compile(
    r'<a href="/" style="position: fixed;[^>]*>\s*<svg[^>]*>.*?<\/svg>\s*Back.*?<\/a>',
    re.IGNORECASE | re.DOTALL
)

new_html = """<a href="/" style="position: fixed; bottom: 20px; left: 20px; z-index: 9999; text-decoration: none; padding: 10px 20px; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); border-radius: 30px; color: #fff; font-family: sans-serif; font-weight: 600; font-size: 14px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; align-items: center; gap: 8px;">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M15 8a.5.5 1 0 1-.5.5H2.707l3.147 3.146a.5.5 0 0 1-.708.708l-4-4a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 7.5H14.5A.5.5 0 0 1 15 8z"/></svg>
    Back to Launcher
</a>"""

count = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if button_pattern.search(content):
        content = button_pattern.sub(new_html, content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Reverted button styling and moved to bottom-left in {count} files.")
