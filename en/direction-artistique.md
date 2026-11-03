Who reads it, and when: `diapo-fabricant`, in full, for the contact sheet of directions (end of phase 1) then for the style charter (phase 5) and to write `controles.py`; the project chat, only the "Lead's part", from the heading `# Lead's part (and the builder's)` to the heading `# Builder's part` excluded (`grep -n "^#" universel/direction-artistique.md`), plus `annexe-palettes.md` and `annexe-polices.md` for the draws, at the end of phase 1; the "art direction" auditor through `interdits.txt`, extracted by script from "What gives away AI".

# Phase 5 · Art direction (`diapo-fabricant`, mission brief from the lead)

**[RULE DA.1]** The agent directly reads `reference/craft-floor.md` of the `impeccable` skill and only the "Commit the world" section of `reference/new-work.md` (`grep -n '^## '`), without launching the skill's full flow; `apple-design` is loaded only for an animated HTML.

**[MUST DA.1b]** **Precedence: this module overrides `craft-floor.md` of `impeccable`.** Where they diverge (step label above the title, giant cover number, row of tiles in Vivid), this module decides; `craft-floor.md` is used only for what this module does not say.

**[RULE DA.2]** It writes `travail/05_charte.md`, `travail/tokens.css` and `travail/gabarits.css`, then adds the `gabarit` field to each page of `02_contenu.yaml`.

**[MUST DA.3]** An **imposed style charter** (school, company, client) overrides, over the person's taste as over the draws: rhythm, layout templates, charts and images are worked inside it.

# Lead's part (and the builder's)

## The target level: beautiful first, different second

**[MUST DA.4]** A deliverable that is **beautiful, clean and thought through**, then specific to the person. Variety never justifies an ugly result: an ugly or heavy draw is redone; the contact sheet veto also applies in Express (on the single direction, at the first check sheet).

**[MUST DA.5]** **Color that carries meaning**, explained, never drawn at random, and visible: a page barely tinted reads like a consulting-firm memo (floor: "Color", point 9 e).

**[MUST DA.5b]** **The accent has a written origin, in one line.** The accent color comes from the subject or the recipient: the client's brand colors (DA.9), the sector's codes (DA.13), the flag or landscape of a country or a place (DA.12), the material or photo of the product (DA.92). The builder writes it in `reglages.yaml` (`couleurs.origine: "brand: raspberry of the client's logo, official site"`; first word among brand, recipient, sector, country, place, product, photo) and `controles.py` fails without it. Never a decorative color, never the one we like; the template's default color is not kept. Derived tints (`accent-clair`, `accent-fonce`) are not brand colors: they serve small areas, and a flat of more than 1.5% of a sheet outside the roles table is a defect.

**[RULE DA.6]** **Light, breathing background** on content pages: at least 30% white. Solid colored areas: "Color", point 9 h. A page in solid color carries few words (a title or a large number, one sentence, three markers at most), preferably a real photo on one half: a full page of color loaded with text is the most visible flaw.

**[RULE DA.7]** **Real, chosen images**, clean tables and charts, an obvious hierarchy.

**[MUST DA.8]** **Few words, not little content**: all the substance (figures, proof, reasoning, nuances) goes through form (`phase-2-contenu.md`, "Page density"); what does not fit goes in the notes or the appendix, never deleted. Airy but hollow: a SEVERE flaw for the recipient.

## The subject sets the tone

**[MUST DA.9]** **When the subject has an identity, it sets the tone before any draw.** Priority 1, **real brand or company** (studied, the case's client, or the person's own company): official logo and brand colors, taken from its website, its press kit or its public charter (Wikimedia Commons often has the logo), with credit. Its palette becomes the roles table ("Color", point 12). The client's brand goes on the cover and in the banner, small, never elsewhere; the logo is never distorted, recolored or redrawn. The drawn axis 2 decides the rest.

**[RULE DA.10]** **The brand's voice is taken up everywhere**: graphic signature (banner, pattern, rounded corners) on every page, the brand's corner radius = the charter's single radius. Typography comes from the drawn axis 2, never from the brand's own, so that a deliverable about a brand does not read like a document from the brand.

**[RULE DA.11]** **Check** (phase 8, art director and decision-maker): with the logo masked, the page must still be recognizable as the brand's.

