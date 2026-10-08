import re

with open('patient-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Active Prescriptions: make the flex row wrap to col on mobile, and add shrink-0 whitespace-nowrap to badges
content = content.replace(
    '<div class="border border-border p-4 rounded-xl flex justify-between items-center">',
    '<div class="border border-border p-4 rounded-xl flex flex-col sm:flex-row justify-between sm:items-center gap-3">'
)
# Add shrink-0 whitespace-nowrap to badges in prescriptions
content = re.sub(r'(<span class="text-xs bg-[a-z]+-[0-9]+ text-[a-z]+-[0-9]+ px-3 py-1 rounded-full">)', r'<span class="text-xs bg-blue-100 text-blue-700 px-3 py-1 rounded-full shrink-0 whitespace-nowrap">', content)

# Wait, regex is greedy/tricky. Let's do it safer.
content = content.replace('class="text-xs bg-blue-100 text-blue-700 px-3 py-1 rounded-full"', 'class="text-xs bg-blue-100 text-blue-700 px-3 py-1 rounded-full shrink-0 whitespace-nowrap inline-block text-center"')
content = content.replace('class="text-xs bg-gray-100 text-gray-700 px-3 py-1 rounded-full"', 'class="text-xs bg-gray-100 text-gray-700 px-3 py-1 rounded-full shrink-0 whitespace-nowrap inline-block text-center"')

# Fix Progress Photos: add flex-wrap to photo-compare
content = content.replace('<div class="photo-compare mt-3">', '<div class="photo-compare mt-3 flex-wrap">')

with open('patient-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
