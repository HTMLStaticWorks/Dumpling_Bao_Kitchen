import os

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract CTA Section
cta_start = index_content.find('        <!-- CTA Section -->')
cta_end = index_content.find('        </section>', cta_start) + len('        </section>')
cta_section = index_content[cta_start:cta_end]

with open('home2.html', 'r', encoding='utf-8') as f:
    home2_content = f.read()

# Extract Split Hero
split_hero_start = home2_content.find('        <section class="grid grid-cols-1 md:grid-cols-2">')
split_hero_end = home2_content.find('        </section>', split_hero_start) + len('        </section>')
split_hero_section = home2_content[split_hero_start:split_hero_end]

# Extract Editorial Hero
ed_hero_start = home2_content.find('        <!-- Editorial Hero -->')
ed_hero_end = home2_content.find('        </section>', ed_hero_start) + len('        </section>')

# Construct new home2.html
new_home2_content = home2_content[:ed_hero_start] + split_hero_section + home2_content[ed_hero_end:split_hero_start] + cta_section + home2_content[split_hero_end:]

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(new_home2_content)