**[RULE DA.12]** Priority 2, **country, city, place**: an emblematic color that carries meaning, explained in one sentence; not the whole flag or folklore, unless asked.

**[RULE DA.13]** Priority 3, **sector or product without a brand**: color drawn from a material, a product or the cover photo.

**[RULE DA.14]** Priority 4, **none of the above**: palette structure from `annexe-palettes.md`, filtered by taste.

**[RULE DA.15]** **Fictional company**: logo created for the deliverable, simple (logotype, monogram or pictogram as SVG drawn by script), in the charter's colors, with no resemblance to a real brand; its color becomes the accent (point 1); the case's name, or one chosen by the person.

**[RULE DA.16]** Brand colors take the role of the accent and accent 2 among the 9 roles; in Vivid, all of them (5 at most) enter the roles table (point 9).

**[RULE DA.17]** Mandatory contrasts: a brand color too light for text is used for solid areas, its dark version for text.

**[RULE DA.18]** The draw decides only what the identity leaves free: fonts (axis 2), grid, cover, charts.

## Anti-generic: every person has a style of their own

**[RULE DA.19]** **The modules fix no font, no color, no cover**: everything comes from the subject, the person's taste and the draws of `travail/tirer.py` in the catalogs of `annexe-polices.md` and `annexe-palettes.md`. Command: `python travail/tirer.py <label> <k> "<option>" ...`, one unique label per draw (`axes/2`, `d1/palette`, `d2/police-titre`...); the script returns k distinct options and logs everything in `travail/tirages.log`.

**[RULE DA.20]** **Editorial identity before color.** At the end of phase 1, write at the top of `05_charte.md`: editorial thesis in one sentence ("this document reads like..."), visual object or metaphor drawn from the subject, title grammar, chart grammar, photo language, 3 distinctive choices and 3 choices to avoid. Two people on the same subject must differ by this identity (architecture, grid, titles, data, images), not only by the palette.

**[RULE DA.21]** **Taste prevails over the draw**: draw among the options compatible with the subject and the taste, even if only one or two remain. The energy of step C sets axis 1 and is never drawn. "Sober" taste: no dark background. No taste: the whole energy catalog.

**[RULE DA.22]** **Express (no contact sheet)**: no direction draw; start from the chosen energy, choose by reasoning the direction that best serves the subject and the taste, write why in `05_charte.md`; the draw only settles the fonts and the palette structure.

**[MUST DA.23]** **A series keeps its charter, and its contact sheet is compared to the best render**: tokens, layout templates, fonts and check script of the previous deliverable reused, only the section hues change; write "sequel to <previous deliverable>, charter reused". The reference is the episode the person liked most (`profil.md`), not the latest: lay the new episode's contact sheet next to that one; denser, more colorful or less illustrated, correct it before delivering.

**[RULE DA.24]** **Never the same style twice for the same person** across different subjects, clients or topics (never between parts of one series): directions, palettes and fonts from the history in `profil.md` are removed before the draw.

**[RULE DA.25]** **Discard the first idea that comes**: note the "obvious" choice discarded in `05_charte.md`.

**[TIP DA.26]** **Going outside the catalog is allowed** if it is more interesting (one line of justification).

**[RULE DA.27]** Reflex fonts from `annexe-polices.md`: forbidden, unless justified in writing.

## The 3 directions (end of phase 1, stop B)

**[RULE DA.28]** The 3 directions **must** differ on axes 2 and 3 and on at least one other axis; A4 intended for print: axes 2, 3 and 4. A single call per axis gives a distinct value per direction (`tirer.py axes/2 3 <values>`). Axis 1 is the energy chosen at step C, kept by all 3 directions; on "I don't know", the draw decides only the order.

**[RULE DA.29]**

