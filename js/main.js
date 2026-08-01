/* ============================================
   سُكون - Sukoon Landing Page JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ============================================
    // Navbar Scroll Effect
    // ============================================
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });

    // ============================================
    // Mobile Menu Toggle
    // ============================================
    const mobileToggle = document.getElementById('mobileToggle');
    const navLinks = document.getElementById('navLinks');

    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
            document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
        });

        // Close menu on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileToggle.classList.remove('active');
                navLinks.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // ============================================
    // Scroll Animations (Intersection Observer)
    // ============================================
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -80px 0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add staggered delay for grid items
                const parent = entry.target.parentElement;
                if (parent) {
                    const siblings = Array.from(parent.children);
                    const idx = siblings.indexOf(entry.target);
                    entry.target.style.transitionDelay = `${idx * 0.08}s`;
                }
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all animated elements
    document.querySelectorAll('.feature-card, .product-card, .review-card, .insta-item').forEach(el => {
        observer.observe(el);
    });

    // ============================================
    // Smooth Scroll for Anchor Links
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const navHeight = navbar.offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ============================================
    // Counter Animation
    // ============================================
    function animateCounters() {
        const stats = document.querySelectorAll('.stat-number');
        stats.forEach(stat => {
            const text = stat.textContent;
            // Only animate if it contains a number
            if (/\d/.test(text)) {
                const match = text.match(/(\d+)/);
                if (match) {
                    const target = parseInt(match[1]);
                    const suffix = text.replace(match[1], '');
                    let current = 0;
                    const increment = Math.ceil(target / 40);
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            current = target;
                            clearInterval(timer);
                        }
                        stat.textContent = current + suffix;
                    }, 30);
                }
            }
        });
    }

    // Trigger counter animation when hero is visible
    const heroObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(animateCounters, 500);
                heroObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    const heroSection = document.querySelector('.hero-stats');
    if (heroSection) {
        heroObserver.observe(heroSection);
    }

    // ============================================
    // Warranty Form Handler
    // ============================================
    const warrantyForm = document.getElementById('warrantyForm');
    if (warrantyForm) {
        warrantyForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(this);
            const name = formData.get('name');
            const phone = formData.get('phone');
            const orderNumber = formData.get('orderNumber');
            const productType = formData.get('productType');
            const message = formData.get('message');

            // Build WhatsApp message
            let waMessage = `مرحبًا، أريد تفعيل الضمان الذهبي\n`;
            waMessage += `الاسم: ${name}\n`;
            waMessage += `رقم الهاتف: ${phone}\n`;
            if (orderNumber) waMessage += `رقم الطلب: ${orderNumber}\n`;
            waMessage += `نوع المنتج: ${productType}\n`;
            if (message) waMessage += `ملاحظات: ${message}`;

            const waUrl = `https://wa.me/96872022112?text=${encodeURIComponent(waMessage)}`;
            window.open(waUrl, '_blank');
        });
    }

    // ============================================
    // Lazy Loading Images
    // ============================================
    if ('IntersectionObserver' in window) {
        const imgObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                    }
                    imgObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imgObserver.observe(img);
        });
    }

    // ============================================
    // Page Load Animation
    // ============================================
    document.body.classList.add('loaded');

    // Add loaded class for smooth transitions
    const style = document.createElement('style');
    style.textContent = `
        body:not(.loaded) * {
            transition: none !important;
            animation: none !important;
        }
    `;
    document.head.appendChild(style);

    // Remove the style after load
    window.addEventListener('load', () => {
        setTimeout(() => style.remove(), 100);
    });
});
