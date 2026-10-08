import re

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add flex layout to the Mission & Values cards
pattern = r'(<div class="bg-card-bg border border-border rounded-2xl overflow-hidden shadow-sm hover:shadow-xl \n?transition-all duration-300 text-center")>'
replacement = r'\1 flex flex-col h-full">'
content = re.sub(pattern, replacement, content)

# Add flex-grow and flex-col to the inner padding div
content = re.sub(r'<div class="p-6 sm:p-8">', r'<div class="p-6 sm:p-8 flex flex-col flex-grow">', content)

# Make sure images don't shrink
content = re.sub(r'class="w-full h-52 object-cover"', r'class="w-full h-52 object-cover shrink-0"', content)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)
