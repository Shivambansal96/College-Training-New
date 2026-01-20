let questions = [];
let currentIndex = 0;
let currentScore = 0;
let answeredQuestions = new Set();
let unansweredQuestions = new Set();

// Load questions from JSON file
async function loadQuestions() {
    try {
        console.log('Attempting to load questions from questions.json...');
        const response = await fetch('questions.json');
        console.log('Fetch response status:', response.status);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Questions loaded successfully. Raw data:', data);
        console.log('Number of questions in data:', data.questions ? data.questions.length : 0);
        
        if (!data || !data.questions || !Array.isArray(data.questions)) {
            throw new Error('Invalid questions data format');
        }
        
        questions = data.questions;
        console.log(`Loaded ${questions.length} questions. Question titles:`, 
            questions.map((q, i) => `${i + 1}: ${q.question}`).join('\n'));
        
        // Initialize the quiz after loading questions
        initializeUnansweredQuestions();
        renderQuestion(currentIndex);
    } catch (error) {
        console.error('Error loading questions:', error);
        document.getElementById("question-box").innerHTML = `
            <h2>Error Loading Questions</h2>
            <p>There was an error loading the questions: ${error.message}</p>
            <p>Please check that:</p>
            <ul>
                <li>The questions.json file exists in the same directory as index.html</li>
                <li>The questions.json file contains valid JSON data</li>
                <li>You are running this through a web server (not just opening the HTML file directly)</li>
            </ul>
            <button onclick="location.reload()">Refresh Page</button>
        `;
        document.getElementById("prevBtn").disabled = true;
        document.getElementById("nextBtn").disabled = true;
        document.getElementById("finishBtn").disabled = true;
    }
}

// Initialize the quiz when the page loads
window.addEventListener('load', () => {
    loadQuestions();
    
    // Show disclaimer if it hasn't been shown before
    if (!localStorage.getItem('disclaimerShown')) {
        showDisclaimer();
    }
});

// Remove the old questions array since we're loading from JSON now
// ... rest of the existing code ...

// Add shuffle function
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function formatCode(code) {
    if (typeof code !== 'string') return '';
    // Replace literal \n with actual newlines and add proper indentation
    return code
        .replace(/\\n/g, '\n')
        .split('\n')
        .map(line => {
            // Add 4 spaces for indentation
            const indent = line.match(/^\s*/)[0].length;
            return '    '.repeat(Math.floor(indent/4)) + line.trimLeft();
        })
        .join('\n');
}

// New function to format text content (output and explanation)
function formatTextContent(text) {
    if (typeof text !== 'string') return '';
    return text.replace(/\\n/g, '\n').trim();
}

