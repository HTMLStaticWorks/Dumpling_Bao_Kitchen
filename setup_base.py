import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

base_dir = "d:/SEPT WEBSITES/Dumpling & Bao Kitchen"
assets_css_dir = os.path.join(base_dir, "assets", "css")
assets_js_dir = os.path.join(base_dir, "assets", "js")
assets_img_dir = os.path.join(base_dir, "assets", "img")

create_directory(assets_css_dir)
create_directory(assets_js_dir)
create_directory(assets_img_dir)

header_html = """
<header class="fixed w-full z-50 bg-white dark:bg-stone-900 transition-colors duration-300 shadow-sm border-b border-stone-200 dark:border-stone-800" id="main-header">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-20">
            <!-- Logo -->
            <div class="flex-shrink-0 flex items-center">
                <a href="index.html" class="flex items-center gap-2 group">
                    <svg class="w-8 h-8 text-orange-600 dark:text-orange-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="4" y="12" width="16" height="8" rx="2" />
                        <path d="M2 12h20" />
                        <path d="M6 12C6 8 8 6 12 6s6 2 6 6" />
                        <path d="M10 6V4h4v2" />
                        <path d="M9 2s1 1 1 2-1 1-1 2" />
                        <path d="M15 2s1 1 1 2-1 1-1 2" />
                    </svg>
                    <span class="font-serif text-xl font-bold text-stone-900 dark:text-white group-hover:text-orange-600 dark:group-hover:text-orange-500 transition-colors">Bamboo & Flour</span>
                </a>
            </div>

            <!-- Desktop Nav -->
            <nav class="hidden lg:flex space-x-8 items-center" id="desktop-nav">
                <a href="index.html" class="nav-link text-stone-600 dark:text-stone-300 hover:text-orange-600 dark:hover:text-orange-400 font-medium transition-colors">Home</a>
                <a href="home2.html" class="nav-link text-stone-600 dark:text-stone-300 hover:text-orange-600 dark:hover:text-orange-400 font-medium transition-colors">Home 2</a>
                <a href="about.html" class="nav-link text-stone-600 dark:text-stone-300 hover:text-orange-600 dark:hover:text-orange-400 font-medium transition-colors">About</a>
                <a href="menu.html" class="nav-link text-stone-600 dark:text-stone-300 hover:text-orange-600 dark:hover:text-orange-400 font-medium transition-colors">Menu</a>
                <a href="blog.html" class="nav-link text-stone-600 dark:text-stone-300 hover:text-orange-600 dark:hover:text-orange-400 font-medium transition-colors">Blog</a>
                <a href="contact.html" class="nav-link text-stone-600 dark:text-stone-300 hover:text-orange-600 dark:hover:text-orange-400 font-medium transition-colors">Contact</a>
            </nav>

            <!-- Actions -->
            <div class="hidden lg:flex items-center space-x-4">
                <button id="theme-toggle" class="w-9 h-9 flex items-center justify-center text-stone-500 hover:text-orange-600 dark:text-stone-400 dark:hover:text-orange-400 transition-colors border border-stone-200 dark:border-stone-700 rounded-md" aria-label="Toggle Theme">
                    <svg class="w-4 h-4 dark:hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                    <svg class="w-4 h-4 hidden dark:block" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                </button>
                <button id="rtl-toggle" class="w-9 h-9 flex items-center justify-center text-stone-500 hover:text-orange-600 dark:text-stone-400 dark:hover:text-orange-400 transition-colors font-medium text-xs border border-stone-200 dark:border-stone-700 rounded-md" aria-label="Toggle RTL">
                    RTL
                </button>
                <a href="login.html" class="text-stone-600 dark:text-stone-300 hover:text-orange-600 dark:hover:text-orange-400 font-medium transition-colors">Login</a>
                <a href="signup.html" class="bg-orange-600 hover:bg-orange-700 text-white px-5 py-2.5 rounded-full font-medium transition-colors shadow-md hover:shadow-lg">Sign Up</a>
            </div>

            <!-- Mobile menu button -->
            <div class="flex items-center lg:hidden space-x-2">
                <button id="mobile-menu-btn" class="text-stone-600 dark:text-stone-300 hover:text-orange-600 p-2 focus:outline-none" aria-label="Menu">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>
    </div>
    
    <!-- Mobile Menu Panel -->
    <div id="mobile-menu" class="hidden lg:hidden bg-white dark:bg-stone-900 border-b border-stone-200 dark:border-stone-800 shadow-lg absolute w-full">
        <div class="px-4 pt-2 pb-6 space-y-1">
            <a href="index.html" class="mobile-nav-link block px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800 hover:text-orange-600 dark:hover:text-orange-400">Home</a>
            <a href="home2.html" class="mobile-nav-link block px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800 hover:text-orange-600 dark:hover:text-orange-400">Home 2</a>
            <a href="about.html" class="mobile-nav-link block px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800 hover:text-orange-600 dark:hover:text-orange-400">About</a>
            <a href="menu.html" class="mobile-nav-link block px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800 hover:text-orange-600 dark:hover:text-orange-400">Menu</a>
            <a href="blog.html" class="mobile-nav-link block px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800 hover:text-orange-600 dark:hover:text-orange-400">Blog</a>
            <a href="contact.html" class="mobile-nav-link block px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800 hover:text-orange-600 dark:hover:text-orange-400">Contact</a>
            <div class="mt-4 pt-4 border-t border-stone-200 dark:border-stone-800 flex flex-col gap-3">
                <button id="mobile-rtl-toggle" class="w-full text-left px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800">Toggle RTL/LTR</button>
                <a href="login.html" class="block px-3 py-2 text-base font-medium text-stone-900 dark:text-white rounded-md hover:bg-orange-50 dark:hover:bg-stone-800">Login</a>
                <a href="signup.html" class="block w-full text-center bg-orange-600 hover:bg-orange-700 text-white px-5 py-3 rounded-full font-medium transition-colors">Sign Up</a>
            </div>
        </div>
    </div>
</header>
"""

