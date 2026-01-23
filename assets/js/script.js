document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeToggle = document.getElementById('theme-toggle');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
    } else if (prefersDarkScheme.matches) {
        document.documentElement.setAttribute('data-theme', 'dark');
    }

    themeToggle.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        if (theme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        }
    });

    // Search and Filter
    const searchInput = document.getElementById('search-input');
    const difficultyFilter = document.getElementById('difficulty-filter');
    const topicFilter = document.getElementById('topic-filter');
    const tableRows = document.querySelectorAll('#problems-table tbody tr');

    function filterProblems() {
        const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
        const difficulty = difficultyFilter ? difficultyFilter.value : 'all';
        const topic = topicFilter ? topicFilter.value : 'all';

        tableRows.forEach(row => {
            const title = row.querySelector('.problem-title').textContent.toLowerCase();
            const rowDifficulty = row.getAttribute('data-difficulty');
            const rowTopics = row.getAttribute('data-topics');

            const matchesSearch = title.includes(searchTerm);
            const matchesDifficulty = difficulty === 'all' || rowDifficulty === difficulty;
            const matchesTopic = topic === 'all' || rowTopics.includes(topic);

            if (matchesSearch && matchesDifficulty && matchesTopic) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    if (searchInput) searchInput.addEventListener('input', filterProblems);
    if (difficultyFilter) difficultyFilter.addEventListener('change', filterProblems);
    if (topicFilter) topicFilter.addEventListener('change', filterProblems);
});
