import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the link back at the end of the FAQ section
link_html = '''
          <div class="text-center mt-10">
              <a href="#contact-info" class="text-accent font-semibold hover:text-primary transition-colors text-sm">
                  Still have questions? Contact us <i class="fa-solid fa-arrow-right ml-1"></i>
              </a>
          </div>
'''

content = content.replace('      </div>\n  </section>', link_html + '      </div>\n  </section>')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)
