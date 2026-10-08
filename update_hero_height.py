import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace min-h-[calc(100vh-6rem)] or min-h-[70vh] with min-h-[80vh]
    # Specifically for the hero sections, but doing a global replace of these classes is safe
    # because they were only used for the hero sections.
    new_content = content.replace('min-h-[calc(100vh-6rem)]', 'min-h-[80vh]')
    new_content = new_content.replace('min-h-[70vh]', 'min-h-[80vh]')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

print("Done updating hero heights.")
