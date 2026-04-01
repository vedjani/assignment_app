import glob
import re

files = glob.glob(r"c:\Users\vedja\OneDrive\Desktop\lab-mod16\mod16\q*\*\*.html", recursive=True)
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regex to find </style> that was accidentally placed BEFORE the responsive CSS
    # It moves </style> to the end of the block, right before <!-- END SPIDEY THEME -->
    pattern = r'</style>(\s*/\* MOBILE & TABLET RESPONSIVE FIXES \*/.*?)\n<!-- END SPIDEY THEME -->'
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, r'\1\n</style>\n<!-- END SPIDEY THEME -->', content, flags=re.DOTALL)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        count += 1

print(f"Fixed CSS exposure in {count} sub-app template files.")