function renderQuestion(index) {
    try {
        if (index < 0 || index >= questions.length) {
            index = 0;
        }
        const q = questions[index];
        if (!q || !q.options || !Array.isArray(q.options)) return;
        currentIndex = index;
        const isAnswered = answeredQuestions.has(index);
        // Map shuffled options to their original indices
        let shuffledOptions, optionMap;
        if (isAnswered && localStorage.getItem(`shuffled_order_${index}`)) {
            // Use stored shuffle order for answered questions
            const order = JSON.parse(localStorage.getItem(`shuffled_order_${index}`));
            shuffledOptions = order.map(i => q.options[i]);
            optionMap = order;
        } else {
            // Shuffle and store the order
            const arr = q.options.map((_, i) => i);
            for (let i = arr.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
            shuffledOptions = arr.map(i => q.options[i]);
            optionMap = arr;
            localStorage.setItem(`shuffled_order_${index}`, JSON.stringify(optionMap));
        }
        const correctAnswerIndex = q.answer;
        const selectedAnswerIndex = localStorage.getItem(`selected_answer_${index}`);
        const isCorrect = localStorage.getItem(`is_correct_${index}`) === 'true';
        const optionsHTML = shuffledOptions.map((option, i) => {
            const origIdx = optionMap[i];
            let optionClasses = ['option'];
            if (isAnswered) {
                optionClasses.push('disabled');
                if (String(origIdx) === selectedAnswerIndex) {
                    optionClasses.push(isCorrect ? 'correct' : 'incorrect');
                }
                if (origIdx === correctAnswerIndex) {
                    optionClasses.push('correct');
                }
            }
            const onclickHandler = isAnswered ? '' : `onclick="handleOptionClick(${index}, ${origIdx})"`;
            return `
                <div class="${optionClasses.join(' ')}" 
                     ${onclickHandler}
                     data-option-idx="${origIdx}"
                     style="pointer-events: ${isAnswered ? 'none' : 'auto'}">
                    ${option}
                    ${isAnswered && origIdx === correctAnswerIndex ? '<span class="correct-indicator">✓</span>' : ''}
                    ${isAnswered && String(origIdx) === selectedAnswerIndex && !isCorrect ? '<span class="incorrect-indicator">✗</span>' : ''}
                </div>
            `;
        }).join('');
        document.getElementById("question-box").innerHTML = `
            <h2>${q.question}</h2>
            <div class="options">
                ${optionsHTML}
            </div>
            <div id="explanation-${index}" class="explanation" style="display: ${isAnswered ? 'block' : 'none'}">
                <p><strong>Correct Answer:</strong> ${q.options[correctAnswerIndex]}</p>
                <p><strong>Explanation:</strong> ${q.explanation || ''}</p>
                ${isAnswered ? `
                    <p class="answer-status">
                        <strong>Your Answer:</strong> 
                        <span class="${isCorrect ? 'correct-text' : 'incorrect-text'}">
                            ${selectedAnswerIndex !== null ? q.options[selectedAnswerIndex] : ''} 
                            ${isCorrect ? '✓' : '✗'}
                        </span>
                    </p>
                ` : ''}
            </div>
        `;
        document.getElementById("prevBtn").disabled = index === 0;
        document.getElementById("nextBtn").disabled = index === questions.length - 1;
        document.getElementById("finishBtn").disabled = false;
        updateUnansweredSidebar();
    } catch (error) {
        document.getElementById("question-box").innerHTML = `<h2>Error Loading Question</h2><p>There was an error loading this question: ${error.message}</p><button onclick="location.reload()">Refresh Page</button>`;
        document.getElementById("prevBtn").disabled = true;
        document.getElementById("nextBtn").disabled = true;
        document.getElementById("finishBtn").disabled = true;
    }
}

// Initialize unanswered questions
function initializeUnansweredQuestions() {
    console.log('Initializing unanswered questions...');
    console.log('Total questions available:', questions.length);
    console.log('Questions array:', questions);
    
    unansweredQuestions.clear();
    answeredQuestions.clear();
    
    // Add all questions to unanswered set
    for (let i = 0; i < questions.length; i++) {
        unansweredQuestions.add(i);
        console.log(`Added question ${i + 1} to unanswered set`);
    }
    
    console.log('Unanswered questions initialized:', Array.from(unansweredQuestions));
    console.log('Total unanswered questions:', unansweredQuestions.size);
    updateUnansweredSidebar();
}

function updateUnansweredSidebar() {
    const sidebar = document.querySelector('.unanswered-list');
    const count = document.querySelector('.unanswered-count');
    
    // Update count
    count.textContent = unansweredQuestions.size;
    console.log('Updating sidebar. Total questions:', questions.length);
    console.log('Unanswered questions:', Array.from(unansweredQuestions));
    
    // Create list of all questions, not just unanswered ones
    sidebar.innerHTML = Array.from({ length: questions.length }, (_, i) => {
        const isUnanswered = unansweredQuestions.has(i);
        const isCurrent = i === currentIndex;
        console.log(`Question ${i + 1}: isUnanswered=${isUnanswered}, isCurrent=${isCurrent}`);
        return `
            <div class="unanswered-item ${isCurrent ? 'current' : ''} ${isUnanswered ? 'unanswered' : 'answered'}" 
                 onclick="goToQuestion(${i})">
                Question ${i + 1}
            </div>
        `;
    }).join('');
}

// New function to go directly to a specific question
function goToQuestion(index) {
    if (index >= 0 && index < questions.length) {
        currentIndex = index;
        renderQuestion(currentIndex);
    }
}

function updateScore() {
    currentScore++;
    document.querySelector('.score-display .score').textContent = currentScore;
}

// New function to handle option clicks
function handleOptionClick(questionIndex, selectedOptionIdx) {
    if (answeredQuestions.has(questionIndex)) return;
    checkAnswer(questionIndex, selectedOptionIdx);
}

function checkAnswer(questionIndex, selectedAnswerIdx) {
    if (answeredQuestions.has(questionIndex)) return;
    const question = questions[questionIndex];
    const isCorrect = Number(selectedAnswerIdx) === question.answer;
    localStorage.setItem(`selected_answer_${questionIndex}`, String(selectedAnswerIdx));
    localStorage.setItem(`is_correct_${questionIndex}`, isCorrect.toString());
    answeredQuestions.add(questionIndex);
    unansweredQuestions.delete(questionIndex);
    if (isCorrect) updateScore();
    renderQuestion(questionIndex);
}

let celebrationInterval = null;
let audioInterval = null;

function cleanupCelebration() {
    // Clear all intervals
    if (celebrationInterval) {
        clearInterval(celebrationInterval);
        celebrationInterval = null;
    }
    if (audioInterval) {
        clearInterval(audioInterval);
        audioInterval = null;
    }

    // Remove all effects
    document.querySelectorAll('.confetti-container, .firecracker, .spark').forEach(e => e.remove());

    // Stop and reset audio
    const audio = document.getElementById('winnerAudio');
    audio.pause();
    audio.currentTime = 0;
}

function createConfetti() {
    // Remove existing confetti container if any
    const existingContainer = document.querySelector('.confetti-container');
    if (existingContainer) {
        existingContainer.remove();
    }

    // Create new container
    const container = document.createElement('div');
    container.className = 'confetti-container';
    document.body.appendChild(container);

    const colors = ['#f00', '#0f0', '#00f', '#ff0', '#f0f', '#0ff'];
    const width = window.innerWidth;

    // Create more confetti for better coverage
    for (let i = 0; i < 200; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        // Distribute confetti across the entire width
        const x = Math.random() * width;
        confetti.style.setProperty('--x', `${x}px`);
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = Math.random() * 3 + 's';
        container.appendChild(confetti);
    }
}

function createFirecrackers() {
    const colors = ['#ff0000', '#ffd700', '#ff69b4', '#00ff00', '#ff4500', '#ffa500'];
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;
    const spread = 200; // Reduced spread for more centered effect

    // Create multiple firecrackers at different positions
    for (let i = 0; i < 5; i++) {
        const x = centerX + (Math.random() - 0.5) * spread;
        const y = centerY + (Math.random() - 0.5) * spread;

        // Create the main explosion
        const firecracker = document.createElement('div');
        firecracker.className = 'firecracker';
        firecracker.style.setProperty('--x', `${x}px`);
        firecracker.style.setProperty('--y', `${y}px`);
        firecracker.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        document.body.appendChild(firecracker);

        // Create sparks
        for (let j = 0; j < 12; j++) {
            const spark = document.createElement('div');
            spark.className = 'spark';
            spark.style.setProperty('--x', `${x}px`);
            spark.style.setProperty('--y', `${y}px`);
            spark.style.setProperty('--angle', `${j * 30}deg`);
            spark.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            document.body.appendChild(spark);
        }

        // Remove elements after animation
        setTimeout(() => {
            firecracker.remove();
            document.querySelectorAll('.spark').forEach(s => s.remove());
        }, 1000);
    }
}

function showWinnerPopup() {
    // Clean up any existing celebration first
    cleanupCelebration();

    const popup = document.getElementById('winnerPopup');
    document.getElementById('finalScore').textContent = currentScore;
    document.getElementById('totalQuestions').textContent = questions.length;
    // Add percentage and score/total display
    const percent = questions.length > 0 ? Math.round((currentScore / questions.length) * 100) : 0;
    let extraInfo = document.getElementById('finalExtraInfo');
    if (!extraInfo) {
        extraInfo = document.createElement('div');
        extraInfo.id = 'finalExtraInfo';
        extraInfo.style.fontSize = '28px';
        extraInfo.style.color = '#00b894';
        extraInfo.style.margin = '20px 0 0 0';
        document.getElementById('finalScore').after(extraInfo);
    }
    extraInfo.innerHTML = `Score: <b>${currentScore}</b> / <b>${questions.length}</b><br>Percentage: <b>${percent}%</b>`;

    // Play audio and show popup
    const audio = document.getElementById('winnerAudio');
    audio.currentTime = 0;

    // Start the celebration
    popup.style.display = 'flex';

    // Initial effects
    createConfetti();
    createFirecrackers();

    // Set up celebration interval
    let timeElapsed = 0;
    celebrationInterval = setInterval(() => {
        timeElapsed += 2;

        if (timeElapsed <= 10) {
            createFirecrackers();
            if (timeElapsed % 3 === 0) {
                createConfetti();
            }
        } else {
            cleanupCelebration();
        }
    }, 2000);

    // Set up audio loop
    const playAudio = () => {
        audio.currentTime = 0;
        audio.play().catch(e => console.log("Audio play failed:", e));
    };

    playAudio(); // Play first time
    audioInterval = setInterval(playAudio, 3000); // Loop every 3 seconds

    // Stop everything after 10 seconds
    setTimeout(cleanupCelebration, 10000);
}

function resetContest() {
    // Clean up celebration
    cleanupCelebration();

    // Clear stored answers
    for (let i = 0; i < questions.length; i++) {
        localStorage.removeItem(`selected_answer_${i}`);
        localStorage.removeItem(`is_correct_${i}`);
    }

    // Reset score and questions
    currentScore = 0;
    answeredQuestions.clear();
    document.querySelector('.score-display .score').textContent = '0';
    initializeUnansweredQuestions();

    // Hide popup
    const popup = document.getElementById('winnerPopup');
    popup.style.display = 'none';

    // Reset to first question
    currentIndex = 0;
    renderQuestion(currentIndex);
}

function finishContest() {
    if (confirm("Are you sure you want to finish the contest and announce the winner?")) {
        showWinnerPopup();
    }
}

function changeQuestion(direction) {
    const newIndex = currentIndex + direction;
    if (newIndex >= 0 && newIndex < questions.length) {
        goToQuestion(newIndex);
    }
}

// Initial render
renderQuestion(currentIndex);

// Initialize unanswered questions when the page loads
window.addEventListener('load', initializeUnansweredQuestions);

// Clean up on page unload
window.addEventListener('beforeunload', cleanupCelebration);

// Theme Management
function toggleTheme() {
    const body = document.body;
    const themeToggle = document.querySelector('.theme-toggle');
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    // Add transition class
    body.style.transition = 'background-color 0.5s ease, color 0.5s ease';
    
    // Update theme
    body.setAttribute('data-theme', newTheme);
    themeToggle.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Remove transition class after animation
    setTimeout(() => {
        body.style.transition = '';
    }, 500);
}

// Load saved theme with animation
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    const themeToggle = document.querySelector('.theme-toggle');
    document.body.setAttribute('data-theme', savedTheme);
    themeToggle.setAttribute('data-theme', savedTheme);
}

