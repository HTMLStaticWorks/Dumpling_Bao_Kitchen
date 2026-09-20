import glob

# 1. Update footer icons in all HTML files
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('class="flex gap-4"', 'class="flex items-center gap-4"')
    
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if 'aria-label="Instagram"' in line:
            if i + 1 < len(lines) and 'h-6 w-6' in lines[i+1]:
                lines[i+1] = lines[i+1].replace('h-6 w-6', 'h-5 w-5')

    with open(file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

# 2. Update blog.html for identical baseline
with open('blog.html', 'r', encoding='utf-8') as f:
    blog_lines = f.read().splitlines()

for i, line in enumerate(blog_lines):
    if 'class="group block"' in line:
        blog_lines[i] = line.replace('class="group block"', 'class="group flex flex-col h-full"')
    if 'class="relative h-64 rounded-xl overflow-hidden shadow-sm mb-6"' in line:
        blog_lines[i] = line.replace('mb-6', 'mb-6 shrink-0')
    if 'group-hover:text-orange-600 transition-colors' in line and '<h3' in line:
        blog_lines[i] = line.replace('transition-colors', 'transition-colors flex-grow')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(blog_lines))
