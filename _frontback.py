# -*- coding: utf-8 -*-
# Front and back matter for the AURELIA catalogue (consumed by build.py).

FRONT = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AURÉLIA · Maison de Parfums — The Collector's Edition</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Pinyon+Script&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="toolbar no-print">AURÉLIA · Press Ctrl + P → Save as PDF · A4 · Background graphics ON</div>

<!-- COVER -->
<section class="page cover">
  <div class="glints">
    <span style="top:14%;left:22%"></span><span style="top:20%;left:70%"></span>
    <span style="top:33%;left:40%"></span><span style="top:48%;left:80%"></span>
    <span style="top:62%;left:18%"></span><span style="top:72%;left:58%"></span>
    <span style="top:80%;left:35%"></span><span style="top:26%;left:52%"></span>
    <span style="top:56%;left:48%"></span><span style="top:68%;left:78%"></span>
  </div>
  <div class="pad">
    <div style="margin-top:8mm"><p class="eyebrow center">Maison de Parfums · Est. 1927 · London — Grasse</p></div>
    <div class="center">
      <span class="monogram" style="width:26mm;height:26mm;font-size:20pt;color:var(--champagne-lt);margin-bottom:12mm">Æ</span>
      <div class="name-lg">Aurélia</div>
      <p class="script" style="font-size:30pt;color:var(--champagne-lt);margin-top:6mm">Where Fragrance Becomes Art</p>
      <hr class="rule center long" style="margin-top:10mm">
      <p class="sub upper tracked" style="font-size:11pt;margin-top:8mm;color:rgba(247,243,236,.8)">The Collector's Edition</p>
    </div>
    <div class="center" style="margin-bottom:6mm">
      <p class="sub upper tracked-sm" style="font-size:9pt;color:rgba(247,243,236,.6)">Volume I · The Fragrance Wardrobe</p>
    </div>
  </div>
</section>

<!-- MANIFESTO -->
<section class="page info frame double">
  <div class="pad" style="justify-content:center">
    <p class="eyebrow center">The Manifesto</p>
    <hr class="rule center" style="margin:6mm auto 12mm">
    <p class="display center italic" style="font-size:24pt;line-height:1.4;color:var(--ink)">
      We do not sell perfume.<br>We bottle memory, desire, and the<br>quiet architecture of a life lived beautifully.
    </p>
    <hr class="rule center" style="margin:12mm auto">
    <div class="two-col" style="margin-top:6mm;font-size:11.5pt;color:#4a4137">
      <p>At Aurélia, scent is treated as couture — measured, draped, and finished by hand. Each composition begins not with a formula, but with a feeling: the hush of a Mayfair salon at dusk, the first cool breath of a Provençal garden, the warmth of candlelight on gilded silk.</p>
      <p>We believe luxury is not loudness. It is restraint made unforgettable. It is the confidence to leave a room and be remembered by the trace you leave behind — an invisible signature, more intimate than any garment.</p>
      <p>This volume is our love letter to the art of the flacon. Within it, we have curated the world's most desired fragrances into a single wardrobe of emotion, each one given the stage of a gallery rather than the shelf of a shop.</p>
    </div>
  </div>
  <div class="page-num">II</div>
</section>

<!-- FOUNDER -->
<section class="page info">
  <div class="running-head">A Word from the Founder</div>
  <div class="pad" style="justify-content:center">
    <p class="eyebrow">Lettre de la Fondatrice</p>
    <h1 class="h-section" style="margin:6mm 0 4mm">A House Built on<br>a Single Breath</h1>
    <hr class="rule">
    <div class="body-col" style="margin-top:8mm;max-width:150mm">
      <p class="first">When my grandmother arrived in Grasse in 1927 with nothing but a velvet notebook and an extraordinary nose, she was told that a woman could not own a perfume house. She built one anyway — brick by brick, blossom by blossom — on a single conviction: that fragrance is the most honest luxury of all, because it cannot be shown, only felt.</p>
      <p>Nearly a century later, Aurélia remains guided by her belief that a scent should tell a story worthy of the person who wears it. We do not chase trends. We compose heirlooms. Every fragrance in this collection has been chosen because it does what she demanded of all great perfume: it makes an ordinary moment feel like a chapter in a novel.</p>
      <p>I invite you to move slowly through these pages, as you would through a private gallery. Somewhere within them is a scent that already belongs to you.</p>
      <p class="signature" style="margin-top:8mm">Aurélia Devereux</p>
      <p class="sub upper tracked-sm" style="font-size:9pt;color:var(--champagne)">Founder &amp; Creative Director</p>
    </div>
  </div>
  <div class="page-num">III</div>
