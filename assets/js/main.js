
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
