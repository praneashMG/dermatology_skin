import re

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('text-center" flex flex-col h-full">', 'text-center flex flex-col h-full">')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)