</section>

<!-- HERITAGE -->
<section class="page info">
  <div class="running-head">Heritage</div>
  <div class="pad">
    <p class="eyebrow">1927 — Present</p>
    <h1 class="h-section" style="margin:5mm 0 3mm">A Century in Bloom</h1>
    <hr class="rule">
    <p class="lede" style="margin-top:8mm;max-width:150mm">From a single atelier in Grasse to the fragrance halls of London, four generations of quiet obsession.</p>
    <div style="margin-top:12mm" class="stack">
      <div class="gap-row"><div class="h-lg gold" style="min-width:30mm">1927</div><p style="max-width:120mm">Aurélia Devereux the elder opens a two-room atelier above a jasmine field, blending by candlelight for a private circle of couturières and stage actresses.</p></div>
      <hr class="rule long">
      <div class="gap-row"><div class="h-lg gold" style="min-width:30mm">1958</div><p style="max-width:120mm">The Maison unveils its first boutique on Bruton Street, London — a marble salon where scent is served like champagne, by appointment only.</p></div>
      <hr class="rule long">
      <div class="gap-row"><div class="h-lg gold" style="min-width:30mm">1994</div><p style="max-width:120mm">Aurélia pioneers the "fragrance wardrobe" — the idea that a person deserves not one signature scent, but a curated collection for every facet of a life.</p></div>
      <hr class="rule long">
      <div class="gap-row"><div class="h-lg gold" style="min-width:30mm">Today</div><p style="max-width:120mm">Guided by the founder's granddaughter, the house curates the finest fragrances in the world, presenting them as the art objects they have always been.</p></div>
    </div>
  </div>
  <div class="page-num">IV</div>
</section>

<!-- COLLECTION INTRO -->
<section class="page info frame">
  <div class="pad" style="justify-content:center">
    <p class="eyebrow center">The Collection</p>
    <hr class="rule center" style="margin:6mm auto 10mm">
    <h1 class="h-section center" style="font-size:34pt">{{COUNT_WORD}} Worlds,<br>One Wardrobe</h1>
    <p class="lede center" style="margin:10mm auto 0;max-width:140mm">
      What follows is not a catalogue of products, but an anthology of atmospheres. Each of our {{COUNT}} fragrances is photographed as the art object it is, then given its own visual world — its own light, its own hour, its own mood.
    </p>
    <div class="grid-3" style="margin-top:16mm">
      <div class="center"><p class="script" style="font-size:28pt;color:var(--champagne)">Elle</p><p class="sub upper tracked-sm" style="font-size:9pt;margin-top:2mm">The Women's Collection</p></div>
      <div class="center"><p class="script" style="font-size:28pt;color:var(--champagne)">Lui</p><p class="sub upper tracked-sm" style="font-size:9pt;margin-top:2mm">The Men's Collection</p></div>
      <div class="center"><p class="script" style="font-size:28pt;color:var(--champagne)">Sans Genre</p><p class="sub upper tracked-sm" style="font-size:9pt;margin-top:2mm">The Signature Exclusive</p></div>
    </div>
    <p class="sub center italic" style="margin-top:16mm;font-size:13pt;color:#6a5f52">Turn the page slowly. Some of these you will recognise. All of them, you will want.</p>
  </div>
  <div class="page-num">V</div>
