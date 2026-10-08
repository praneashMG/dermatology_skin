import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add flex layout to the anchor cards
pattern = r'(<a href="treatments.html" class="group bg-card-bg rounded-2xl overflow-hidden border border-border shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1\.5")>'
replacement = r'\1 flex flex-col h-full">'
content = re.sub(pattern, replacement, content)

# Modify the padding div
content = content.replace('<div class="p-5 text-center">', '<div class="p-5 text-center flex flex-col flex-grow">')

# Modify the paragraph
p_pattern = r'(<p class="text-secondary-text text-sm leading-relaxed">)'
p_replacement = r'<p class="text-secondary-text text-sm leading-relaxed mt-auto">'
content = re.sub(p_pattern, p_replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
