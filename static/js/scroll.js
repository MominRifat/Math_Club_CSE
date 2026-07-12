document.addEventListener("DOMContentLoaded", () => {

    const elements = document.querySelectorAll("main > *");

    elements.forEach(el => {
        el.classList.add("reveal");
    });

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    }, {
        threshold: 0.1
    });

    elements.forEach(el => observer.observe(el));

});