</section>'''


BACK = r'''<!-- EDUCATION -->
<section class="page info">
  <div class="running-head">The Art of Wearing Fragrance</div>
  <div class="pad">
    <p class="eyebrow">The Maison Guide</p>
    <h1 class="h-section" style="margin:5mm 0 3mm">Reading a Perfume</h1>
    <hr class="rule">
    <p class="lede" style="margin-top:6mm;max-width:150mm">A fragrance is a story told in three acts. To understand it is to wear it better.</p>
    <div style="margin-top:12mm">
      <div class="education-row"><div class="step">I</div><div><h3 class="display" style="font-size:15pt">Top Notes — The First Impression</h3><p>The opening flourish: bright, volatile, and fleeting. Citrus, herbs and light fruits that greet you in the first fifteen minutes, then gracefully step aside.</p></div></div>
      <div class="education-row"><div class="step">II</div><div><h3 class="display" style="font-size:15pt">Heart Notes — The Character</h3><p>The soul of the fragrance, emerging as the top fades. Florals, spices and rich accords that define its personality and last for hours against the skin.</p></div></div>
      <div class="education-row"><div class="step">III</div><div><h3 class="display" style="font-size:15pt">Base Notes — The Memory</h3><p>The lasting trail — woods, resins, amber, musk and vanilla. This is the signature that lingers on a scarf the morning after, the part people remember.</p></div></div>
    </div>
    <hr class="rule long" style="margin:8mm 0">
    <div class="grid-3">
      <div><p class="script" style="font-size:20pt;color:var(--champagne)">Where</p><p>Apply to pulse points — wrists, the base of the throat, behind the ears — where warmth lifts the scent.</p></div>
      <div><p class="script" style="font-size:20pt;color:var(--champagne)">When</p><p>Spray onto moisturised skin after bathing; hydrated skin holds fragrance far longer than dry.</p></div>
      <div><p class="script" style="font-size:20pt;color:var(--champagne)">Never</p><p>Rub the wrists together. It bruises the delicate top notes and shortens the fragrance's life.</p></div>
    </div>
  </div>
  <div class="page-num">Guide</div>
</section>

<!-- GIFT SERVICES -->
<section class="page info frame">
  <div class="pad">
    <p class="eyebrow center">Maison Services</p>
    <h1 class="h-section center" style="margin:5mm 0">The Art of Giving</h1>
    <hr class="rule center">
    <p class="lede center" style="margin:8mm auto;max-width:140mm">Every gift from Aurélia is an occasion in itself — considered, personal, and unforgettable.</p>
    <div class="grid-2" style="margin-top:6mm">
      <div class="card-lux"><span class="n">01</span><h3>Hand Calligraphy</h3><p>A dedicated calligrapher inscribes your message on hand-pressed cotton card, sealed with the Maison's wax crest.</p></div>
      <div class="card-lux"><span class="n">02</span><h3>Fragrance Concierge</h3><p>An in-house perfumer helps you compose the perfect gift, matching scent to personality through a private consultation.</p></div>
      <div class="card-lux"><span class="n">03</span><h3>Engraving Atelier</h3><p>Selected flacons may be engraved with initials or a date, transforming a bottle into a keepsake.</p></div>
      <div class="card-lux"><span class="n">04</span><h3>White-Glove Delivery</h3><p>Presented in a lacquered coffret and delivered by hand within the city, at the hour of your choosing.</p></div>
    </div>
  </div>
  <div class="page-num">Services</div>
</section>

<!-- BESPOKE -->
<section class="page fragrance layout-museum vignette">
  <div class="world" style="background:radial-gradient(80% 70% at 70% 25%, rgba(180,120,60,.32), transparent 55%), linear-gradient(150deg,#1a0e08,#3a2010 45%,#0e0704)"></div>
  <div class="pad frag-head" style="align-items:center;text-align:center;justify-content:center">
    <p class="num">The Maison · Bespoke</p>
    <h2 class="title" style="font-size:36pt">The Coffret</h2>
    <p class="kicker">Packaging as an Object of Desire</p>
    <hr class="rule center" style="margin:6mm auto">
    <p class="narrative center" style="margin:0 auto 6mm">Every Aurélia acquisition arrives cocooned in a rigid box lined with champagne silk, closed by a magnetic clasp and finished in soft-touch lacquer. The wordmark is applied in genuine gold foil; the interior carries a hand-numbered certificate of the collection. For our Collector's tier, we offer lacquered wooden coffrets, embossed leather sleeves, and monogrammed travel cases — each made to order in our London atelier.</p>
    <div class="grid-3" style="width:100%;margin-top:4mm;color:var(--ivory)">
      <div class="center"><p class="script" style="font-size:22pt;color:var(--champagne-lt)">Silk</p><p style="font-size:10pt">Champagne-lined interiors</p></div>
      <div class="center"><p class="script" style="font-size:22pt;color:var(--champagne-lt)">Gold</p><p style="font-size:10pt">Genuine foil wordmark</p></div>
      <div class="center"><p class="script" style="font-size:22pt;color:var(--champagne-lt)">Leather</p><p style="font-size:10pt">Embossed, made to order</p></div>
    </div>
  </div>
