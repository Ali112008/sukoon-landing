#!/usr/bin/env python3
"""Create a composite image showing two pillows side by side for the 'مخدتين' product card."""

from PIL import Image, ImageDraw, ImageFilter
import os

# Source image - the hero pillow image (hand pressing, clean background)
SRC = "/home/z/my-project/assets/images/hero-pillow.jpg"
DST = "/home/z/my-project/assets/images/product-two-pillows.jpg"

# Also use the original high-res source for better quality
SRC_HR = "/home/z/my-project/upload/extracted/IMG_7484 (1).png"

# Target dimensions for product card
TARGET_W = 800
TARGET_H = 600

try:
    # Use the high-res source for better quality
    img = Image.open(SRC_HR)
    
    # Convert to RGB if necessary
    if img.mode in ('RGBA', 'P', 'LA'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        if img.mode == 'LA':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if 'A' in img.mode else None)
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # The source image is square (6336x6336). We need to extract the pillow area
    # and create a composite with two pillows side by side.
    
    # Crop the pillow area from the source (center portion, avoiding too much background)
    # The pillow is roughly in the center with the hand
    src_w, src_h = img.size
    
    # Crop a generous area around the pillow
    crop_margin = int(src_w * 0.1)
    # Take a landscape crop from the center
    crop_top = int(src_h * 0.15)
    crop_bottom = int(src_h * 0.75)
    crop_left = crop_margin
    crop_right = src_w - crop_margin
    
    pillow_single = img.crop((crop_left, crop_top, crop_right, crop_bottom))
    
    # Resize the single pillow to fit half the target width
    single_w = TARGET_W // 2
    single_h = TARGET_H
    
    # Calculate resize maintaining aspect ratio
    pw, ph = pillow_single.size
    ratio = min(single_w / pw, single_h / ph)
    new_w = int(pw * ratio)
    new_h = int(ph * ratio)
    
    pillow_single = pillow_single.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Create the composite canvas
    canvas = Image.new('RGB', (TARGET_W, TARGET_H), (220, 230, 240))  # Light blue-grey background
    
    # Place first pillow on the left
    x1 = (single_w - new_w) // 2
    y1 = (TARGET_H - new_h) // 2
    canvas.paste(pillow_single, (x1, y1))
    
    # Place second pillow on the right (slightly offset for natural look)
    x2 = single_w + (single_w - new_w) // 2 - 10
    y2 = (TARGET_H - new_h) // 2 + 8
    canvas.paste(pillow_single, (x2, y2))
    
    # Save
    canvas.save(DST, 'JPEG', quality=88, optimize=True, progressive=True)
    
    size_kb = os.path.getsize(DST) / 1024
    print(f"Created: product-two-pillows.jpg ({TARGET_W}x{TARGET_H}) - {size_kb:.0f} KB")
    
except Exception as e:
    print(f"Error: {e}")
    # Fallback: just use the package image which shows the full product
    import shutil
    shutil.copy("/home/z/my-project/assets/images/product-package.jpg", DST)
    print("Fallback: copied product-package.jpg as product-two-pillows.jpg")
