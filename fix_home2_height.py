import re

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('class="relative overflow-hidden bg-background py-16 md:py-24 px-4 sm:px-6"', 'class="relative overflow-hidden bg-background min-h-[80vh] flex items-center py-10 lg:py-0 px-4 sm:px-6"')
content = content.replace('<div class="max-w-7xl mx-auto">', '<div class="w-full max-w-7xl mx-auto py-8">')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)
