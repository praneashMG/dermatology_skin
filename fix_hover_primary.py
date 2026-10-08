import glob
import re

html_files = glob.glob('*.html')
new_rule = '''
        .hover\\:text-primary:hover {
            color: var(--color-primary);
        }
'''

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '.hover\\:text-primary:hover' not in content:
        # Insert after .text-primary { ... }
        pattern = r'(\.text-primary \{\s*color: var\(--color-primary\);\s*\})'
        if re.search(pattern, content):
            new_content = re.sub(pattern, r'\1' + new_rule, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