| # | Axis | Possible values |
|---|---|---|
| 1 | Energy (color strategy), chosen at step C | **Sober**: tinted light background; colored area (measured as in point 9 e of "Color") of 8% or more of the deliverable (except Typographic Sober, if the person chooses it). **Vivid**: light background, 3 to 5 vivid colors in fixed roles (point 9), banner or signature, cards with an edge rule, step chevrons, number tiles in solid color, cover in solid color; colored area of 10 to 30%. **Poster**: one saturated color; colored area of 30 to 60% (full-height column, half page, break backgrounds). **Dark** (only if the person asks for a dark or immersive look): tinted dark background, or a colored background on at least 60% of pages; ink and accent contrast with that background. |
| 2 | Display voice (cover, key figures, section words) | reading serif; display serif; bold grotesque; condensed; a single family in 2 weights; slab serif |
| 3 | Cover | typographic with a large white space; solid area on 60% with the title in reverse; full-frame image or map; giant number; reproduction of a document from the case |
| 4 | Grid | 12 columns; full-height column that carries the title; asymmetric one third, two thirds; modular |
| 5 | Charts | fine rules and one accent bar; thick bars and very large numbers; bright points and lines on a dark background |
| 6 | Images (3 at least, always: DA.94) | black and white; duotone ink and accent; natural color, full frame; thumbnails cropped into the grid |
| 7 | Navigation marker | page number alone in the footer; strip of sections in the footer, with the current section in accent; vertical running title in the margin; one tint of the accent per section |
| 8 | Page title | under a rule, top left; in the left column; above the chart, aligned with it; in capitals in the margin |
| 9 | Tables | horizontal rules only; header row in solid accent; light alternating bands; total in bold and column of figures on the right |

**[RULE DA.30]** **Compatibilities**: a draw that breaks a line below is redone with the label suffixed `/bis`.

**[RULE DA.31]** Axis 5 "bright on a dark background": requires axis 1 Dark and a structure whose background has a lightness below 0.35 (`annexe-palettes.md`: 3, 4, 6, 15, 21, 26, 30, 39); "bright" = light and saturated, never a halo.

**[RULE DA.32]** Axis 6 "cropped thumbnails" excludes axis 3 "full-frame image"; axis 3 "document from the case" requires a document supplied by the case.

**[RULE DA.33]** A4 intended for print: Sober, Vivid or Poster, without "bright on a dark background"; a full-page dark background (lightness below 0.35) is forbidden; Dark does not apply to an A4.

**[RULE DA.34]** Vivid and Poster: cover with a solid area of at least a quarter of the page; axis 3 "typographic with a large white space" allowed only with that solid area (wide banner, column).

**[RULE DA.35]** **The name of each direction**: an object from the subject or a real referent, never "modern" or "elegant"; plus 3 mood words and the object the accent comes from.

**[RULE DA.36]** **Lead: the contact sheet.**
1. Draws for the 3 directions: axes 2 to 9 (axis 1 comes from step C), palette, title and text fonts, hue shift.
2. A single order to `diapo-fabricant`: it reads "Color", "Typography", `annexe-polices.md`, `annexe-palettes.md` and `tirages.log`, produces for each direction `travail/directions/d<n>/` (`tokens.css`, a cover, a page with an annotated chart on the real subject), then assembles `travail/directions/planche.png`, in 3 columns.
3. You read only the contact sheet.

**[MUST DA.37]** **Contact sheet veto**: before showing it, look for 5 flaws per direction: cover title over more than 3 lines; text on a solid area unreadable at 960 px wide; palette dulled by the gamut; two neighboring font families (a grotesque with a humanist sans); dominant cover element unreadable as a thumbnail. Faulty direction: redone once, label `/bis`.

**[RULE DA.38]** After stop B, `diapo-fabricant` builds the complete charter of the chosen direction.

## Color: where it comes from (points 1 and 2)

**[RULE DA.39]** **1. Structure drawn from `annexe-palettes.md`, hue replaced.** Draw `d<n>/palette` among the lines of the chosen energy (Vivid: Sober and Poster lines with a light background). A line gives a structure (lightness, chroma, relations between hues), not colors to keep.

**[RULE DA.40]** **2. Target hue**: that of an object from the subject (material, product, packaging, client logo, document from the case), shifted by -30, -15, 0, +15 or +30 degrees per draw (`d<n>/decalage`). An emblematic color is welcome if it carries a meaning explained in one sentence (not the whole flag or folklore, unless asked); never the sector's default color without a reason. The charter writes down the object the hue comes from.

## What gives away AI (forbidden)

