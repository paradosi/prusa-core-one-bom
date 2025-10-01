#!/bin/bash

# Script to scrape Prusa Core ONE manual for hardware components
# Output will be saved to prusa_hardware_raw.txt

OUTPUT_FILE="/Users/jim/Downloads/prusa_hardware_raw.txt"
> "$OUTPUT_FILE"  # Clear file

echo "Scraping Prusa Core ONE Manual - 216 pages..."
echo "This will take several minutes..."

for page in {1..216}; do
    echo "Processing page $page/216..."

    # Fetch page content and extract text
    curl -s "https://www.manualslib.com/manual/3741293/Original-Prusa-Core-One.html?page=$page" \
        -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
        | grep -v '<style' \
        | grep -v '<script' \
        | sed 's/<[^>]*>/ /g' \
        | tr -s ' ' \
        | grep -E -i '(screw|bolt|nut|bearing|motor|M[0-9]|x[0-9]|mm|cable|rod|belt|pulley|sensor|board|printed|part|qty|quantity|pcs|piece)' \
        >> "$OUTPUT_FILE"

    # Rate limiting to avoid being blocked
    sleep 0.5
done

echo ""
echo "Raw data saved to: $OUTPUT_FILE"
echo "Total lines extracted: $(wc -l < "$OUTPUT_FILE")"