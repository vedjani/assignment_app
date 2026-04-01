import os
import glob
import re

base_dir = r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16"
html_files = glob.glob(os.path.join(base_dir, "q*", "templates", "**", "*.html"), recursive=True)

# Regex to match the Back to Launcher button specifically
# Look for <a href="/" ... Back to Launcher ... </a>
button_pattern = re.compile(
    r'<a href="/" style="position: fixed;[^>]+>\s*<svg[^>]+>.*?<\/svg>\s*Back to Launcher\s*<\/a>',
    re.IGNORECASE | re.DOTALL
)

count = 0
for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if button_pattern.search(content):
        content = button_pattern.sub('', content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        
print(f"Removed Back button from {count} files.")
