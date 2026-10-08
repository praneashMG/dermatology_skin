import re

with open('patient-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<span class="text-xs bg-blue-100 text-blue-700 px-3 py-1 rounded-full shrink-0 whitespace-nowrap">No refill</span>',
    '<span class="text-xs bg-gray-100 text-gray-700 px-3 py-1 rounded-full shrink-0 whitespace-nowrap">No refill</span>'
)

with open('patient-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
