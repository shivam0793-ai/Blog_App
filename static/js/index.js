// ===============================
// Dark Mode
// ===============================

const themeBtn = document.getElementById("themeBtn");

themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    const icon = themeBtn.querySelector("i");

    if (document.body.classList.contains("dark")) {
        icon.classList.remove("fa-moon");
        icon.classList.add("fa-sun");
    } else {
        icon.classList.remove("fa-sun");
        icon.classList.add("fa-moon");
    }

});

// ===============================
// Mobile Menu
// ===============================

const menuBtn = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".nav-links");

menuBtn.addEventListener("click", () => {

    navLinks.classList.toggle("active");

});

// ===============================

// ===============================
// Newsletter Form
// ===============================

const newsletter = document.querySelector(".newsletter form");

newsletter.addEventListener("submit", (e) => {

    e.preventDefault();

    const email = newsletter.querySelector("input").value.trim();

    if (email === "") {
        alert("Please enter your email.");
        return;
    }

    alert("Thanks for subscribing! 🎉");

    newsletter.reset();

});

// ===============================
// Sticky Header Shadow
// ===============================

const header = document.querySelector("header");

window.addEventListener("scroll", () => {

    if (window.scrollY > 20) {

        header.style.boxShadow = "0 8px 20px rgba(0,0,0,.15)";

    } else {

        header.style.boxShadow = "0 2px 10px rgba(0,0,0,.08)";

    }

});

// ===============================
// Smooth Scroll
// ===============================

document.querySelectorAll('a[href="#"]').forEach(link => {

    link.addEventListener("click", (e) => {

        e.preventDefault();

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

});