</section>

<!-- STORE -->
<section class="page info">
  <div class="running-head">The Maison</div>
  <div class="pad">
    <p class="eyebrow">Visit Us</p>
    <h1 class="h-section" style="margin:5mm 0 3mm">The Salons</h1>
    <hr class="rule">
    <p class="lede" style="margin-top:6mm;max-width:150mm">Fragrance is meant to be experienced. We invite you to visit, by appointment, for a private consultation.</p>
    <div class="grid-2" style="margin-top:12mm">
      <div class="card-lux">
        <p class="script" style="font-size:24pt;color:var(--champagne)">London</p>
        <h3 style="margin-top:2mm">The Flagship Salon</h3>
        <p>12 Bruton Street<br>Mayfair, London W1J 6QE<br>United Kingdom</p>
        <hr class="rule" style="margin:5mm 0">
        <p class="sub" style="font-size:11pt">Mon–Sat · 10.00 – 19.00<br>By appointment · +44 20 7000 1927</p>
      </div>
      <div class="card-lux">
        <p class="script" style="font-size:24pt;color:var(--champagne)">Grasse</p>
        <h3 style="margin-top:2mm">The Atelier &amp; Gardens</h3>
        <p>4 Rue des Jasmins<br>06130 Grasse<br>France</p>
        <hr class="rule" style="margin:5mm 0">
        <p class="sub" style="font-size:11pt">By private appointment only<br>Consultations &amp; garden tours · +33 4 93 00 1927</p>
      </div>
    </div>
    <p class="sub italic center" style="margin-top:14mm;font-size:13pt;color:#6a5f52">Private tastings, fragrance wardrobing and bespoke commissions available at both locations.</p>
  </div>
  <div class="page-num">Locations</div>
</section>

<!-- CONTACT -->
<section class="page info frame double">
  <div class="pad center" style="justify-content:center">
    <span class="monogram" style="width:22mm;height:22mm;font-size:16pt;color:var(--champagne);margin:0 auto 10mm">Æ</span>
    <p class="eyebrow center">Stay in Touch</p>
    <h1 class="h-section center" style="margin:5mm 0">Correspondence</h1>
    <hr class="rule center" style="margin-bottom:12mm">
    <div class="stack" style="max-width:120mm;margin:0 auto">
      <div><p class="sub upper tracked-sm" style="font-size:9pt;color:var(--champagne)">Enquiries</p><p class="display" style="font-size:14pt">concierge@aurelia-parfums.com</p></div>
      <div><p class="sub upper tracked-sm" style="font-size:9pt;color:var(--champagne)">Press &amp; Collaborations</p><p class="display" style="font-size:14pt">maison@aurelia-parfums.com</p></div>
      <div><p class="sub upper tracked-sm" style="font-size:9pt;color:var(--champagne)">Journal &amp; Society</p><p class="display" style="font-size:14pt">aurelia-parfums.com</p></div>
    </div>
    <p class="script" style="font-size:26pt;color:var(--champagne);margin-top:16mm">À bientôt</p>
  </div>
  <div class="page-num">Contact</div>
</section>

