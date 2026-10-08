import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('fa-calendar-heart', 'fa-heart')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
