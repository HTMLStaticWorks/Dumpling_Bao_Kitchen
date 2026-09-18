import os
from setup_base import write_page

# ================== MENU ==================
menu_body = """
<!-- Menu Hero -->
<section class="pt-32 pb-16 bg-stone-100 dark:bg-stone-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-5xl md:text-6xl font-serif font-bold text-stone-900 dark:text-white mb-6">Our Menu</h1>
        <p class="text-xl text-stone-600 dark:text-stone-300 max-w-2xl mx-auto">Hand-folded daily. Steamed to order.</p>
    </div>
</section>

<!-- Menu Categories Navigation -->
<section class="sticky top-20 z-40 bg-white/90 dark:bg-stone-950/90 backdrop-blur-md border-b border-stone-200 dark:border-stone-800 py-4 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex overflow-x-auto pb-2 space-x-6 hide-scrollbar justify-start md:justify-center">
            <a href="#pork" class="whitespace-nowrap font-medium text-stone-600 dark:text-stone-400 hover:text-orange-600 dark:hover:text-orange-500 transition-colors">Pork & Meat</a>
            <a href="#chicken" class="whitespace-nowrap font-medium text-stone-600 dark:text-stone-400 hover:text-orange-600 dark:hover:text-orange-500 transition-colors">Chicken & Seafood</a>
            <a href="#vegetarian" class="whitespace-nowrap font-medium text-stone-600 dark:text-stone-400 hover:text-orange-600 dark:hover:text-orange-500 transition-colors">Vegetarian</a>
            <a href="#bao" class="whitespace-nowrap font-medium text-stone-600 dark:text-stone-400 hover:text-orange-600 dark:hover:text-orange-500 transition-colors">Bao Selection</a>
            <a href="#sides" class="whitespace-nowrap font-medium text-stone-600 dark:text-stone-400 hover:text-orange-600 dark:hover:text-orange-500 transition-colors">Sides & Sauces</a>
            <a href="#frozen" class="whitespace-nowrap font-medium text-stone-600 dark:text-stone-400 hover:text-orange-600 dark:hover:text-orange-500 transition-colors">Frozen Packs</a>
        </div>
    </div>
</section>

<div class="bg-stone-50 dark:bg-stone-950 pb-24">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-24 pt-16">
        
        <!-- Pork & Meat -->
        <section id="pork" class="scroll-mt-32">
            <h2 class="text-3xl font-serif font-bold text-stone-900 dark:text-white mb-8 border-b-2 border-orange-500 pb-2 inline-block">Pork & Meat Dumplings</h2>
            <div class="space-y-8">
                <!-- Item -->
                <div class="flex flex-col sm:flex-row gap-6 bg-white dark:bg-stone-900 p-6 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800">
                    <img src="https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=2129&auto=format&fit=crop" class="w-full sm:w-48 h-32 object-cover rounded-lg">
                    <div class="flex-grow">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="text-xl font-bold text-stone-900 dark:text-white">Classic Pork & Chive</h3>
                            <span class="text-lg font-bold text-orange-600 dark:text-orange-400">$8.50</span>
                        </div>
                        <p class="text-stone-600 dark:text-stone-400 text-sm mb-3">Heritage pork, fresh garlic chives, ginger, light soy sauce.</p>
                        <span class="inline-block bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 text-xs px-2 py-1 rounded">6 pcs | Steamed or Pan-fried</span>
                    </div>
                </div>
                <!-- Item -->
                <div class="flex flex-col sm:flex-row gap-6 bg-white dark:bg-stone-900 p-6 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800">
                    <div class="w-full sm:w-48 h-32 bg-stone-200 dark:bg-stone-800 rounded-lg flex items-center justify-center text-stone-400">
                        <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                    </div>
                    <div class="flex-grow">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="text-xl font-bold text-stone-900 dark:text-white">Spicy Beef & Onion</h3>
                            <span class="text-lg font-bold text-orange-600 dark:text-orange-400">$9.50</span>
                        </div>
                        <p class="text-stone-600 dark:text-stone-400 text-sm mb-3">Minced beef, sweet onions, black pepper, chili oil infusion.</p>
                        <span class="inline-block bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 text-xs px-2 py-1 rounded">6 pcs | Steamed</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Chicken & Seafood -->
        <section id="chicken" class="scroll-mt-32">
            <h2 class="text-3xl font-serif font-bold text-stone-900 dark:text-white mb-8 border-b-2 border-orange-500 pb-2 inline-block">Chicken & Seafood</h2>
            <div class="space-y-8">
                <!-- Item -->
                <div class="flex flex-col sm:flex-row gap-6 bg-white dark:bg-stone-900 p-6 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800">
                    <img src="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?q=80&w=2070&auto=format&fit=crop" class="w-full sm:w-48 h-32 object-cover rounded-lg">
                    <div class="flex-grow">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="text-xl font-bold text-stone-900 dark:text-white">Shrimp & Ginger</h3>
                            <span class="text-lg font-bold text-orange-600 dark:text-orange-400">$10.50</span>
                        </div>
                        <p class="text-stone-600 dark:text-stone-400 text-sm mb-3">Plump shrimp, minced pork backfat, fresh ginger, bamboo shoots.</p>
                        <span class="inline-block bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 text-xs px-2 py-1 rounded">6 pcs | Steamed</span>
                    </div>
                </div>
                 <!-- Item -->
                 <div class="flex flex-col sm:flex-row gap-6 bg-white dark:bg-stone-900 p-6 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800">
                    <div class="w-full sm:w-48 h-32 bg-stone-200 dark:bg-stone-800 rounded-lg flex items-center justify-center text-stone-400">
                        <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                    </div>
                    <div class="flex-grow">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="text-xl font-bold text-stone-900 dark:text-white">Chicken & Shiitake</h3>
                            <span class="text-lg font-bold text-orange-600 dark:text-orange-400">$8.50</span>
                        </div>
                        <p class="text-stone-600 dark:text-stone-400 text-sm mb-3">Minced chicken, dried shiitake mushrooms, scallions.</p>
                        <span class="inline-block bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 text-xs px-2 py-1 rounded">6 pcs | Steamed or Pan-fried</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Vegetarian -->
        <section id="vegetarian" class="scroll-mt-32">
            <h2 class="text-3xl font-serif font-bold text-stone-900 dark:text-white mb-8 border-b-2 border-orange-500 pb-2 inline-block">Vegetarian</h2>
            <div class="space-y-8">
                <!-- Item -->
                <div class="flex flex-col sm:flex-row gap-6 bg-white dark:bg-stone-900 p-6 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800">
                    <img src="https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=2070&auto=format&fit=crop" class="w-full sm:w-48 h-32 object-cover rounded-lg">
                    <div class="flex-grow">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="text-xl font-bold text-stone-900 dark:text-white">Crispy Vegetable Gyoza</h3>
                            <span class="text-lg font-bold text-orange-600 dark:text-orange-400">$7.50</span>
                        </div>
                        <p class="text-stone-600 dark:text-stone-400 text-sm mb-3">Cabbage, carrots, glass noodles, wood ear mushrooms, spinach wrapper.</p>
                        <span class="inline-block bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 text-xs px-2 py-1 rounded">6 pcs | Pan-fried</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Bao -->
        <section id="bao" class="scroll-mt-32">
            <h2 class="text-3xl font-serif font-bold text-stone-900 dark:text-white mb-8 border-b-2 border-orange-500 pb-2 inline-block">Bao Selection</h2>
            <div class="space-y-8">
                <!-- Item -->
                <div class="flex flex-col sm:flex-row gap-6 bg-white dark:bg-stone-900 p-6 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800">
                    <img src="https://images.unsplash.com/photo-1625938146369-adc83368bda7?q=80&w=1925&auto=format&fit=crop" class="w-full sm:w-48 h-32 object-cover rounded-lg">
                    <div class="flex-grow">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="text-xl font-bold text-stone-900 dark:text-white">Char Siu Bao</h3>
                            <span class="text-lg font-bold text-orange-600 dark:text-orange-400">$6.50</span>
                        </div>
                        <p class="text-stone-600 dark:text-stone-400 text-sm mb-3">Fluffy steamed buns filled with sweet roasted BBQ pork.</p>
                        <span class="inline-block bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 text-xs px-2 py-1 rounded">2 pcs | Steamed</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Sides & Sauces -->
        <section id="sides" class="scroll-mt-32">
            <h2 class="text-3xl font-serif font-bold text-stone-900 dark:text-white mb-8 border-b-2 border-orange-500 pb-2 inline-block">Sides & Sauces</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <!-- Item -->
                <div class="bg-white dark:bg-stone-900 p-4 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800 flex justify-between items-center">
                    <div>
                        <h3 class="font-bold text-stone-900 dark:text-white">Smashed Cucumber Salad</h3>
                        <p class="text-stone-500 text-sm">Garlic, black vinegar, sesame oil.</p>
                    </div>
                    <span class="font-bold text-orange-600 dark:text-orange-400">$5.00</span>
                </div>
                <!-- Item -->
                <div class="bg-white dark:bg-stone-900 p-4 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800 flex justify-between items-center">
                    <div>
                        <h3 class="font-bold text-stone-900 dark:text-white">Edamame</h3>
                        <p class="text-stone-500 text-sm">Steamed, with sea salt.</p>
                    </div>
                    <span class="font-bold text-orange-600 dark:text-orange-400">$4.50</span>
                </div>
                <!-- Item -->
                <div class="bg-white dark:bg-stone-900 p-4 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800 flex justify-between items-center">
                    <div>
                        <h3 class="font-bold text-stone-900 dark:text-white">House Chili Oil</h3>
                        <p class="text-stone-500 text-sm">Our secret spicy, crispy recipe.</p>
                    </div>
                    <span class="font-bold text-orange-600 dark:text-orange-400">$1.50</span>
                </div>
                 <!-- Item -->
                 <div class="bg-white dark:bg-stone-900 p-4 rounded-xl shadow-sm border border-stone-100 dark:border-stone-800 flex justify-between items-center">
                    <div>
                        <h3 class="font-bold text-stone-900 dark:text-white">Scallion Ginger Sauce</h3>
                        <p class="text-stone-500 text-sm">Fresh and aromatic.</p>
                    </div>
                    <span class="font-bold text-orange-600 dark:text-orange-400">$1.50</span>
                </div>
            </div>
        </section>

        <!-- CTA -->
        <section class="text-center pt-8 border-t border-stone-200 dark:border-stone-800">
            <h3 class="text-2xl font-bold text-stone-900 dark:text-white mb-4">Ready to Order?</h3>
            <a href="contact.html" class="inline-block bg-orange-600 hover:bg-orange-700 text-white px-8 py-3 rounded-full font-bold transition-colors shadow-md">Enquire for Pickup</a>
        </section>

    </div>
</div>

<!-- Frozen Retail Packs -->
<section id="frozen" class="scroll-mt-32 py-24 bg-stone-50 dark:bg-stone-950 border-t border-stone-200 dark:border-stone-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
            <h2 class="text-4xl font-serif font-bold text-stone-900 dark:text-white mb-4">Frozen Retail Packs</h2>
            <p class="text-xl text-stone-600 dark:text-stone-300 max-w-2xl mx-auto">Restaurant quality, crafted in our kitchen, steamed in yours.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Product Card -->
            <div class="bg-white dark:bg-stone-900 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-shadow border border-stone-100 dark:border-stone-800 group">
                <div class="h-64 bg-stone-200 dark:bg-stone-800 overflow-hidden relative">
                    <img src="https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=2129&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    <div class="absolute top-4 right-4 bg-white dark:bg-stone-900 text-orange-600 dark:text-orange-500 font-bold px-3 py-1 rounded-full text-sm shadow-sm">24 Pack</div>
                </div>
                <div class="p-6">
                    <div class="text-xs font-bold text-orange-500 uppercase tracking-wider mb-2">Dumpling</div>
                    <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Pork & Chive</h3>
                    <p class="text-stone-600 dark:text-stone-400 text-sm mb-4">Our signature recipe. Ready to boil, pan-fry, or steam directly from frozen.</p>
                    <div class="flex justify-between items-center mt-4 pt-4 border-t border-stone-100 dark:border-stone-800">
                        <span class="font-bold text-stone-900 dark:text-white">$24.00</span>
                    </div>
                </div>
            </div>
             <!-- Product Card -->
             <div class="bg-white dark:bg-stone-900 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-shadow border border-stone-100 dark:border-stone-800 group">
                <div class="h-64 bg-stone-200 dark:bg-stone-800 overflow-hidden relative">
                    <img src="https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=2070&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    <div class="absolute top-4 right-4 bg-white dark:bg-stone-900 text-orange-600 dark:text-orange-500 font-bold px-3 py-1 rounded-full text-sm shadow-sm">24 Pack</div>
                </div>
                <div class="p-6">
                    <div class="text-xs font-bold text-orange-500 uppercase tracking-wider mb-2">Gyoza</div>
                    <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Vegetable Gyoza</h3>
                    <p class="text-stone-600 dark:text-stone-400 text-sm mb-4">Perfect for pan-frying. Vegan friendly filling with rich umami flavor.</p>
                    <div class="flex justify-between items-center mt-4 pt-4 border-t border-stone-100 dark:border-stone-800">
                        <span class="font-bold text-stone-900 dark:text-white">$22.00</span>
                    </div>
                </div>
            </div>
             <!-- Product Card -->
             <div class="bg-white dark:bg-stone-900 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-shadow border border-stone-100 dark:border-stone-800 group">
                <div class="h-64 bg-stone-200 dark:bg-stone-800 overflow-hidden relative">
                    <img src="https://images.unsplash.com/photo-1625938146369-adc83368bda7?q=80&w=1925&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    <div class="absolute top-4 right-4 bg-white dark:bg-stone-900 text-orange-600 dark:text-orange-500 font-bold px-3 py-1 rounded-full text-sm shadow-sm">8 Pack</div>
                </div>
                <div class="p-6">
                    <div class="text-xs font-bold text-orange-500 uppercase tracking-wider mb-2">Bao</div>
                    <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Char Siu Bao</h3>
                    <p class="text-stone-600 dark:text-stone-400 text-sm mb-4">Fluffy steamed buns. Reheats perfectly in the microwave or steamer.</p>
                    <div class="flex justify-between items-center mt-4 pt-4 border-t border-stone-100 dark:border-stone-800">
                        <span class="font-bold text-stone-900 dark:text-white">$18.00</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Instructions -->
<section class="py-24 bg-white dark:bg-stone-900 border-t border-stone-100 dark:border-stone-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
            <h2 class="text-3xl font-serif font-bold text-stone-900 dark:text-white mb-4">Easy at Home</h2>
            <p class="text-stone-600 dark:text-stone-400">Do not thaw before cooking. Cook straight from the freezer.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
            <div class="p-8 bg-stone-50 dark:bg-stone-800 rounded-2xl">
                <div class="w-16 h-16 bg-orange-100 dark:bg-stone-700 text-orange-600 dark:text-orange-400 rounded-full flex items-center justify-center mx-auto mb-6">
                    <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Steam</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm">Line steamer with parchment paper. Steam over boiling water for 10-12 minutes.</p>
            </div>
            <div class="p-8 bg-stone-50 dark:bg-stone-800 rounded-2xl">
                <div class="w-16 h-16 bg-orange-100 dark:bg-stone-700 text-orange-600 dark:text-orange-400 rounded-full flex items-center justify-center mx-auto mb-6">
                    <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.879 16.121A3 3 0 1012.015 11L11 14H9c0 .768.293 1.536.879 2.121z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Pan-Fry</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm">Heat oil in non-stick pan. Add dumplings. Fry bottom until golden, add 1/4 cup water, cover and steam 5 mins.</p>
            </div>
            <div class="p-8 bg-stone-50 dark:bg-stone-800 rounded-2xl">
                <div class="w-16 h-16 bg-orange-100 dark:bg-stone-700 text-orange-600 dark:text-orange-400 rounded-full flex items-center justify-center mx-auto mb-6">
                    <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-stone-900 dark:text-white mb-2">Boil</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm">Drop into boiling water. Wait for them to float, then boil for an additional 4-5 minutes.</p>
            </div>
        </div>
    </div>
</section>

<!-- Enquiry CTA -->
<section class="py-20 bg-orange-600 text-center px-4">
    <h2 class="text-3xl font-serif font-bold text-white mb-6">Retail & Wholesale</h2>
    <p class="text-orange-100 mb-8 max-w-xl mx-auto">Are you a cafe, restaurant, or retailer interested in stocking our products? Contact us for bulk pricing.</p>
    <a href="contact.html" class="inline-block bg-white text-orange-600 hover:bg-stone-100 px-8 py-4 rounded-full font-bold transition-colors">Wholesale Enquiry</a>
</section>
"""
write_page("menu.html", "Menu", "Explore our handcrafted menu.", menu_body)
print("menu written")
