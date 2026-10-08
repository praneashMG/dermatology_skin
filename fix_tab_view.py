import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change the grid from sm:grid-cols-2 lg:grid-cols-4 to md:grid-cols-2 xl:grid-cols-4
content = content.replace('grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8', 'grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 lg:gap-8')

# Also, let's make the cards flex flex-col h-full just in case they have slightly different heights on very large screens
pattern = r'(<div class="relative bg-card-bg rounded-2xl p-6 sm:p-8 border border-border text-center hover:shadow-xl transition-all duration-300")>'
replacement = r'\1 flex flex-col h-full">'
content = re.sub(pattern, replacement, content)

# Make the paragraph flex-grow to stretch evenly
content = content.replace('<p class="text-sm text-secondary-text leading-relaxed">', '<p class="text-sm text-secondary-text leading-relaxed flex-grow">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
