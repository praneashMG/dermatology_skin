import re

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('grid md:grid-cols-3 gap-6 lg:gap-8', 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)
