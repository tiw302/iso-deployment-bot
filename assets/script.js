document.addEventListener('DOMContentLoaded', () => {
    // search & empty state
    const searchInput = document.getElementById('searchInput');
    const sections = document.querySelectorAll('.category-section');
    const emptyState = document.getElementById('emptyState');
    let currentTab = 'library';

    // focus search input when clicking anywhere on the search wrapper
    const searchWrapper = document.querySelector('.search-wrapper');
    if (searchWrapper && searchInput) {
        searchWrapper.addEventListener('click', (e) => {
            if (e.target !== searchInput) {
                searchInput.focus();
            }
        });
        // set initial has-value state for restored values
        searchWrapper.classList.toggle('has-value', searchInput.value.trim() !== '');
    }

    // custom autocomplete
    const autocompleteDropdown = document.getElementById('autocompleteDropdown');
    const allOSNames = Array.from(new Set(Array.from(document.querySelectorAll('.iso-card')).map(card => card.dataset.name)));
    let currentFocus = -1;

    // levenshtein distance for typo tolerance
    function levenshtein(a, b) {
        if (a.length === 0) return b.length;
        if (b.length === 0) return a.length;
        const matrix = [];
        for (let i = 0; i <= b.length; i++) matrix[i] = [i];
        for (let j = 0; j <= a.length; j++) matrix[0][j] = j;
        for (let i = 1; i <= b.length; i++) {
            for (let j = 1; j <= a.length; j++) {
                if (b.charAt(i - 1) === a.charAt(j - 1)) {
                    matrix[i][j] = matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] = Math.min(
                        matrix[i - 1][j - 1] + 1,
                        matrix[i][j - 1] + 1,
                        matrix[i - 1][j] + 1
                    );
                }
            }
        }
        return matrix[b.length][a.length];
    }

    function isMatch(term, name) {
        if (name.includes(term)) return true;

        const words = name.split(/[\s-]+/);
        for (let word of words) {
            const allowedTypos = term.length >= 5 ? 2 : (term.length >= 3 ? 1 : 0);
            if (allowedTypos > 0) {
                const prefix = word.substring(0, term.length);
                if (levenshtein(term, prefix) <= allowedTypos) return true;
            }
        }
        return false;
    }

    if (searchInput) {
        const searchClear = document.getElementById('searchClear');
        if (searchClear) {
            searchClear.addEventListener('click', (e) => {
                e.stopPropagation();
                searchInput.value = '';
                searchClear.style.display = 'none';
                if (autocompleteDropdown) autocompleteDropdown.style.display = 'none';
                searchInput.dispatchEvent(new Event('input'));
                searchInput.focus();
            });
        }

        searchInput.addEventListener('input', (e) => {
            if (currentTab === 'about') return;
            const term = e.target.value.toLowerCase().trim();
            let anyMatch = false;

            if (searchWrapper) {
                searchWrapper.classList.toggle('has-value', term !== '');
            }

            if (searchClear) {
                searchClear.style.display = term !== '' ? 'inline-block' : 'none';
            }

            // reset active filter pill to 'all' on search input to prevent visual desync
            if (term !== '') {
                const pillClass = currentTab === 'library' ? '.lib-pill' : '.disc-pill';
                document.querySelectorAll(pillClass).forEach(p => {
                    p.classList.toggle('active', p.dataset.target === 'all');
                });
            }

            sections.forEach(section => {
                // only search in active tab
                if ((currentTab === 'library' && !section.classList.contains('library-section')) ||
                    (currentTab === 'discovery' && !section.classList.contains('discovery-section'))) {
                    return;
                }

                let hasMatch = false;
                const cards = section.querySelectorAll('.iso-card');

                cards.forEach(card => {
                    const name = card.dataset.name.toLowerCase();
                    let tagsText = '';
                    try {
                        if (card.dataset.details) {
                            const details = JSON.parse(card.dataset.details);
                            if (details.tags && Array.isArray(details.tags)) {
                                tagsText = details.tags.join(' ').toLowerCase();
                            }
                        }
                    } catch (e) {}

                    if (term === '' || isMatch(term, name) || (tagsText && tagsText.includes(term))) {
                        card.style.display = 'flex';
                        hasMatch = true;
                        anyMatch = true;
                    } else {
                        card.style.display = 'none';
                    }
                });

                section.style.display = hasMatch ? 'block' : 'none';
            });

            emptyState.style.display = (!anyMatch && term !== '') ? 'block' : 'none';

            // populate autocomplete dropdown
            currentFocus = -1;
            if (autocompleteDropdown) {
                autocompleteDropdown.innerHTML = '';
                if (term !== '') {
                    const activeCards = document.querySelectorAll(currentTab === 'library' ? '.library-section .iso-card' : '.discovery-section .iso-card');
                    const tabOSNames = Array.from(new Set(Array.from(activeCards).map(card => card.dataset.name)));
                    const matches = tabOSNames.filter(name => isMatch(term, name.toLowerCase()));
                    if (matches.length > 0) {
                        autocompleteDropdown.style.display = 'block';
                        // limit to top 10 suggestions
                        matches.slice(0, 10).forEach(match => {
                            const item = document.createElement('div');
                            item.className = 'autocomplete-item';
                            item.textContent = match;
                            item.addEventListener('click', () => {
                                searchInput.value = match;
                                autocompleteDropdown.style.display = 'none';
                                searchInput.dispatchEvent(new Event('input'));
                            });
                            autocompleteDropdown.appendChild(item);
                        });
                    } else {
                        autocompleteDropdown.style.display = 'none';
                    }
                } else {
                    autocompleteDropdown.style.display = 'none';
                }
            }
        });

        // hide dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (autocompleteDropdown && !searchInput.contains(e.target) && !autocompleteDropdown.contains(e.target)) {
                autocompleteDropdown.style.display = 'none';
            }
        });

        // keydown support for arrows, enter, and escape
        searchInput.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                if (autocompleteDropdown) autocompleteDropdown.style.display = 'none';
                return;
            }
            if (!autocompleteDropdown || autocompleteDropdown.style.display === 'none') return;
            const items = autocompleteDropdown.getElementsByClassName('autocomplete-item');
            if (items.length === 0) return;

            if (e.key === 'ArrowDown') {
                e.preventDefault();
                currentFocus++;
                addActive(items);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                currentFocus--;
                addActive(items);
            } else if (e.key === 'Enter') {
                if (currentFocus > -1) {
                    e.preventDefault();
                    items[currentFocus].click();
                }
            }
        });

        function addActive(items) {
            if (!items) return false;
            removeActive(items);
            if (currentFocus >= items.length) currentFocus = 0;
            if (currentFocus < 0) currentFocus = items.length - 1;
            items[currentFocus].classList.add('selected');
            items[currentFocus].scrollIntoView({ block: 'nearest' });
        }

        function removeActive(items) {
            for (let i = 0; i < items.length; i++) {
                items[i].classList.remove('selected');
            }
        }

        // show dropdown on focus if there are matches
        searchInput.addEventListener('focus', () => {
            if (autocompleteDropdown && searchInput.value.trim() !== '' && autocompleteDropdown.children.length > 0) {
                autocompleteDropdown.style.display = 'block';
            }
        });
    }

    // tabs
    const tabs = ['library', 'discovery', 'about'];
    const tabButtons = {
        library: document.getElementById('libTab'),
        discovery: document.getElementById('discTab'),
        about: document.getElementById('aboutTab')
    };
    const tabContents = {
        library: document.getElementById('libraryContent'),
        discovery: document.getElementById('discoveryContent'),
        about: document.getElementById('aboutContent')
    };

    function switchTab(tab) {
        currentTab = tab;
        tabs.forEach(t => {
            const btn = tabButtons[t];
            const content = tabContents[t];
            if (btn) btn.classList.toggle('active', t === tab);
            if (content) content.style.display = t === tab ? 'block' : 'none';
        });

        const searchContainer = document.getElementById('searchContainer');
        if (searchContainer) {
            searchContainer.style.display = tab === 'about' ? 'none' : 'block';
        }

        if (tab !== 'about') {
            document.getElementById('searchPrompt').innerText = tab === 'library' ? "user@linux:~$ search library" : "user@linux:~$ search discovery";
            if (searchInput && searchInput.value) {
                searchInput.dispatchEvent(new Event('input'));
            }
            updateArrows(tab === 'library' ? 'libNav' : 'discNav');
        }
    }

    Object.keys(tabButtons).forEach(tab => {
        const btn = tabButtons[tab];
        if (btn) {
            btn.addEventListener('click', () => switchTab(tab));
        }
    });

    // filters
    window.filterContent = function (type, categoryId) {
        const sectionClass = type === 'lib' ? '.library-section' : '.discovery-section';
        const pillClass = type === 'lib' ? '.lib-pill' : '.disc-pill';
        const targetSections = document.querySelectorAll(sectionClass);
        const pills = document.querySelectorAll(pillClass);

        pills.forEach(p => p.classList.toggle('active', p.dataset.target === categoryId));

        targetSections.forEach(s => {
            if (categoryId === 'all') {
                s.style.display = 'block';
            } else {
                s.style.display = s.id === categoryId ? 'block' : 'none';
            }
        });

        // reset search
        searchInput.value = '';
        emptyState.style.display = 'none';

        // show all cards inside the sections
        targetSections.forEach(s => {
            s.querySelectorAll('.iso-card').forEach(c => c.style.display = 'flex');
        });
    };

    // nav arrows
    function updateArrows(navId) {
        const nav = document.getElementById(navId);
        const leftArrow = document.getElementById(navId === 'libNav' ? 'libArrowLeft' : 'discArrowLeft');
        const rightArrow = document.getElementById(navId === 'libNav' ? 'libArrowRight' : 'discArrowRight');
        if (!nav || !leftArrow || !rightArrow) return;
        const isScrollable = nav.scrollWidth > nav.clientWidth;
        if (!isScrollable) {
            leftArrow.style.display = 'none';
            rightArrow.style.display = 'none';
            return;
        }
        leftArrow.style.display = nav.scrollLeft > 5 ? 'flex' : 'none';
        rightArrow.style.display = (nav.scrollLeft + nav.clientWidth < nav.scrollWidth - 5) ? 'flex' : 'none';
    }

    ['libNav', 'discNav'].forEach(id => {
        const nav = document.getElementById(id);
        const leftArrow = document.getElementById(id === 'libNav' ? 'libArrowLeft' : 'discArrowLeft');
        const rightArrow = document.getElementById(id === 'libNav' ? 'libArrowRight' : 'discArrowRight');
        if (!nav) return;
        leftArrow.onclick = () => nav.scrollBy({ left: -200, behavior: 'smooth' });
        rightArrow.onclick = () => nav.scrollBy({ left: 200, behavior: 'smooth' });
        nav.addEventListener('wheel', (e) => {
            if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
                e.preventDefault();
                nav.scrollLeft += e.deltaY;
            }
        });
        nav.addEventListener('scroll', () => updateArrows(id));
        setTimeout(() => updateArrows(id), 100);
    });

    window.addEventListener('resize', () => {
        updateArrows('libNav');
        updateArrows('discNav');
    });

    // theme toggle with localstorage persistence
    const themes = ['dark', 'light'];
    const savedTheme = localStorage.getItem('theme') || 'dark';
    let currentThemeIndex = themes.indexOf(savedTheme);
    if (currentThemeIndex === -1) currentThemeIndex = 0;

    const themeToggle = document.getElementById('themeToggle');
    const themeLabel = document.getElementById('themeLabel');
    const htmlElement = document.documentElement;

    // set initial label based on current state
    if (themeLabel) themeLabel.innerText = `theme: ${savedTheme}`;

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            currentThemeIndex = (currentThemeIndex + 1) % themes.length;
            const newTheme = themes[currentThemeIndex];
            htmlElement.setAttribute('data-theme', newTheme);
            themeLabel.innerText = `theme: ${newTheme}`;
            localStorage.setItem('theme', newTheme);
        });
    }

    // back to top & scroll cat
    const backToTopBtn = document.getElementById('backToTop');
    const scrollCat = document.getElementById('scrollCat');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.style.display = 'flex';
            if (scrollCat) scrollCat.classList.add('raised');
        } else {
            backToTopBtn.style.display = 'none';
            if (scrollCat) scrollCat.classList.remove('raised');
        }
    });
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    if (scrollCat) {
        const catBubble = document.getElementById('catBubble');
        const catAnim = document.getElementById('catAnim');
        const meows = [
            "[ meow! ]",
            "[ nya~ ]",
            "[ *purr* ]",
            "[ *sniff sniff* ]",
            "[ miau~ ]",
            "[ *happy purring* ]",
            "[ rawr! ]",
            "[ *blink* ]"
        ];
        
        // ascii facial animation frames (no paws)
        const animFrames = [
            // frame 1: squinting eyes prep
`  /\\_/\\
 ( >.< )
  > ^ <`,
            // frame 2: happy, mouth open
`  /\\_/\\
 ( ^o^ )
  > ^ <`,
            // frame 3: meowing, wide mouth open
`  /\\_/\\
 ( ^O^ )
  > ^ <`,
            // frame 4: wink
`  /\\_/\\
 ( ^.~ )
  > ^ <`,
            // frame 5: happy face
`  /\\_/\\
 ( ^.^ )
  > ^ <`
        ];

        let isAnimating = false;
        
        scrollCat.addEventListener('click', () => {
            if (isAnimating) return;
            isAnimating = true;
            
            const randomMeow = meows[Math.floor(Math.random() * meows.length)];
            if (catBubble) {
                catBubble.textContent = randomMeow;
            }
            
            scrollCat.classList.add('animating');
            scrollCat.classList.add('meowing');
            
            let frameIndex = 0;
            if (catAnim) {
                catAnim.textContent = animFrames[0];
            }
            
            const frameInterval = setInterval(() => {
                frameIndex++;
                if (frameIndex < animFrames.length) {
                    if (catAnim) {
                        catAnim.textContent = animFrames[frameIndex];
                    }
                } else {
                    clearInterval(frameInterval);
                    setTimeout(() => {
                        scrollCat.classList.remove('animating');
                        scrollCat.classList.remove('meowing');
                        isAnimating = false;
                    }, 300);
                }
            }, 120);
        });
    }

    // copy links
    const toast = document.getElementById('toast');
    const checkIcon = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;

    document.querySelectorAll('.btn-copy').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const url = btn.dataset.url;
            navigator.clipboard.writeText(url).then(() => {
                const originalHTML = btn.innerHTML;
                btn.innerHTML = checkIcon;
                btn.style.pointerEvents = 'none'; // prevent double clicks during change

                toast.classList.add('show');

                setTimeout(() => {
                    btn.innerHTML = originalHTML;
                    btn.style.pointerEvents = 'auto';
                }, 1500);

                setTimeout(() => toast.classList.remove('show'), 2000);
            });
        });
    });

    // detailed os modal interactivity
    const infoModal = document.getElementById('infoModal');
    const closeModalBtn = document.getElementById('closeModal');
    const modalBody = document.getElementById('modalBody');

    // modal tab switching
    const modalTabsContainer = document.getElementById('modalTabs');
    if (modalTabsContainer) {
        modalTabsContainer.addEventListener('click', (e) => {
            const btn = e.target.closest('.modal-tab-btn');
            if (!btn) return;
            
            const tabName = btn.dataset.modalTab;
            
            // toggle active class on tab buttons
            document.querySelectorAll('.modal-tab-btn').forEach(b => {
                b.classList.toggle('active', b === btn);
            });
            
            // toggle visibility on bodies
            document.getElementById('modalBody').style.display = tabName === 'info' ? 'block' : 'none';
            document.getElementById('modalWget').style.display = tabName === 'wget' ? 'block' : 'none';
            document.getElementById('modalCurl').style.display = tabName === 'curl' ? 'block' : 'none';
            document.getElementById('modalProxmox').style.display = tabName === 'proxmox' ? 'block' : 'none';
        });
    }

    function openModal(card) {
        if (!infoModal || !modalBody || !card.dataset.details) return;
        
        let details;
        try {
            details = JSON.parse(card.dataset.details);
        } catch (e) {
            console.error("Failed to parse OS details:", e);
            return;
        }

        const isDiscovery = card.classList.contains('discovery-card');
        const modalTabs = document.getElementById('modalTabs');
        if (modalTabs) {
            modalTabs.style.display = isDiscovery ? 'none' : 'flex';
        }

        // reset tabs in modal
        const modalTabBtns = document.querySelectorAll('.modal-tab-btn');
        modalTabBtns.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.modalTab === 'info');
        });
        
        document.getElementById('modalBody').style.display = 'block';
        document.getElementById('modalWget').style.display = 'none';
        document.getElementById('modalCurl').style.display = 'none';
        document.getElementById('modalProxmox').style.display = 'none';

        // build terminal-style modal layout
        let html = `
            <div class="detail-row">
                <span class="detail-label">[system_name]</span>
                <span class="detail-val">${details.name}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">[developer]</span>
                <span class="detail-val">${details.developer}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">[os_type]</span>
                <span class="detail-val">${details.type}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">[credentials]</span>
                <span class="detail-val">${details.default_user}</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">[references]</span>
                <span class="detail-val"><a href="${details.docs}" target="_blank">${details.docs}</a></span>
            </div>
        `;

        if (details.sha256) {
            html += `
                <div class="detail-row">
                    <span class="detail-label">[sha256]</span>
                    <span class="detail-val" style="word-break: break-all; font-size: 0.75rem;">${details.sha256}</span>
                </div>
            `;
        }

        html += `
            <div class="detail-divider"></div>
            <div class="detail-section-title">[description]</div>
            <div class="detail-block">${details.description}</div>
        `;

        if (details.notes) {
            html += `
                <div class="detail-section-title">[deployment_notes]</div>
                <div class="detail-block">${details.notes}</div>
            `;
        }

        modalBody.innerHTML = html;

        // generate copyable commands
        const copyBtn = card.querySelector('.btn-copy');
        const downloadUrl = copyBtn ? copyBtn.dataset.url : '';
        const filename = details.filename || (details.name.toLowerCase().replace(/[^a-z0-9]+/g, '_') + '.iso');

        // wget command
        const wgetCmd = `wget -O ${filename} "${downloadUrl}"`;
        document.getElementById('modalWget').innerHTML = `
            <div class="command-desc">run this command to download the iso using wget:</div>
            <div class="command-container">
                <pre class="command-block" id="wgetCmdText">${wgetCmd}</pre>
                <button class="command-copy-btn" data-target="wgetCmdText">copy</button>
            </div>
        `;

        // curl command
        const curlCmd = `curl -L -o ${filename} "${downloadUrl}"`;
        document.getElementById('modalCurl').innerHTML = `
            <div class="command-desc">run this command to download the iso using curl:</div>
            <div class="command-container">
                <pre class="command-block" id="curlCmdText">${curlCmd}</pre>
                <button class="command-copy-btn" data-target="curlCmdText">copy</button>
            </div>
        `;

        // proxmox import command
        const proxmoxCmd = `wget -O /var/lib/vz/template/iso/${filename} "${downloadUrl}"`;
        document.getElementById('modalProxmox').innerHTML = `
            <div class="command-desc">run this command in your proxmox shell to download the iso directly into the local iso directory:</div>
            <div class="command-container">
                <pre class="command-block" id="proxmoxCmdText">${proxmoxCmd}</pre>
                <button class="command-copy-btn" data-target="proxmoxCmdText">copy</button>
            </div>
        `;

        // attach event listeners to command copy buttons
        document.querySelectorAll('.command-copy-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const targetId = btn.dataset.target;
                const text = document.getElementById(targetId).textContent;
                navigator.clipboard.writeText(text).then(() => {
                    const originalText = btn.textContent;
                    btn.textContent = 'copied!';
                    btn.style.color = '#22c55e';
                    btn.style.borderColor = '#22c55e';
                    setTimeout(() => {
                        btn.textContent = originalText;
                        btn.style.color = '';
                        btn.style.borderColor = '';
                    }, 1500);
                });
            });
        });

        // open native dialog
        infoModal.showModal();
        // trigger style transition
        setTimeout(() => infoModal.classList.add('show'), 10);
    }

    function closeModal() {
        if (!infoModal) return;
        infoModal.classList.remove('show');
        setTimeout(() => {
            infoModal.close();
        }, 250); // match css transition time
    }

    // attach click listener on all card bodies
    document.querySelectorAll('.iso-card').forEach(card => {
        card.addEventListener('click', (e) => {
            // if the user clicked a copy button, a download link, or an svg inside them, do not open the modal
            if (e.target.closest('.btn-copy') || e.target.closest('.btn-download')) {
                return;
            }
            openModal(card);
        });
    });

    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', closeModal);
    }

    // close on click outside modal content
    if (infoModal) {
        infoModal.addEventListener('click', (e) => {
            if (e.target === infoModal) {
                closeModal();
            }
        });
    }

    // escape key listener for closing modal
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            if (infoModal && infoModal.classList.contains('show')) {
                closeModal();
            }
        }
    });

    // global shortcut to focus search input (press '/' key)
    document.addEventListener('keydown', (e) => {
        const activeElement = document.activeElement;
        const isInputActive = activeElement && (activeElement.tagName === 'INPUT' || activeElement.tagName === 'TEXTAREA');

        if (e.key === '/' && !isInputActive) {
            e.preventDefault();
            if (searchInput) {
                searchInput.focus();
            }
        }
    });

    // ascii logo glitch animation
    const asciiLogo = document.querySelector('pre.ascii-art');
    if (asciiLogo) {
        let isGlitching = false;
        const originalText = asciiLogo.textContent;
        const chars = '$#@%&?*+/|{}[]';

        asciiLogo.style.cursor = 'pointer';
        asciiLogo.title = 'Click to run diagnostics';

        asciiLogo.addEventListener('click', () => {
            if (isGlitching) return;
            isGlitching = true;

            let duration = 600; // ms
            let interval = 40; // ms
            let elapsed = 0;

            const timer = setInterval(() => {
                elapsed += interval;
                if (elapsed >= duration) {
                    clearInterval(timer);
                    asciiLogo.textContent = originalText;
                    isGlitching = false;
                    return;
                }

                const progress = elapsed / duration;
                let newText = '';
                for (let i = 0; i < originalText.length; i++) {
                    const char = originalText[i];
                    if (char === '\n' || char === ' ') {
                        newText += char;
                    } else if (char === '#' || char === '/' || char === '\\' || char === '_' || char === '(' || char === ')' || char === '<' || char === '>' || char === '^' || char === '.') {
                        if (Math.random() < 0.15 * (1 - progress)) {
                            newText += chars[Math.floor(Math.random() * chars.length)];
                        } else {
                            newText += char;
                        }
                    } else {
                        if (Math.random() < 0.6 * (1 - progress)) {
                            newText += chars[Math.floor(Math.random() * chars.length)];
                        } else {
                            newText += char;
                        }
                    }
                }
                asciiLogo.textContent = newText;
            }, interval);
        });
    }

    // dynamic tag coloring
    function colorizeTags() {
        function getHash(str) {
            let hash = 0;
            for (let i = 0; i < str.length; i++) {
                hash = str.charCodeAt(i) + ((hash << 5) - hash);
            }
            return Math.abs(hash);
        }
        
        document.querySelectorAll('.tag-badge').forEach(tag => {
            const text = tag.textContent.trim().toLowerCase();
            const hue = getHash(text) % 360;
            tag.style.setProperty('--tag-hue', hue);
        });
    }
    colorizeTags();
});
