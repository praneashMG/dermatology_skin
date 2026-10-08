import re

def fix_gradient(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the bright gradient with a darker one
    content = content.replace('bg-gradient-to-br from-[#0F766E] to-[#0ea5e9]', 'bg-gradient-to-br from-[#042F2E] to-[#0F766E]')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

fix_gradient('login.html')
fix_gradient('signup.html')
