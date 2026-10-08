import re

with open('treatments.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('min-h-[calc(100vh-6rem)] flex items-start pt-16 lg:pt-28', 'min-h-[70vh] flex items-center')

with open('treatments.html', 'w', encoding='utf-8') as f:
    f.write(content)
