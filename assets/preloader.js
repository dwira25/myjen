/* ===== Preloader controller: Partai Rakyat Indonesia ===== */
(function () {
    var MIN_MS = 1400;   // minimum time the loader stays visible (animations get to play)
    var MAX_MS = 4000;   // hard cap so a slow/blocked resource never traps the user

    var el = document.getElementById('pri-preloader');
    if (!el) return;

    var fill = el.querySelector('.pri-bar-fill');
    var start = Date.now();
    var finished = false;

    // Smoothly creep the bar toward 90% while the page loads.
    var creep = 0;
    var timer = setInterval(function () {
        creep += (88 - creep) * 0.14;
        if (fill) fill.style.width = creep.toFixed(1) + '%';
    }, 120);

    function finish() {
        if (finished) return;
        finished = true;
        clearInterval(timer);
        if (fill) fill.style.width = '100%';

        var elapsed = Date.now() - start;
        var wait = Math.max(0, MIN_MS - elapsed);
        setTimeout(function () {
            el.classList.add('pri-done');
            document.documentElement.classList.remove('pri-loading');
            // Remove from DOM after the fade-out transition completes.
            setTimeout(function () { el.remove(); }, 800);
        }, wait);
    }

    // Finish as soon as the window has fully loaded...
    if (document.readyState === 'complete') {
        finish();
    } else {
        window.addEventListener('load', finish);
    }

    // ...but never later than MAX_MS.
    setTimeout(finish, MAX_MS);
})();