// Keyboard Shortcuts
document.addEventListener('keydown', function (e) {
    // Don't trigger shortcuts if user is typing in an input, textarea, or code block
    if (e.target.tagName === 'INPUT' ||
        e.target.tagName === 'TEXTAREA' ||
        e.target.tagName === 'PRE' ||
        e.target.closest('pre') !== null) {
        return;
    }

    // Don't trigger shortcuts if user is holding modifier keys
    if (e.ctrlKey || e.altKey || e.metaKey || e.shiftKey) {
        return;
    }

    // Check if current question is already answered
    const isCurrentQuestionAnswered = answeredQuestions.has(currentIndex);

    switch (e.key) {
        case 'ArrowLeft':
            if (!document.getElementById('prevBtn').disabled) {
                changeQuestion(-1);
            }
            break;
        case 'ArrowRight':
            if (!document.getElementById('nextBtn').disabled) {
                changeQuestion(1);
            }
            break;
        case '1':
        case '2':
        case '3':
        case '4':
            // Only allow option selection if question is not answered
            if (!isCurrentQuestionAnswered) {
                const optionIndex = parseInt(e.key) - 1;
                const options = document.querySelectorAll('.option');
                if (options[optionIndex] && !options[optionIndex].classList.contains('disabled')) {
                    options[optionIndex].click();
                }
            }
            break;
        case 'f':
        case 'F':
            if (!document.getElementById('finishBtn').disabled) {
                finishContest();
            }
            break;
        case 't':
        case 'T':
            toggleTheme();
            break;
        case 'h':
        case 'H':
            showDisclaimer();
            break;
    }
});

