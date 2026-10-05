import re
import os
import json

files = ['index.html', 'profil.html', 'pengabdian.html', 'gagasan.html', 'kontak.html']

old_font_link = 'family=Barlow+Condensed:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400'
new_font_link = 'family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Manrope:wght@400;500;600;700;800'

old_tw_heading = 'heading: [\'"Barlow Condensed"\', \'sans-serif\']'
new_tw_heading = 'heading: [\'"Lora"\', \'serif\']'

old_tw_body = 'body: [\'"IBM Plex Sans"\', \'sans-serif\']'
new_tw_body = 'body: [\'"Manrope"\', \'sans-serif\']'

for filename in files:
    if not os.path.exists(filename): continue
    with open(filename, 'r') as f:
        content = f.read()
    
    content = content.replace(old_font_link, new_font_link)
    content = content.replace(old_tw_heading, new_tw_heading)
    content = content.replace(old_tw_body, new_tw_body)
        
    with open(filename, 'w') as f:
        f.write(content)

# Create vercel.json for clean URLs and proper caching
vercel_config = {
  "cleanUrls": True,
  "trailingSlash": False,
  "headers": [
    {
      "source": "/assets/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}

with open('vercel.json', 'w') as f:
    json.dump(vercel_config, f, indent=2)

print("Fonts updated and vercel.json created.")
