import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new FAQ accordion HTML
new_faq_html = '''
        <div class="max-w-4xl mx-auto grid md:grid-cols-2 gap-6">
            <!-- FAQ 1 -->
            <details class="bg-card-bg border border-border rounded-2xl group">
                <summary class="font-bold text-primary-text p-5 sm:p-6 flex items-center justify-between cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                    <span class="flex items-center gap-3">
                        <span class="w-7 h-7 rounded-full bg-hover text-accent flex items-center justify-center font-bold text-sm shrink-0">1</span>
                        How soon will I get a reply?
                    </span>
                    <span class="transition-transform duration-300 group-open:rotate-180 text-accent">
                        <i class="fa-solid fa-chevron-down"></i>
                    </span>
                </summary>
                <div class="px-5 sm:px-6 pb-6 text-sm text-secondary-text leading-relaxed">
                    We aim to respond to all inquiries within 2 business hours during clinic hours.
                </div>
            </details>
            <!-- FAQ 2 -->
            <details class="bg-card-bg border border-border rounded-2xl group">
                <summary class="font-bold text-primary-text p-5 sm:p-6 flex items-center justify-between cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                    <span class="flex items-center gap-3">
                        <span class="w-7 h-7 rounded-full bg-hover text-accent flex items-center justify-center font-bold text-sm shrink-0">2</span>
                        Do I need an appointment?
                    </span>
                    <span class="transition-transform duration-300 group-open:rotate-180 text-accent">
                        <i class="fa-solid fa-chevron-down"></i>
                    </span>
                </summary>
                <div class="px-5 sm:px-6 pb-6 text-sm text-secondary-text leading-relaxed">
                    Walk-ins are welcome, but we recommend booking to avoid waiting and to choose your preferred doctor.
                </div>
            </details>
            <!-- FAQ 3 -->
            <details class="bg-card-bg border border-border rounded-2xl group">
                <summary class="font-bold text-primary-text p-5 sm:p-6 flex items-center justify-between cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                    <span class="flex items-center gap-3">
                        <span class="w-7 h-7 rounded-full bg-hover text-accent flex items-center justify-center font-bold text-sm shrink-0">3</span>
                        Do you accept insurance?
                    </span>
                    <span class="transition-transform duration-300 group-open:rotate-180 text-accent">
                        <i class="fa-solid fa-chevron-down"></i>
                    </span>
                </summary>
                <div class="px-5 sm:px-6 pb-6 text-sm text-secondary-text leading-relaxed">
                    Yes, we accept most major insurance providers. Contact us for a full list and verification.
                </div>
            </details>
            <!-- FAQ 4 -->
            <details class="bg-card-bg border border-border rounded-2xl group">
                <summary class="font-bold text-primary-text p-5 sm:p-6 flex items-center justify-between cursor-pointer list-none [&::-webkit-details-marker]:hidden">
                    <span class="flex items-center gap-3">
                        <span class="w-7 h-7 rounded-full bg-hover text-accent flex items-center justify-center font-bold text-sm shrink-0">4</span>
                        Is there parking available?
                    </span>
                    <span class="transition-transform duration-300 group-open:rotate-180 text-accent">
                        <i class="fa-solid fa-chevron-down"></i>
                    </span>
                </summary>
                <div class="px-5 sm:px-6 pb-6 text-sm text-secondary-text leading-relaxed">
                    Yes, free patient parking is available on-site, with additional paid street parking nearby.
                </div>
            </details>
        </div>
'''

# Find the old grid and replace it
import re

old_grid_pattern = re.compile(r'<div class="grid md:grid-cols-2 gap-6">.*?</div>\s*</div>\s*</section>', re.DOTALL)
replacement = new_faq_html + '\n      </div>\n  </section>'

content = old_grid_pattern.sub(replacement, content)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)