**[MUST DA.41]** Forbidden, checked by the art director and in part by `controles.py`:
- a cream background, with a contrasting serif title, an italic word and a terracotta accent;
- a decorative over-title that repeats the title (a step label useful for navigation, such as the name of the reference's step, remains allowed);
- decorative "01, 02, 03";
- a row of 3 identical cards, or of 3 big numbers (in Vivid, the solid key-number tiles are allowed, each in the color of its role);
- a thick bar on the left edge of a callout box (in Vivid, the card with a thin colored edge rule is allowed), decorative dots (not the status dot of point 9 f), rounded cards everywhere (the brand's corner radius, taken up as is, is allowed);
- filler icons, emojis;
- gradients, blur, frosted glass, CSS filters, drop shadows (except the soft shadow of a cut-out product, on the cover, included in the image by script);
- a centered paragraph, a bullet of 3 lines;
- the titles "Introduction", "Conclusion", "Thank you";
- 4 fonts in one deliverable, a hue outside the roles table, more hues on a page than the energy allows, more framed blocks than point 9 g allows, a page below the color floor (point 9 e);
- a pie chart, a 3D chart;
- "Lorem", forgotten dummy values.

# Builder's part

## Color: the construction (points 3 to 12)

**[RULE DA.42]** **3. Rotation**: the gap between the target hue and the line's accent hue is added to the hue of the 4 columns.

**[RULE DA.43]** **4. Gamut**: a script brings each color back into the sRGB gamut by lowering chroma; another line if the accent loses more than 0.04 chroma, or if the background of a Poster or a Dark loses more than 0.05.

**[RULE DA.44]** **5. The 9 roles**, computed by script in `tokens.css`:
- `fond`, `encre`, `accent`, `accent-2`: the 4 columns after rotation; `accent-2` never covers more than 10% of a page;
- `fond-rupture`: the accent in Poster and in Vivid; in Sober and in Dark, a swap of background and ink; reserved for break solid areas (point 9 h; A4: only Vivid and Poster);
- `accent-fonce`: hue of the accent, lightness shifted in steps of 0.02 until 4.5:1 on the background; colored text, rules, main series;
- `accent-clair`: a wash, almost white: the background's lightness minus 0.03 (0.95 at most), chroma a third of the accent's and 0.04 at most, never an intermediate tone (at lightness 0.79, a pink reads as dirty); on a dark background, lightness stays halfway between the background and the accent;
- `encre-secondaire`: the ink moved toward the background by a quarter of the lightness gap between the two;
- `filet`: the background, moved apart by 0.10 in lightness.

**[MUST DA.45]** **6. Contrasts**, measured by script: ink on background 7:1; secondary ink 4.5:1; text on an accent solid area 4.5:1; `accent-fonce` on background 4.5:1; very large titles 3:1.

**[RULE DA.46]** Before discarding a line on "text on an accent solid area", the script shifts the accent's lightness in steps of 0.02, by 0.10 at most, and keeps the first value that passes 4.5:1 with the background or with the ink; if a contrast still fails, another line is drawn.

**[RULE DA.47]** **7. Neutrals** tinted toward the accent: light background with the highest chroma the sRGB gamut allows, up to 0.04 (at lightness 0.97, often 0.013 to 0.02); ink with chroma 0.02 to 0.04. No pure white, no pure black, no pure gray.

**[RULE DA.48]** **8. Cream background** allowed only with a saturated accent that carries meaning; cream with terracotta or brick chosen by default: AI cliché, forbidden. Neutrals then warm, paler than the accent's hue, background chroma under 0.015.

**[RULE DA.49]** **9. Color on two levels** (it replaces the single ceiling of hues per page). a) **The brand signature is exempt from the ceiling** (multicolor banner, logo, official colors of a real brand).

**[RULE DA.50]** b) **The content follows the chosen energy.** Sober: 2 non-neutral hues at most per page. Vivid: all the colors of the declared palette, 5 at most (`accent`, `accent-2`, then 1 to 3 hues at least 40° apart, or the brand's official palette). Poster: one dominant color and an accent.

**[MUST DA.51]** c) **Color by role: the roles table** (role / color), written once in `05_charte.md`; each color is a token of `tokens.css`, it does not replace the 9 roles of point 5. Any hue outside this table is forbidden, each hue keeps the same meaning on all pages: this is the countermeasure to the rainbow. Sober: 2 hues, roles shared out.

