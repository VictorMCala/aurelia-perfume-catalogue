# -*- coding: utf-8 -*-
"""Generate catalogue.html from the real bottle images in /images.
Data-driven: each fragrance = one real cut-out photo + world + copy + notes."""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")

# ---------- fragrance data (driven by the real images we have) ----------
F = [
 # WOMEN
 dict(slug="armani-power-of-you", house="Emporio Armani", title="Power of You", kicker="Her Strength, Made Visible",
      collection="women", layout="hero", family="Amber Floral", size="100 ml EDP", eur="€95", czk="≈ 2 320 Kč",
      top="Raspberry · Pink Pepper", heart="Jasmine · Peony", base="Vanilla · Tonka · Patchouli",
      world="radial-gradient(90% 80% at 30% 20%, rgba(190,80,120,.5), transparent 55%), linear-gradient(150deg,#3a0f22,#6a1a38 45%,#200a14)",
      text=("A fragrance about the quiet power of belonging to no one but yourself. A juicy burst of raspberry and "
            "pink pepper opens like a smile that means it, before a couture heart of jasmine and peony gives way to a "
            "warm base of vanilla, tonka and patchouli. Power of You is worn by the woman who walks into her own life "
            "as if she designed it — because she did. Bold, romantic and utterly self-possessed, it turns confidence "
            "into something you can wear on the skin.")),
 dict(slug="black-opium", house="Yves Saint Laurent", title="Black Opium", kicker="Midnight, Poured Over Coffee",
      collection="women", layout="museum", family="Amber Vanilla", size="90 ml EDP", eur="€140", czk="≈ 3 430 Kč",
      top="Pear · Pink Pepper", heart="Coffee · Jasmine · Orange Blossom", base="Vanilla · Patchouli · Cedar",
      world="radial-gradient(80% 70% at 70% 20%, rgba(198,161,91,.4), transparent 55%), linear-gradient(150deg,#0a0908,#241a12 45%,#070605)",
      text=("A shot of black coffee laced with vanilla and white flowers — the scent of the after-hours, of a leather "
            "jacket thrown over an evening gown, of a city that never quite goes to sleep. Adrenalising and addictive, "
            "it belongs to the woman who is the last to leave and the first thing everyone remembers. Warm, dark and "
            "gloriously unrepentant, Black Opium is not about being good. It is about being unforgettable — a glittering "
            "flacon that catches the light exactly as she does.")),
 dict(slug="crystal-noir", house="Versace", title="Crystal Noir", kicker="A Dark Flower in Bloom",
      collection="women", layout="split", family="Amber Floral", size="90 ml EDP", eur="€72", czk="≈ 1 760 Kč",
      top="Ginger · Cardamom · Pepper", heart="Gardenia · Orange Blossom · Coconut", base="Amber · Sandalwood · Musk",
      world="radial-gradient(85% 75% at 30% 20%, rgba(198,161,91,.38), transparent 55%), linear-gradient(150deg,#100e0c,#2a2118 45%,#080706)",
      text=("Mysterious and enveloping, Crystal Noir wraps a luminous gardenia in spice and shadow. Ginger and pepper "
            "spark at the opening; a velvety heart of gardenia, orange blossom and coconut milk glows at its centre; "
            "amber, sandalwood and musk close it like the hush of a private box at the opera. Housed in smoked black "
            "crystal edged with gold, it is the scent of a woman who keeps a little of herself back — elegant, sensual "
            "and quietly magnetic. Beauty with a secret it has no intention of telling.")),
 dict(slug="good-girl-blush", house="Carolina Herrera", title="Good Girl Blush", kicker="Sweetness with a Sharp Heel",
      collection="women", layout="museum", family="Amber Floral", size="80 ml EDP", eur="€120", czk="≈ 2 940 Kč",
      top="Bergamot · Pink Pepper", heart="Tuberose · Ylang-Ylang", base="Vanilla · Sandalwood · Musk",
      world="radial-gradient(85% 75% at 70% 22%, rgba(210,140,160,.45), transparent 55%), linear-gradient(150deg,#2a1620,#5a2a3e 45%,#180b12)",
      text=("The softer, sunnier sister — femininity dialled to a warm blush. Bright bergamot and pink pepper lift a "
            "creamy heart of tuberose and ylang-ylang, cushioned by vanilla, sandalwood and musk. Poised in its iconic "
            "cobalt stiletto rendered in rose, Good Girl Blush belongs to the woman who is tender and formidable in the "
            "same breath. She dresses for herself, laughs a little too loudly on purpose, and leaves a trail that lingers "
            "in the lift long after the doors have closed.")),
 dict(slug="la-vie-est-belle", house="Lancôme", title="La Vie Est Belle", kicker="The Choice of Happiness",
      collection="women", layout="hero", family="Sweet Gourmand", size="100 ml EDP", eur="€125", czk="≈ 3 060 Kč",
      top="Blackcurrant · Pear", heart="Iris · Jasmine · Orange Blossom", base="Praline · Vanilla · Tonka · Patchouli",
      world="radial-gradient(90% 80% at 30% 20%, rgba(230,180,190,.4), transparent 55%), linear-gradient(150deg,#3a2028,#6a3a44 45%,#22121a)",
      text=("A declaration in a bottle: beauty is a decision, and joy is a form of courage. A noble iris — one of the "
            "most precious materials in perfumery — is wrapped in sweet praline, vanilla and patchouli, luminous and "
            "endlessly comforting. La Vie Est Belle is worn by the woman who has chosen contentment on her own terms, "
            "who finds glamour in ordinary Tuesdays. Its crystal smile of a flacon says everything: life is beautiful, "
            "and she intends to enjoy every last drop of it.")),
 dict(slug="libre", house="Yves Saint Laurent", title="Libre", kicker="The Scent of Freedom, Tailored",
      collection="women", layout="split", family="Floral Lavender", size="90 ml EDP", eur="€135", czk="≈ 3 300 Kč",
      top="Lavender · Mandarin", heart="Orange Blossom · Jasmine", base="Vanilla · Musk · Ambergris",
      world="radial-gradient(90% 80% at 70% 20%, rgba(120,150,220,.35), transparent 55%), linear-gradient(150deg,#141b2e,#2a2140 45%,#0c1020)",
      text=("The tension between two icons: the cool lavender of a man's dressing table and the warm sensuality of "
            "Moroccan orange blossom. Libre is the fragrance of a woman who does exactly as she pleases and makes it look "
            "like generosity. Vanilla and musk smoulder beneath a crisp, almost architectural top — freedom given "
            "structure, rebellion given couture. She wears a tuxedo to the wedding and outshines the bride. Liberty, it "
            "reminds us, is not the absence of rules, but the confidence to write your own.")),
 dict(slug="miss-dior", house="Christian Dior", title="Miss Dior", kicker="A Love Letter in Roses",
      collection="women", layout="museum", family="Floral", size="100 ml EDP", eur="€150", czk="≈ 3 670 Kč",
      top="Bergamot · Blood Orange", heart="Grasse Rose · Peony", base="Musk · Woods",
      world="radial-gradient(85% 75% at 30% 20%, rgba(230,170,190,.42), transparent 55%), linear-gradient(150deg,#2e1a22,#5a2e3c 45%,#1a0e14)",
      text=("Tied with its couture bow, Miss Dior is romance made modern. A sparkling burst of bergamot lifts a heart of "
            "Grasse rose and peony — grown in Dior's own fields — before a soft, luminous base of musk and woods settles "
            "against the skin. It is the fragrance of first love and last dances, of a woman who is delicate and daring "
            "at once. Feminine without apology, timeless without effort, it turns every wearer into the heroine of her "
            "own quietly extraordinary story.")),
 dict(slug="paradoxe", house="Prada", title="Paradoxe Intense", kicker="A Woman in Constant Reinvention",
      collection="women", layout="split", family="Amber Floral", size="90 ml EDP", eur="€145", czk="≈ 3 550 Kč",
      top="Neroli · Bergamot", heart="Jasmine · Orange Blossom", base="Amber · Vanilla · Musk",
      world="radial-gradient(90% 80% at 70% 20%, rgba(240,150,110,.45), transparent 55%), linear-gradient(150deg,#3a1c16,#7a3a26 45%,#1c0e0a)",
      text=("A fragrance that refuses to sit still. Neroli sparkles at the top, a golden heart of jasmine and orange "
            "blossom glows at the centre, and a warm base of amber, vanilla and musk keeps it close to the skin — a "
            "portrait of a woman who is many things at once and apologises for none of them. Poured into its striking "
            "coral triangle, Paradoxe Intense is minimalist yet sensual, clean yet magnetic. She is a walking "
            "contradiction, and it is precisely her most beautiful quality.")),
 dict(slug="valentino-vendetta", house="Valentino", title="Born In Roma · Intense", kicker="Ancient City, Future Attitude",
      collection="women", layout="campaign", family="Amber Floral", size="100 ml EDP", eur="€130", czk="≈ 3 180 Kč",
      top="Blackcurrant · Bergamot", heart="Jasmine Grandiflorum · Iris", base="Vanilla Bourbon · Leather · Amber",
      world="radial-gradient(90% 80% at 30% 22%, rgba(180,40,70,.5), transparent 55%), linear-gradient(150deg,#2a0c16,#6a1428 45%,#160610)",
      text=("Sealed beneath its bold crimson V, this is the eternal city seen through studded couture. Blackcurrant and "
            "bergamot crack open over a heart of jasmine grandiflorum and iris, before a smooth, addictive base of "
            "vanilla bourbon, leather and amber. Reverent of the past and entirely unafraid of the future, it belongs to "
            "the woman who wears trainers to the opera and somehow looks more elegant for it. Bold, magnetic and "
            "unmistakably now — a modern Roman holiday in a single spray.")),
 # MEN
 dict(slug="born-in-roma-uomo", house="Valentino", title="Uomo Born In Roma", kicker="The Modern Roman",
      collection="men", layout="museum", family="Aromatic Fougère", size="100 ml EDT", eur="€110", czk="≈ 2 690 Kč",
      top="Ginger · Violet Leaf", heart="Vetiver · Clary Sage", base="Tonka · Woods · Mineral Accord",
      world="radial-gradient(85% 75% at 30% 20%, rgba(150,60,60,.35), transparent 55%), linear-gradient(150deg,#1a0e0c,#3a1a18 45%,#0c0605)",
      text=("Heritage and rebellion, cast in studded black and oxblood glass. A cool jolt of ginger and violet leaf "
            "opens over an aromatic heart of vetiver and clary sage, grounded by tonka, woods and a clean mineral accord "
            "that feels like marble under midday sun. Uomo Born In Roma is worn by the man who honours where he comes "
            "from and answers only to where he is going. Contemporary, confident and quietly commanding — the eternal "
            "city dressed for a very modern night.")),
 dict(slug="le-male-le-parfum", house="Jean Paul Gaultier", title="Le Male Le Parfum", kicker="Seduction, Turned Up",
      collection="men", layout="split", family="Amber Spicy", size="125 ml EDP Intense", eur="€110", czk="≈ 2 690 Kč",
      top="Cardamom", heart="Lavender", base="Vanilla · Benzoin · Amber Woods",
      world="radial-gradient(90% 80% at 70% 20%, rgba(90,120,200,.4), transparent 55%), linear-gradient(150deg,#0c1428,#1e2c4a 45%,#070c18)",
      text=("The iconic sailor, stripped to pure temptation. Spicy cardamom flares over the house's signature lavender "
            "before a sumptuous base of vanilla, benzoin and amber woods pulls everything close and warm. Cast in deep "
            "midnight blue, Le Male Le Parfum is unapologetically sensual — the fragrance of a man who knows the effect "
            "he has and wears it lightly. Bold, addictive and impossibly smooth, it is charisma bottled: the last thing "
            "you notice before the night gets interesting, and the first thing you remember after.")),
 dict(slug="hawas-ice", house="Rasasi", title="Hawas Ice", kicker="Cool Water, Warm Intent",
      collection="men", layout="museum", family="Aromatic Aquatic", size="100 ml EDP", eur="€55", czk="≈ 1 350 Kč",
      top="Bergamot · Apple · Grapefruit", heart="Cardamom · Cinnamon · Jasmine", base="Ambergris · Musk · Oakmoss",
      world="radial-gradient(85% 75% at 30% 20%, rgba(90,150,210,.42), transparent 55%), linear-gradient(150deg,#0a1a2a,#16344e 45%,#060f18)",
      text=("A rush of cold air over warm skin. Sparkling bergamot, crisp apple and grapefruit open like sea spray, "
            "before a spiced heart of cardamom, cinnamon and jasmine reveals the intent beneath the freshness; ambergris, "
            "musk and oakmoss give it depth and remarkable staying power. Hawas Ice is the scent of a man at ease "
            "anywhere — deck of a yacht, corner of a bar, edge of a decision. Effortlessly fresh, quietly magnetic, and "
            "generous enough to fill a room without ever raising its voice.")),
 dict(slug="paradigme", house="Prada", title="Paradigme Le Parfum", kicker="A New Model of Man",
      collection="men", layout="split", family="Woody Amber", size="100 ml EDP", eur="€130", czk="≈ 3 180 Kč",
      top="Bergamot · Mandarin", heart="Neroli · Ambrette", base="Cedar · Amber · Musk",
      world="radial-gradient(90% 80% at 70% 20%, rgba(60,150,110,.38), transparent 55%), linear-gradient(150deg,#0a1e16,#153a28 45%,#061410)",
      text=("Refinement rewritten for a man with nothing left to prove. Bright bergamot and mandarin open with easy "
            "confidence; a heart of neroli and ambrette adds a soft, human warmth; cedar, amber and musk close it with "
            "understated authority. Housed in deep emerald glass, Paradigme Le Parfum is modern masculinity as quiet "
            "self-assurance rather than force. He listens more than he speaks and is remembered for both. Elegant, "
            "magnetic and beautifully composed — the new template, worn by the man who set it.")),
 # UNISEX
 dict(slug="sharaf-blend", house="Zimaya", title="Sharaf Blend", kicker="The Warmth of the East",
      collection="unisex", layout="museum", family="Oriental Woody", size="100 ml EDP", eur="€60", czk="≈ 1 470 Kč",
      top="Saffron · Nutmeg", heart="Rose · Oud · Patchouli", base="Amber · Musk · Vanilla",
      world="radial-gradient(80% 70% at 30% 22%, rgba(200,140,60,.45), transparent 55%), linear-gradient(150deg,#2a1608,#5a3212 45%,#160a04)",
      text=("An opulent oriental poured, fittingly, into a vessel like cut crystal glowing with amber liquor. Saffron and "
            "nutmeg spark the opening; a sumptuous heart of rose, oud and patchouli unfolds with slow confidence; amber, "
            "musk and vanilla close it in a warm, resinous embrace. Sharaf Blend is honour made scent — generous, "
            "enveloping and utterly luxurious, the fragrance of long evenings, deep armchairs and conversations that "
            "matter. Worn by anyone bold enough to carry a little of the desert's gold on their skin.")),
]

