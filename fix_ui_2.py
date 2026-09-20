import os

# --- 1. login.html changes ---
with open('login.html', 'r', encoding='utf-8') as f:
    login = f.read()

# Title font size
login = login.replace('<h1 class="text-2xl font-serif font-bold text-stone-900 dark:text-white">Sign in to Bamboo & Flour</h1>',
                      '<h1 class="text-xl font-serif font-bold text-stone-900 dark:text-white mt-4">Sign in to Bamboo & Flour</h1>')

# Remove Back to Home
back_to_home = '''    <div class="mt-4 text-center">
        <a href="index.html" class="text-sm font-medium text-stone-500 dark:text-stone-400 hover:text-stone-900 dark:hover:text-white transition-colors">&larr; Back to Home</a>
    </div>'''
login = login.replace(back_to_home, '')

# Move Forgot Password
old_password_label = '''            <div class="flex justify-between items-center mb-2">
                <label class="block text-sm font-medium text-stone-700 dark:text-stone-300">Password</label>
                <a href="#" class="text-sm font-medium text-orange-600 hover:text-orange-500">Forgot Password?</a>
            </div>'''
new_password_label = '''            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Password</label>'''
login = login.replace(old_password_label, new_password_label)

old_remember = '''        <div class="flex items-center">
            <input type="checkbox" id="remember" class="h-4 w-4 text-orange-600 focus:ring-orange-500 border-stone-300 rounded">
            <label for="remember" class="ml-2 block text-sm text-stone-700 dark:text-stone-300">Remember me</label>
        </div>'''
new_remember = '''        <div class="flex justify-between items-center">
            <div class="flex items-center">
                <input type="checkbox" id="remember" class="h-4 w-4 text-orange-600 focus:ring-orange-500 border-stone-300 rounded">
                <label for="remember" class="ml-2 block text-sm text-stone-700 dark:text-stone-300">Remember me</label>
            </div>
            <a href="#" class="text-sm font-medium text-orange-600 hover:text-orange-500">Forgot Password?</a>
        </div>'''
login = login.replace(old_remember, new_remember)

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(login)

# --- 2. signup.html changes ---
with open('signup.html', 'r', encoding='utf-8') as f:
    signup = f.read()

# Title font size
signup = signup.replace('<h1 class="text-2xl font-serif font-bold text-stone-900 dark:text-white">Create an Account</h1>',
                        '<h1 class="text-xl font-serif font-bold text-stone-900 dark:text-white mt-4">Create an Account</h1>')
with open('signup.html', 'w', encoding='utf-8') as f:
    f.write(signup)

# --- 3. index.html cards ---
with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# The Handmade Philosophy cards (class="bg-white dark:bg-stone-800 p-8 rounded-2xl shadow-sm border border-stone-100 dark:border-stone-700 text-center group hover:shadow-md transition-shadow")
index = index.replace('class="bg-white dark:bg-stone-800 p-8 rounded-2xl shadow-sm border border-stone-100 dark:border-stone-700 text-center group hover:shadow-md transition-shadow"',
                      'class="bg-white dark:bg-stone-800 p-8 rounded-2xl shadow-sm border border-stone-100 dark:border-stone-700 text-center group hover:shadow-md transition-shadow flex flex-col h-full"')

for title in ['Fresh Ingredients', 'Artisan Dough', 'Careful Folding', 'Bamboo Steaming']:
    index = index.replace(f'<h3 class="text-xl font-bold text-stone-900 dark:text-white mb-3">{title}</h3>',
                          f'<h3 class="text-xl font-bold text-stone-900 dark:text-white mb-3 flex-grow">{title}</h3>')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index)

# --- 4. home2.html cards ---
with open('home2.html', 'r', encoding='utf-8') as f:
    home2 = f.read()

# Char Siu, Spicy Mushroom, Ginger Chicken cards
# They are inside <div class="p-8 text-center flex flex-col flex-grow">. 
# h3 has class="text-2xl font-bold font-serif text-stone-900 dark:text-white mb-3"
for title in ['Char Siu', 'Spicy Mushroom\\n                            ', 'Ginger Chicken\\n                            ']:
    # Let's just blindly replace the h3 classes for all of them
    pass

home2 = home2.replace('<h3 class="text-2xl font-bold font-serif text-stone-900 dark:text-white mb-3">',
                      '<h3 class="text-2xl font-bold font-serif text-stone-900 dark:text-white mb-3 flex-grow">')
# And remove mt-auto from the links if it messes up the distribution
home2 = home2.replace('class="mt-auto text-orange-600 dark:text-orange-400 font-semibold hover:underline uppercase text-sm tracking-wider">',
                      'class="mt-6 text-orange-600 dark:text-orange-400 font-semibold hover:underline uppercase text-sm tracking-wider">')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(home2)
