import re

with open('treatments.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace missing icon
content = content.replace('fa-solid fa-sparkles', 'fa-solid fa-wand-magic-sparkles')

# Add flex flex-col h-full to the cards
# The cards are inside <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
pattern = r'(<div class="bg-card-bg border border-border rounded-2xl p-6 sm:p-8 text-center hover:shadow-xl hover:border-accent transition-all duration-300")>'
replacement = r'\1 flex flex-col h-full">'
content = re.sub(pattern, replacement, content)

# Add mt-auto to the View treatments link
link_pattern = r'(class="inline-flex items-center gap-2 text-accent font-semibold text-sm hover:gap-3 transition-all")>'
link_replacement = r'class="inline-flex items-center gap-2 text-accent font-semibold text-sm hover:gap-3 transition-all mt-auto">'
content = re.sub(link_pattern, link_replacement, content)

with open('treatments.html', 'w', encoding='utf-8') as f:
    f.write(content)
