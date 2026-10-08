import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('transition-all duration-300" flex flex-col h-full">', 'transition-all duration-300 flex flex-col h-full">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
