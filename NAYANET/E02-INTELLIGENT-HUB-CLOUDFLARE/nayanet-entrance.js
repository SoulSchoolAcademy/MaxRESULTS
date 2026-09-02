(() => {
  'use strict';

  // Front Door contract: identity first, authentication underneath.
  // Do not fabricate credentials in the browser. The current runtime preserves
  // name continuity; the real credential/passkey layer is a backend concern.
  const NAME = 'nayanetName';
  const LEGACY = 'nayanet_name';
  const STATE = 'nayanet:intelligence:v1';
  const form = document.getElementById('entryForm');
  const input = document.getElementById('nameInput');
  if (!form || !input) return;

  const clean = value => String(value || '').replace(/\s+/g, ' ').trim().slice(0, 80);
  const saved = clean(localStorage.getItem(NAME) || localStorage.getItem(LEGACY));
  if (saved) input.value = saved;

  const button = form.querySelector('button[type="submit"]');
  const syncButton = () => {
    const ready = clean(input.value).length > 0;
    if (button) {
      button.disabled = !ready;
      button.setAttribute('aria-disabled', String(!ready));
    }
  };

  input.addEventListener('input', syncButton);
  syncButton();

  form.addEventListener('submit', event => {
    event.preventDefault();
    const name = clean(input.value);
    if (!name) { input.focus(); return; }

    localStorage.setItem(NAME, name);
    localStorage.setItem(LEGACY, name);
    try {
      const state = JSON.parse(localStorage.getItem(STATE) || '{}');
      state.name = name;
      state.lastSeen = Date.now();
      localStorage.setItem(STATE, JSON.stringify(state));
    } catch (_) {}

    document.body.classList.add('nayanet-entering');
    if (button) {
      button.setAttribute('aria-busy', 'true');
      button.setAttribute('data-state', 'entering');
      button.disabled = true;
    }

    window.setTimeout(() => { window.location.assign('/hub.html'); }, 520);
  });
})();
