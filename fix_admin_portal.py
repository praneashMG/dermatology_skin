import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace in desktop dropdown
    content = content.replace(
        '<a href="appointment.html">Book Appointment</a>',
        '<a href="appointment.html">Admin Portal</a>'
    )
    
    # Replace in mobile menu
    content = content.replace(
        '<a href="appointment.html" class="text-secondary hover:text-accent py-1 px-2">Book Appointment</a>',
        '<a href="appointment.html" class="text-secondary hover:text-accent py-1 px-2">Admin Portal</a>'
    )
    
    # Check if there are other variations in the dashboard dropdown
    # Actually, the sidebar in patient-dashboard.html might also have "Book Appointment"?
    # Let's check.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