// Responsive Design Improvements
function updateLayout() {
    const width = window.innerWidth;
    const container = document.querySelector('.container');
    const sidebar = document.querySelector('.unanswered-sidebar');
    const shortcuts = document.querySelector('.keyboard-shortcuts');

    if (width <= 768) {
        container.style.margin = '10px';
        container.style.padding = '15px';
        if (sidebar) {
            sidebar.style.position = 'static';
            sidebar.style.width = 'auto';
            sidebar.style.margin = '20px 0';
        }
        if (shortcuts) {
            shortcuts.style.display = 'none';
        }
    } else if (width <= 1200) {
        container.style.margin = '20px';
        container.style.padding = '20px';
        if (sidebar) {
            sidebar.style.position = 'fixed';
            sidebar.style.width = '220px';
        }
        if (shortcuts) {
            shortcuts.style.display = 'block';
        }
    } else {
        container.style.margin = 'auto';
        container.style.marginRight = '250px';
        container.style.marginLeft = '100px';
        if (sidebar) {
            sidebar.style.position = 'fixed';
            sidebar.style.width = '220px';
        }
        if (shortcuts) {
            shortcuts.style.display = 'block';
        }
    }
}

// Initial layout update
updateLayout();

// Update layout on window resize
window.addEventListener('resize', updateLayout);

