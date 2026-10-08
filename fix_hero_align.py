import re
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the extra top padding and items-start, replace with items-center
    new_content = content.replace('flex items-start pt-16 lg:pt-28 py-10 lg:py-0', 'flex items-center py-10 lg:py-0')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

print("Done fixing alignment.")
