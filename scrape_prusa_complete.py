#!/usr/bin/env python3
"""
Scrape Prusa Core ONE manual for all hardware components
"""

import re
import time
import urllib.request
import urllib.parse
from collections import defaultdict

def fetch_page(page_num):
    """Fetch a single page from the manual"""
    url = f"https://www.manualslib.com/manual/3741293/Original-Prusa-Core-One.html?page={page_num}"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching page {page_num}: {e}")
        return ""

def clean_html(html):
    """Remove HTML tags and clean text"""
    # Remove script and style tags
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL|re.I)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL|re.I)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', html)
    # Clean whitespace
    text = ' '.join(text.split())
    return text

def extract_hardware(text, page_num):
    """Extract hardware components from text"""
    components = []

    # Split into sentences for context
    sentences = re.split(r'[.!?]\s+', text)

    for sentence in sentences:
        # Skip if too short or likely not relevant
        if len(sentence) < 10:
            continue

        # Patterns for hardware components
        patterns = {
            # Screws with specifications (M3x10, M5x16, etc.)
            'screw': r'M[2-8]x[0-9]+[a-zA-Z]*\s*(?:screw|bolt)',
            # Self-tapping screws
            'self_tap': r'[0-9.]+x[0-9.]+[a-zA-Z]*\s*self-tapping',
            # Nuts
            'nut': r'M[2-8]\s*(?:nut|square\s*nut)',
            # Bearings
            'bearing': r'(?:bearing|ball\s*bearing)\s*[0-9x]+',
            # Motors
            'motor': r'(?:stepper\s*)?motor(?:\s+[A-Z0-9-]+)?',
            # Belts
            'belt': r'(?:GT[2-9]|timing)\s*belt',
            # Rods
            'rod': r'(?:smooth|linear|threaded)\s*rod',
            # Pulleys
            'pulley': r'pulley\s*(?:[0-9]+T)?',
            # Cables
            'cable': r'(?:cable|wire)\s*(?:[0-9]+\s*(?:pin|wire|conductor))?',
            # Printed parts
            'printed': r'printed\s*(?:part|component)',
            # Generic parts with measurements
            'measurement': r'[0-9]+x[0-9]+(?:x[0-9]+)?\s*mm',
        }

        for ptype, pattern in patterns.items():
            matches = re.finditer(pattern, sentence, re.I)
            for match in matches:
                # Get context around match
                start = max(0, match.start() - 30)
                end = min(len(sentence), match.end() + 30)
                context = sentence[start:end].strip()

                # Look for quantity
                qty_match = re.search(r'\(([0-9]+)x\)', sentence)
                qty = qty_match.group(1) if qty_match else ""

                components.append({
                    'page': page_num,
                    'type': ptype,
                    'component': match.group(0),
                    'quantity': qty,
                    'context': context
                })

    return components

def main():
    """Main scraping function"""
    print("Prusa Core ONE Manual Hardware Scraper")
    print("=" * 60)
    print(f"Total pages to process: 216")
    print("This will take approximately 5-10 minutes...")
    print()

    all_components = []

    # Process all 216 pages
    for page in range(1, 217):
        if page % 10 == 0:
            print(f"Progress: {page}/216 pages processed...")

        html = fetch_page(page)
        if not html:
            continue

        text = clean_html(html)
        components = extract_hardware(text, page)
        all_components.extend(components)

        # Rate limiting
        time.sleep(0.3)

    print(f"\nCompleted! Found {len(all_components)} component mentions")

    # Save raw data
    with open('/Users/jim/Downloads/prusa_hardware_raw.txt', 'w') as f:
        for comp in all_components:
            f.write(f"Page {comp['page']}: {comp['component']} ({comp['quantity']}) - {comp['context']}\n")

    # Aggregate components
    component_counts = defaultdict(lambda: {'total': 0, 'pages': set()})
    for comp in all_components:
        key = comp['component'].upper().strip()
        component_counts[key]['total'] += 1
        component_counts[key]['pages'].add(comp['page'])
        if comp['quantity']:
            component_counts[key]['qty'] = comp['quantity']

    # Save aggregated CSV
    with open('/Users/jim/Downloads/prusa_hardware_bom.csv', 'w') as f:
        f.write("Component Name,Quantity,Mentions,Pages Found,Type\n")
        for comp, data in sorted(component_counts.items()):
            qty = data.get('qty', 'Unknown')
            mentions = data['total']
            pages = ','.join(map(str, sorted(data['pages'])))
            f.write(f'"{comp}",{qty},{mentions},"{pages[:100]}",Hardware\n')

    print(f"\nOutput files created:")
    print(f"  - /Users/jim/Downloads/prusa_hardware_raw.txt (detailed)")
    print(f"  - /Users/jim/Downloads/prusa_hardware_bom.csv (aggregated BOM)")

if __name__ == "__main__":
    main()