// Disclaimer Management
function showDisclaimer() {
    const modal = document.getElementById('disclaimerModal');
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden'; // Prevent scrolling when modal is open
    
    // Add click event to close modal when clicking outside
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            hideDisclaimer();
        }
    });

    // Add keyboard event to close modal with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            hideDisclaimer();
        }
    });
}

function hideDisclaimer() {
    const modal = document.getElementById('disclaimerModal');
    modal.style.display = 'none';
    document.body.style.overflow = ''; // Restore scrolling
    
    // Save that disclaimer has been shown
    localStorage.setItem('disclaimerShown', 'true');
}

// Show disclaimer on page load if not shown before
window.addEventListener('load', () => {
    initializeUnansweredQuestions();
    
    // Show disclaimer if it hasn't been shown before
    if (!localStorage.getItem('disclaimerShown')) {
        showDisclaimer();
    }
});

// Modify the showWinnerPopup function to show disclaimer after results
const originalShowWinnerPopup = showWinnerPopup;
showWinnerPopup = function () {
    originalShowWinnerPopup();
    // Show disclaimer after a short delay
    setTimeout(() => {
        showDisclaimer();
    }, 2000);
};

// Add keyboard shortcut to show disclaimer
document.addEventListener('keydown', function (e) {
    if (e.key === 'h' || e.key === 'H') {
        showDisclaimer();
    }
});

// Update keyboard shortcuts panel to include help shortcut
document.querySelector('.keyboard-shortcuts').insertAdjacentHTML('beforeend', `
    <div class="shortcut-item">
        <span>Show Features</span>
        <span class="key">H</span>
    </div>
`);

// Add keyboard shortcuts toggle functionality
function toggleShortcuts() {
    const shortcuts = document.querySelector('.keyboard-shortcuts');
    const fab = document.querySelector('.shortcut-fab');
    shortcuts.classList.toggle('visible');
    fab.classList.toggle('active');
}

// Close shortcuts when clicking outside
document.addEventListener('click', function (event) {
    const shortcuts = document.querySelector('.keyboard-shortcuts');
    const fab = document.querySelector('.shortcut-fab');
    if (!shortcuts.contains(event.target) && !fab.contains(event.target)) {
        shortcuts.classList.remove('visible');
        fab.classList.remove('active');
    }
});

// Add keyboard shortcut to toggle shortcuts panel
document.addEventListener('keydown', function (e) {
    if (e.key === 'k' || e.key === 'K') {
        toggleShortcuts();
    }
});

// Add click handlers for feature buttons
document.addEventListener('DOMContentLoaded', function() {
    const features = document.querySelectorAll('.disclaimer-feature');
    features.forEach(feature => {
        feature.addEventListener('click', function() {
            const action = this.getAttribute('data-action');
            if (action === 'save') {
                showSaveModal();
                hideDisclaimer();
            } else if (action === 'load') {
                showLoadModal();
                hideDisclaimer();
            } else if (action === 'export') {
                showExportModal();
                hideDisclaimer();
            }
        });
    });
});

function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);

    // Trigger animation
    setTimeout(() => toast.classList.add('show'), 100);

    // Remove toast after 3 seconds
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Add toast styles
const style = document.createElement('style');
style.textContent = `
    .toast {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%) translateY(100px);
        background: var(--container-bg);
        color: var(--text-color);
        padding: 15px 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        z-index: 3000;
        opacity: 0;
        transition: all 0.3s ease;
        border: 2px solid var(--button-gradient);
    }

    .toast.show {
        transform: translateX(-50%) translateY(0);
        opacity: 1;
    }

    .toast-success {
        border-color: var(--correct-gradient);
    }

    .toast-error {
        border-color: var(--incorrect-gradient);
    }

    .no-saves {
        text-align: center;
        padding: 20px;
        color: var(--text-color);
        font-size: 16px;
        background: var(--option-bg);
        border-radius: 12px;
        border: 1px solid var(--option-border);
    }
`;
document.head.appendChild(style);