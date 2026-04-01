import glob
import re

files = glob.glob(r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16\q15\templates\*.html")
count = 0

q15_mobile_css = """
    /* Q15 Specific Mobile Fixes */
    <style>
    @media (max-width: 768px) {
        .nav { padding: 1rem !important; }
        .nav-links { flex-direction: column !important; gap: 8px !important; align-items: center !important; padding: 0 !important; }
        .nav-links li { width: 100% !important; }
        .nav-links a { display: block !important; width: 100% !important; text-align: center !important; padding: 12px !important; background: rgba(10,36,99,0.5) !important; border-radius: 6px !important; }
        .stats-grid, .book-grid, .category-grid { grid-template-columns: 1fr !important; gap: 1.5rem !important; }
        .header { padding: 1.5rem 10px !important; }
        .stat-card, .book-card, .category-card { width: 100% !important; }
    }
    </style>
"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "/* Q15 Specific Mobile Fixes */" not in content:
        if "<!-- SPIDEY THEME INJECT -->" in content:
            new_content = content.replace("<!-- SPIDEY THEME INJECT -->", q15_mobile_css + "\n<!-- SPIDEY THEME INJECT -->")
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1

print(f"Fixed Q15 mobile layout in {count} templates.")
