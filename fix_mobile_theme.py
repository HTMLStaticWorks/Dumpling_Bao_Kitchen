import os
import glob
import re

html_files = glob.glob('*.html')
py_files = glob.glob('*.py')

def fix_content(content):
    # Regex to find the mobile-theme-toggle button in the header
    pattern_remove = r'[ \t]*<button id="mobile-theme-toggle"[^>]*>.*?</button>\n'
    content = re.sub(pattern_remove, '', content, flags=re.DOTALL)
    
    # Check if the button was already inserted to avoid duplicates
    if 'id="mobile-theme-toggle"' not in content and 'mobile-rtl-toggle' in content:
        insert_target = r'(<div class="mt-4 pt-4 border-t border-stone-200 dark:border-stone-200 dark:border-stone-800 flex flex-col gap-3">)'
        
        insert_content = r'''\1
                    <button id="mobile-theme-toggle" class="w-full flex justify-between items-center px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800 hover:text-orange-600 dark:hover:text-orange-400">
                        Toggle Theme
                        <div>
                            <svg class="w-5 h-5 dark:hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z">
                                </path>
                            </svg>
                            <svg class="w-5 h-5 hidden dark:block" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z">
                                </path>
                            </svg>
                        </div>
                    </button>'''
        
        content = re.sub(insert_target, insert_content, content, count=1)
        
    return content

for f in html_files + py_files:
    # skip this script itself
    if f == 'fix_mobile_theme.py':
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'id="mobile-menu-btn"' in content or 'mobile-rtl-toggle' in content:
        new_content = fix_content(content)
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated {f}')
