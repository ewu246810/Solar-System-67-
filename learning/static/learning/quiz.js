document.querySelectorAll('.quiz-form').forEach((form) => {
  const questions = Array.from(form.querySelectorAll('.quiz-question'));
  const result = form.querySelector('.quiz-result');

  form.addEventListener('submit', (event) => {
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

    let score = 0;
    questions.forEach((question, index) => {
      const selected = answers[index];
      const isCorrect = selected.value === question.dataset.answer;
      const feedback = question.querySelector('.question-feedback');
      const correctOption = question.querySelector(
        `input[value="${question.dataset.answer}"]`
      );

      question.classList.toggle('quiz-question--correct', isCorrect);
      question.classList.toggle('quiz-question--incorrect', !isCorrect);
      question.querySelectorAll('.quiz-choice').forEach((choice) => {
        choice.classList.remove('quiz-choice--correct', 'quiz-choice--selected-wrong');
      });
      correctOption.closest('.quiz-choice').classList.add('quiz-choice--correct');

      if (isCorrect) {
        score += 1;
        feedback.textContent = `Correct! ${question.dataset.explanation}`;
      } else {
        selected.closest('.quiz-choice').classList.add('quiz-choice--selected-wrong');
        const correctText = correctOption.closest('.quiz-choice').querySelector('span').textContent;
        feedback.textContent = `Not quite. The answer is ${correctText}. ${question.dataset.explanation}`;
      }
    });

    result.textContent = `You scored ${score} out of ${questions.length}. ${score === questions.length ? 'Excellent work!' : 'Read the explanations, then try again.'}`;
  });

  form.addEventListener('reset', () => {
    window.setTimeout(() => {
      questions.forEach((question) => {
        question.classList.remove('quiz-question--correct', 'quiz-question--incorrect');
        question.querySelectorAll('.quiz-choice').forEach((choice) => {
          choice.classList.remove('quiz-choice--correct', 'quiz-choice--selected-wrong');
        });
        question.querySelector('.question-feedback').textContent = '';
      });
      result.textContent = '';
      result.hidden = true;
      result.classList.remove('quiz-result--needs-answer');
    }, 0);
  });
});
