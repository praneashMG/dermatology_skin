import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add flex layout to testimonial cards
content = content.replace('class="testimonial-card p-6 border border-border shadow-sm"', 'class="testimonial-card p-6 border border-border shadow-sm flex flex-col"')

# Add mt-auto to the author block (which is a flex container with gap-3)
content = content.replace('<div class="flex items-center gap-3">\n                      <img src="https://images.unsplash.com/', '<div class="flex items-center gap-3 mt-auto">\n                      <img src="https://images.unsplash.com/')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
