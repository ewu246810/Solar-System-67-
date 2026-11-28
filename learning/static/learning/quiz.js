document.querySelectorAll('.quiz-form').forEach((form) => {
  const questions = Array.from(form.querySelectorAll('.quiz-question'));
  const result = form.querySelector('.quiz-result');
  const submit = form.querySelector('.quiz-submit');
  const retry = form.querySelector('#quiz-retry');

  retry?.addEventListener('click', () => window.location.reload());

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const answers = questions.map((question) =>
      question.querySelector('input[type="radio"]:checked')
    );

    result.hidden = false;
    result.classList.remove('quiz-result--needs-answer');
    if (answers.some((answer) => answer === null)) {
      result.textContent = 'Choose an answer for each question first.';
      result.classList.add('quiz-result--needs-answer');
      return;
    }

    submit.disabled = true;
    submit.textContent = 'Checking your answers…';
    try {
      const response = await fetch(form.dataset.submitUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: JSON.stringify({
          quiz_id: form.dataset.quizId,
          answers: answers.map((answer) => Number(answer.value)),
        }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'The quiz could not be checked. Please try again.');

      questions.forEach((question, index) => {
        const selected = answers[index];
        const feedback = question.querySelector('.question-feedback');
        const resultItem = data.feedback[index];
        const correctOption = question.querySelector(`input[value="${resultItem.answer_index}"]`);
        question.classList.toggle('quiz-question--correct', resultItem.correct);
        question.classList.toggle('quiz-question--incorrect', !resultItem.correct);
        correctOption.closest('.quiz-choice').classList.add('quiz-choice--correct');
        if (!resultItem.correct) selected.closest('.quiz-choice').classList.add('quiz-choice--selected-wrong');
        feedback.textContent = resultItem.correct
          ? `Correct! ${resultItem.explanation}`
          : `Not quite. The answer is ${resultItem.answer_text}. ${resultItem.explanation}`;
      });

      let summary = `You scored ${data.score} out of ${data.total}. `;
      if (data.logged_in) {
        if (data.coins_earned) summary += `You earned ${data.coins_earned} coins! `;
        else if (data.saved) summary += 'Your result has been saved. ';
        else summary += 'Your best result and coins are already saved. ';
        summary += data.score === data.total ? 'Excellent work!' : 'Review the explanations and try another quiz to improve your best score.';
      } else {
        summary += data.score === data.total ? 'Excellent work! ' : 'Review the explanations and keep practising. ';
        summary += 'Log in to save progress and earn coins.';
      }
      result.textContent = summary;
      if (!data.logged_in) {
        const loginLink = document.createElement('a');
        loginLink.href = `/accounts/login/?next=${encodeURIComponent(window.location.pathname)}`;
        loginLink.textContent = 'Log in to save progress and earn coins';
        result.append(' ', loginLink);
      }
      questions.forEach((question) => question.querySelectorAll('input').forEach((input) => { input.disabled = true; }));
      submit.hidden = true;
      retry.hidden = false;
    } catch (error) {
      result.textContent = error.message || 'Could not connect to check the quiz. Please try again.';
      result.classList.add('quiz-result--needs-answer');
    } finally {
      submit.disabled = false;
      submit.innerHTML = 'Submit another answer <span aria-hidden="true">↗</span>';
    }
  });
});