**[RULE DA.52]** d) **The data carries the color**: any categorical variable (country, criterion, phase, cost nature) gets its color from the roles table and keeps it everywhere (headers, bars, Gantt, tiles, bullets); Sober and Poster: hues of the accent ordered by lightness.

**[MUST DA.53]** e) **Floor, not only ceiling**: Vivid and Poster, at least 3 color moments per page (signature, solid area or card with an edge rule, chart or figures in color) and a cover with a solid area of at least a quarter of the page; Sober, at least one clear color moment per page, key figures in the color of their role. Less than 3% colored area on a page: flaw, except for a Typographic Sober chosen and written in `05_charte.md`.

**[RULE DA.54]** **Measurement** of point 9 e, by the template's `controles.py` (P6.20), on each rendered page: share of pixels with OKLCH chroma above 0.04, photos excluded (numerator and denominator), written in `07_controles.md`. Floor of 3% page by page; the energy's range (axis 1) across all pages, and **maximum per sheet: 30% in Sober, 45% in Vivid, 75% in Poster**; vivid flat (chroma above 0.14) on 15% of a sheet at most in Sober, 20% in Vivid; overall 8 to 25% in Sober, 10 to 30% in Vivid, 30 to 60% in Poster. A flat of more than 1.5% of a sheet outside the roles table fails. In Vivid, under 10% across all pages blocks the phase 7 gate (`phase-7-controles.md`, P7.10b): plan the banner, the solid tiles and the section backgrounds from the charter on.

**[RULE DA.55]** f) **Status dots** (FACT, ASSUMPTION, TO VERIFY) allowed in Vivid, colors from the roles table only, one per block at most; the other uncertainty tags remain text. Never green, yellow or red added outside the palette.

**[RULE DA.56]** g) **Framed blocks**: 6 at most per page, 8 in Vivid.

**[RULE DA.57]** h) **Solid colored areas.** In Sober and in Vivid, the solid area goes to the cover, the decision page and the break pages, 25% of pages at most (except a dark or immersive look expressly requested); in Poster, half pages are added; in Vivid, color also takes the banner, the cards, the tiles and light solid areas. A break can be light (large accent rule, large title or large number): the solid area is never mandatory.

**[RULE DA.58]** Format exception: a Sober A4, printed or not, has a full-color page only for the cover; break and decision stay light, with no color at the page edge.

**[RULE DA.59]** Title banners follow their own rule: a solid banner behind the title of a content page, 10% of the height at most; otherwise the title is colored on the background, with a short rule.

**[RULE DA.60]** **10. Colors of meaning** (green = favorable, red = unfavorable, yellow = to watch): reserved, never added to the palette; they are used only if the roles table contains them, with that meaning and no other. If the table does not contain one, or if a hue of the palette is within 40° of it: sign and word instead. Meaning never rests on color alone; they are used for data, in small areas.

**[RULE DA.61]** Levels and statuses (risk, priority, step): intensity of the accent or a word, never a green, yellow or red dot next to each line (except the dot of point 9 f): a page of multicolored dots is the flaw the person notices first.

**[RULE DA.62]** **11. Color grammar**: one hue family per part of the argument, kept from the start to the end of the deliverable and from one deliverable to the next in a series; the charter writes it in one line ("hue A for analysis, hue B for choices, hue C for the decision"). Categorical variable of point 9 d: never a hue outside the roles table, limit of hues per page maintained.

**[MUST DA.63]** **12. Imposed brand** (brand palette, or the supplied charter of the company, client or school): this palette is the roles table; no draw in `annexe-palettes.md`, no hue shift (points 1 to 4), no color added.

**[RULE DA.64]** Each role takes a color from the imposed palette; if there are fewer colors than roles, roles share a color and are told apart by a word, a sign or intensity. The contrary requirements lapse: one hue per part (point 11, axis 7) exists only if the palette offers it; the 10% limit on `accent-2` does not apply between brand colors.

## Typography

**[RULE DA.65]** **1 to 3 families**, each with its role; the class of the display font comes from axis 2, correspondence with the catalog in `annexe-polices.md`.

