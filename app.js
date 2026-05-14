const progressBar = document.querySelector('.scroll-progress span');
const revealItems = document.querySelectorAll('.section, .channel-card, .roadmap-grid article, .community-grid article');

function updateProgress() {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
  progressBar.style.width = `${Math.min(progress, 100)}%`;
}

if ('IntersectionObserver' in window) {
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  revealItems.forEach((item) => {
    item.classList.add('reveal');
    revealObserver.observe(item);
  });
}

document.querySelectorAll('[data-tabs]').forEach((tabs) => {
  const buttons = tabs.querySelectorAll('[role="tab"]');
  const panels = tabs.querySelectorAll('[role="tabpanel"]');

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const selectedTab = button.dataset.tab;

      buttons.forEach((tab) => {
        const isActive = tab === button;
        tab.classList.toggle('active', isActive);
        tab.setAttribute('aria-selected', String(isActive));
      });

      panels.forEach((panel) => {
        const isActive = panel.dataset.panel === selectedTab;
        panel.classList.toggle('active', isActive);
        panel.hidden = !isActive;
      });
    });
  });
});

window.addEventListener('scroll', updateProgress, { passive: true });
updateProgress();
