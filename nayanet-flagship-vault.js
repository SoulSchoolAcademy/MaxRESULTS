(() => {
  'use strict';
  const root = document.getElementById('frontDoor');
  const form = document.getElementById('entryForm');
  const input = document.getElementById('nameInput');
  const button = document.getElementById('enterButton');
  const status = root?.querySelector('.v-status');
  if (!root || !form || !input || !button) return;

  // Never prefill the identity field. Every visit starts with a clean invitation.
  input.value = '';
  button.disabled = true;
  button.setAttribute('aria-disabled', 'true');

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let running = false;
  const announce = (label, message) => {
    if (!status) return;
    status.innerHTML = `<span>${label}</span><strong>${message}</strong>`;
  };
  const sync = () => {
    const valid = input.value.trim().length > 0;
    button.disabled = !valid || running;
    button.setAttribute('aria-disabled', String(button.disabled));
  };
  input.addEventListener('input', sync);

  const activate = () => {
    if (running) return;
    const name = input.value.trim();
    if (!name) { input.focus(); return; }
    running = true;
    button.disabled = true;
    button.setAttribute('aria-busy', 'true');
    try { localStorage.setItem('nayanetName', name); } catch (_) {}

    const steps = reduced ? [
      [0, 'charging', 'PRESS', 'Presence received.'],
      [80, 'awakening', 'VAULT ADVANCES', 'The threshold is responding.'],
      [160, 'opening', 'SYSTEM RESPONDS', 'NayaNET recognizes you.'],
      [250, 'opening', 'THRESHOLD OPENS', 'The way forward is clear.'],
      [360, 'open', 'ARRIVE', `Welcome, ${name}.`]
    ] : [
      [0, 'charging', 'PRESS', 'Presence received.'],
      [280, 'awakening', 'VAULT ADVANCES', 'The threshold is responding.'],
      [570, 'awakening', 'PURPLE INTELLIGENCE AWAKENS', 'NayaNET intelligence is alive.'],
      [900, 'opening', 'SYSTEM RESPONDS', 'NayaNET recognizes you.'],
      [1260, 'opening', 'THRESHOLD OPENS', 'The way forward is clear.'],
      [1650, 'open', 'ARRIVE', `Welcome, ${name}.`]
    ];

    steps.forEach(([delay, state, label, message]) => {
      window.setTimeout(() => {
        root.dataset.state = state;
        root.dataset.activation = label;
        announce(label, message);
      }, delay);
    });

    window.setTimeout(() => {
      window.location.assign('/hub.html');
    }, reduced ? 500 : 1900);
  };

  form.addEventListener('submit', event => {
    event.preventDefault();
    activate();
  });
  input.addEventListener('keydown', event => {
    if (event.key === 'Enter' && !button.disabled) {
      event.preventDefault();
      activate();
    }
  });

  sync();
  window.NayaNETVault = Object.freeze({ version: '2.0.0-flagship', activate });
})();