**[RULE DA.66]** **Download**, by Python script, without an access key; files in `travail/polices/` (nothing is loaded from a website at render time).
- Google Fonts: `https://fonts.googleapis.com/css2?family=<Name+with+pluses>:wght@400;600;700`, called without a browser header, returns a CSS with full TTFs, only for the weights that exist; download each `fonts.gstatic.com` URL from the CSS. These TTFs are used for the PDF and installed for PowerPoint and LibreOffice.
- Fontshare [FS]: `https://api.fontshare.com/v2/css?f[]=<id>@400,700&display=swap` returns the CSS with the addresses to download.

**[RULE DA.67]** **Verification** by script, with `fontTools`: the font covers the characters of the deliverable language. French: `àâçéèêëîïôœùûüÿÀÂÇÉÈÊËÎÏÔŒÙÛÜ«»€%’` and the non-breaking space (the capital `Ÿ` is not tested: absent from the `latin` subset, no common French word uses it). English: `“”‘’€%`.

**[RULE DA.68]** **Tables of figures**: font with the `tnum` feature (GSUB table, read with fontTools) or same-width digits; otherwise the columns of figures go in the charter's mono.

**[RULE DA.69]** **Weights**: title font, only the weight used (Gloock, Young Serif, Rozha One, Gambarino and Tanker exist only in 400: the charter sets them in 400); text font, 400 and one weight from 600 to 700 (Cardo and Libre Caslon Text have only 700: that is enough). Fontshare does not return a 404 for a missing weight: the script counts the `@font-face` in the CSS received and compares them with the weights requested. Only a failure of weight 400 discards a font (another one from the same category is drawn). `html { font-synthesis: none }` in `tokens.css`, so that no fake bold is produced.

**[RULE DA.70]** **Three roles at most**: display font, readable text font, font for labels, tags and sources (fixed width or spaced capitals). One word of the cover title may go in italic and in color.

**[RULE DA.71]** **Expressive or rounded display font, bounded use**: cover title, large key figures, short section words. Sentence titles of pages in the text family, in bold: 70 characters and 2 lines at most.

**[RULE DA.72]** **Legibility of display figures**: render "1 I 0 O € 5" at 48 px in that font and compare the glyphs of each pair (1 and I, 0 and O, € and 5), by image difference or on the contact sheet; if they are confused, all the figures go in the text font.

**[RULE DA.73]** **Three levels per content page**: short label above (name of the step or section); title = the page's conclusion; visual object, "so what?" line, sources line.

**[RULE DA.74]** **No system fallback font**: the check verifies with `pdffonts` that the embedded fonts are those of the charter.

**[RULE DA.75]** **Size scale:**

| Element | Slide deck 1920 × 1080 px | A4 |
|---|---|---|
| Title | 64 to 80 px, 2 lines at most | 22 to 26 pt |
| Subtitle | 40 px | 14 pt |
| Text | 32 px | 10.5 to 11 pt |
| Table cells | 28 px | 9.5 pt |
| Chart labels | 24 px | 9 pt |
| Sources and notes | 22 px | 8.5 pt |
| Page number | 20 px | 8 pt |
| Cover and dividers | 120 to 160 px | 40 to 56 pt |
| Single number | 200 px | 72 pt |
| Giant cover number (axis 3) | 360 to 480 px | 140 to 200 pt |

**[RULE DA.76]** Size checks compare px read from the DOM, never pt read from the PDF: in Chromium's PDF, 1 px equals 0.75 pt.

**[RULE DA.77]** **Line spacing** 1.15 to 1.25 for titles, 1.4 to 1.5 for text; lines of 45 to 75 characters.

**[RULE DA.78]** **CSS**: `text-wrap: balance` on titles, `text-wrap: pretty` on paragraphs, `font-variant-numeric: tabular-nums` in tables, `white-space: nowrap` on numbers and on labels of 3 words or fewer, `<html lang>` in the deliverable language.

## Rhythm and layout templates

**[RULE DA.79]** **The 10 layout templates** (one per page): 1. **Cover**, a single dominant element; 2. **Summary**; 3. **Section divider**; 4. **Annotated chart** (chart on 60% of the width, reading alongside); 5. **Reference table**, full width; 6. **Comparison** (2 or 3 columns separated by rules, never cards, except the edge-rule cards of Vivid); 7. **Single number**; 8. **Image or map**; 9. **Path** (timeline strip, steps, flow); 10. **Decision**, 2 pages at most: page 1, the decision, the conditions, the cost and the gain, the stop criterion; page 2, the actions, the indicators, the first step at 30 days.

