const form = document.getElementById('match-form');
const tabButtons = document.querySelectorAll('.tab-btn');
const resultsEl = document.getElementById('results');
const loadingEl = document.getElementById('loading');
const errorEl = document.getElementById('error');

tabButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    tabButtons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('resume-text').style.display = 'none';
    document.getElementById('resume-file').style.display = 'none';
    const target = document.getElementById(btn.dataset.tab);
    target.style.display = 'block';
  });
});

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  errorEl.classList.add('hidden');
  resultsEl.classList.add('hidden');
  loadingEl.classList.remove('hidden');

  const formData = new FormData(form);

  try {
    const response = await fetch('/api/match/', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('Server responded with ' + response.status);
    }

    const data = await response.json();
    renderResults(data);
  } catch (err) {
    errorEl.textContent = 'Something went wrong: ' + err.message;
    errorEl.classList.remove('hidden');
  } finally {
    loadingEl.classList.add('hidden');
  }
});

function renderResults(data) {
  document.getElementById('score-value').textContent = data.score;
  document.getElementById('score-summary').textContent = data.explanation.summary;

  renderTags('must-matched', data.must_have_skills.matched);
  renderTags('must-missing', data.must_have_skills.missing);
  renderTags('nice-matched', data.nice_to_have_skills.matched);
  renderTags('nice-missing', data.nice_to_have_skills.missing);

  const suggestionsList = document.getElementById('suggestions-list');
  suggestionsList.innerHTML = '';
  data.explanation.suggestions.forEach(function (s) {
    const li = document.createElement('li');
    li.textContent = s;
    suggestionsList.appendChild(li);
  });

  resultsEl.classList.remove('hidden');
}

function renderTags(containerId, skills) {
  const container = document.getElementById(containerId);
  container.innerHTML = '';
  skills.forEach(function (skill) {
    const span = document.createElement('span');
    span.className = 'tag';
    span.textContent = skill;
    container.appendChild(span);
  });
}