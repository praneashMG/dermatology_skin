import re

with open('doctors.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add flex layout to review cards
content = content.replace('bg-card-bg border border-border rounded-2xl p-6 sm:p-8 hover:shadow-xl transition-all duration-300 text-center', 'bg-card-bg border border-border rounded-2xl p-6 sm:p-8 hover:shadow-xl transition-all duration-300 text-center flex flex-col h-full')

# Add mt-auto to author block
content = content.replace('<div class="flex items-center justify-center gap-3">', '<div class="flex items-center justify-center gap-3 mt-auto">')

with open('doctors.html', 'w', encoding='utf-8') as f:
    f.write(content)
