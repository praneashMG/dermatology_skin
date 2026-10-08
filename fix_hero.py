import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the hero section fit the screen height better
old_hero_class = 'class="relative overflow-hidden bg-background py-16 md:py-24 lg:py-28 px-4 sm:px-6"'
new_hero_class = 'class="relative overflow-hidden bg-background min-h-[calc(100vh-6rem)] flex items-center py-10 lg:py-0 px-4 sm:px-6"'

content = content.replace(old_hero_class, new_hero_class)

# The particles container shouldn't block the new flex layout
content = content.replace('<div class="relative z-10 max-w-7xl mx-auto">', '<div class="relative z-10 w-full max-w-7xl mx-auto py-8">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
