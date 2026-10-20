const swashTranslations = window.swashTranslations || {};

document.addEventListener('DOMContentLoaded', initializeSite);

function initializeSite() {
  const root = document.documentElement;
  const themeToggle = document.querySelector('.theme-toggle');
  const themeIcon = document.querySelector('.theme-icon');
  const themeNavItem = document.querySelector('.theme-nav-item');
  let theme = getStoredValue('team-swash-theme') || getStoredValue('nordlicht-theme') || 'light';
  let language = getStoredValue('team-swash-language') || 'de';

  const languageToggle = document.createElement('button');
  languageToggle.className = 'language-toggle';
  languageToggle.type = 'button';
  languageToggle.textContent = 'DE';
  if (themeNavItem) themeNavItem.append(languageToggle);

  const originalText = new Map();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) originalText.set(walker.currentNode, walker.currentNode.nodeValue);
  const originalAttributes = [];
  document.querySelectorAll('[aria-label], [alt], [placeholder], [title]').forEach((element) => {
    ['aria-label', 'alt', 'placeholder', 'title'].forEach((name) => {
      if (element.hasAttribute(name)) originalAttributes.push({ element, name, value: element.getAttribute(name) });
    });
  });
  const description = document.querySelector('meta[name="description"]');
  const originalDescription = description?.content || '';
  const originalTitle = document.title;

  const translated = (value) => swashTranslations[value] || value;
  const setLanguage = (nextLanguage) => {
    language = nextLanguage;
    const isEnglish = language === 'en';
    root.lang = isEnglish ? 'en' : 'de-AT';
    originalText.forEach((value, node) => {
      const trimmed = value.trim();
      const leading = value.match(/^\s*/)?.[0] || '';
      const trailing = value.match(/\s*$/)?.[0] || '';
      const replacement = isEnglish
        ? (Object.prototype.hasOwnProperty.call(swashTranslations, value) ? swashTranslations[value] : translated(trimmed))
        : trimmed;
      node.nodeValue = leading + replacement + trailing;
    });
    originalAttributes.forEach(({ element, name, value }) => {
      element.setAttribute(name, isEnglish ? translated(value) : value);
    });
    document.title = isEnglish ? translated(originalTitle) : originalTitle;
    if (description) description.content = isEnglish ? translated(originalDescription) : originalDescription;
    if (languageToggle) {
      languageToggle.textContent = isEnglish ? 'EN' : 'DE';
      languageToggle.setAttribute('aria-label', isEnglish ? 'Switch language to German' : 'Sprache auf Englisch umstellen');
      languageToggle.setAttribute('aria-pressed', String(isEnglish));
    }
    if (themeToggle) {
      const isDark = theme === 'dark';
      themeToggle.setAttribute('aria-pressed', String(isDark));
      themeToggle.setAttribute('aria-label', isEnglish
        ? (isDark ? 'Switch to light mode' : 'Switch to dark mode')
        : (isDark ? 'Hellmodus aktivieren' : 'Dunkelmodus aktivieren'));
    }
    const menuToggle = document.querySelector('.menu-toggle');
    if (menuToggle) {
      const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
      menuToggle.setAttribute('aria-label', isEnglish
        ? (isOpen ? 'Close menu' : 'Open menu')
        : (isOpen ? 'Menü schließen' : 'Menü öffnen'));
    }
  };

  const setTheme = (nextTheme) => {
    theme = nextTheme;
    root.dataset.theme = theme;
    if (themeToggle) {
      const isDark = theme === 'dark';
      themeToggle.setAttribute('aria-pressed', String(isDark));
      themeToggle.setAttribute('aria-label', language === 'en'
        ? (isDark ? 'Switch to light mode' : 'Switch to dark mode')
        : (isDark ? 'Hellmodus aktivieren' : 'Dunkelmodus aktivieren'));
      if (themeIcon) themeIcon.textContent = isDark ? '☼' : '☾';
    }
  };

  setLanguage(language === 'en' ? 'en' : 'de');
  setTheme(theme === 'dark' ? 'dark' : 'light');
  // Store a setting only once the visitor changes it, as the privacy policy states.
  languageToggle.addEventListener('click', () => {
    setLanguage(language === 'de' ? 'en' : 'de');
    setStoredValue('team-swash-language', language);
  });
  if (themeToggle) themeToggle.addEventListener('click', () => {
    setTheme(theme === 'dark' ? 'light' : 'dark');
    setStoredValue('team-swash-theme', theme);
  });

  const privacyDialog = document.querySelector('#privacy-dialog');
  const privacyDismiss = document.querySelector('[data-privacy-dismiss]');
  const privacyKey = 'team-swash-privacy-notice';
  const noticeWasSeen = () => {
    return getStoredValue(privacyKey) === 'seen' || getStoredValue(privacyKey, 'session') === 'seen';
  };
  if (privacyDialog && !noticeWasSeen()) {
    if (typeof privacyDialog.showModal === 'function') privacyDialog.showModal();
    else privacyDialog.setAttribute('open', '');
  }
  if (privacyDialog && privacyDismiss) {
    privacyDismiss.addEventListener('click', () => {
      if (!setStoredValue(privacyKey, 'seen')) setStoredValue(privacyKey, 'seen', 'session');
      if (typeof privacyDialog.close === 'function') privacyDialog.close();
      else privacyDialog.removeAttribute('open');
    });
  }

  const currentPage = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.site-nav a').forEach((link) => {
    if (link.getAttribute('href') === currentPage) link.setAttribute('aria-current', 'page');
  });

  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  if (menuToggle && nav) {
    menuToggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('is-open');
      menuToggle.setAttribute('aria-expanded', String(isOpen));
      menuToggle.setAttribute('aria-label', language === 'en'
        ? (isOpen ? 'Close menu' : 'Open menu')
        : (isOpen ? 'Menü schließen' : 'Menü öffnen'));
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest('a')) {
        nav.classList.remove('is-open');
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.setAttribute('aria-label', language === 'en' ? 'Open menu' : 'Menü öffnen');
      }
    });
  }

  const sectionLabels = document.querySelectorAll('.section-label');
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (sectionLabels.length && 'IntersectionObserver' in window && !prefersReducedMotion) {
    // Observe the surrounding block: the clipped label itself has no visible area to intersect.
    const labelObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.querySelectorAll(':scope > .section-label').forEach((label) => label.classList.add('is-typed'));
        labelObserver.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -15% 0px' });
    sectionLabels.forEach((label) => {
      label.classList.add('type-ready');
      labelObserver.observe(label.parentElement);
    });
  }

  const form = document.querySelector('#contact-form');
  if (form) {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const status = document.querySelector('#form-status');
      if (status) {
        status.textContent = language === 'en'
          ? 'Thank you. Your entries are valid, but the form is not connected to a sending service yet.'
          : 'Danke. Die Eingaben sind gültig; das Formular ist noch nicht mit einem Versanddienst verbunden.';
        status.classList.add('is-visible');
      }
    });
  }
  document.querySelectorAll('[data-year]').forEach((node) => {
    node.textContent = String(new Date().getFullYear());
  });
}

function getStoredValue(key, storageType = 'local') {
  try {
    const storage = storageType === 'session' ? window.sessionStorage : window.localStorage;
    return storage.getItem(key);
  } catch {
    return null;
  }
}

function setStoredValue(key, value, storageType = 'local') {
  try {
    const storage = storageType === 'session' ? window.sessionStorage : window.localStorage;
    storage.setItem(key, value);
    return true;
  } catch {
    return false;
  }
}
