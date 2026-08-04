"""Compress and optimize the new two-pillows image for web."""
from PIL import Image
import os

SRC = "/home/z/my-project/upload/soukon1 (1).png"
DST_JPG = "/home/z/my-project/assets/images/product-two-pillows.jpg"
DST_WEBP = "/home/z/my-project/assets/images/webp/product-two-pillows.webp"

# Open and process
img = Image.open(SRC)
print(f"Original: {img.size[0]}x{img.size[1]}, mode={img.mode}")

# Convert palette/indexed to RGB
if img.mode != "RGB":
    img = img.convert("RGB")
    print(f"Converted to RGB")

# Resize - target ~800px wide for product image (mobile-friendly, sharp enough)
MAX_DIM = 800
w, h = img.size
if w > MAX_DIM or h > MAX_DIM:
    # Keep aspect ratio
    ratio = min(MAX_DIM / w, MAX_DIM / h)
    new_w = int(w * ratio)
    new_h = int(h * ratio)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    print(f"Resized to: {new_w}x{new_h}")

# Save as optimized JPEG
os.makedirs(os.path.dirname(DST_JPG), exist_ok=True)
img.save(DST_JPG, "JPEG", quality=85, optimize=True, progressive=True)
jpg_size = os.path.getsize(DST_JPG)
print(f"JPG saved: {DST_JPG} ({jpg_size/1024:.0f}KB)")

# Save as WebP (better compression)
os.makedirs(os.path.dirname(DST_WEBP), exist_ok=True)
img.save(DST_WEBP, "WEBP", quality=82)
webp_size = os.path.getsize(DST_WEBP)
print(f"WebP saved: {DST_WEBP} ({webp_size/1024:.0f}KB)")

print(f"\nCompression: {7300}KB → {jpg_size/1024:.0f}KB JPG ({100-jpg_size/73000*100:.0f}% smaller) + {webp_size/1024:.0f}KB WebP")
