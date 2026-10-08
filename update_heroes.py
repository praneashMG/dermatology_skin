import re
import os

files_to_update = ['about.html', 'treatments.html', 'doctors.html', 'contact.html', 'appointment.html', 'home2.html']

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The hero sections look like <section id="XYZ-hero" class="relative overflow-hidden bg-background py-16 md:py-24 px-4 sm:px-6">
    # Or some variant. We'll use a regex to replace the class content while keeping the rest intact.
    
    pattern = r'(<section id="[^"]*hero"[^>]*class="relative overflow-hidden bg-background) (py-16 md:py-24|py-16 md:py-24 lg:py-28) (px-4 sm:px-6")'
    replacement = r'\1 min-h-[calc(100vh-6rem)] flex items-center py-10 lg:py-0 \3'
    
    content = re.sub(pattern, replacement, content)

    # We also need to add w-full and maybe py-8 to the immediate child div if it's max-w-7xl
    content = re.sub(r'(<section id="[^"]*hero"[^>]*>[\s\S]*?)<div class="max-w-7xl mx-auto">', r'\1<div class="w-full max-w-7xl mx-auto py-8">', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished updating hero sections.")
