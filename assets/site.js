document.addEventListener('DOMContentLoaded', initializeSite);

function initializeSite() {
  const root = document.documentElement;
  const themeToggle = document.querySelector('.theme-toggle');
  const themeIcon = document.querySelector('.theme-icon');
  const themeNavItem = document.querySelector('.theme-nav-item');
  // Each language has its own pages (/team and /en/team, built by tools/build_en.py).
  // The switch is a plain link to the same page in the other language.
  const language = root.lang.startsWith('en') ? 'en' : 'de';
  const other = language === 'en' ? 'de' : 'en';
  const alternate = document.querySelector(`link[rel="alternate"][hreflang="${other === 'de' ? 'de-AT' : 'en'}"]`);
  const languageToggle = document.createElement('a');
  languageToggle.className = 'language-toggle';
  languageToggle.textContent = other.toUpperCase();
  languageToggle.href = alternate ? new URL(alternate.href).pathname : (other === 'en' ? '/en/' : '/');
  languageToggle.hreflang = other;
  languageToggle.lang = other;
  languageToggle.setAttribute('aria-label', other === 'en' ? 'English version' : 'Deutsche Version');
  if (themeNavItem) themeNavItem.append(languageToggle);

  // Colour scheme: the page follows the system setting. The toggle only stores
  // an override when the visitor picks the opposite of the system; toggling back
  // to the system scheme removes it again. The inline script in each <head>
  // applies a stored override before the first paint; styles.css reads it from
  // <meta name="color-scheme">.
  const schemeKey = 'team-swash-color-scheme';
  const schemeMeta = document.querySelector('meta[name="color-scheme"]');
  const systemDark = window.matchMedia('(prefers-color-scheme: dark)');
  const readOverride = () => {
    const value = getStoredValue(schemeKey);
    return value === 'light' || value === 'dark' ? value : null;
  };
  // Earlier versions stored 'light' or 'dark' under another key on every click.
  // Only 'dark' was a real choice against the light default, so carry that over.
  const legacyTheme = getStoredValue('team-swash-theme');
  if (legacyTheme !== null) {
    if (legacyTheme === 'dark' && readOverride() === null) setStoredValue(schemeKey, 'dark');
    removeStoredValue('team-swash-theme');
  }
  let override = readOverride();
  const renderedScheme = () => override || (systemDark.matches ? 'dark' : 'light');
  const applyScheme = () => {
    if (schemeMeta) schemeMeta.content = override || 'light dark';
    if (!themeToggle) return;
    const isDark = renderedScheme() === 'dark';
    themeToggle.setAttribute('aria-label', language === 'en'
      ? (isDark ? 'Switch to light mode' : 'Switch to dark mode')
      : (isDark ? 'Hellmodus aktivieren' : 'Dunkelmodus aktivieren'));
    if (themeIcon) themeIcon.textContent = isDark ? '☼' : '☾';
  };

  applyScheme();
  if (themeToggle) themeToggle.addEventListener('click', () => {
    const target = renderedScheme() === 'dark' ? 'light' : 'dark';
    const system = systemDark.matches ? 'dark' : 'light';
    // Store only a choice against the system, as the privacy policy states.
    override = target === system ? null : target;
    if (override) setStoredValue(schemeKey, override);
    else removeStoredValue(schemeKey);
    applyScheme();
  });
  // Keep the icon right when the system switches, and follow other tabs.
  systemDark.addEventListener('change', applyScheme);
  window.addEventListener('storage', (event) => {
    if (event.key !== schemeKey && event.key !== null) return;
    override = readOverride();
    applyScheme();
  });

  const privacyDialog = document.querySelector('#privacy-dialog');
  const privacyDismiss = document.querySelector('[data-privacy-dismiss]');
  const privacyKey = 'team-swash-privacy-notice';
  const noticeWasSeen = () => {
    return getStoredValue(privacyKey) === 'seen' || getStoredValue(privacyKey, 'session') === 'seen';
  };
  if (privacyDialog) {
    // However it is closed (button, Esc, click outside), the notice counts as seen.
    privacyDialog.addEventListener('close', () => {
      if (!setStoredValue(privacyKey, 'seen')) setStoredValue(privacyKey, 'seen', 'session');
    });
    privacyDismiss?.addEventListener('click', () => privacyDialog.close());
    if (!noticeWasSeen()) privacyDialog.showModal();
  }

  // The simulation guide opens once by itself; afterwards only through its button.
  const simGuide = document.querySelector('#sim-guide');
  const simGuideKey = 'team-swash-sim-guide';
  const openSimGuide = () => simGuide.showModal();
  if (simGuide) {
    // The buttons open and close the guide via command/commandfor in the HTML.
    // Browsers without invoker commands get the same through click listeners.
    if (!('commandForElement' in HTMLButtonElement.prototype)) {
      document.querySelectorAll('[data-sim-guide-open]').forEach((button) => button.addEventListener('click', () => simGuide.showModal()));
      simGuide.querySelector('[data-sim-guide-dismiss]')?.addEventListener('click', () => simGuide.close());
    }
    simGuide.addEventListener('close', () => setStoredValue(simGuideKey, 'seen'));
    if (getStoredValue(simGuideKey) !== 'seen') {
      // Wait for the privacy notice, so two dialogs never stack.
      if (privacyDialog?.open) privacyDialog.addEventListener('close', openSimGuide, { once: true });
      else openSimGuide();
    }
  }

  // Links use clean URLs (/team); also accept /team.html and /index.html.
  const pageKey = (path) => path.replace(/\.html$/, '').replace(/\/index$/, '/').replace(/(.)\/$/, '$1');
  const currentPage = pageKey(location.pathname);
  document.querySelectorAll('.site-nav a').forEach((link) => {
    if (pageKey(new URL(link.href).pathname) === currentPage) link.setAttribute('aria-current', 'page');
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
    const status = document.querySelector('#form-status');
    const submitButton = form.querySelector('button[type="submit"]');
    const showStatus = (de, en, isError = false) => {
      if (!status) return;
      status.textContent = language === 'en' ? en : de;
      status.classList.add('is-visible');
      status.classList.toggle('is-error', isError);
    };
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const accessKey = form.dataset.accessKey || '';
      if (!accessKey || accessKey === 'WEB3FORMS_ACCESS_KEY') {
        showStatus(
          'Das Formular ist noch nicht freigeschaltet. Bitte schreiben Sie uns an eine der angegebenen E-Mail-Adressen.',
          'The form is not active yet. Please email one of the contacts listed.',
          true,
        );
        return;
      }
      const data = Object.fromEntries(new FormData(form));
      if (data.botcheck) return;
      const payload = {
        access_key: accessKey,
        subject: `Neue Nachricht über cansat-swash.org von ${data.name}`,
        from_name: 'Website Team SWASH',
        name: data.name,
        email: data.email,
        phone: data.phone || '',
        message: data.message,
      };
      if (submitButton) submitButton.disabled = true;
      showStatus('Nachricht wird gesendet …', 'Sending your message …');
      try {
        const response = await fetch(form.action, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(payload),
        });
        const result = await response.json().catch(() => ({}));
        if (!response.ok || !result.success) throw new Error(result.message || response.statusText);
        form.reset();
        showStatus(
          'Danke! Ihre Nachricht ist bei uns angekommen. Wir melden uns so bald wie möglich.',
          'Thank you! Your message has reached us. We will get back to you as soon as we can.',
        );
      } catch {
        showStatus(
          'Die Nachricht konnte nicht gesendet werden. Bitte versuchen Sie es später noch einmal oder schreiben Sie uns direkt per E-Mail.',
          'Your message could not be sent. Please try again later or email us directly.',
          true,
        );
      } finally {
        if (submitButton) submitButton.disabled = false;
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

function removeStoredValue(key) {
  try {
    window.localStorage.removeItem(key);
  } catch {
    // Storage blocked: nothing was stored either.
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
