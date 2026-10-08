import re

with open('doctors.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add flex layout to doctor cards
# Note: they are in a grid: <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8">
pattern = r'(<div class="bg-card-bg border border-border rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1\.5")>'
replacement = r'\1 flex flex-col h-full">'
content = re.sub(pattern, replacement, content)

# Make the inner padding div flex-col and flex-grow
content = content.replace('<div class="p-5 text-center">', '<div class="p-5 text-center flex flex-col flex-grow">')

# Add mt-auto to the social icons container
content = content.replace('<div class="flex justify-center gap-3">', '<div class="flex justify-center gap-3 mt-auto">')

with open('doctors.html', 'w', encoding='utf-8') as f:
    f.write(content)