DIVIDERS = {
 "women": ("Pour Elle", "The Women's Collection",
           "Roses that remember. Vanilla that lingers. Fragrances for women who never once asked permission to be extraordinary."),
 "men":   ("Pour Lui", "The Men's Collection",
           "Cardamom and cedar. Sea spray and quiet authority. Scents for the man who need not raise his voice to be heard."),
 "unisex":("Sans Genre", "The Signature Exclusive",
           "Oud and amber, saffron and gold — too magnificent to belong to anyone but the person bold enough to wear it."),
}
DIV_IDX = {"women": "I", "men": "II", "unisex": "III"}


def notes_html(f, center=False):
    j = ' style="justify-content:center"' if center else ''
    return (f'<div class="notes"{j}>'
            f'<div class="col"><div class="lbl">Top</div><p>{f["top"]}</p></div>'
            f'<div class="col"><div class="lbl">Heart</div><p>{f["heart"]}</p></div>'
            f'<div class="col"><div class="lbl">Base</div><p>{f["base"]}</p></div></div>')


def bottle_html(f):
    path = os.path.join(IMG, f["slug"] + ".png")
    w, h = Image.open(path).size
    aspect = w / h
    # size container to the image aspect so nothing is letterboxed
    if aspect >= 1.05:            # wide box+bottle composition
        cw = 108; ch = cw / aspect
        if ch > 82: ch = 82; cw = ch * aspect
    else:                          # portrait single bottle
        ch = 96; cw = ch * aspect
    style = f"width:{cw:.0f}mm;height:{ch:.0f}mm"
    return (f'<div class="bottle has-photo" style="{style}">'
            f'<img class="photo" src="images/{f["slug"]}.png" alt="{f["title"]} bottle" '
            f'onerror="this.closest(&#39;.bottle&#39;).classList.remove(&#39;has-photo&#39;);this.remove()"></div>')


