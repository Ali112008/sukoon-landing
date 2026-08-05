"""Reorder sections: Hero → Products → Inside → Features → Reviews → CTA → FAQ"""
import re

html_path = "/home/z/my-project/index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Extract each section by its unique markers
# We need to cut: features, inside, products and reorder them

# Pattern: extract full <section>...</section> blocks
def extract_section(html, section_id):
    """Extract a full section block by its id or class."""
    # Try by id first
    pattern = rf'(<section[^>]*id="{section_id}"[^>]*>.*?</section>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        return match.group(1)
    # Try by class
    pattern = rf'(<section[^>]*class="{section_id}"[^>]*>.*?</section>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        return match.group(1)
    return None

# Extract sections
features = extract_section(html, "features")
inside = extract_section(html, "inside")
products = extract_section(html, "products")

print(f"Features section: {len(features)} chars" if features else "Features: NOT FOUND")
print(f"Inside section: {len(inside)} chars" if inside else "Inside: NOT FOUND")
print(f"Products section: {len(products)} chars" if products else "Products: NOT FOUND")

# Find the range from start of features to end of products
# This is the block we need to replace
features_start = html.find('<section class="features" id="features">')
products_end = html.find('</section>', html.find('<section class="products" id="products">')) + len('</section>')

old_block = html[features_start:products_end]
print(f"\nOld block: {len(old_block)} chars")

# New order: Products → Inside → Features
# Add some spacing between sections
new_block = products + "\n\n    " + inside + "\n\n    " + features

print(f"New block: {len(new_block)} chars")

# Replace
new_html = html[:features_start] + new_block + html[products_end:]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("\n✅ Sections reordered: Hero → Products → Inside → Features → Reviews → CTA → FAQ")
