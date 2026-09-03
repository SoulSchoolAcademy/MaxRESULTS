(() => {
  'use strict';
  const root = document.getElementById('frontDoor');
  const form = document.getElementById('entryForm');
  const button = form?.querySelector('button[type="submit"]');
  const status = root?.querySelector('[data-vault-status]');
  if (!root || !form || !button) return;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const steps = [
    ['charging','PRESS','Presence received.'],
    ['awakening','VAULT ADVANCES','The threshold is responding.'],
    ['awakening','PURPLE INTELLIGENCE AWAKENS','NayaNET intelligence is alive.'],
    ['opening','SYSTEM RESPONDS','The system recognizes the invitation.'],
    ['opening','THRESHOLD OPENS','The way forward is clear.'],
    ['open','ARRIVE','Welcome to NayaNET.']
  ];
  let running = false;
  const announce = (title, detail) => {
    if (status) status.innerHTML = `<span>${title}</span><strong>${detail}</strong>`;
  };
  const activate = () => {
    if (running) return;
    const input = document.getElementById('nameInput');
    if (!input || !String(input.value || '').trim()) return;
    running = true;
    button.disabled = true;
    button.setAttribute('aria-busy','true');
    root.dataset.vault = 'charging';
    root.dataset.activation = 'PRESS';
    announce('PRESS','Presence received.');
    const delay = reduced ? 60 : 260;
    steps.slice(1).forEach((step, index) => {
      window.setTimeout(() => {
        root.dataset.vault = step[0];
        root.dataset.activation = step[1];
        announce(step[1], step[2]);
      }, delay * (index + 1));
    });
    window.setTimeout(() => {
      window.location.assign('/hub.html');
    }, reduced ? 420 : 1780);
  };
  form.addEventListener('submit', event => {
    event.preventDefault();
    activate();
  });
  window.NayaNETVault = Object.freeze({ version:'1.0.0', activate });
})();
