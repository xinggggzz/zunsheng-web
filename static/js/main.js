// Main JavaScript functionality for Zunsheng Website

document.addEventListener('DOMContentLoaded', () => {
    // Header Scroll Effect - Optional if needed later
    const header = document.querySelector('.site-header');
    
    // Smooth scroll for anchors
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    console.log('Zunsheng Website loaded');
});
