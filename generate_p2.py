import os
from setup_base import write_page

# ================== HOME 2 ==================
home2_body = """
<!-- Editorial Hero -->
<section class="min-h-screen flex flex-col lg:flex-row bg-stone-50 dark:bg-stone-900 pt-20 lg:pt-0">
    <div class="lg:w-1/2 flex items-center justify-center p-8 lg:p-16 z-10 relative">
        <div class="max-w-xl">
            <h1 class="text-6xl md:text-8xl font-serif font-black text-stone-900 dark:text-white leading-none tracking-tight mb-8">Steam <br/><span class="text-orange-600 dark:text-orange-500">& Fold.</span></h1>
            <p class="text-xl md:text-2xl text-stone-600 dark:text-stone-300 font-light mb-12">Redefining the modern dumpling experience with heritage techniques and uncompromising ingredients.</p>
            <div class="flex flex-col sm:flex-row gap-4">
                <a href="menu.html" class="bg-stone-900 dark:bg-white text-white dark:text-stone-900 hover:bg-orange-600 dark:hover:bg-orange-500 px-8 py-4 font-bold uppercase tracking-wider text-sm transition-colors text-center">Discover the Menu</a>
                <a href="about.html" class="border-2 border-stone-900 dark:border-white text-stone-900 dark:text-white hover:bg-stone-100 dark:hover:bg-stone-800 px-8 py-4 font-bold uppercase tracking-wider text-sm transition-colors text-center">Our Craft</a>
            </div>
        </div>
    </div>
    <div class="lg:w-1/2 relative h-[50vh] lg:h-screen">
        <img src="https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?q=80&w=1976&auto=format&fit=crop" alt="Close up of handmade dumplings" class="w-full h-full object-cover">
    </div>
</section>

<!-- Dumpling Craft -->
<section class="py-24 bg-stone-900 dark:bg-stone-950 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="space-y-8">
                <h2 class="text-4xl md:text-5xl font-serif font-bold">The Art of the Fold</h2>
                <div class="h-1 w-20 bg-orange-500"></div>
                <p class="text-lg text-stone-300 leading-relaxed">Our dumpling wrappers are made daily using only flour, water, and time. It's a delicate balance of hydration and resting that yields the perfect chew, strong enough to hold our rich, savory broths and fillings.</p>
                <p class="text-lg text-stone-300 leading-relaxed">Each dumpling is pleated by hand—a rhythmic, meditative process that ensures a perfect seal and a beautiful presentation in the steamer basket.</p>
            </div>
            <div class="grid grid-cols-2 gap-4">
                <img src="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?q=80&w=2070&auto=format&fit=crop" alt="Steamer" class="w-full h-64 object-cover rounded-sm">
                <img src="https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=2129&auto=format&fit=crop" alt="Dumplings" class="w-full h-64 object-cover rounded-sm mt-8">
            </div>
        </div>
    </div>
</section>

<!-- Bao Bar -->
<section class="py-24 bg-orange-50 dark:bg-stone-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
            <h2 class="text-4xl font-serif font-bold text-stone-900 dark:text-white mb-4">The Bao Bar</h2>
            <p class="text-stone-600 dark:text-stone-400 max-w-2xl mx-auto">Soft, pillowy steamed buns with bold, textured fillings.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white dark:bg-stone-800 shadow-xl rounded-xl overflow-hidden group">
                <div class="h-64 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1625938146369-adc83368bda7?q=80&w=1925&auto=format&fit=crop" alt="Char Siu Bao" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-8 text-center">
                    <h3 class="text-2xl font-bold font-serif text-stone-900 dark:text-white mb-3">Char Siu</h3>
                    <p class="text-stone-600 dark:text-stone-400 mb-6">Sweet roasted pork, scallions, rich soy glaze.</p>
                    <a href="menu.html" class="text-orange-600 dark:text-orange-400 font-semibold hover:underline uppercase text-sm tracking-wider">Order Now</a>
                </div>
            </div>
            <div class="bg-white dark:bg-stone-800 shadow-xl rounded-xl overflow-hidden group">
                <div class="h-64 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=2070&auto=format&fit=crop" alt="Mushroom Bao" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-8 text-center">
                    <h3 class="text-2xl font-bold font-serif text-stone-900 dark:text-white mb-3">Spicy Mushroom</h3>
                    <p class="text-stone-600 dark:text-stone-400 mb-6">Shiitake, wood ear, chili crisp, cilantro.</p>
                    <a href="menu.html" class="text-orange-600 dark:text-orange-400 font-semibold hover:underline uppercase text-sm tracking-wider">Order Now</a>
                </div>
            </div>
            <div class="bg-white dark:bg-stone-800 shadow-xl rounded-xl overflow-hidden group">
                <div class="h-64 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?q=80&w=2070&auto=format&fit=crop" alt="Chicken Bao" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                </div>
                <div class="p-8 text-center">
                    <h3 class="text-2xl font-bold font-serif text-stone-900 dark:text-white mb-3">Ginger Chicken</h3>
                    <p class="text-stone-600 dark:text-stone-400 mb-6">Minced chicken, fresh ginger, sesame oil.</p>
                    <a href="menu.html" class="text-orange-600 dark:text-orange-400 font-semibold hover:underline uppercase text-sm tracking-wider">Order Now</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Customer Favorites -->
<section class="py-24 bg-white dark:bg-stone-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl md:text-4xl font-serif font-bold text-center text-stone-900 dark:text-white mb-16">Most Loved</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- 1 -->
            <div class="relative group cursor-pointer">
                <img src="https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=2129&auto=format&fit=crop" alt="Favorite 1" class="w-full h-80 object-cover rounded-lg">
                <div class="absolute inset-0 bg-stone-900/60 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center p-6 text-center">
                    <div>
                        <h3 class="text-white font-bold text-xl mb-2">Pork & Chive</h3>
                        <p class="text-orange-400 font-medium">$8.50</p>
                    </div>
                </div>
            </div>
            <!-- 2 -->
            <div class="relative group cursor-pointer">
                <img src="https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=2070&auto=format&fit=crop" alt="Favorite 2" class="w-full h-80 object-cover rounded-lg">
                <div class="absolute inset-0 bg-stone-900/60 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center p-6 text-center">
                    <div>
                        <h3 class="text-white font-bold text-xl mb-2">Vegetable Gyoza</h3>
                        <p class="text-orange-400 font-medium">$7.50</p>
                    </div>
                </div>
            </div>
            <!-- 3 -->
            <div class="relative group cursor-pointer">
                <img src="https://images.unsplash.com/photo-1625938146369-adc83368bda7?q=80&w=1925&auto=format&fit=crop" alt="Favorite 3" class="w-full h-80 object-cover rounded-lg">
                <div class="absolute inset-0 bg-stone-900/60 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center p-6 text-center">
                    <div>
                        <h3 class="text-white font-bold text-xl mb-2">Char Siu Bao</h3>
                        <p class="text-orange-400 font-medium">$6.50</p>
                    </div>
                </div>
            </div>
            <!-- 4 -->
            <div class="relative group cursor-pointer">
                <img src="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?q=80&w=2070&auto=format&fit=crop" alt="Favorite 4" class="w-full h-80 object-cover rounded-lg">
                <div class="absolute inset-0 bg-stone-900/60 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center p-6 text-center">
                    <div>
                        <h3 class="text-white font-bold text-xl mb-2">Shrimp & Ginger</h3>
                        <p class="text-orange-400 font-medium">$9.50</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Split CTA -->
<section class="grid grid-cols-1 md:grid-cols-2">
    <div class="relative h-[60vh] flex items-center justify-center group overflow-hidden">
        <img src="https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?q=80&w=1976&auto=format&fit=crop" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000">
        <div class="absolute inset-0 bg-stone-900/50"></div>
        <div class="relative z-10 text-center p-8">
            <h2 class="text-4xl font-serif font-bold text-white mb-6">Dine at Our Kitchen</h2>
            <a href="contact.html" class="inline-block border-2 border-white text-white hover:bg-white hover:text-stone-900 px-8 py-3 uppercase tracking-wider font-bold text-sm transition-colors">Book a Table</a>
        </div>
    </div>
    <div class="relative h-[60vh] flex items-center justify-center group overflow-hidden bg-orange-600">
        <img src="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?q=80&w=2070&auto=format&fit=crop" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000 mix-blend-multiply opacity-50">
        <div class="relative z-10 text-center p-8">
            <h2 class="text-4xl font-serif font-bold text-white mb-6">Enjoy at Home</h2>
            <a href="menu.html#frozen" class="inline-block border-2 border-white text-white hover:bg-white hover:text-orange-600 px-8 py-3 uppercase tracking-wider font-bold text-sm transition-colors">Shop Frozen Packs</a>
        </div>
    </div>
</section>
"""

