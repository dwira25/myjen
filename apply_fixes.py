import re
import os

files = ['index.html', 'profil.html', 'pengabdian.html', 'gagasan.html']

seo_tags = '''
    <meta name="description" content="Profil resmi Mayjen TNI (Purn.) dr. Subandono Bambang Indrasto, Sp.M., S.H., M.M. Dokter spesialis mata, purnawirawan TNI, pemimpin organisasi, dan pengabdian masyarakat di Jawa Barat.">
    <meta name="keywords" content="Subandono Bambang Indrasto, Mayjen TNI Subandono, Partai Rakyat Indonesia, PRI Jawa Barat, Dokter Subandono, RSPAD">
    <meta property="og:title" content="Mayjen TNI (Purn.) dr. Subandono Bambang Indrasto | Profil & Pengabdian">
    <meta property="og:description" content="Profil resmi Mayjen TNI (Purn.) dr. Subandono Bambang Indrasto. Menelusuri jejak pengabdian sebagai Dokter, Prajurit, dan Pemimpin.">
    <meta property="og:image" content="assets/dokter.jpg">
    <link rel="icon" type="image/png" href="assets/logo-pri.png">
</head>'''

unified_nav = '''<nav class="bg-navy fixed w-full z-50 shadow-lg transition-all duration-300" id="navbar">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex-shrink-0 flex items-center gap-3">
                    <img src="assets/logo-pri.png" alt="Logo Garuda" class="h-10 w-10 rounded-full object-cover bg-white">
                    <div class="text-white">
                        <div class="text-[10px] font-semibold tracking-wider text-gold">MAYJEN TNI (PURN.)</div>
                        <div class="font-heading font-bold text-lg md:text-xl leading-tight tracking-wide">dr. Subandono B.I.</div>
                    </div>
                </div>
                <!-- Desktop Menu -->
                <div class="hidden md:flex items-center space-x-6 text-sm text-gray-300">
                    <a href="index.html" class="nav-link hover:text-white">Beranda</a>
                    <a href="profil.html" class="nav-link hover:text-white">Profil</a>
                    <a href="pengabdian.html" class="nav-link hover:text-white">Pengabdian</a>
                    <a href="gagasan.html" class="nav-link hover:text-white">Gagasan</a>
                    <a href="kontak.html" class="btn-primary px-5 py-2 rounded font-medium">Hubungi Tim</a>
                </div>
                <!-- Mobile menu button -->
                <div class="md:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-white hover:text-gold focus:outline-none p-2">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden bg-navy border-t border-white/10">
            <div class="px-4 pt-2 pb-6 space-y-2 text-center shadow-2xl">
                <a href="index.html" class="block px-3 py-3 text-white hover:text-gold rounded-md text-base font-medium">Beranda</a>
                <a href="profil.html" class="block px-3 py-3 text-white hover:text-gold rounded-md text-base font-medium">Profil</a>
                <a href="pengabdian.html" class="block px-3 py-3 text-white hover:text-gold rounded-md text-base font-medium">Pengabdian</a>
                <a href="gagasan.html" class="block px-3 py-3 text-white hover:text-gold rounded-md text-base font-medium">Gagasan</a>
                <a href="kontak.html" class="block px-3 py-3 mt-4 btn-primary rounded-md text-base font-medium w-full">Hubungi Tim</a>
            </div>
        </div>
    </nav>'''

unified_script = '''<script>
        // Sticky navbar effect
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 10) {
                navbar.classList.add('bg-navy/95', 'backdrop-blur-sm');
                navbar.classList.remove('bg-navy');
            } else {
                navbar.classList.remove('bg-navy/95', 'backdrop-blur-sm');
                navbar.classList.add('bg-navy');
            }
        });

        // Mobile menu toggle
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');
        if (btn && menu) {
            btn.addEventListener('click', () => {
                menu.classList.toggle('hidden');
            });
        }
    </script>'''

for filename in files:
    if not os.path.exists(filename): continue
    with open(filename, 'r') as f:
        content = f.read()

    # 1. SEO Tags & Favicon
    if '<meta name="description"' not in content:
        content = content.replace('</head>', seo_tags)

    # 2. Navbar Replacement
    # Need to match <nav ...> ... </nav> across multiple lines
    nav_pattern = re.compile(r'<nav[^>]*id="navbar"[^>]*>.*?</nav>', re.DOTALL)
    content = nav_pattern.sub(unified_nav, content)

    # 3. Script Replacement
    script_pattern = re.compile(r'<script>\s*// Simple sticky navbar effect.*?</script>', re.DOTALL)
    content = script_pattern.sub(unified_script, content)
    
    script_pattern2 = re.compile(r'<script>\s*window\.addEventListener\(\'scroll\'.*?</script>', re.DOTALL)
    content = script_pattern2.sub(unified_script, content)

    # 4. Remove empty social links
    social_pattern = re.compile(r'<div class="flex gap-4">\s*<a href="#" class="w-10 h-10 rounded bg-white/10 flex items-center justify-center hover:bg-red hover:text-white transition"><i class="fab fa-instagram"></i></a>\s*<a href="#" class="w-10 h-10 rounded bg-white/10 flex items-center justify-center hover:bg-red hover:text-white transition"><i class="fab fa-facebook-f"></i></a>\s*<a href="#" class="w-10 h-10 rounded bg-white/10 flex items-center justify-center hover:bg-red hover:text-white transition"><i class="fab fa-youtube"></i></a>\s*</div>', re.DOTALL)
    content = social_pattern.sub('', content)

    # 5. Fix any footer contact link leftovers
    content = content.replace('href="index.html#kontak"', 'href="kontak.html"')
    content = content.replace('href="#kontak"', 'href="kontak.html"')

    # Fix footer "Hubungi Tim" button if it exists as 'btn-primary'
    content = content.replace('<a href="kontak.html" class="mt-6 inline-block w-full text-center btn-primary px-4 py-2 rounded">', '<a href="kontak.html" class="mt-6 inline-block w-full text-center btn-primary px-4 py-2 rounded font-bold">')
    
    with open(filename, 'w') as f:
        f.write(content)

print("Fixes applied successfully.")
