import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'class="testimonial-card p-6 border border-border shadow-sm"', r'class="testimonial-card p-6 border border-border shadow-sm flex flex-col"', content)
content = re.sub(r'<div class="flex items-center gap-3">\s*<img src="https://images.unsplash.com/', r'<div class="flex items-center gap-3 mt-auto">\n                      <img src="https://images.unsplash.com/', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