write_page("home2.html", "Home Alternative", "Editorial showcase of Bamboo & Flour.", home2_body)
print("home2.html written")

# ================== ABOUT ==================
about_body = """
<section class="pt-24 pb-16 bg-stone-50 dark:bg-stone-900 text-center">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 class="text-5xl md:text-6xl font-serif font-bold text-stone-900 dark:text-white mb-6">Our Story</h1>
        <p class="text-xl text-stone-600 dark:text-stone-300">Born from a passion for authentic flavors and modern hospitality.</p>
    </div>
</section>

<section class="py-16 bg-white dark:bg-stone-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <img src="https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?q=80&w=1976&auto=format&fit=crop" class="w-full h-96 object-cover rounded-xl shadow-lg">
            <div>
                <h2 class="text-3xl font-serif font-bold mb-6 text-stone-900 dark:text-white">The Steam Kitchen Philosophy</h2>
                <p class="text-stone-600 dark:text-stone-400 mb-6 leading-relaxed">Bamboo & Flour started with a simple belief: the best food is made by hand. We wanted to create a space that celebrates the artistry of folding dough and the comforting warmth of a bamboo steamer.</p>
                <p class="text-stone-600 dark:text-stone-400 leading-relaxed">Every morning, our kitchen comes alive with the sound of chopping, kneading, and the hiss of steam. We don't take shortcuts because we know you can taste the difference.</p>
            </div>
        </div>
    </div>
</section>

<section class="py-24 bg-stone-900 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
            <h2 class="text-3xl font-serif font-bold mb-4">Ingredients & Sourcing</h2>
            <p class="text-stone-400 max-w-2xl mx-auto">Great food starts with great ingredients.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="p-6 border border-stone-800 rounded-lg">
                <h3 class="text-xl font-bold mb-3 text-orange-500">Fresh Vegetables</h3>
                <p class="text-stone-400">Crisp cabbage, vibrant garlic chives, and earthy shiitake mushrooms, chopped fresh daily to maintain crunch and flavor.</p>
            </div>
            <div class="p-6 border border-stone-800 rounded-lg">
                <h3 class="text-xl font-bold mb-3 text-orange-500">Quality Proteins</h3>
                <p class="text-stone-400">We source premium heritage pork and free-range chicken, ensuring rich, savory fillings with perfect texture.</p>
            </div>
            <div class="p-6 border border-stone-800 rounded-lg">
                <h3 class="text-xl font-bold mb-3 text-orange-500">Careful Aromatics</h3>
                <p class="text-stone-400">Ginger, garlic, scallions, and pure sesame oil form the aromatic backbone of our signature recipes.</p>
            </div>
        </div>
    </div>
</section>

<section class="py-24 bg-orange-50 dark:bg-stone-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-serif font-bold mb-12 text-stone-900 dark:text-white">Our Core Values</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <div>
                <div class="text-4xl mb-4">🤲</div>
                <h3 class="text-xl font-bold mb-2 text-stone-900 dark:text-white">Craft</h3>
                <p class="text-stone-600 dark:text-stone-400">Dedicated to the handmade tradition.</p>
            </div>
            <div>
                <div class="text-4xl mb-4">🥬</div>
                <h3 class="text-xl font-bold mb-2 text-stone-900 dark:text-white">Freshness</h3>
                <p class="text-stone-600 dark:text-stone-400">Made daily, never compromised.</p>
            </div>
            <div>
                <div class="text-4xl mb-4">🥢</div>
                <h3 class="text-xl font-bold mb-2 text-stone-900 dark:text-white">Hospitality</h3>
                <p class="text-stone-600 dark:text-stone-400">Welcoming every guest with warmth.</p>
            </div>
            <div>
                <div class="text-4xl mb-4">🎯</div>
                <h3 class="text-xl font-bold mb-2 text-stone-900 dark:text-white">Consistency</h3>
                <p class="text-stone-600 dark:text-stone-400">Perfectly steamed, every single time.</p>
            </div>
        </div>
    </div>
</section>
"""

write_page("about.html", "About Us", "Learn about our kitchen philosophy and ingredients.", about_body)
print("about.html written")
