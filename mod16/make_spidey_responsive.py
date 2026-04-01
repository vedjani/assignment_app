import glob

files = glob.glob(r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16\q*\*\*.html", recursive=True)
count = 0

responsive_css = """
    /* MOBILE & TABLET RESPONSIVE FIXES */
    @media (max-width: 1024px) {
        .container, main, .content, form {
            padding: 20px !important;
        }
    }
    
    @media (max-width: 768px) {
        body { padding: 10px !important; }
        h1 { font-size: 2.5rem !important; }
        h2 { font-size: 2rem !important; }
        .container, main, .content { padding: 15px !important; border-radius: 8px !important; }
        form { padding: 15px !important; margin-bottom: 1.5rem !important; }
        input[type="text"], input[type="number"], input[type="email"], input[type="password"], select, textarea {
            width: 100% !important; max-width: none !important;
        }
        table { display: block !important; overflow-x: auto !important; white-space: nowrap !important; font-size: 0.95rem !important; }
        th, td { padding: 8px 10px !important; }
        button, input[type="submit"], .btn { width: 100% !important; font-size: 1.1rem !important; margin-bottom: 5px; }
        .next-app-btn { bottom: 10px !important; right: 10px !important; padding: 8px 15px !important; font-size: 12px !important; }
    }
"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Inject directly at the bottom of the injected SPIDEY THEME
    if "/* MOBILE & TABLET RESPONSIVE FIXES */" not in content and "<!-- END SPIDEY THEME -->" in content:
        new_content = content.replace("<!-- END SPIDEY THEME -->", responsive_css + "\n<!-- END SPIDEY THEME -->")
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1

print(f"Applied Global Responsive Optimization to {count} sub-app templates.")
