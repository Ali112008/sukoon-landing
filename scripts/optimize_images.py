#!/usr/bin/env python3
"""Optimize and compress client product images for web use."""

from PIL import Image
import os

# Source and destination paths
SRC_DIR = "/home/z/my-project/upload/extracted"
DST_DIR = "/home/z/my-project/assets/images"

# Ensure destination exists
os.makedirs(DST_DIR, exist_ok=True)

# Image mapping - source -> destination
IMAGES = {
    "IMG_7484 (1).png": "hero-pillow.jpg",       # Best hero image - hand pressing pillow
    "IMG_7492.png": "product-detail.jpg",          # Unzipped showing shredded foam
    "_DSC9887.png": "product-lifestyle.jpg",        # Lifestyle image with woman
    "_DSC9999.png": "product-package.jpg",          # Product with packaging/box
    "sokoun ai.jpg": "product-interior.jpg",        # Interior close-up showing foam
}

# Target sizes
HERO_SIZE = (1200, 800)       # Hero image - landscape
PRODUCT_SIZE = (800, 600)     # Product detail - landscape
LIFESTYLE_SIZE = (800, 600)   # Lifestyle - landscape
THUMB_SIZE = (600, 450)       # Smaller images

SIZES = {
    "hero-pillow.jpg": HERO_SIZE,
    "product-detail.jpg": PRODUCT_SIZE,
    "product-lifestyle.jpg": LIFESTYLE_SIZE,
    "product-package.jpg": PRODUCT_SIZE,
    "product-interior.jpg": PRODUCT_SIZE,
}

for src_name, dst_name in IMAGES.items():
    src_path = os.path.join(SRC_DIR, src_name)
    dst_path = os.path.join(DST_DIR, dst_name)
    
    if not os.path.exists(src_path):
        print(f"SKIP: {src_name} not found")
        continue
    
    try:
        img = Image.open(src_path)
        print(f"Processing: {src_name} ({img.size[0]}x{img.size[1]}) -> {dst_name}")
        
        # Convert to RGB if necessary (for PNG with transparency)
        if img.mode in ('RGBA', 'P', 'LA'):
            # Create white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            if img.mode == 'LA':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if 'A' in img.mode else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Get target size
        target = SIZES.get(dst_name, PRODUCT_SIZE)
        
        # Resize maintaining aspect ratio, then crop to exact size
        img_ratio = img.width / img.height
        target_ratio = target[0] / target[1]
        
        if img_ratio > target_ratio:
            # Image is wider - fit height, crop width
            new_height = target[1]
            new_width = int(new_height * img_ratio)
        else:
            # Image is taller - fit width, crop height
            new_width = target[0]
            new_height = int(new_width / img_ratio)
        
        # Use high-quality resampling
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Center crop to exact target size
        left = (new_width - target[0]) // 2
        top = (new_height - target[1]) // 2
        right = left + target[0]
        bottom = top + target[1]
        img = img.crop((left, top, right, bottom))
        
        # Save as optimized JPEG
        img.save(dst_path, 'JPEG', quality=85, optimize=True, progressive=True)
        
        # Report file size
        size_kb = os.path.getsize(dst_path) / 1024
        print(f"  Saved: {dst_name} ({target[0]}x{target[1]}) - {size_kb:.0f} KB")
        
    except Exception as e:
        print(f"ERROR processing {src_name}: {e}")

print("\nDone! All images optimized.")
