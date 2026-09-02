(() => {
  'use strict';
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
    if (button) { button.setAttribute('aria-busy', 'true'); button.disabled = true; }
    window.setTimeout(() => { window.location.assign('/hub.html'); }, 520);
  });

  document.querySelectorAll('.threshold-doors [data-preview]').forEach(orb => {
    orb.addEventListener('click', () => {
      document.querySelectorAll('.threshold-doors [data-preview]').forEach(item => item.classList.remove('is-selected'));
      orb.classList.add('is-selected');
      const copy = {
        naya: 'Naya is the intelligence at the center.',
        brain: 'Your context compounds instead of starting over.',
        identity: 'Your Smart Identity is your doorway into the network.',
        player: 'Power Player keeps the ideas moving with you.',
        network: 'Connection happens by permission.'
      }[orb.dataset.preview];
      const invitation = document.querySelector('.threshold-invitation');
      if (invitation && copy) invitation.textContent = copy;
    });
  });
})();
