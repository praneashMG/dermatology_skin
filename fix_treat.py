with open('treatments.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(' <main class="relative pt-24">\n', '', 1)
content = content.replace('</main>\n', '', 1)

with open('treatments.html', 'w', encoding='utf-8') as f:
    f.write(content)
