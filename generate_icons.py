from PIL import Image, ImageDraw
import os

def make_icon(size, path):
    img = Image.new('RGB', (size, size), color='#1D9E75')
    draw = ImageDraw.Draw(img)
    # Draw a simple leaf/flame shape as text
    margin = size // 6
    # White circle in center
    cx, cy, r = size//2, size//2, size//3
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill='white')
    # Green fork-like lines
    lw = max(2, size//32)
    draw.rectangle([cx-lw, cy-r+size//10, cx+lw, cy+size//8], fill='#1D9E75')
    img.save(path, 'PNG')

os.makedirs('icons', exist_ok=True)
make_icon(192, 'icons/icon-192.png')
make_icon(512, 'icons/icon-512.png')
print("Icons generated")
