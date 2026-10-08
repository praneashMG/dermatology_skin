import re

with open('treatments.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the text container flex-col, flex-grow, justify-start
content = content.replace('flex flex-col justify-center text-center sm:text-left', 'flex flex-col flex-grow justify-start text-center sm:text-left')

# Add mt-auto to the price span
# Wait, let's use regex to find the price spans and add mt-auto
content = re.sub(r'(<span class="text-xs font-semibold text-accent uppercase tracking-wide">From \$[0-9]+ / session</span>)', r'<span class="text-xs font-semibold text-accent uppercase tracking-wide mt-auto pt-2">\1', content)

# Actually, the replacement above wraps it in another span? No, it replaces with the span inside itself but with an extra span!
# That is wrong!
