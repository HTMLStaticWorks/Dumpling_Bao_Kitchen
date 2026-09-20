import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="favicon.svg">\n</head>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
