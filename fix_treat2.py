import re

with open('treatments.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change flex items-center to something that pushes it up a bit
content = content.replace('min-h-[calc(100vh-6rem)] flex items-center', 'min-h-[calc(100vh-6rem)] flex items-start pt-16 lg:pt-28')

with open('treatments.html', 'w', encoding='utf-8') as f:
    f.write(content)
