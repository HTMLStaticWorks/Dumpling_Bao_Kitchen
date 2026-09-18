import os
from setup_base import write_page

# ================== BLOG ==================
blog_body = """
<!-- Blog Hero -->
<section class="py-24 bg-stone-100 dark:bg-stone-900 text-center px-4">
    <h1 class="text-5xl md:text-6xl font-serif font-bold text-stone-900 dark:text-white mb-6">Kitchen Journal</h1>
    <p class="text-xl text-stone-600 dark:text-stone-300 max-w-2xl mx-auto">Stories, recipes, and news from our steam kitchens.</p>
</section>

<section class="py-16 bg-white dark:bg-stone-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Featured -->
        <div class="mb-20">
            <a href="#" class="group block">
                <div class="relative h-[60vh] rounded-2xl overflow-hidden shadow-lg mb-8">
                    <img src="https://images.unsplash.com/photo-1541696432-82c6da8ce7bf?q=80&w=2070&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    <div class="absolute inset-0 bg-stone-900/30"></div>
                </div>
                <div class="max-w-3xl mx-auto text-center px-4">
                    <span class="text-orange-600 font-bold uppercase tracking-wider text-sm mb-4 block">Kitchen Stories</span>
                    <h2 class="text-3xl md:text-4xl font-serif font-bold text-stone-900 dark:text-white mb-4 group-hover:text-orange-600 transition-colors">The Art of Steaming: Why Bamboo Matters</h2>
                    <p class="text-stone-600 dark:text-stone-400 text-lg mb-6 line-clamp-3">We explore the traditional use of bamboo steamers, how they absorb moisture, and why they remain the superior method for cooking delicate dumplings.</p>
                    <span class="text-stone-900 dark:text-white font-medium border-b-2 border-orange-500 pb-1">Read Story</span>
                </div>
            </a>
        </div>

        <!-- Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            <!-- Article -->
            <a href="#" class="group block">
                <div class="relative h-64 rounded-xl overflow-hidden shadow-sm mb-6">
                    <img src="https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?q=80&w=1976&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <span class="text-orange-600 font-bold uppercase tracking-wider text-xs mb-3 block">Guide</span>
                <h3 class="text-xl font-serif font-bold text-stone-900 dark:text-white mb-3 group-hover:text-orange-600 transition-colors">How Dumplings Are Folded: The 15 Pleat Rule</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm mb-4 line-clamp-2">A step-by-step visual guide to folding the perfect soup dumpling and locking in the rich broth.</p>
            </a>
            <!-- Article -->
            <a href="#" class="group block">
                <div class="relative h-64 rounded-xl overflow-hidden shadow-sm mb-6">
                    <img src="https://images.unsplash.com/photo-1625938146369-adc83368bda7?q=80&w=1925&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <span class="text-orange-600 font-bold uppercase tracking-wider text-xs mb-3 block">Recipe</span>
                <h3 class="text-xl font-serif font-bold text-stone-900 dark:text-white mb-3 group-hover:text-orange-600 transition-colors">The Perfect Soy Dipping Sauce</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm mb-4 line-clamp-2">Create our signature balanced dipping sauce at home using just five simple pantry ingredients.</p>
            </a>
            <!-- Article -->
            <a href="#" class="group block">
                <div class="relative h-64 rounded-xl overflow-hidden shadow-sm mb-6">
                    <img src="https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=2070&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <span class="text-orange-600 font-bold uppercase tracking-wider text-xs mb-3 block">News</span>
                <h3 class="text-xl font-serif font-bold text-stone-900 dark:text-white mb-3 group-hover:text-orange-600 transition-colors">Introducing Our New Vegan Range</h3>
                <p class="text-stone-600 dark:text-stone-400 text-sm mb-4 line-clamp-2">We've spent six months perfecting our new plant-based gyoza and mushroom bao fillings.</p>
            </a>
        </div>
    </div>
</section>

<!-- Newsletter CTA -->
<section class="py-24 bg-orange-50 dark:bg-stone-900">
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-serif font-bold text-stone-900 dark:text-white mb-4">Join Our Community</h2>
        <p class="text-stone-600 dark:text-stone-400 mb-8">Subscribe to receive exclusive recipes, early access to new seasonal menus, and kitchen news.</p>
        <form class="flex flex-col sm:flex-row gap-4" onsubmit="event.preventDefault(); alert('Subscribed successfully!');">
            <input type="email" placeholder="Email Address" required class="flex-grow px-6 py-4 rounded-full border border-stone-200 dark:border-stone-700 bg-white dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500">
            <button type="submit" class="bg-orange-600 hover:bg-orange-700 text-white px-8 py-4 rounded-full font-bold transition-colors">Subscribe</button>
        </form>
    </div>
</section>
"""
write_page("blog.html", "Blog", "Kitchen journal and stories.", blog_body)

