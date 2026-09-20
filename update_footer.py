import os, glob

replacements = [
    ('class="bg-stone-950 text-stone-300', 'class="bg-stone-100 dark:bg-stone-950 text-stone-600 dark:text-stone-300'),
    ('text-white group-hover:text-orange-400', 'text-stone-900 dark:text-white group-hover:text-orange-600 dark:group-hover:text-orange-400'),
    ('class="text-stone-400 text-sm leading-relaxed"', 'class="text-stone-600 dark:text-stone-400 text-sm leading-relaxed"'),
    ('text-stone-400 hover:text-white', 'text-stone-600 dark:text-stone-400 hover:text-orange-600 dark:hover:text-white'),
    ('class="text-white font-semibold mb-6 uppercase tracking-wider text-sm"', 'class="text-stone-900 dark:text-white font-semibold mb-6 uppercase tracking-wider text-sm"'),
    ('class="hover:text-orange-400 transition-colors"', 'class="text-stone-600 dark:text-stone-300 hover:text-orange-600 dark:hover:text-orange-400 transition-colors"'),
    ('border-stone-800', 'border-stone-200 dark:border-stone-800'),
    ('text-stone-500', 'text-stone-500 dark:text-stone-400'),
    ('class="hover:text-white transition-colors"', 'class="text-stone-600 dark:text-stone-400 hover:text-orange-600 dark:hover:text-white transition-colors"')
]

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
