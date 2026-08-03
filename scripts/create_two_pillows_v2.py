#!/usr/bin/env python3
"""Create a better two-pillows product image using the bed/packaging shot."""

from PIL import Image, ImageDraw, ImageFont
import os

# Use the DSC9999 image which shows pillow on bed with packaging
SRC = "/home/z/my-project/upload/extracted/_DSC9999.png"
DST = "/home/z/my-project/assets/images/product-two-pillows.jpg"

TARGET_W = 800
TARGET_H = 600

try:
    img = Image.open(SRC)
    
    # Convert to RGB
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
    
    # The image is 5184x3464 (landscape). Crop to focus on the pillow area.
    src_w, src_h = img.size
    
    # Target aspect ratio
    target_ratio = TARGET_W / TARGET_H  # 1.333
    img_ratio = src_w / src_h  # 1.495
    
    if img_ratio > target_ratio:
        # Image is wider - crop sides
        new_w = int(src_h * target_ratio)
        left = (src_w - new_w) // 2
        img = img.crop((left, 0, left + new_w, src_h))
    else:
        # Image is taller - crop top/bottom
        new_h = int(src_w / target_ratio)
        top = (src_h - new_h) // 2
        img = img.crop((0, top, src_w, top + new_h))
    
    # Resize to target
    img = img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    
    # Add a subtle "×2" badge in the top-left corner
    # Create a circular badge with gold background
    badge_size = 80
    badge_x = 30
    badge_y = 30
    
    # Draw semi-transparent overlay for badge
    overlay = Image.new('RGBA', (TARGET_W, TARGET_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Gold circle badge
    badge_color = (200, 169, 110, 230)  # Gold with alpha
    draw.ellipse([badge_x, badge_y, badge_x + badge_size, badge_y + badge_size], fill=badge_color)
    
    # Add "×2" text
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    text = "×2"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = badge_x + (badge_size - text_w) // 2
    text_y = badge_y + (badge_size - text_h) // 2 - 2
    
    # Draw text (dark navy on gold)
    draw.text((text_x, text_y), text, fill=(30, 58, 95, 255), font=font)
    
    # Composite overlay onto image
    img_rgba = img.convert('RGBA')
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    img = img_rgba.convert('RGB')
    
    # Save
    img.save(DST, 'JPEG', quality=88, optimize=True, progressive=True)
    
    size_kb = os.path.getsize(DST) / 1024
    print(f"Created: product-two-pillows.jpg ({TARGET_W}x{TARGET_H}) - {size_kb:.0f} KB")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
