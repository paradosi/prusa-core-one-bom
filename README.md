# Prusa Core ONE Bill of Materials (BOM)

Interactive HTML viewer for complete Prusa Core ONE 3D printer hardware bill of materials.

## 🖨️ Overview

Comprehensive hardware BOM for the Prusa Core ONE 3D printer, compiled from official Prusa documentation, community forums, and technical specifications. The interactive web interface allows easy searching, filtering, and reference during assembly or maintenance.

## ✨ Features

- 🔍 **Real-time Search** - Instantly filter components by name, category, or specifications
- 📊 **Interactive Table** - Sortable columns with detailed specifications
- 🎨 **Prusa Branding** - Beautiful orange-themed responsive design
- 📱 **Mobile Friendly** - Works on desktop, tablet, and mobile devices
- 📦 **70+ Components** - Complete hardware inventory across 13 categories

## 📋 BOM Categories

### Frame & Structure
- Aluminum extrusions (6mm, 8mm profiles)
- Acrylic panels and enclosure parts
- Frame connectors and brackets

### CoreXY Motion System
- GT2 belts and pulleys
- Linear motion components
- Idlers and tensioners

### Fasteners
- **M3 Hardware** - Screws, nuts, washers, heatset inserts
- **M4 Hardware** - Screws, nuts, washers, heatset inserts
- **M5 Hardware** - Screws, nuts, washers, heatset inserts

### Motors
- NEMA 17 stepper motors (X, Y, Z, E)
- Motor cables and connectors

### Electronics
- **xBuddy Board** - Main controller
- **Sensors** - Endstops, filament sensor, PINDA probe
- **Heating** - Heated bed, heater cartridge, thermistors
- **Cooling** - Print cooling fan, hotend fan, electronics fan
- **Displays & Controls** - LCD screen, rotary encoder

### Nextruder Extruder
- Gears and motor components
- PTFE tube and fittings
- Hotend assembly parts

### Print Bed
- Spring steel sheet
- Magnetic base
- Leveling components

### Enclosure
- Panels and hinges
- LED lighting
- Cable management

### Printed Parts
- Structural components
- Cable guides and clips
- Fan shrouds and ducts

### Tools & Accessories
- Hex keys and wrenches
- Spare parts kit
- Lubrication

### Miscellaneous
- Cables and wire harness
- Zip ties and fasteners
- Firmware and software

## 🚀 Usage

### View Online
Open `index.html` in any modern web browser.

### Search & Filter
Type in the search box to instantly filter components:
- Search by part name: "stepper motor"
- Search by category: "fasteners"
- Search by size: "M3"
- Search by specification: "GT2"

### Sort Data
Click any column header to sort:
- Category
- Part Name
- Quantity
- Specifications
- Notes

## 📁 Files

**`index.html`** - Interactive web viewer
- Responsive HTML interface
- Built-in JavaScript search and filter
- Prusa orange branding (#FF6600)

**`core_one_hardware_bom_master.csv`** - Complete BOM database
- 70+ components with full specifications
- CSV format for easy editing and importing
- Categories, quantities, specs, and notes

**`scrape_prusa_complete.py`** - Python web scraper
- Automated scraping of Prusa documentation
- Extracts hardware specifications
- Generates CSV output

**`scrape_prusa_manual.sh`** - Shell wrapper script
- Downloads Prusa assembly manual PDFs
- Batch processing for multiple documents
- Error handling and retry logic

## 🔧 Updating the BOM

### Edit CSV Manually
1. Open `core_one_hardware_bom_master.csv` in Excel or text editor
2. Add/modify components following existing format
3. Save CSV file
4. Refresh `index.html` to see changes

### Using Scraper Scripts

**Download assembly manuals:**
```bash
./scrape_prusa_manual.sh
```

**Scrape BOM data:**
```bash
python3 scrape_prusa_complete.py
```

## 📊 BOM Statistics

- **Total Components:** 70+
- **Categories:** 13
- **Fastener Types:** M3, M4, M5 (screws, nuts, washers, heatsets)
- **Motors:** 4 NEMA 17 steppers
- **Sensors:** 5+ (endstops, filament, probe, thermistors)
- **Fans:** 3 types (print cooling, hotend, electronics)

## 🛠️ Development

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.x (for scraper scripts)
- Text editor or IDE

### Local Development
1. Clone repository
   ```bash
   git clone https://git.k42.ovh/jim/prusa-core-one-bom.git
   cd prusa-core-one-bom
   ```

2. Open in browser
   ```bash
   open index.html
   # or
   python3 -m http.server 8000
   # then visit http://localhost:8000
   ```

3. Edit CSV for updates
   - Modify `core_one_hardware_bom_master.csv`
   - Reload page to see changes

## 📚 Data Sources

BOM compiled from:
- [Prusa Knowledge Base](https://help.prusa3d.com) - Official assembly guides
- [Prusa Community Forums](https://forum.prusa3d.com) - User modifications
- [Prusa GitHub](https://github.com/prusa3d) - Technical specifications
- Official Prusa Core ONE teardown documentation

## 🎯 Use Cases

- **Assembly** - Reference during printer build
- **Maintenance** - Identify replacement parts
- **Upgrades** - Plan modifications and improvements
- **Inventory** - Track spare parts and consumables
- **Documentation** - Technical reference for specifications

## 📝 Notes

- BOM includes both standard and optional components
- Some quantities are approximate (e.g., "various" for assorted fasteners)
- Specifications based on official Prusa documentation
- Community modifications may require additional hardware

## 🔗 Resources

- [Prusa Core ONE Product Page](https://www.prusa3d.com/product/prusa-core-one-3d-printer/)
- [Assembly Instructions](https://help.prusa3d.com/guide/prusa-core-one-kit-assembly)
- [Prusa Forum - Core ONE](https://forum.prusa3d.com/forum/original-prusa-core-one/)
- [Printables - Core ONE Mods](https://www.printables.com/search/models?q=core%20one)

---

**Repository:** https://git.k42.ovh/jim/prusa-core-one-bom
**Last Updated:** 2025-09-30
**Printer Model:** Prusa Core ONE
**BOM Version:** 1.0