footer_html = """
<footer class="bg-stone-950 text-stone-300 py-16 border-t-4 border-orange-600">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
            <!-- Brand -->
            <div class="space-y-6">
                <a href="index.html" class="flex items-center gap-2 group">
                    <svg class="w-8 h-8 text-orange-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="4" y="12" width="16" height="8" rx="2" />
                        <path d="M2 12h20" />
                        <path d="M6 12C6 8 8 6 12 6s6 2 6 6" />
                        <path d="M10 6V4h4v2" />
                        <path d="M9 2s1 1 1 2-1 1-1 2" />
                        <path d="M15 2s1 1 1 2-1 1-1 2" />
                    </svg>
                    <span class="font-serif text-xl font-bold text-white group-hover:text-orange-400 transition-colors">Bamboo & Flour</span>
                </a>
                <p class="text-stone-400 text-sm leading-relaxed">
                    Handmade daily in our steam kitchens. We bring authentic flavors and contemporary craft to every dumpling and bao we serve.
                </p>
                <div class="flex space-x-4">
                    <a href="#" class="text-stone-400 hover:text-white transition-colors" aria-label="Instagram">
                        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                    </a>
                    <a href="#" class="text-stone-400 hover:text-white transition-colors" aria-label="Facebook">
                        <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/></svg>
                    </a>
                </div>
            </div>

            <!-- Explore -->
            <div>
                <h3 class="text-white font-semibold mb-6 uppercase tracking-wider text-sm">Explore</h3>
                <ul class="space-y-3 text-sm">
                    <li><a href="index.html" class="hover:text-orange-400 transition-colors">Home</a></li>
                    <li><a href="about.html" class="hover:text-orange-400 transition-colors">About Us</a></li>
                    <li><a href="menu.html" class="hover:text-orange-400 transition-colors">Menu</a></li>
                    <li><a href="blog.html" class="hover:text-orange-400 transition-colors">Journal & Blog</a></li>
                </ul>
            </div>

            <!-- Customer -->
            <div>
                <h3 class="text-white font-semibold mb-6 uppercase tracking-wider text-sm">Customer</h3>
                <ul class="space-y-3 text-sm">
                    <li><a href="contact.html" class="hover:text-orange-400 transition-colors">Contact & Enquiries</a></li>
                    <li><a href="login.html" class="hover:text-orange-400 transition-colors">Account Login</a></li>
                    <li><a href="signup.html" class="hover:text-orange-400 transition-colors">Create Account</a></li>
                </ul>
            </div>

            <!-- Contact -->
            <div>
                <h3 class="text-white font-semibold mb-6 uppercase tracking-wider text-sm">Contact Us</h3>
                <ul class="space-y-3 text-sm">
                    <li class="flex items-start gap-3">
                        <svg class="w-5 h-5 text-orange-500 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                        <span>(555) 123-4567</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <svg class="w-5 h-5 text-orange-500 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                        <span>hello@dumplingbao.com</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <svg class="w-5 h-5 text-orange-500 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        <span>Mon - Sun: 11:00 AM - 10:00 PM</span>
                    </li>
                </ul>
            </div>
        </div>
        
        <div class="mt-16 pt-8 border-t border-stone-800 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-stone-500">
            <p>&copy; 2026 Bamboo & Flour. All rights reserved.</p>
            <div class="flex space-x-6">
                <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
                <a href="#" class="hover:text-white transition-colors">Terms of Service</a>
            </div>
        </div>
    </div>
</footer>

<button id="scroll-to-top" class="fixed bottom-8 right-8 bg-orange-600 hover:bg-orange-700 text-white p-3 rounded-full shadow-lg opacity-0 pointer-events-none transition-all duration-300 z-50 transform translate-y-4" aria-label="Scroll to top">
    <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"></path>
    </svg>
</button>
"""

