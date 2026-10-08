import re

files = ['about.html', 'doctors.html', 'contact.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('min-h-[calc(100vh-6rem)] flex items-center', 'min-h-[calc(100vh-6rem)] flex items-start pt-16 lg:pt-28')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
