/**
 * Great Controversy — Shared Quiz Widget
 * Usage: call initQuiz() after DOM is loaded.
 * Each quiz block needs:
 *   <div class="quiz-section" data-correct="2">
 *     <div class="quiz-title">Quick Check</div>
 *     <p class="quiz-question">Question text?</p>
 *     <div class="quiz-options">
 *       <button class="quiz-option">Option A</button>
 *       <button class="quiz-option">Option B</button>
 *       <button class="quiz-option">Option C (correct — index matches data-correct)</button>
 *     </div>
 *     <div class="quiz-feedback"></div>
 *   </div>
 */

function initQuiz() {
  document.querySelectorAll('.quiz-section').forEach(section => {
    const correctIndex = parseInt(section.dataset.correct, 10);
    const options = section.querySelectorAll('.quiz-option');
    const feedback = section.querySelector('.quiz-feedback');

    options.forEach((btn, i) => {
      btn.addEventListener('click', () => {
        // Prevent re-answering
        options.forEach(b => b.disabled = true);

        if (i === correctIndex) {
          btn.classList.add('correct');
          feedback.textContent = section.dataset.feedbackCorrect || '✓ Correct.';
          feedback.style.color = 'var(--correct)';
        } else {
          btn.classList.add('wrong');
          options[correctIndex].classList.add('correct');
          feedback.textContent = section.dataset.feedbackWrong || '✗ Not quite — see the highlighted answer.';
          feedback.style.color = 'var(--wrong)';
        }
      });
    });
  });
}

document.addEventListener('DOMContentLoaded', initQuiz);