def price_html(f, right=False):
    j = ' style="justify-content:flex-end"' if right else ''
    return (f'<div class="price-tag"{j}><span class="size">{f["size"]}</span>'
            f'<span class="price">{f["eur"]}</span><span class="czk">{f["czk"]}</span></div>')


def frag_section(f, n):
    num = f"Fragrance No. {n:02d}"
    world = f'<div class="world" style="background:{f["world"]}"></div>'
    L = f["layout"]
    if L == "hero":
        body = f'''  <div class="pad frag-head">
    <div style="max-width:98mm">
      <p class="num">{num}</p><p class="house">{f["house"]}</p>
      <h2 class="title">{f["title"]}</h2><p class="kicker">{f["kicker"]}</p>
      <hr class="rule" style="margin:6mm 0">
      <p class="narrative">{f["text"]}</p>
      {notes_html(f)}
    </div>
    <div class="mt-auto flex-between">
      <span class="family-chip">{f["family"]}</span>{price_html(f)}
    </div>
  </div>
  {bottle_html(f)}'''
    elif L == "campaign":
        body = f'''  <div class="pad frag-head">
    <p class="num">{num}</p><p class="house">{f["house"]}</p>
    <div style="margin-top:auto">
      <p class="bigtype gold">{f["title"].upper()}</p>
      <p class="kicker" style="margin-top:2mm">{f["kicker"]}</p>
      <div class="flex-between" style="align-items:flex-end;margin-top:6mm">
        <p class="narrative">{f["text"]}</p>
        <div style="text-align:right;min-width:70mm">
          {notes_html(f, center=False)}
          <div class="flex-between" style="justify-content:flex-end;gap:6mm;margin-top:6mm">
            <span class="family-chip">{f["family"]}</span>{price_html(f, right=True)}
          </div>
        </div>
      </div>
    </div>
  </div>
  {bottle_html(f)}'''
    elif L == "split":
        body = f'''  <div class="pad">
    {bottle_html(f)}
    <div class="frag-head">
      <p class="num">{num}</p><p class="house">{f["house"]}</p>
      <h2 class="title" style="font-size:30pt">{f["title"]}</h2>
      <p class="kicker">{f["kicker"]}</p>
      <hr class="rule" style="margin:5mm 0">
      <p class="narrative" style="font-size:10.6pt">{f["text"]}</p>
      {notes_html(f)}
      <div style="margin-top:6mm">
        <span class="family-chip">{f["family"]}</span>
        <div style="margin-top:4mm">{price_html(f)}</div>
      </div>
    </div>
  </div>'''
    else:  # museum
        body = f'''  <div class="pad frag-head" style="align-items:center;text-align:center;justify-content:center">
    <p class="num">{num}</p>
    {bottle_html(f)}
    <p class="house" style="margin-top:4mm">{f["house"]}</p>
    <h2 class="title" style="font-size:34pt">{f["title"]}</h2>
    <p class="kicker">{f["kicker"]}</p>
    <hr class="rule center" style="margin:5mm auto">
    <p class="narrative center" style="margin:0 auto">{f["text"]}</p>
    {notes_html(f, center=True)}
    <div class="flex-between" style="width:100%;margin-top:8mm">
      <span class="family-chip">{f["family"]}</span>{price_html(f)}
    </div>
  </div>'''
    return f'<section class="page fragrance layout-{L} vignette">\n  {world}\n{body}\n</section>'


