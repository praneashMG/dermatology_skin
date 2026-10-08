import re

with open('treatments.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('flex flex-col justify-center text-center sm:text-left', 'flex flex-col flex-grow justify-start text-center sm:text-left')

pattern = r'<span class="text-xs font-semibold text-accent uppercase tracking-wide">From \$([0-9]+) / session</span>'
replacement = r'<span class="text-xs font-semibold text-accent uppercase tracking-wide mt-auto pt-4 block">From $\1 / session</span>'
content = re.sub(pattern, replacement, content)

with open('treatments.html', 'w', encoding='utf-8') as f:
    f.write(content)