common_head = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Bamboo & Flour</title>
    <meta name="description" content="{description}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        orange: {{
                            50: '#fff7ed',
                            100: '#ffedd5',
                            400: '#fb923c',
                            500: '#f97316',
                            600: '#ea580c',
                            700: '#c2410c',
                        }},
                        stone: {{
                            50: '#fafaf9',
                            800: '#292524',
                            900: '#1c1917',
                            950: '#0c0a09',
                        }}
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        serif: ['Playfair Display', 'Georgia', 'serif'],
                    }}
                }}
            }}
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="bg-stone-50 text-stone-900 dark:bg-stone-900 dark:text-stone-100 transition-colors duration-300 antialiased selection:bg-orange-200 selection:text-orange-900 flex flex-col min-h-screen">
    <script>
        // Inline script to prevent FOUC for theme and RTL
        if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
            document.documentElement.classList.add('dark');
        }}
        if (localStorage.getItem('dir') === 'rtl') {{
            document.documentElement.setAttribute('dir', 'rtl');
        }}
    </script>
"""

common_scripts = """
    <script src="assets/js/main.js"></script>
</body>
</html>
"""

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


# Now the python script should create the actual JS file and CSS file.
with open(os.path.join(assets_js_dir, "main.js"), "w") as f:
    f.write("""
document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const mobileThemeToggleBtn = document.getElementById('mobile-theme-toggle');
    
    function toggleTheme() {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        }
    }
    
    if(themeToggleBtn) themeToggleBtn.addEventListener('click', toggleTheme);
    if(mobileThemeToggleBtn) mobileThemeToggleBtn.addEventListener('click', toggleTheme);

    // RTL Toggle
    const rtlToggleBtn = document.getElementById('rtl-toggle');
    const mobileRtlToggleBtn = document.getElementById('mobile-rtl-toggle');
    
    function toggleRTL() {
        if (document.documentElement.getAttribute('dir') === 'rtl') {
            document.documentElement.removeAttribute('dir');
            localStorage.setItem('dir', 'ltr');
        } else {
            document.documentElement.setAttribute('dir', 'rtl');
            localStorage.setItem('dir', 'rtl');
        }
    }

    if(rtlToggleBtn) rtlToggleBtn.addEventListener('click', toggleRTL);
    if(mobileRtlToggleBtn) mobileRtlToggleBtn.addEventListener('click', toggleRTL);

    // Mobile Menu
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Scroll to Top
    const scrollToTopBtn = document.getElementById('scroll-to-top');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollToTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
            scrollToTopBtn.classList.add('opacity-100', 'translate-y-0');
        } else {
            scrollToTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
            scrollToTopBtn.classList.remove('opacity-100', 'translate-y-0');
        }
    });

    if (scrollToTopBtn) {
        scrollToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Set Active Nav Link
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('text-orange-600', 'dark:text-orange-500', 'font-semibold');
            link.classList.remove('text-stone-600', 'dark:text-stone-300', 'text-stone-900');
        }
    });
});
""")

with open(os.path.join(assets_css_dir, "style.css"), "w") as f:
    f.write("""
/* Custom utilities if needed */
html[dir="rtl"] {
    text-align: right;
}
html[dir="rtl"] #mobile-menu {
    left: auto;
    right: 0;
}
""")
