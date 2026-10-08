import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Title and Favicon
content = content.replace("🎭", "✨")
content = content.replace("<title>Danzora</title>", "<title>Dermatology & Skin Clinic</title>")

# Theme Variables
css_vars = '''        /* =========================
           THEME VARIABLES - TEAL & BLUE
        ========================= */
        :root,
        html[data-theme='light'] {
            --color-background: #FFFFFF;
            --color-primary-text: #000000;
            --color-secondary-text: #4B5563;
            --color-primary: #0F766E; /* Teal */
            --color-secondary: #0ea5e9; /* Light blue */
            --color-accent: #0F766E; /* Teal */
            --color-border: #E5E7EB;
            --color-hover: #F0FDF4;
            --color-footer-bg: #042F2E;
            --color-footer-text: #FFFFFF;
            --color-card-bg: #FFFFFF;
        }

        html[data-theme='dark'] {
            --color-background: #09090B; /* Near Black */
            --color-primary-text: #FFFFFF;
            --color-secondary-text: #9CA3AF;
            --color-primary: #14B8A6; /* Teal */
            --color-secondary: #38BDF8; /* Light blue */
            --color-accent: #14B8A6; /* Teal */
            --color-border: #27272A;
            --color-hover: #134E4A;
            --color-footer-bg: #000000;
            --color-footer-text: #FFFFFF;
            --color-card-bg: #18181B; /* Dark Gray */
        }'''
content = re.sub(r'/\*\s*={25}\s*THEME VARIABLES - PURPLE & PINK\s*={25}\s*\*/.*?(?=\s*html,\s*body {)', css_vars, content, flags=re.DOTALL)

# Header Logo
content = content.replace('<i class="fa-solid fa-masks-theater mr-2"></i>Danzora', '<i class="fa-solid fa-spa mr-2"></i>Skin Clinic')

# Desktop Navigation Links
nav_links = '''                    <a href="treatments.html" class="nav-link">Treatments</a>
                    <a href="doctors.html" class="nav-link">Doctors</a>
                    <a href="about.html" class="nav-link">About</a>
                    <a href="contact.html" class="nav-link">Contact</a>'''
content = re.sub(r'<a href="programs\.html".*?<a href="contact\.html" class="nav-link">Contact</a>', nav_links, content, flags=re.DOTALL)

# Mobile Navigation Links
mob_nav_links = '''                <a href="treatments.html" class="text-primary-text font-semibold text-lg hover:text-accent py-2">Treatments</a>
                <a href="doctors.html" class="text-primary-text font-semibold text-lg hover:text-accent py-2">Doctors</a>
                <a href="about.html" class="text-primary-text font-semibold text-lg hover:text-accent py-2">About</a>
                <a href="contact.html" class="text-primary-text font-semibold text-lg hover:text-accent py-2">Contact</a>'''
content = re.sub(r'<a href="programs\.html" class="text-primary-text font-semibold text-lg hover:text-accent py-2">Programs</a>.*?<a href="contact\.html" class="text-primary-text font-semibold text-lg hover:text-accent py-2">Contact</a>', mob_nav_links, content, flags=re.DOTALL)

# Dashboard dropdown links (desktop)
dashboard_links = '''                            <a href="patient-dashboard.html">Patient Dashboard</a>
                            <a href="appointment.html">Book Appointment</a>'''
content = re.sub(r'<a href="admin-dashboard\.html">Admin Dashboard</a>\s*<a href="user-dashboard\.html">User Dashboard</a>', dashboard_links, content)

# Dashboard dropdown links (mobile)
mob_dashboard_links = '''                        <a href="patient-dashboard.html" class="text-secondary hover:text-accent py-1 px-2">Patient Dashboard</a>
                        <a href="appointment.html" class="text-secondary hover:text-accent py-1 px-2">Book Appointment</a>'''
content = re.sub(r'<a href="admin-dashboard\.html" class="text-secondary hover:text-accent py-1 px-2">Admin Dashboard</a>\s*<a href="user-dashboard\.html" class="text-secondary hover:text-accent py-1 px-2">User Dashboard</a>', mob_dashboard_links, content)


# Footer Updates
footer_about = '''                    <h3 class="text-2xl sm:text-3xl font-serif font-semibold mb-4 text-accent"><i class="fa-solid fa-spa mr-2"></i>Skin Clinic</h3>
                    <p class="text-sm leading-relaxed max-w-xs text-white">Experience refined, clinical-chic dermatology and skin care. We offer advanced treatments for all your skin needs, including acne care, laser therapy, and more.</p>'''
content = re.sub(r'<h3 class="text-2xl sm:text-3xl font-serif font-semibold mb-4 text-accent"><i class="fa-solid fa-masks-theater mr-2"></i>Danzora</h3>\s*<p class="text-sm leading-relaxed max-w-xs text-white">.*?</p>', footer_about, content, flags=re.DOTALL)

footer_programs = '''                    <h4 class="text-lg font-medium mb-4 text-accent">Treatments</h4>
                    <ul class="space-y-2">
                        <li><a href="treatments.html" class="footer-link">Acne Care</a></li>
                        <li><a href="treatments.html" class="footer-link">Laser Therapy</a></li>
                        <li><a href="treatments.html" class="footer-link">Anti-Aging</a></li>
                        <li><a href="treatments.html" class="footer-link">Skin Rejuvenation</a></li>
                    </ul>'''
content = re.sub(r'<h4 class="text-lg font-medium mb-4 text-accent">Programs</h4>\s*<ul class="space-y-2">.*?</ul>', footer_programs, content, flags=re.DOTALL)

footer_links = '''                    <h4 class="text-lg font-medium mb-4 text-accent">Quick Links</h4>
                    <ul class="space-y-2">
                        <li><a href="index.html" class="footer-link">Home</a></li>
                        <li><a href="doctors.html" class="footer-link">Doctors</a></li>
                        <li><a href="about.html" class="footer-link">About Us</a></li>
                        <li><a href="contact.html" class="footer-link">Contact</a></li>
                    </ul>'''
content = re.sub(r'<h4 class="text-lg font-medium mb-4 text-accent">Quick Links</h4>\s*<ul class="space-y-2">.*?</ul>', footer_links, content, flags=re.DOTALL)

content = content.replace('&copy; 2026 Kids Dance & Performing Arts Academy. All rights reserved.', '&copy; 2026 Dermatology & Skin Clinic. All rights reserved.')
content = content.replace('Get the latest updates on class schedules & studio news.', 'Get the latest updates on skin care tips & clinic news.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
