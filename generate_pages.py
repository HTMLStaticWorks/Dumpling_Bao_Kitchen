import os
from setup_base import header_html, footer_html, common_head, common_scripts

base_dir = "d:/SEPT WEBSITES/Dumpling & Bao Kitchen"

def write_page(filename, title, description, content_body, include_header_footer=True):
    path = os.path.join(base_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(common_head.format(title=title, description=description))
        if include_header_footer:
            f.write(header_html)
            f.write('<main class="pt-20 flex-grow">\\n')
        else:
            f.write('<main class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">\\n')
            
        f.write(content_body)
        
        if include_header_footer:
            f.write('</main>\\n')
            f.write(footer_html)
        else:
            f.write('</main>\\n')
            
        f.write(common_scripts)

# ================== HOME 1 ==================
home1_body = """
<!-- Hero -->
<section class="relative bg-stone-900 overflow-hidden h-[90vh] min-h-[600px] flex items-center">
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?q=80&w=2070&auto=format&fit=crop" alt="Premium steamed dumplings in bamboo steamer" class="w-full h-full object-cover opacity-50">
        <div class="absolute inset-0 bg-gradient-to-t from-stone-900 via-stone-900/60 to-transparent"></div>
    </div>
    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full text-center lg:text-left">
        <div class="inline-block bg-orange-600 text-white text-xs font-bold tracking-wider uppercase px-3 py-1 rounded-full mb-6">Handmade Daily</div>
        <h1 class="text-5xl md:text-6xl lg:text-7xl font-serif font-bold text-white mb-6 leading-tight">Crafted with <br/><span class="text-orange-500">tradition & steam.</span></h1>
        <p class="mt-4 text-xl text-stone-200 max-w-2xl mb-10 mx-auto lg:mx-0">Experience the warmth of our authentic, handmade dumplings and fluffy bao. Prepared fresh daily using locally sourced ingredients and traditional folding techniques.</p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
            <a href="menu.html" class="bg-orange-600 hover:bg-orange-700 text-white px-8 py-4 rounded-full font-medium transition-all shadow-lg hover:shadow-xl text-lg text-center">Explore Menu</a>
        </div>
    </div>
</section>

<!-- Handmade Signature -->
<section class="py-24 bg-stone-50 dark:bg-stone-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16">
            <h2 class="text-3xl md:text-4xl font-serif font-bold text-stone-900 dark:text-white mb-6">The Handmade Philosophy</h2>
            <p class="text-lg text-stone-600 dark:text-stone-300">Every single dumpling and bao that leaves our kitchen is a testament to our dedication. We believe in the magic of handmade food.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="bg-white dark:bg-stone-800 p-8 rounded-2xl shadow-sm border border-stone-100 dark:border-stone-700 text-center group hover:shadow-md transition-shadow">
                <div class="w-24 h-24 mx-auto mb-6 overflow-hidden rounded-full shadow-sm">
                    <img src="https://images.unsplash.com/photo-1518843875459-f738682238a6?q=80&w=2070&auto=format&fit=crop" alt="Fresh Ingredients" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                </div>
                <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-3">Fresh Ingredients</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm">Locally sourced produce and premium proteins selected every morning.</p>
            </div>
            <div class="bg-white dark:bg-stone-800 p-8 rounded-2xl shadow-sm border border-stone-100 dark:border-stone-700 text-center group hover:shadow-md transition-shadow">
                <div class="w-24 h-24 mx-auto mb-6 overflow-hidden rounded-full shadow-sm">
                    <img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=2072&auto=format&fit=crop" alt="Artisan Dough" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                </div>
                <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-3">Artisan Dough</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm">Perfectly hydrated, rested, and rolled wrappers for the ideal chew.</p>
            </div>
            <div class="bg-white dark:bg-stone-800 p-8 rounded-2xl shadow-sm border border-stone-100 dark:border-stone-700 text-center group hover:shadow-md transition-shadow">
                <div class="w-24 h-24 mx-auto mb-6 overflow-hidden rounded-full shadow-sm">
                    <img src="https://images.unsplash.com/photo-1528712306091-ed0763094c98?q=80&w=2000&auto=format&fit=crop" alt="Careful Folding" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                </div>
                <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-3">Careful Folding</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm">Over 15 distinct folds to seal the flavor and create beautiful shapes.</p>
            </div>
            <div class="bg-white dark:bg-stone-800 p-8 rounded-2xl shadow-sm border border-stone-100 dark:border-stone-700 text-center group hover:shadow-md transition-shadow">
                <div class="w-24 h-24 mx-auto mb-6 overflow-hidden rounded-full shadow-sm">
                    <img src="https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=2129&auto=format&fit=crop" alt="Bamboo Steaming" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                </div>
                <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-3">Bamboo Steaming</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm">Gentle steam locks in moisture, resulting in tender, flavorful bites.</p>
            </div>
        </div>
    </div>
</section>

<!-- Signature Items -->
<section class="py-24 bg-white dark:bg-stone-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-end mb-12">
            <div>
                <h2 class="text-3xl md:text-4xl font-serif font-bold text-stone-900 dark:text-white mb-4">Signature Creations</h2>
                <p class="text-stone-600 dark:text-stone-400 max-w-lg">Our most loved dumplings and fluffy bao, crafted to perfection.</p>
            </div>
            <a href="menu.html" class="hidden md:flex items-center gap-2 text-orange-600 dark:text-orange-500 font-semibold hover:text-orange-700 dark:hover:text-orange-400 transition-colors">
                View Full Menu <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
            </a>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Item 1 -->
            <div class="group rounded-2xl overflow-hidden bg-stone-50 dark:bg-stone-900 border border-stone-100 dark:border-stone-800">
                <div class="aspect-w-4 aspect-h-3 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=2129&auto=format&fit=crop" alt="Pork & Chive Dumplings" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <div class="p-6">
                    <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Pork & Chive Dumplings</h3>
                    <p class="text-stone-600 dark:text-stone-400 text-sm mb-4">Our classic family recipe. Heritage pork mixed with fresh garlic chives and ginger, hand-folded into a delicate wheat wrapper.</p>
                    <div class="flex justify-between items-center">
                        <span class="text-lg font-semibold text-orange-600 dark:text-orange-400">$8.50</span>
                        <span class="text-xs font-medium bg-stone-200 dark:bg-stone-800 text-stone-800 dark:text-stone-300 px-2 py-1 rounded">6 pcs</span>
                    </div>
                </div>
            </div>
            <!-- Item 2 -->
            <div class="group rounded-2xl overflow-hidden bg-stone-50 dark:bg-stone-900 border border-stone-100 dark:border-stone-800">
                <div class="aspect-w-4 aspect-h-3 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1625938146369-adc83368bda7?q=80&w=1925&auto=format&fit=crop" alt="Spicy Mushroom Bao" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <div class="p-6">
                    <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Char Siu Bao</h3>
                    <p class="text-stone-600 dark:text-stone-400 text-sm mb-4">Cloud-like fluffy steamed buns filled with slow-roasted, sweet and savory BBQ pork. A comforting classic.</p>
                    <div class="flex justify-between items-center">
                        <span class="text-lg font-semibold text-orange-600 dark:text-orange-400">$6.50</span>
                        <span class="text-xs font-medium bg-stone-200 dark:bg-stone-800 text-stone-800 dark:text-stone-300 px-2 py-1 rounded">2 pcs</span>
                    </div>
                </div>
            </div>
            <!-- Item 3 -->
            <div class="group rounded-2xl overflow-hidden bg-stone-50 dark:bg-stone-900 border border-stone-100 dark:border-stone-800">
                <div class="aspect-w-4 aspect-h-3 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=2070&auto=format&fit=crop" alt="Vegetable Gyoza" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <div class="p-6">
                    <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Crispy Vegetable Gyoza</h3>
                    <p class="text-stone-600 dark:text-stone-400 text-sm mb-4">Pan-fried to golden perfection. Filled with shiitake mushrooms, cabbage, carrots, and glass noodles.</p>
                    <div class="flex justify-between items-center">
                        <span class="text-lg font-semibold text-orange-600 dark:text-orange-400">$7.50</span>
                        <span class="text-xs font-medium bg-stone-200 dark:bg-stone-800 text-stone-800 dark:text-stone-300 px-2 py-1 rounded">6 pcs</span>
                    </div>
                </div>
            </div>
        </div>
            <div class="mt-12 text-center">
                <a href="menu.html#frozen" class="inline-flex items-center gap-2 bg-stone-900 dark:bg-stone-100 text-white dark:text-stone-900 hover:bg-stone-800 dark:hover:bg-white px-8 py-4 rounded-full font-medium transition-all shadow-md">
                    Shop Frozen Retail Packs
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                </a>
            </div>
    </div>
</section>

<!-- Journey -->
<section class="py-24 bg-stone-100 dark:bg-stone-900 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
            <h2 class="text-3xl md:text-4xl font-serif font-bold text-stone-900 dark:text-white mb-4">From Basket to Table</h2>
            <p class="text-lg text-stone-600 dark:text-stone-400 max-w-2xl mx-auto">The journey of our dumplings is one of patience and precision.</p>
        </div>
        
        <div class="relative">
            <!-- connecting line -->
            <div class="hidden lg:block absolute top-1/2 left-0 w-full h-0.5 bg-stone-300 dark:bg-stone-700 -translate-y-1/2 z-0"></div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 relative z-10">
                <div class="bg-white dark:bg-stone-800 p-6 rounded-2xl shadow-sm text-center">
                    <div class="w-12 h-12 bg-orange-600 text-white rounded-full flex items-center justify-center font-bold text-xl mx-auto mb-4 border-4 border-stone-100 dark:border-stone-900 shadow-md">1</div>
                    <h3 class="font-bold text-lg mb-2 text-stone-900 dark:text-white">Prepare</h3>
                    <p class="text-sm text-stone-600 dark:text-stone-400">Fresh dough is kneaded and fillings are meticulously chopped.</p>
                </div>
                <div class="bg-white dark:bg-stone-800 p-6 rounded-2xl shadow-sm text-center">
                    <div class="w-12 h-12 bg-orange-600 text-white rounded-full flex items-center justify-center font-bold text-xl mx-auto mb-4 border-4 border-stone-100 dark:border-stone-900 shadow-md">2</div>
                    <h3 class="font-bold text-lg mb-2 text-stone-900 dark:text-white">Fold</h3>
                    <p class="text-sm text-stone-600 dark:text-stone-400">Each piece is hand-folded by our skilled artisans.</p>
                </div>
                <div class="bg-white dark:bg-stone-800 p-6 rounded-2xl shadow-sm text-center">
                    <div class="w-12 h-12 bg-orange-600 text-white rounded-full flex items-center justify-center font-bold text-xl mx-auto mb-4 border-4 border-stone-100 dark:border-stone-900 shadow-md">3</div>
                    <h3 class="font-bold text-lg mb-2 text-stone-900 dark:text-white">Steam</h3>
                    <p class="text-sm text-stone-600 dark:text-stone-400">Cooked to perfection in traditional bamboo baskets.</p>
                </div>
                <div class="bg-white dark:bg-stone-800 p-6 rounded-2xl shadow-sm text-center">
                    <div class="w-12 h-12 bg-orange-600 text-white rounded-full flex items-center justify-center font-bold text-xl mx-auto mb-4 border-4 border-stone-100 dark:border-stone-900 shadow-md">4</div>
                    <h3 class="font-bold text-lg mb-2 text-stone-900 dark:text-white">Serve</h3>
                    <p class="text-sm text-stone-600 dark:text-stone-400">Delivered piping hot with our signature sauces.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Frozen Section -->
<section class="py-24 bg-white dark:bg-stone-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row items-center gap-16">
            <div class="lg:w-1/2">
                <div class="relative rounded-2xl overflow-hidden shadow-2xl">
                    <img src="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?q=80&w=2070&auto=format&fit=crop" alt="Frozen Dumpling Packs" class="w-full h-auto object-cover">
                    <div class="absolute inset-0 bg-stone-900/10"></div>
                </div>
            </div>
            <div class="lg:w-1/2">
                <h2 class="text-3xl md:text-4xl font-serif font-bold text-stone-900 dark:text-white mb-6">Take the Steam Kitchen Home</h2>
                <p class="text-lg text-stone-600 dark:text-stone-400 mb-6">Enjoy restaurant-quality dumplings anytime. Our frozen retail packs are made with the exact same ingredients and care as our dine-in menu, flash-frozen to lock in freshness.</p>
                <ul class="space-y-4 mb-8 text-stone-700 dark:text-stone-300">
                    <li class="flex items-center gap-3">
                        <svg class="w-5 h-5 text-orange-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                        Ready in 10 minutes
                    </li>
                    <li class="flex items-center gap-3">
                        <svg class="w-5 h-5 text-orange-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                        No thawing required
                    </li>
                    <li class="flex items-center gap-3">
                        <svg class="w-5 h-5 text-orange-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                        Available in 12 and 24 pack sizes
                    </li>
                </ul>
                <a href="menu.html#frozen" class="inline-flex items-center gap-2 bg-stone-900 dark:bg-stone-100 text-white dark:text-stone-900 hover:bg-stone-800 dark:hover:bg-white px-8 py-4 rounded-full font-medium transition-all shadow-md">
                    Shop Frozen Packs
                </a>
            </div>
        </div>
    </div>
</section>

<!-- CTA Section -->
<section class="py-24 bg-orange-600 relative overflow-hidden">
    <div class="absolute inset-0 opacity-10 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-white via-transparent to-transparent"></div>
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <h2 class="text-4xl md:text-5xl font-serif font-bold text-white mb-6">Craving Authenticity?</h2>
        <p class="text-xl text-orange-100 mb-10">Join us for a meal or bring our kitchen to yours. Experience the best handmade dumplings and bao today.</p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="contact.html" class="bg-orange-700 border border-orange-500 text-white hover:bg-orange-800 px-8 py-4 rounded-full font-bold transition-colors shadow-lg text-lg">Enquire Now</a>
        </div>
    </div>
</section>
"""

write_page("index.html", "Home", "Premium handmade dumplings and bao in a cozy steam kitchen.", home1_body)

print("index.html written")