def divider(coll):
    eyebrow, title, sub = DIVIDERS[coll]
    return f'''<section class="page divider {coll}">
  <div class="idx">{DIV_IDX[coll]}</div>
  <div class="pad">
    <p class="script" style="font-size:36pt;color:var(--champagne-lt)">{eyebrow}</p>
    <h1 class="h-section">{title}</h1>
    <hr class="rule center long" style="margin:8mm auto">
    <p class="sub italic center" style="font-size:15pt;max-width:120mm;color:rgba(247,243,236,.85)">{sub}</p>
  </div>
</section>'''


# ---------- assemble body ----------
parts = []
n = 1
last_coll = None
for f in F:
    if f["collection"] != last_coll:
        parts.append(divider(f["collection"]))
        last_coll = f["collection"]
    parts.append(frag_section(f, n))
    n += 1
FRAG_HTML = "\n\n".join(parts)
COUNT = len(F)

with open(os.path.join(HERE, "_frontback.py"), encoding="utf-8") as fh:
    ns = {}
    exec(fh.read(), ns)
import re
back = re.sub(r"\s*<!-- CD REVIEW -->.*?(?=<!-- BACK COVER -->)", "\n\n", ns["BACK"], flags=re.DOTALL)
html = ns["FRONT"].replace("{{COUNT_WORD}}", "Fourteen").replace("{{COUNT}}", str(COUNT)) + "\n\n" + FRAG_HTML + "\n\n" + back

with open(os.path.join(HERE, "catalogue.html"), "w", encoding="utf-8") as fh:
    fh.write(html)
print(f"Wrote catalogue.html with {COUNT} fragrances, {html.count('<section')} sections.")
