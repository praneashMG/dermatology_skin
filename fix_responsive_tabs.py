import re

with open('treatments.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('grid grid-cols-1 md:grid-cols-2 gap-6', 'grid grid-cols-1 lg:grid-cols-2 gap-6')

with open('treatments.html', 'w', encoding='utf-8') as f:
    f.write(content)
