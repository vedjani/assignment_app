import glob
import re

files = glob.glob(r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16\q*\*\*.html", recursive=True)
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Target all light/white backgrounds (e.g., #fff, #f0f0f0, #f6f8fa, #eee, white) and replace them with a semi-transparent dark layer.
    new_content = re.sub(
        r'background(?:-color)?\s*:\s*(?:#[eEfF][A-Fa-f0-9]{2,5}|white)(?:\s+!important)?\s*(;|\})', 
        r'background: rgba(0,0,0,0.6)\1', 
        content
    )
    
    # Inject extra critical dark mode fixes globally inside the injected Spidey theme
    if "/* Forms */" in new_content and "option {" not in new_content:
        extra_css = """/* Forms */
    option { background: var(--spidey-dark) !important; color: white !important; }
    .output, .result, .message, .alert { background: rgba(0,0,0,0.5) !important; border: 1px solid var(--spidey-blue) !important; color: var(--spidey-light) !important; padding: 15px !important; border-radius: 8px !important; }"""
        new_content = new_content.replace('/* Forms */', extra_css)

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1
        print(f"Patched: {f}")

print(f"Fixed white backgrounds in {count} files.")
