// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', function () {

    // Add fade-in animation to content elements
    const contentElements = document.querySelectorAll('.hero-section, .card, .gallery-item, .section-title');

    contentElements.forEach((element, index) => {
        element.classList.add('fade-in');
        element.style.animationDelay = `${index * 0.1}s`;
    });

    // Add glow effect to image cards on hover
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.classList.add('glow-effect');
        });

        card.addEventListener('mouseleave', function () {
            this.classList.remove('glow-effect');
        });
    });

    // Initialize the random photos carousel
    const randomCarousel = document.getElementById('randomPhotosCarousel');
    if (randomCarousel) {
        // Initialize Bootstrap carousel with options
        const carousel = new bootstrap.Carousel(randomCarousel, {
            interval: 5000, // Change slides every 5 seconds
            wrap: true, // Loop continuously
            touch: true // Enable touch swiping
        });

        // Add glow effect on slide transition
        randomCarousel.addEventListener('slide.bs.carousel', function () {
            randomCarousel.classList.add('glow-effect');
            setTimeout(function () {
                randomCarousel.classList.remove('glow-effect');
            }, 1000);
        });

        // Randomize the transition speeds for dynamic effect
        const carouselItems = randomCarousel.querySelectorAll('.carousel-item');
        carouselItems.forEach(item => {
            // Random transition duration between 1s and 2s
            const transitionDuration = 1 + Math.random();
            item.style.transition = `transform ${transitionDuration}s ease-in-out`;
        });

        // This function will randomize the next slide sometimes
        // instead of going in sequence
        function randomizeNextSlide() {
            // 30% chance to show a random slide instead of the next one
            if (Math.random() < 0.3) {
                const totalItems = carouselItems.length;
                const randomIndex = Math.floor(Math.random() * totalItems);
                carousel.to(randomIndex);
            }
        }

        // Apply random slide selection occasionally
        setInterval(randomizeNextSlide, 15000);
    }

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(16, 0, 43, 0.95)';
            navbar.style.boxShadow = '0 5px 20px rgba(157, 78, 221, 0.3)';
        } else {
            navbar.style.background = 'rgba(16, 0, 43, 0.9)';
            navbar.style.boxShadow = '0 0 20px 0 var(--dark-purple)';
        }
    });

    // Lightbox for gallery images
    const galleryItems = document.querySelectorAll('.gallery-item img');

    if (galleryItems.length > 0) {
        galleryItems.forEach(item => {
            item.addEventListener('click', function () {
                const imgSrc = this.getAttribute('src');
                const lightbox = document.createElement('div');
                lightbox.classList.add('lightbox');

                lightbox.innerHTML = `
                    <div class="lightbox-content">
                        <img src="${imgSrc}" alt="Enlarged image">
                        <span class="close-lightbox">&times;</span>
                    </div>
                `;

                document.body.appendChild(lightbox);
                document.body.style.overflow = 'hidden';

                // Close lightbox on click
                lightbox.addEventListener('click', function (e) {
                    if (e.target === lightbox || e.target.classList.contains('close-lightbox')) {
                        document.body.removeChild(lightbox);
                        document.body.style.overflow = 'auto';
                    }
                });
            });
        });
    }

    // Video play button effect
    const videoThumbnails = document.querySelectorAll('.video-thumbnail');

    if (videoThumbnails.length > 0) {
        videoThumbnails.forEach(thumbnail => {
            thumbnail.addEventListener('mouseenter', function () {
                const playButton = this.querySelector('.play-button');

                if (playButton) {
                    playButton.style.transform = 'scale(1.1)';
                    playButton.style.opacity = '1';
                }
            });

            thumbnail.addEventListener('mouseleave', function () {
                const playButton = this.querySelector('.play-button');

                if (playButton) {
                    playButton.style.transform = 'scale(1)';
                    playButton.style.opacity = '0.8';
                }
            });
        });
    }

    // Dynamic stars
    function createStars() {
        const starsContainer = document.querySelector('.stars-container');
        if (!starsContainer) return;

        for (let i = 0; i < 50; i++) {
            const star = document.createElement('div');
            star.classList.add('dynamic-star');

            // Random position
            const x = Math.random() * window.innerWidth;
            const y = Math.random() * window.innerHeight;

            // Random size
            const size = Math.random() * 3;

            // Random opacity animation duration
            const duration = 3 + Math.random() * 5;

            star.style.left = `${x}px`;
            star.style.top = `${y}px`;
            star.style.width = `${size}px`;
            star.style.height = `${size}px`;
            star.style.animationDuration = `${duration}s`;

            starsContainer.appendChild(star);
        }
    }

    // Create dynamic stars
    createStars();

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
