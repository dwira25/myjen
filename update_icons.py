import re
import os

filename = 'index.html'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Update Kesehatan
    content = content.replace(
        '<i class="fas fa-heartbeat"></i>',
        '<i class="fas fa-briefcase-medical"></i>'
    )
    # Update Kesehatan image
    content = content.replace(
        'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1584362917165-526a968579e8?auto=format&fit=crop&w=600&q=80'
    )

    # 2. Update Kebangsaan
    content = content.replace(
        '<i class="fas fa-flag"></i>',
        '<i class="fas fa-medal"></i>'
    )
    # Image for Kebangsaan is already Indonesian flag (photo-1582213782179), but let's make sure it's dramatic. We'll leave it as is.

    # 3. Update Kepemimpinan
    content = content.replace(
        '<i class="fas fa-shield-alt"></i>',
        '<i class="fas fa-star"></i>'
    )
    # Update Kepemimpinan image to something more authoritative/military
    content = content.replace(
        'https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1590494165264-1ebe3602eb80?auto=format&fit=crop&w=600&q=80' # More formal/official looking
    )

    # 4. Update Kerakyatan
    content = content.replace(
        '<i class="fas fa-users"></i>',
        '<i class="fas fa-handshake"></i>'
    )
    # Update Kerakyatan image to something more hands-on/community
    content = content.replace(
        'https://images.unsplash.com/photo-1529156069898-49953eb1b5ce?auto=format&fit=crop&w=600&q=80',
        'https://images.unsplash.com/photo-1593113580326-7248130833b9?auto=format&fit=crop&w=600&q=80'
    )

    with open(filename, 'w') as f:
        f.write(content)

    print("Icons and images updated.")
else:
    print("index.html not found.")
