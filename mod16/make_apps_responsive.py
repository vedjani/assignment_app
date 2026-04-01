import os
import glob
import re

base_dir = r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16"
html_files = glob.glob(os.path.join(base_dir, "q*", "**", "*.html"), recursive=True)

viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

responsive_css = """
    <!-- Automatically injected responsive styles -->
    <style>
        html, body { max-width: 100%; overflow-x: hidden; }
        body { padding: 10px; box-sizing: border-box; }
        img, video, iframe, canvas, table { max-width: 100%; height: auto; display: block; overflow-x: auto; }
        .container, main, section, div { box-sizing: border-box; max-width: 100%; }
        /* Add some margin to tables on mobile so they scroll instead of break width */
        table { display: block; overflow-x: auto; white-space: nowrap; }
    </style>
"""

count_meta = 0
count_css = 0

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Inject viewport meta tag if missing
    if "name=\"viewport\"" not in content.lower() and "name='viewport'" not in content.lower():
        # find <head> case insensitive
        content, c = re.subn(r'(<head[^>]*>)', r'\1\n    ' + viewport_meta, content, count=1, flags=re.IGNORECASE)
        if c > 0:
            count_meta += 1
            modified = True
            
    # Inject basic responsive CSS just before closing </head>
    if "max-width: 100%; overflow-x: hidden;" not in content:
        content, c = re.subn(r'(</head>)', responsive_css + r'\n\1', content, count=1, flags=re.IGNORECASE)
        if c > 0:
            count_css += 1
            modified = True

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Injected viewport meta into {count_meta} files.")
print(f"Injected responsive CSS into {count_css} files.")
