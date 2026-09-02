(() => {
  'use strict';
  const KEY = 'nayanet:e01:v1';
  const $ = (s) => document.querySelector(s);
  const arrival = $('#arrival'), identity = $('#identity'), reveal = $('#reveal'), toolbox = $('#toolbox');
  const sun = $('#sun'), sunState = $('#sunState'), sunMessage = $('#sunMessage'), toast = $('#toast');
  let state = { stage: 'arrival', name: '', smartName: '', smartLink: '' };

  function load() {
    try { state = { ...state, ...JSON.parse(localStorage.getItem(KEY) || '{}') }; } catch (_) {}
    if (state.name && state.stage === 'home') show('home');
    else if (state.name && state.stage === 'identityCreated') show('reveal');
    else show('arrival');
  }

  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (_) { toastMsg('Local storage is unavailable. Your session will continue without persistence.'); }
  }

  function slug(name) {
    return (name || 'friend').toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'friend';
  }

  function setSun(mode, message) {
    const labels = { RESTING: 'Naya is here when you\'re ready.', ATTENTION: 'Naya is paying attention.', LISTENING: 'Naya is listening.', SUCCESS: 'Your first connection is ready.', ERROR: 'Something needs your attention.' };
    sun.dataset.state = mode;
    sunState.textContent = mode;
    sunMessage.textContent = message || labels[mode] || labels.RESTING;
    sun.setAttribute('aria-label', `Naya is ${mode.toLowerCase()}. ${sunMessage.textContent}`);
  }

  function toastMsg(message) {
    toast.textContent = message; toast.classList.add('show');
    clearTimeout(toast.t); toast.t = setTimeout(() => toast.classList.remove('show'), 2800);
  }

  function show(which) {
    arrival.hidden = which !== 'arrival'; identity.hidden = which !== 'identity'; reveal.hidden = which !== 'reveal'; toolbox.hidden = which !== 'home';
    state.stage = which === 'home' ? 'home' : which === 'reveal' ? 'identityCreated' : which;
    if (which === 'arrival') { setSun('RESTING'); window.scrollTo(0, 0); }
    if (which === 'identity') { setSun('LISTENING'); setTimeout(() => $('#nameInput')?.focus(), 60); window.scrollTo({ top: 0, behavior: 'smooth' }); }
    if (which === 'reveal') {
      $('#revealedName').textContent = state.name;
      $('#smartName').textContent = state.smartName;
      $('#smartLink').textContent = state.smartLink;
      setSun('SUCCESS'); window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    if (which === 'home') {
      $('#toolName').textContent = state.name.toUpperCase();
      setSun('ATTENTION', `Welcome, ${state.name}. Your toolbox is ready.`);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  $('#createCta').onclick = () => show('identity');
  $('#meetCta').onclick = () => { setSun('ATTENTION'); toastMsg('Hi. I\'m Naya. Think with me. Start by creating your free local identity.'); $('#createCta').focus(); };
  $('#identityBack').onclick = () => show('arrival');
  $('#identityForm').onsubmit = (event) => {
    event.preventDefault();
    const input = $('#nameInput'), name = input.value.trim();
    if (name.length < 2) { $('#nameError').textContent = 'Please enter at least two characters.'; setSun('ERROR'); input.focus(); return; }
    if (name.length > 80) { $('#nameError').textContent = 'Please use a shorter name.'; setSun('ERROR'); input.focus(); return; }
    $('#nameError').textContent = '';
    state.name = name; state.smartName = `naya/${slug(name)}`; state.smartLink = `nayanet.xyz/${slug(name)}`;
    save(); show('reveal');
  };

  $('#copyLink').onclick = async () => {
    const value = state.smartLink;
    try { await navigator.clipboard.writeText(value); toastMsg('Smart Link copied.'); }
    catch (_) { const code = $('#smartLink'); const range = document.createRange(); range.selectNodeContents(code); const sel = getSelection(); sel.removeAllRanges(); sel.addRange(range); toastMsg('Clipboard unavailable — the Smart Link is selected for you.'); }
  };

  $('#toolboxCta').onclick = () => show('home');
  $('#revealMeet').onclick = () => { show('reveal'); setSun('ATTENTION', `Good to meet you, ${state.name}.`); toastMsg('Naya is here. Your next useful move is yours to choose.'); };
  $('#toolNaya').onclick = () => { setSun('ATTENTION', 'Naya is ready to think with you.'); toastMsg('Naya is ready. Ask, think, and create together.'); };
  $('#toolChallenge').onclick = () => toastMsg('Five-Day Challenge is the next construction block. No fake route has been created.');
  $('#toolPower').onclick = () => toastMsg('Naya Power is the next experience. This E01 room does not fake the destination.');
  $('#nextAction').onclick = () => { setSun('ATTENTION', 'Momentum starts with one real goal.'); toastMsg('Five-Day Challenge is the next construction block.'); };
  $('#resetIdentity').onclick = () => {
    if (!window.confirm('Reset only this local E01 identity?')) return;
    state = { stage: 'arrival', name: '', smartName: '', smartLink: '' };
    try { localStorage.removeItem(KEY); } catch (_) {}
    show('arrival'); toastMsg('Local E01 identity reset.');
  };
  $('#brandHome').onclick = () => show(state.name ? 'home' : 'arrival');
  sun.addEventListener('click', () => { setSun('ATTENTION'); toastMsg('Naya is paying attention.'); });

  load();
})();
