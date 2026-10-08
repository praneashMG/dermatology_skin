import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace map image with Google Maps iframe
iframe_html = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.617355152019!2d-73.98777908459461!3d40.74844454332219!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c259a9b3117469%3A0xd134e199a405a163!2sEmpire%20State%20Building!5e0!3m2!1sen!2sus!4v1684365773238!5m2!1sen!2sus" class="w-full h-full border-0 min-h-[320px]" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'

content = re.sub(
    r'<img src="https://images\.unsplash\.com/photo-1524661135-423995f22d0b\?w=1200&q=80"\s*\n\s*alt="Clinic location map" class="w-full h-full object-cover">',
    iframe_html,
    content
)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)