**[RULE DA.80]** **Cover** (template 1): product image never on a background of its own dominant color (a script measures the contrast between the two, 3:1 at least); image of about 55% of the width, soft shadow if it is cut out; 3 figures at most.

**[RULE DA.81]** **Rhythm**: never 3 pages in a row on the same template; after 2 dense pages, an airy page.

**[RULE DA.82]** A break page (divider, single number, image, decision) at the latest after 6 pages without a break, and 2 at least per deliverable (1 under 8 pages); it can be light, the solid break background is never mandatory (point 9 h) and exists only in slide decks and in Vivid or Poster A4.

**[RULE DA.83]** Beyond 12 pages, a divider opens each section.

**[RULE DA.84]** The last pages are the decision, never "Thank you" or "Questions?"; the appendices follow.

## Charts

**[RULE DA.85]**

| Question | Form |
|---|---|
| Compare items | sorted horizontal bars; aligned dots beyond 10 |
| Show a trend | line, label at the end of the line |
| Show the share of a whole | 100% bar, or the number in large type |
| Compare to a target | bullet chart |
| Break down a total | waterfall |
| Rank on 2 criteria | 2 × 2 matrix, graduated axes |
| Show size and composition | Marimekko, or stacked bars |
| Locate a place | flat map with a single colored region |
| Phase | timeline strip or Gantt, dated milestones, one owner per line |
| Show a link between two variables | scatter plot, key points named |
| Put figures on a project | projection table, fine rules, total in bold |

**[RULE DA.86]** Title = conclusion, the point that proves it **annotated on the chart**.

**[RULE DA.87]** The message's series in `accent-fonce`, the others in secondary ink; 3 to 5 series: hues of the accent ordered by lightness; Vivid: categorical variable in the colors of the roles table (point 9 d).

**[RULE DA.88]** Labels placed on the data; bars from zero; no dual axis, no frame; chart on 55% of the usable area at least.

**[MUST DA.89]** **Each chart is an SVG generated by script from `travail/donnees.csv`**: a value absent from the file is not displayed; no matplotlib, no canvas.

**[RULE DA.90]** Unit, year and source underneath; a chart without a message is replaced by a single number.

## Images

**[RULE DA.91]** **At least 2 pages out of 3** carry a chart, a diagram, a map or an image.

**[RULE DA.92]** **The photo first, the hue after**: first choose, when possible, the cover image (object, material or place of the subject), then take the accent from that photo: the color is then explained in one sentence.

**[TIP DA.93]** Light grain texture on large solid areas, against the template effect.

**[MUST DA.94]** **At least 3 real, relevant images in any deliverable**, unless told otherwise: royalty-free and sourced (Unsplash, Pexels, Wikimedia Commons, or the brand's official site, cited); proof or marker, never decoration (places, products, documents from the case, people at work), one of them on the cover if the direction allows it; on the subject, recent if possible; to compare options, a diptych of the same height and the same format. Zero images: SEVERE flaw for the art director; a deliverable made mostly of tables: MEDIUM. **A page with a large white space** gets an image or a visual (diagram, map, large number), never stretched text (`phase-6-fabrication.md`, P6.21).

**[RULE DA.95]** **Sources**, downloaded by Python script: files supplied by the person; Wikimedia Commons, keyless API (`https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&prop=imageinfo&iiprop=url|extmetadata&format=json`), which gives the author and the license, with a one-second pause between two requests (otherwise error 429); official product visuals of a real brand, taken from its site, credit "© brand"; Natural Earth for maps (`https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip`), drawn as SVG; Unsplash and Pexels (free license), with the author and the address of the photo's page; a single family of pictograms (Lucide or Phosphor), for a category that recurs.

**[RULE DA.96]** **Credit** in `travail/credits.md`, and under the image.

**[MUST DA.97]** **Forbidden**: generated image imitating a photo; generic stock photo (handshake, light bulb, rocket); national folklore, unless asked.

**[RULE DA.98]** **A single image treatment** for the whole deliverable, applied by script, never by a CSS filter. **Text on image**: plain veil in the ink color, at 55 to 70%, or a calm area; contrast measured on the result. **Each image is used only once** and proves one idea of its page.
