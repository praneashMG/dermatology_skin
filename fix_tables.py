import re

for filepath in ['patient-dashboard.html', 'appointment.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add whitespace-nowrap to tables to make them scroll properly
    content = content.replace('<table class="w-full text-sm data-table">', '<table class="w-full text-sm data-table whitespace-nowrap">')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
