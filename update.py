import os

files = ['index.html', 'profil.html', 'pengabdian.html']

old_font_link = 'family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400'
new_font_link = 'family=Barlow+Condensed:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400'

old_tw_heading = 'heading: [\'"Playfair Display"\', \'serif\']'
new_tw_heading = 'heading: [\'"Barlow Condensed"\', \'sans-serif\']'

old_tw_body = 'body: [\'"Inter"\', \'sans-serif\']'
new_tw_body = 'body: [\'"IBM Plex Sans"\', \'sans-serif\']'

old_pri_btn = '''<a href="#" class="inline-block bg-white text-red hover:bg-offwhite px-6 py-3 rounded font-semibold transition shadow-md">
                        Lihat Aktivitas PRI Jabar <i class="fas fa-arrow-right ml-1"></i>
                    </a>'''
new_pri_btn = '''<a href="https://partairakyat.id/daftar-kader" target="_blank" class="inline-block bg-white text-red hover:bg-offwhite px-6 py-3 rounded font-semibold transition shadow-md">
                        Gabung Bersama kami <i class="fas fa-arrow-right ml-1"></i>
                    </a>'''

old_dokter_img = 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=200&q=80'
new_dokter_img = 'assets/dokter.jpg'


for filename in files:
    if not os.path.exists(filename): continue
    with open(filename, 'r') as f:
        content = f.read()
    
    content = content.replace(old_font_link, new_font_link)
    content = content.replace(old_tw_heading, new_tw_heading)
    content = content.replace(old_tw_body, new_tw_body)
    
    if filename == 'index.html':
        content = content.replace(old_pri_btn, new_pri_btn)
        content = content.replace(old_dokter_img, new_dokter_img)
        
    with open(filename, 'w') as f:
        f.write(content)

print("Update script completed.")
