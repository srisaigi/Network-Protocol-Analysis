const navLinks = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('.content-section');

navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.forEach((item) => item.classList.remove('active'));
    link.classList.add('active');
  });
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    const matchingLink = document.querySelector(`.nav-link[href="#${entry.target.id}"]`);
    if (matchingLink) {
      navLinks.forEach((item) => item.classList.remove('active'));
      matchingLink.classList.add('active');
    }
  });
}, { threshold: 0.25 });
sections.forEach((section) => observer.observe(section));

const toast = document.getElementById('toast');
document.querySelectorAll('.filter-item').forEach((button) => {
  button.addEventListener('click', async () => {
    const filter = button.dataset.filter;
    try {
      await navigator.clipboard.writeText(filter);
      toast.textContent = 'Filter copied to clipboard';
    } catch (_) {
      toast.textContent = filter;
    }
    toast.classList.add('show');
    window.setTimeout(() => toast.classList.remove('show'), 1800);
  });
});

document.getElementById('themeToggle').addEventListener('click', () => {
  document.body.classList.toggle('high-contrast');
});
