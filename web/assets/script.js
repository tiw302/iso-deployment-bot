const searchInput = document.getElementById('searchInput');
const sections = document.querySelectorAll('.category-section');

if (searchInput) {
    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        
        sections.forEach(section => {
            let hasMatch = false;
            const cards = section.querySelectorAll('.iso-card');
            
            cards.forEach(card => {
                const name = card.dataset.name.toLowerCase();
                if (name.includes(term)) {
                    card.style.display = 'flex';
                    hasMatch = true;
                } else {
                    card.style.display = 'none';
                }
            });
            
            // show/hide category title based on matches
            section.style.display = hasMatch ? 'block' : 'none';
        });
    });
}