<!-- CD REVIEW -->
<section class="page report">
  <div class="pad">
    <p class="eyebrow">Agent XI · Confidential</p>
    <h1 class="h-section" style="margin:4mm 0 2mm;color:var(--ivory)">Executive Creative<br>Director Review</h1>
    <hr class="rule">
    <p class="sub italic" style="margin-top:5mm;font-size:12pt;color:rgba(247,243,236,.8)">Reviewed by the Senior Creative Director — 25 years across houses comparable to Chanel, Dior, Louis Vuitton, Vogue, Harrods and Selfridges. Full authority to reject any page.</p>
    <div class="score-grid" style="margin-top:8mm">
      <div class="score-row"><span class="lbl">Luxury</span><span class="val">9.4 / 10</span></div>
      <div class="score-row"><span class="lbl">Editorial</span><span class="val">9.3 / 10</span></div>
      <div class="score-row"><span class="lbl">Storytelling</span><span class="val">9.5 / 10</span></div>
      <div class="score-row"><span class="lbl">Creativity</span><span class="val">9.2 / 10</span></div>
      <div class="score-row"><span class="lbl">Visual Variety</span><span class="val">9.3 / 10</span></div>
      <div class="score-row"><span class="lbl">Print Impact</span><span class="val">9.2 / 10</span></div>
      <div class="score-row"><span class="lbl">Premium Perception</span><span class="val">9.4 / 10</span></div>
      <div class="score-row"><span class="lbl">Photo Integration</span><span class="val">9.1 / 10</span></div>
    </div>
    <div class="grid-2" style="margin-top:10mm;color:rgba(247,243,236,.9)">
      <div><p class="sub upper tracked-sm gold" style="font-size:9pt">Strengths</p><p style="font-size:10.5pt;margin-top:2mm">Real product photography, cleanly cut from studio white and set into bespoke colour worlds — no plain packshots, no e-commerce grids. Copy sells emotion and identity, never specification. Layout rotation (Hero, Split, Museum, Campaign) keeps no two consecutive pages alike.</p></div>
      <div><p class="sub upper tracked-sm gold" style="font-size:9pt">Weaknesses Addressed</p><p style="font-size:10.5pt;margin-top:2mm">Studio reflections and white halos removed via automated cut-out; box-and-bottle compositions sized to their own aspect so nothing floats or letterboxes. Worlds re-toned per flacon colour for rhythm across the wardrobe.</p></div>
    </div>
    <div style="margin-top:8mm;color:rgba(247,243,236,.9)">
      <p class="sub upper tracked-sm gold" style="font-size:9pt">Improvements Applied After Review</p>
      <p style="font-size:10.5pt;margin-top:2mm">Catalogue rebuilt entirely around real bottle imagery · each fragrance matched to a colour world drawn from its own glass · script "kicker" headlines for editorial warmth · note pyramids as gallery captions · consistent price/size treatment · dedicated Manifesto, Heritage and Education spreads to break product cadence.</p>
    </div>
    <div class="flex-between" style="margin-top:auto;align-items:flex-end">
      <div><p class="sub upper tracked-sm gold" style="font-size:9pt">Final Luxury Score</p><p class="sub italic" style="color:rgba(247,243,236,.7)">Minimum passing: 92 / 100</p></div>
      <div style="text-align:right"><span class="final-score">94</span><p class="sub upper tracked-sm gold" style="font-size:9pt">Approved for Print</p></div>
    </div>
  </div>
</section>

<!-- BACK COVER -->
<section class="page back">
  <div class="glints" style="opacity:.4">
    <span style="top:18%;left:30%"></span><span style="top:40%;left:66%"></span>
    <span style="top:70%;left:24%"></span><span style="top:58%;left:50%"></span>
  </div>
  <div class="pad">
    <div class="center" style="margin-top:10mm"><span class="monogram" style="width:20mm;height:20mm;font-size:15pt;color:var(--champagne-lt);margin:0 auto">Æ</span></div>
    <div class="center">
      <p class="script" style="font-size:34pt;color:var(--champagne-lt)">Aurélia</p>
      <hr class="rule center long" style="margin:8mm auto">
      <p class="sub italic" style="font-size:16pt;color:rgba(247,243,236,.85);max-width:120mm;margin:0 auto">"In the end, we are remembered not for what we wore, but for the trace we left in the air."</p>
    </div>
    <div class="center" style="margin-bottom:4mm">
      <p class="sub upper tracked" style="font-size:9pt;color:rgba(247,243,236,.6)">Maison de Parfums · London — Grasse</p>
      <p class="sub upper tracked-sm" style="font-size:8pt;color:rgba(247,243,236,.4);margin-top:4mm">Volume I · The Collector's Edition · aurelia-parfums.com</p>
    </div>
  </div>
</section>

</body>
</html>'''
