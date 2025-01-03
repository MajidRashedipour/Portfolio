const navItems = document.querySelectorAll('li');
const homeNav = document.querySelector('.home-btn');
const resumeNav = document.querySelector('.resume-btn');
const messageNav = document.querySelector('.message-btn');

const indicator = document.querySelector('.indicator');

const sections = document.querySelectorAll('section');

window.addEventListener('load', () => {
    indicator.style.transform = `translateX(${homeNav.offsetLeft - 16}px)`;
})

homeNav.addEventListener('click', () => {
    navItems.forEach((item) => {
        item.classList.remove('active');
    })
    homeNav.classList.add('active');
    
    indicator.style.transform = `translateX(${homeNav.offsetLeft - 16}px)`;

    sections.forEach((sec) => {
        sec.classList.remove('active');
        if (sec.className == 'home') {
            sec.classList.add('active');
        }
        if (sec.className == 'resume') {
            sec.style.transform = 'translate(100%, -100%)';
        }
    })
})

resumeNav.addEventListener('click', () => {
    navItems.forEach((item) => {
        item.classList.remove('active');
    })
    resumeNav.classList.add('active');

    indicator.style.transform = `translateX(${resumeNav.offsetLeft - 17}px)`;

    sections.forEach((sec) => {
        sec.classList.remove('active');
        if (sec.className == 'resume') {
            sec.classList.add('active');
            sec.style.transform = 'translate(0%, -100%)';
        }
    })
})

messageNav.addEventListener('click', () => {
    navItems.forEach((item) => {
        item.classList.remove('active');
    })
    messageNav.classList.add('active');

    indicator.style.transform = `translateX(${messageNav.offsetLeft - 17}px)`;

    sections.forEach((sec) => {
        sec.classList.remove('active');
        if (sec.className == 'resume') {
            sec.style.transform = 'translate(-100%, -100%)';
        }
        if (sec.className == 'contact-me') {
            sec.classList.add('active');
        }
    })
})