# ================== CONTACT ==================
contact_body = """
<section class="pt-24 pb-16 bg-stone-50 dark:bg-stone-900 text-center px-4">
    <h1 class="text-5xl md:text-6xl font-serif font-bold text-stone-900 dark:text-white mb-6">Contact Us</h1>
    <p class="text-xl text-stone-600 dark:text-stone-300 max-w-2xl mx-auto">We'd love to hear from you.</p>
</section>

<section class="py-16 bg-white dark:bg-stone-950">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
            
            <!-- Contact Info & Map -->
            <div class="space-y-12">
                <div>
                    <h2 class="text-2xl font-bold text-stone-900 dark:text-white mb-6">Get in Touch</h2>
                    <ul class="space-y-6">
                        <li class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-orange-100 dark:bg-stone-800 text-orange-600 dark:text-orange-400 rounded-full flex items-center justify-center shrink-0">
                                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                            </div>
                            <div>
                                <h3 class="font-bold text-stone-900 dark:text-white">Phone</h3>
                                <p class="text-stone-600 dark:text-stone-400">(555) 123-4567</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-orange-100 dark:bg-stone-800 text-orange-600 dark:text-orange-400 rounded-full flex items-center justify-center shrink-0">
                                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            </div>
                            <div>
                                <h3 class="font-bold text-stone-900 dark:text-white">Email</h3>
                                <p class="text-stone-600 dark:text-stone-400">hello@dumplingbao.com</p>
                            </div>
                        </li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-2xl font-bold text-stone-900 dark:text-white mb-6">Our Location</h2>
                    <div class="h-80 bg-stone-200 dark:bg-stone-800 rounded-xl overflow-hidden shadow-inner flex items-center justify-center text-stone-500">
                        <!-- Simple Map Placeholder / IFRAME goes here -->
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.25279998634!2d-74.14448763529324!3d40.69763123337996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY!5e0!3m2!1sen!2sus!4v1714571985444!5m2!1sen!2sus" class="w-full h-full border-0" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>
            </div>

            <!-- Form -->
            <div class="bg-stone-50 dark:bg-stone-900 p-8 md:p-10 rounded-2xl shadow-sm border border-stone-100 dark:border-stone-800">
                <h2 class="text-2xl font-bold text-stone-900 dark:text-white mb-8">Send an Enquiry</h2>
                <form class="space-y-6" onsubmit="event.preventDefault(); alert('Message sent successfully!');">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Full Name</label>
                            <input type="text" required class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-white dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Email</label>
                            <input type="email" required class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-white dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500">
                        </div>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Phone</label>
                            <input type="tel" class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-white dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Enquiry Type</label>
                            <select class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-white dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500">
                                <option>General Enquiry</option>
                                <option>Large Order / Catering</option>
                                <option>Retail / Wholesale</option>
                                <option>Feedback</option>
                            </select>
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Message</label>
                        <textarea required rows="5" class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-white dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500"></textarea>
                    </div>
                    <button type="submit" class="w-full bg-orange-600 hover:bg-orange-700 text-white px-8 py-4 rounded-lg font-bold transition-colors">Send Message</button>
                </form>
            </div>

        </div>
    </div>
</section>
"""
write_page("contact.html", "Contact", "Get in touch with Bamboo & Flour.", contact_body)

