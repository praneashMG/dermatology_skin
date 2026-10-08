import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('bg-card-bg/95', 'bg-card-bg')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
