document.addEventListener('DOMContentLoaded', () => {
    // search & empty state
    const searchInput = document.getElementById('searchInput');
    const sections = document.querySelectorAll('.category-section');
    const emptyState = document.getElementById('emptyState');
    let currentTab = 'library';

    // modal commands and typing timer
    let currentModalCommands = {};
    let typingTimer = null;
    let focusedCardIndex = -1;
    let searchTimeout = null;

    // cache card search data to avoid dom query/parse on keypress
    document.querySelectorAll('.iso-card').forEach(card => {
        const name = card.dataset.name || '';
        let tagsText = '';
        try {
            if (card.dataset.details) {
                const details = JSON.parse(card.dataset.details);
                if (details.tags && Array.isArray(details.tags)) {
                    tagsText = details.tags.join(' ').toLowerCase();
                }
            }
        } catch (e) {}
        card._searchData = { name, tagsText };
    });

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

    // levenshtein distance for typo tolerance (optimized early-exit version)
    function levenshtein(a, b, maxDist) {
        const lenA = a.length;
        const lenB = b.length;
        if (Math.abs(lenA - lenB) > maxDist) return maxDist + 1;
        
        let prev = Array(lenB + 1);
        let curr = Array(lenB + 1);
        
        for (let j = 0; j <= lenB; j++) prev[j] = j;
        
        for (let i = 1; i <= lenA; i++) {
            curr[0] = i;
            let rowMin = curr[0];
            for (let j = 1; j <= lenB; j++) {
                if (a.charAt(i - 1) === b.charAt(j - 1)) {
                    curr[j] = prev[j - 1];
                } else {
                    curr[j] = Math.min(prev[j - 1] + 1, curr[j - 1] + 1, prev[j] + 1);
                }
                if (curr[j] < rowMin) rowMin = curr[j];
            }
            if (rowMin > maxDist) return maxDist + 1;
            
            // swap rows
            const temp = prev;
            prev = curr;
            curr = temp;
        }
        return prev[lenB];
    }

    function isMatch(term, name) {
        if (name.includes(term)) return true;

        const words = name.split(/[\s-]+/);
        for (let word of words) {
            const allowedTypos = term.length >= 5 ? 2 : (term.length >= 3 ? 1 : 0);
            if (allowedTypos > 0) {
                const prefix = word.substring(0, term.length);
                if (levenshtein(term, prefix, allowedTypos) <= allowedTypos) return true;
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

            if (searchWrapper) {
                searchWrapper.classList.toggle('has-value', term !== '');
            }

            if (searchClear) {
                searchClear.style.display = term !== '' ? 'inline-block' : 'none';
            }

            if (searchTimeout) clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                let anyMatch = false;

                // clear highlights first
                document.querySelectorAll('.iso-name, .iso-desc').forEach(el => {
                    if (el.dataset.original) {
                        el.innerHTML = el.dataset.original;
                    }
                });

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
                        const searchData = card._searchData || { name: '', tagsText: '' };
                        const name = searchData.name;
                        const tagsText = searchData.tagsText;

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

                if (term !== '') {
                    document.querySelectorAll('.iso-card').forEach(card => {
                        if (card.style.display !== 'none') {
                            const nameEl = card.querySelector('.iso-name');
                            const descEl = card.querySelector('.iso-desc');
                            if (nameEl) highlightHTML(nameEl, term);
                            if (descEl) highlightHTML(descEl, term);
                        }
                    });
                }

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
                                    searchInput.focus();
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
        }, 60); // 60ms debounce to prevent layout thrashing
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
        clearCardFocus();
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

        // show all cards inside the sections and clear highlights/focus
        document.querySelectorAll('.iso-name, .iso-desc').forEach(el => {
            if (el.dataset.original) {
                el.innerHTML = el.dataset.original;
            }
        });
        clearCardFocus();

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
    const COPY_ICON_SVG = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`;

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

    // Event delegation for copy buttons in modal
    if (infoModal) {
        infoModal.addEventListener('click', (e) => {
            const btn = e.target.closest('.command-copy-btn');
            if (!btn) return;
            
            const targetId = btn.dataset.target;
            let text = '';
            if (targetId === 'wgetCmdText') text = currentModalCommands.wget;
            else if (targetId === 'curlCmdText') text = currentModalCommands.curl;
            else if (targetId === 'proxmoxCmdText') text = currentModalCommands.proxmox;
            else {
                const el = document.getElementById(targetId);
                text = el ? el.textContent : '';
            }

            navigator.clipboard.writeText(text).then(() => {
                const originalHTML = btn.innerHTML;
                btn.innerHTML = checkIcon;
                btn.style.color = '#22c55e';
                btn.style.borderColor = '#22c55e';
                btn.style.pointerEvents = 'none';

                toast.classList.add('show');

                setTimeout(() => {
                    btn.innerHTML = originalHTML;
                    btn.style.color = '';
                    btn.style.borderColor = '';
                    btn.style.pointerEvents = 'auto';
                }, 1500);

                setTimeout(() => toast.classList.remove('show'), 2000);
            });
        });
    }

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

            // trigger terminal typing simulation
            if (tabName === 'wget') {
                typeCommand('wgetCmdText', currentModalCommands.wget);
            } else if (tabName === 'curl') {
                typeCommand('curlCmdText', currentModalCommands.curl);
            } else if (tabName === 'proxmox') {
                typeCommand('proxmoxCmdText', currentModalCommands.proxmox);
            }
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

        // reset tabs in modal and cancel active typing timers
        if (typingTimer) clearInterval(typingTimer);
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
                <pre class="command-block"><span class="command-prompt">user@homelab:~$ </span><span class="command-text" id="wgetCmdText">${wgetCmd}</span></pre>
                <button class="command-copy-btn" data-target="wgetCmdText" title="Copy Command">${COPY_ICON_SVG}</button>
            </div>
        `;

        // curl command
        const curlCmd = `curl -L -o ${filename} "${downloadUrl}"`;
        document.getElementById('modalCurl').innerHTML = `
            <div class="command-desc">run this command to download the iso using curl:</div>
            <div class="command-container">
                <pre class="command-block"><span class="command-prompt">user@homelab:~$ </span><span class="command-text" id="curlCmdText">${curlCmd}</span></pre>
                <button class="command-copy-btn" data-target="curlCmdText" title="Copy Command">${COPY_ICON_SVG}</button>
            </div>
        `;

        // proxmox import command
        const proxmoxCmd = `wget -O /var/lib/vz/template/iso/${filename} "${downloadUrl}"`;
        document.getElementById('modalProxmox').innerHTML = `
            <div class="command-desc">run this command in your proxmox shell to download the iso directly into the local iso directory:</div>
            <div class="command-container">
                <pre class="command-block"><span class="command-prompt">user@homelab:~$ </span><span class="command-text" id="proxmoxCmdText">${proxmoxCmd}</span></pre>
                <button class="command-copy-btn" data-target="proxmoxCmdText" title="Copy Command">${COPY_ICON_SVG}</button>
            </div>
        `;

        // save command texts for typing simulator
        currentModalCommands = {
            wget: wgetCmd,
            curl: curlCmd,
            proxmox: proxmoxCmd
        };

        // open native dialog
        infoModal.showModal();
        // trigger style transition
        setTimeout(() => infoModal.classList.add('show'), 10);
    }

    function closeModal() {
        if (!infoModal) return;
        if (typingTimer) clearInterval(typingTimer);
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

    // global keyboard navigation
    document.addEventListener('keydown', (e) => {
        const activeElement = document.activeElement;
        const isInputActive = activeElement && (activeElement.tagName === 'INPUT' || activeElement.tagName === 'TEXTAREA');

        // escape key: close modal or reset focus
        if (e.key === 'Escape') {
            if (infoModal && infoModal.classList.contains('show')) {
                closeModal();
            } else {
                clearCardFocus();
            }
            return;
        }

        // tab key: cycle library / discovery / about tabs when not inputting/modal active
        if (e.key === 'Tab' && !isInputActive && !(infoModal && infoModal.classList.contains('show'))) {
            e.preventDefault();
            const tabOrder = ['library', 'discovery', 'about'];
            let nextIdx = (tabOrder.indexOf(currentTab) + (e.shiftKey ? -1 : 1)) % tabOrder.length;
            if (nextIdx < 0) nextIdx = tabOrder.length - 1;
            switchTab(tabOrder[nextIdx]);
            return;
        }

        // slash key: focus search input on pressing '/'
        if (e.key === '/' && !isInputActive) {
            e.preventDefault();
            if (searchInput) {
                searchInput.focus();
                clearCardFocus();
            }
            return;
        }

        // arrow down in search: move to grid cards
        if (isInputActive) {
            if (e.target === searchInput && e.key === 'ArrowDown') {
                if (!autocompleteDropdown || autocompleteDropdown.style.display === 'none') {
                    e.preventDefault();
                    searchInput.blur();
                    focusCard(0);
                }
            }
            return;
        }

        // arrow/vim navigation for grid selection
        const cards = getVisibleCards();
        if (cards.length === 0) return;

        if (e.key === 'ArrowDown' || e.key === 'j' || e.key === 'J') {
            e.preventDefault();
            if (focusedCardIndex === -1) {
                focusCard(0);
            } else {
                const cols = getGridColumnsCount();
                focusCard(focusedCardIndex + cols);
            }
        } else if (e.key === 'ArrowUp' || e.key === 'k' || e.key === 'K') {
            e.preventDefault();
            if (focusedCardIndex === -1) {
                focusCard(cards.length - 1);
            } else {
                const cols = getGridColumnsCount();
                focusCard(focusedCardIndex - cols);
            }
        } else if (e.key === 'ArrowRight' || e.key === 'l' || e.key === 'L') {
            e.preventDefault();
            if (focusedCardIndex === -1) {
                focusCard(0);
            } else {
                focusCard(focusedCardIndex + 1);
            }
        } else if (e.key === 'ArrowLeft' || e.key === 'h' || e.key === 'H') {
            e.preventDefault();
            if (focusedCardIndex === -1) {
                focusCard(cards.length - 1);
            } else {
                focusCard(focusedCardIndex - 1);
            }
        } else if (e.key === 'Enter') {
            if (focusedCardIndex >= 0 && focusedCardIndex < cards.length) {
                e.preventDefault();
                openModal(cards[focusedCardIndex]);
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

    // helper utils for highlight and nav
    function escapeRegExp(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    function highlightHTML(el, term) {
        const original = el.dataset.original || el.innerHTML;
        if (!el.dataset.original) el.dataset.original = original;
        
        if (!term) {
            el.innerHTML = original;
            return;
        }
        
        const regex = new RegExp(`(${escapeRegExp(term)})`, 'gi');
        const temp = document.createElement('div');
        temp.innerHTML = original;
        
        highlightNode(temp, regex);
        el.innerHTML = temp.innerHTML;
    }
    
    function highlightNode(node, regex) {
        if (node.nodeType === Node.TEXT_NODE) {
            const text = node.nodeValue;
            if (regex.test(text)) {
                const span = document.createElement('span');
                span.innerHTML = text.replace(regex, '<mark class="search-highlight">$1</mark>');
                node.parentNode.replaceChild(span, node);
            }
        } else if (node.nodeType === Node.ELEMENT_NODE) {
            if (node.classList.contains('status-secured')) return;
            const children = Array.from(node.childNodes);
            for (let child of children) {
                highlightNode(child, regex);
            }
        }
    }

    function getVisibleCards() {
        if (currentTab === 'about') return [];
        const sectionClass = currentTab === 'library' ? '.library-section' : '.discovery-section';
        const visibleSections = Array.from(document.querySelectorAll(sectionClass))
                                     .filter(s => s.style.display !== 'none');
        
        const visibleCards = [];
        visibleSections.forEach(s => {
            s.querySelectorAll('.iso-card').forEach(c => {
                if (c.style.display !== 'none') {
                    visibleCards.push(c);
                }
            });
        });
        return visibleCards;
    }

    function focusCard(index) {
        const cards = getVisibleCards();
        if (cards.length === 0) return;
        
        if (focusedCardIndex >= 0 && focusedCardIndex < cards.length) {
            cards[focusedCardIndex].classList.remove('focused');
        }
        
        if (index < 0) index = cards.length - 1;
        if (index >= cards.length) index = 0;
        
        focusedCardIndex = index;
        const activeCard = cards[focusedCardIndex];
        activeCard.classList.add('focused');
        activeCard.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }

    function clearCardFocus() {
        document.querySelectorAll('.iso-card').forEach(c => c.classList.remove('focused'));
        focusedCardIndex = -1;
    }

    function getGridColumnsCount() {
        const gridEl = document.querySelector(currentTab === 'library' ? '.grid' : '.discovery-grid');
        if (!gridEl) return 1;
        const compStyle = window.getComputedStyle(gridEl);
        const gridTemplateCols = compStyle.getPropertyValue('grid-template-columns');
        return gridTemplateCols.split(' ').length || 1;
    }

    function typeCommand(elementId, fullCommand) {
        if (typingTimer) clearInterval(typingTimer);
        
        const el = document.getElementById(elementId);
        if (!el) return;
        
        el.innerHTML = '';
        
        let index = 0;
        typingTimer = setInterval(() => {
            if (index < fullCommand.length) {
                el.textContent = fullCommand.substring(0, index + 1) + '█';
                index++;
            } else {
                clearInterval(typingTimer);
                el.textContent = fullCommand;
            }
        }, 8);
    }

    colorizeTags();
});
