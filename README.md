# AURÉLIA — Maison de Parfums

An ultra-luxury, print-ready perfume catalogue built as a self-contained A4 (portrait) publication.

## Files
- `catalogue.html` — The complete catalogue (cover → back cover), print-optimised for A4.
- `styles.css` — Luxury editorial design system (palette, typography, layouts, print rules).

## View it
Open `catalogue.html` in any modern browser (Chrome/Edge recommended).

## Bottles / real product photos (demo)
Each fragrance is drawn as its **own distinct flacon** (unique silhouette, cap and colour) so no two look alike — these are original vector renders, not copyrighted photography.

To swap in **real product photos** for a demo:
1. Open `download-images.ps1` and paste a direct image URL for each fragrance (in your browser: right‑click a product image → "Copy image address").
2. Run: `powershell -ExecutionPolicy Bypass -File .\download-images.ps1`
3. Reload `catalogue.html`. Any bottle with a photo shows it; any missing photo automatically falls back to the drawn flacon.

Photos are saved to `images/` using the exact names the catalogue expects (`01-baccarat-rouge-540.png` … `20-angels-share.png`). Product imagery belongs to the respective brands — use for a private demo only, not for publication or resale.

## Export a print-ready PDF
1. Open `catalogue.html` in Chrome or Edge.
2. Press `Ctrl + P` (Print).
3. Destination: **Save as PDF**.
4. Layout: **Portrait** · Paper size: **A4**.
5. Margins: **None**.
6. Enable **Background graphics** (essential — this renders the luxury colour worlds).
7. Save.

## Print production notes
- Format: **A4 portrait**, full-bleed colour worlds.
- Screen colour space is sRGB. For **offset printing**, hand the PDF to your print house and request a **CMYK conversion with soft-proofing**; specify **300 DPI** for any raster imagery you substitute in.
- Recommended stock for the coffee-table feel: **150–170 gsm silk/satin text**, **300 gsm soft-touch laminate cover**, with optional **gold-foil** on the wordmark and **spot UV** on hero elements.
- Bleed: add **3 mm bleed** and crop marks at export if your printer requires them.

## Pricing disclaimer
Prices shown are **indicative recommended retail** (EUR/CZK) for editorial layout purposes and should be verified against the live Notino CZ listing before publication, as fragrance pricing fluctuates.
