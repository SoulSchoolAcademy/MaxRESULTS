(() => {
  'use strict';

  // Front Door contract: identity first, authentication underneath.
  // The browser preserves identity continuity; real credential/passkey logic belongs server-side.
  const NAME = 'nayanetName';
  const LEGACY = 'nayanet_name';
  const STATE = 'nayanet:intelligence:v1';
  const form = document.getElementById('entryForm');
  const input = document.getElementById('nameInput');
  if (!form || !input) return;

  const clean = value => String(value || '').replace(/\s+/g, ' ').trim().slice(0, 80);
  const portal = form.querySelector('.portal-input');
  const button = form.querySelector('button[type="submit"]');
  const saved = clean(localStorage.getItem(NAME) || localStorage.getItem(LEGACY));
  if (saved) input.value = saved;

  const syncState = () => {
    const name = clean(input.value);
    const ready = name.length > 0;
    if (portal) portal.dataset.state = ready ? 'ready' : 'idle';
    if (button) {
      button.disabled = !ready;
      button.setAttribute('aria-disabled', String(!ready));
    }
  };

  input.addEventListener('input', () => {
    const name = clean(input.value);
    if (portal) portal.dataset.state = name ? 'active' : 'idle';
    syncState();
  });
  input.addEventListener('blur', syncState);
  syncState();

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
    if (portal) portal.dataset.state = 'entering';
    if (button) {
      button.setAttribute('aria-busy', 'true');
      button.setAttribute('data-state', 'entering');
      button.disabled = true;
      button.setAttribute('aria-disabled', 'true');
    }

    window.setTimeout(() => { window.location.assign('/hub.html'); }, 520);
  });
})();
