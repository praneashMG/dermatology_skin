import re

with open('doctors.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('hover:-translate-y-1.5" flex flex-col h-full">', 'hover:-translate-y-1.5 flex flex-col h-full">')

with open('doctors.html', 'w', encoding='utf-8') as f:
    f.write(content)