# ================== LOGIN ==================
login_body = """
<div class="w-full max-w-md bg-white dark:bg-stone-900 rounded-2xl shadow-xl border border-stone-100 dark:border-stone-800 p-8 m-4">
    <div class="text-center mb-8">
        <a href="index.html" class="inline-flex items-center gap-2 mb-6">
            <svg class="w-10 h-10 text-orange-600 dark:text-orange-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="4" y="12" width="16" height="8" rx="2" />
                <path d="M2 12h20" />
                <path d="M6 12C6 8 8 6 12 6s6 2 6 6" />
                <path d="M10 6V4h4v2" />
                <path d="M9 2s1 1 1 2-1 1-1 2" />
                <path d="M15 2s1 1 1 2-1 1-1 2" />
            </svg>
        </a>
        <h1 class="text-2xl font-serif font-bold text-stone-900 dark:text-white">Sign in to Bamboo & Flour</h1>
        <p class="text-stone-600 dark:text-stone-400 mt-2 text-sm">Access your orders and saved favorites.</p>
    </div>

    <form class="space-y-6" onsubmit="event.preventDefault(); window.location.href='index.html';">
        <div>
            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Email Address</label>
            <input type="email" required class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-stone-50 dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500 transition-shadow">
        </div>
        
        <div>
            <div class="flex justify-between items-center mb-2">
                <label class="block text-sm font-medium text-stone-700 dark:text-stone-300">Password</label>
                <a href="#" class="text-sm font-medium text-orange-600 hover:text-orange-500">Forgot Password?</a>
            </div>
            <div class="relative">
                <input type="password" id="password" required class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-stone-50 dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500 transition-shadow">
                <button type="button" onclick="const p=document.getElementById('password'); p.type=p.type==='password'?'text':'password';" class="absolute right-3 top-3 text-stone-400 hover:text-stone-600 dark:hover:text-stone-300">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                </button>
            </div>
        </div>

        <div class="flex items-center">
            <input type="checkbox" id="remember" class="h-4 w-4 text-orange-600 focus:ring-orange-500 border-stone-300 rounded">
            <label for="remember" class="ml-2 block text-sm text-stone-700 dark:text-stone-300">Remember me</label>
        </div>

        <button type="submit" class="w-full bg-orange-600 hover:bg-orange-700 text-white px-4 py-3 rounded-lg font-bold transition-colors shadow-md">Sign In</button>
    </form>

    <div class="mt-8 text-center text-sm text-stone-600 dark:text-stone-400">
        Don't have an account? <a href="signup.html" class="font-medium text-orange-600 hover:text-orange-500">Sign Up</a>
    </div>
    <div class="mt-4 text-center">
        <a href="index.html" class="text-sm font-medium text-stone-500 hover:text-stone-900 dark:hover:text-white transition-colors">&larr; Back to Home</a>
    </div>
</div>
"""
write_page("login.html", "Login", "Sign in to your account.", login_body, include_header_footer=False)

# ================== SIGNUP ==================
signup_body = """
<div class="w-full max-w-md bg-white dark:bg-stone-900 rounded-2xl shadow-xl border border-stone-100 dark:border-stone-800 p-8 m-4">
    <div class="text-center mb-8">
        <a href="index.html" class="inline-flex items-center gap-2 mb-6">
            <svg class="w-10 h-10 text-orange-600 dark:text-orange-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="4" y="12" width="16" height="8" rx="2" />
                <path d="M2 12h20" />
                <path d="M6 12C6 8 8 6 12 6s6 2 6 6" />
                <path d="M10 6V4h4v2" />
                <path d="M9 2s1 1 1 2-1 1-1 2" />
                <path d="M15 2s1 1 1 2-1 1-1 2" />
            </svg>
        </a>
        <h1 class="text-2xl font-serif font-bold text-stone-900 dark:text-white">Create an Account</h1>
        <p class="text-stone-600 dark:text-stone-400 mt-2 text-sm">Join Bamboo & Flour for faster checkout.</p>
    </div>

    <form class="space-y-5" onsubmit="event.preventDefault(); window.location.href='index.html';">
        <div>
            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Full Name</label>
            <input type="text" required class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-stone-50 dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500 transition-shadow">
        </div>
        
        <div>
            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Email Address</label>
            <input type="email" required class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-stone-50 dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500 transition-shadow">
        </div>
        
        <div>
            <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Phone (Optional)</label>
            <input type="tel" class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-stone-50 dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500 transition-shadow">
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
                <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Password</label>
                <input type="password" required class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-stone-50 dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500 transition-shadow">
            </div>
            <div>
                <label class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-2">Confirm</label>
                <input type="password" required class="w-full px-4 py-3 rounded-lg border border-stone-200 dark:border-stone-700 bg-stone-50 dark:bg-stone-800 text-stone-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-orange-500 transition-shadow">
            </div>
        </div>

        <div class="flex items-start mt-4">
            <input type="checkbox" id="terms" required class="h-4 w-4 mt-1 text-orange-600 focus:ring-orange-500 border-stone-300 rounded">
            <label for="terms" class="ml-2 block text-sm text-stone-600 dark:text-stone-400">
                I agree to the <a href="#" class="text-orange-600 hover:underline">Terms of Service</a> and <a href="#" class="text-orange-600 hover:underline">Privacy Policy</a>
            </label>
        </div>

        <button type="submit" class="w-full bg-orange-600 hover:bg-orange-700 text-white px-4 py-3 rounded-lg font-bold transition-colors shadow-md mt-6">Create Account</button>
    </form>

    <div class="mt-8 text-center text-sm text-stone-600 dark:text-stone-400">
        Already have an account? <a href="login.html" class="font-medium text-orange-600 hover:text-orange-500">Sign In</a>
    </div>
    <div class="mt-4 text-center">
        <a href="index.html" class="text-sm font-medium text-stone-500 hover:text-stone-900 dark:hover:text-white transition-colors">&larr; Back to Home</a>
    </div>
</div>
"""
write_page("signup.html", "Sign Up", "Create your account.", signup_body, include_header_footer=False)
print("Finished p4")
