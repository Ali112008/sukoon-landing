"""Compress the posture comparison image for web."""
from PIL import Image
import os

SRC = "/home/z/my-project/upload/IMG-20260802-WA0002(1).jpg"
DST_JPG = "/home/z/my-project/assets/images/posture-comparison.jpg"
DST_WEBP = "/home/z/my-project/assets/images/webp/posture-comparison.webp"

img = Image.open(SRC)
print(f"Original: {img.size[0]}x{img.size[1]}, mode={img.mode}")

if img.mode != "RGB":
    img = img.convert("RGB")

# Resize - target ~600px wide for this image (it's tall 738x1600)
MAX_DIM = 600
w, h = img.size
ratio = min(MAX_DIM / w, MAX_DIM / h)
new_w = int(w * ratio)
new_h = int(h * ratio)
img = img.resize((new_w, new_h), Image.LANCZOS)
print(f"Resized to: {new_w}x{new_h}")

# Save JPG
os.makedirs(os.path.dirname(DST_JPG), exist_ok=True)
img.save(DST_JPG, "JPEG", quality=85, optimize=True, progressive=True)
print(f"JPG: {os.path.getsize(DST_JPG)/1024:.0f}KB")

# Save WebP
os.makedirs(os.path.dirname(DST_WEBP), exist_ok=True)
img.save(DST_WEBP, "WEBP", quality=82)
print(f"WebP: {os.path.getsize(DST_WEBP)/1024:.0f}KB")
