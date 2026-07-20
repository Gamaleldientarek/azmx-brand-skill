#!/usr/bin/env python3
"""Rebuild references/image-index.md and index.html from whatever is in assets/images.

Usage:
    python3 scripts/rebuild-index.py

Run this after adding, removing, or replacing images. It measures each image's
dominant colour and luminance, then regenerates the agent-readable index and the
public gallery page. Requires Pillow (pip3 install Pillow).
"""
import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow is required:  pip3 install Pillow")
    sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "images")
RAW = "https://raw.githubusercontent.com/Gamaleldientarek/azmx-brand-skill/main/assets/images"
GALLERY = "https://gamaleldientarek.github.io/azmx-brand-skill/"

TITLES = {"gradient": "Gradients", "blue": "Abstract Blue", "orange": "Orange",
          "purple": "Purple", "green": "Green", "yellow": "Yellow",
          "red": "Red", "white": "White"}
NOTE = {
    "gradient": "Navy to electric gradient fields. Event surfaces only: covers, dividers, closings.",
    "blue": "The core brand set. Default choice for any AZMX surface needing an image.",
    "white": "The only lighter set. Navy titles and Electric accents work here.",
    "orange": "Recoloured variants. Categorical or client work only, not brand colours.",
    "purple": "Measures closer to Blue 900 and Dark Navy than to purple. Safe on AZMX surfaces.",
    "red": "Recoloured variants. Semantic or client work only.",
    "green": "Recoloured variants. Semantic or client work only.",
    "yellow": "Recoloured variants. Semantic or client work only."}
ORDER = ["gradient", "blue", "white", "purple", "orange", "red", "green", "yellow"]

TOKENS = {
    "Electric #001AFF": (0x00, 0x1A, 0xFF), "Dark Navy #040038": (0x04, 0x00, 0x38),
    "Light Blue #5D8FFF": (0x5D, 0x8F, 0xFF), "White #FFFFFF": (0xFF, 0xFF, 0xFF),
    "Blue 50 #F0F5FF": (0xF0, 0xF5, 0xFF), "Blue 100 #DDE8FF": (0xDD, 0xE8, 0xFF),
    "Blue 200 #BFD5FF": (0xBF, 0xD5, 0xFF), "Blue 300 #93B6FF": (0x93, 0xB6, 0xFF),
    "Blue 500 #2661FF": (0x26, 0x61, 0xFF), "Blue 700 #0200D3": (0x02, 0x00, 0xD3),
    "Blue 900 #01006E": (0x01, 0x00, 0x6E), "Blue 950 #010040": (0x01, 0x00, 0x40),
    "Neutral 900 #111927": (0x11, 0x19, 0x27), "Neutral 200 #E5E7EB": (0xE5, 0xE7, 0xEB),
    "Red #FF2B3C": (0xFF, 0x2B, 0x3C), "Yellow #FED340": (0xFE, 0xD3, 0x40),
    "Green #22C36F": (0x22, 0xC3, 0x6F), "Orange #F47A48": (0xF4, 0x7A, 0x48),
    "Purple #C68FFF": (0xC6, 0x8F, 0xFF)}


def nearest(rgb):
    return min(TOKENS.items(), key=lambda kv: sum((a - b) ** 2 for a, b in zip(rgb, kv[1])))[0]


def luminance(rgb):
    def f(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def analyse():
    secs = {}
    for sec in ORDER:
        d = os.path.join(IMG, sec)
        if not os.path.isdir(d):
            continue
        rows = []
        for fn in sorted(os.listdir(d)):
            if not fn.lower().endswith(".jpg"):
                continue
            im = Image.open(os.path.join(d, fn)).convert("RGB").resize((80, 80))
            q = im.quantize(colors=5, method=Image.MEDIANCUT).convert("RGB")
            dom = sorted(q.getcolors(10000), reverse=True)[0][1]
            px = list(im.getdata())
            avg = tuple(sum(p[i] for p in px) // len(px) for i in range(3))
            rows.append({"f": fn, "dom": "#%02X%02X%02X" % dom,
                         "tok": nearest(dom), "L": round(luminance(avg), 3)})
        if rows:
            secs[sec] = rows
    return secs


def text_for(lum):
    if lum < 0.18:
        return "White + Light Blue accent"
    if lum < 0.5:
        return "White, test contrast"
    return "Navy + Electric accent"


def write_index(secs):
    total = sum(len(v) for v in secs.values())
    L = ["# AZMX Image Index\n",
         f"Every image in the library ({total} total) with its direct download link, dominant colour, and the text colour that is safe on top of it.\n",
         "Download any image directly with curl, or paste the URL into a browser, Figma, Canva, or an email builder:\n",
         '```bash\ncurl -L -O "' + RAW + '/blue/blue-001.jpg"\n```\n',
         f"Browse them visually at {GALLERY}\n",
         "`Text on top` is derived from each image's measured luminance. Dark images take White titles with Light Blue accents; Electric is never used for text on these surfaces because it fails contrast on dark.\n",
         "---\n"]
    for s in ORDER:
        rows = secs.get(s, [])
        if not rows:
            continue
        L.append(f"## {TITLES[s]} ({len(rows)})\n")
        L.append("| Image | Dominant | Nearest token | Text on top | Link |")
        L.append("|---|---|---|---|---|")
        for r in rows:
            L.append(f"| `{r['f']}` | `{r['dom']}` | {r['tok']} | {text_for(r['L'])} | [download]({RAW}/{s}/{r['f']}) |")
        L.append("")
    with open(os.path.join(ROOT, "references", "image-index.md"), "w") as fh:
        fh.write("\n".join(L))
    return total


def load_prompts():
    import json
    p = os.path.join(ROOT, "scripts", "recolor-prompts.json")
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def recolour_section():
    """The recolour prompt cards, each with an always-visible copy button.

    Copy button follows the UX rules: 44px minimum target, always visible rather
    than hover-only (hover does not exist on touch), 180ms state change, and the
    result announced through a live region for screen readers.
    """
    data = load_prompts()
    if not data:
        return ""
    h = ['<section id="recolor"><h2>Recolour prompts</h2>',
         f'<p class="sub">{esc(data["note"])} Model used: <code>{esc(data["model"])}</code>.</p>',
         '<div class="pgrid">']
    for p in data["prompts"]:
        h.append(
            f'<article class="pcard">'
            f'<div class="phead">'
            f'<span class="pname"><i class="pdot" style="background:{p["swatch"]}"></i>{esc(p["label"])}</span>'
            f'<button class="copy" type="button" data-prompt="{p["key"]}" '
            f'aria-label="Copy the {esc(p["label"])} recolour prompt">'
            f'<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            f'<rect x="5.5" y="5.5" width="8" height="8" rx="1"/>'
            f'<path d="M10.5 5.5v-2a1 1 0 0 0-1-1h-6a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h2"/></svg>'
            f'<span class="copy-label">Copy</span></button>'
            f'</div>'
            f'<p class="psum">{esc(p["summary"])}</p>'
            f'<p class="ptext" id="prompt-{p["key"]}">{esc(p["text"])}</p>'
            f'</article>')
    h.append('</div><p class="sr" role="status" aria-live="polite" id="copy-status"></p></section>')
    h.append("""<script>
document.querySelectorAll('.copy').forEach(function(btn){
  btn.addEventListener('click', function(){
    var key = btn.dataset.prompt;
    var text = document.getElementById('prompt-' + key).textContent;
    var label = btn.querySelector('.copy-label');
    var done = function(){
      label.textContent = 'Copied';
      btn.dataset.copied = '1';
      document.getElementById('copy-status').textContent = key + ' prompt copied to clipboard';
      setTimeout(function(){
        label.textContent = 'Copy';
        btn.removeAttribute('data-copied');
      }, 2000);
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done).catch(fallback);
    } else { fallback(); }
    function fallback(){
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly','');
      ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); }
      catch (e) { label.textContent = 'Select manually'; }
      document.body.removeChild(ta);
    }
  });
});
</script>""")
    return "\n".join(h)


def write_gallery(secs, total):
    h = ["""<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AZMX Image Library</title>
<meta name="description" content="AZMX brand image library. Gradients, abstract blue, and recoloured brand imagery, free to download.">
<link rel="icon" href="assets/logo/azmx-favicon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AZMX Brand Skill">
<meta property="og:title" content="AZMX Image Library">
<meta property="og:description" content="AZMX brand image library. Gradients, abstract blue, and recoloured brand imagery, free to download.">
<meta property="og:url" content="https://gamaleldientarek.github.io/azmx-brand-skill/">
<meta property="og:image" content="https://gamaleldientarek.github.io/azmx-brand-skill/assets/cover-social-1280x640.jpg">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="640">
<meta property="og:image:alt" content="AZMX Brand Skill">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="AZMX Image Library">
<meta name="twitter:description" content="AZMX brand image library. Gradients, abstract blue, and recoloured brand imagery, free to download.">
<meta name="twitter:image" content="https://gamaleldientarek.github.io/azmx-brand-skill/assets/cover-social-1280x640.jpg">
<style>
:root{--navy:#040038;--electric:#001AFF;--lightblue:#5D8FFF;--blue100:#DDE8FF;--blue200:#BFD5FF}
*{box-sizing:border-box}
body{margin:0;background:var(--navy);color:#fff;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Tahoma,sans-serif;-webkit-font-smoothing:antialiased}
header{padding:clamp(48px,9vw,120px) clamp(24px,5vw,80px) 56px;max-width:1200px}
.eyebrow{color:var(--lightblue);text-transform:uppercase;letter-spacing:2.4px;font-size:14px;font-weight:600;margin:0 0 28px}
h1{font-family:Georgia,'Times New Roman',serif;font-size:clamp(44px,7vw,96px);font-weight:400;letter-spacing:-2px;line-height:1.02;margin:0 0 28px}
.lede{color:var(--blue100);font-size:clamp(17px,2vw,21px);line-height:1.65;max-width:62ch;margin:0 0 12px;opacity:.88}
.meta{color:var(--blue200);opacity:.7;font-size:15px;margin:24px 0 0;font-variant-numeric:tabular-nums}
nav{padding:0 clamp(24px,5vw,80px) 8px;display:flex;flex-wrap:wrap;gap:10px}
nav a{color:var(--blue100);text-decoration:none;border:1px solid rgba(255,255,255,.18);padding:8px 16px;font-size:14px;transition:.15s}
nav a:hover{border-color:var(--lightblue);color:#fff}
section{padding:0 clamp(24px,5vw,80px)}
h2{font-family:Georgia,serif;font-weight:500;font-size:clamp(28px,3.4vw,40px);margin:72px 0 6px;border-top:1px solid rgba(255,255,255,.14);padding-top:28px;letter-spacing:-.5px}
.sub{color:var(--blue200);opacity:.7;font-size:15px;margin:0 0 28px;max-width:60ch;line-height:1.6}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:24px}
figure{margin:0}
.shot{position:relative;display:block;line-height:0}
a.card{display:block;text-decoration:none;color:inherit}
img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block;background:#01006E;transition:opacity .15s}
a.card:hover img{opacity:.82}
.dl{position:absolute;top:10px;right:10px;display:inline-flex;align-items:center;gap:6px;
padding:7px 12px;background:rgba(4,0,56,.82);color:#fff;border:1px solid rgba(255,255,255,.28);
font-size:12px;line-height:1;text-decoration:none;letter-spacing:.4px;
opacity:0;transform:translateY(-4px);transition:opacity .15s,transform .15s,background .15s;
backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.shot:hover .dl,.dl:focus{opacity:1;transform:translateY(0)}
.dl:hover{background:var(--electric);border-color:var(--electric)}
.dl svg{width:13px;height:13px;flex:none}
@media (hover:none){.dl{opacity:1;transform:none}}
figcaption{display:flex;justify-content:space-between;align-items:center;gap:10px;padding-top:10px;font-size:12.5px;color:var(--blue200);opacity:.72;font-variant-numeric:tabular-nums}
.sw{width:11px;height:11px;display:inline-block;margin-right:6px;vertical-align:-1px;border:1px solid rgba(255,255,255,.25)}
footer{margin-top:88px;padding:56px clamp(24px,5vw,80px) 72px;border-top:1px solid rgba(255,255,255,.14);color:var(--blue200);font-size:15px;line-height:1.8;opacity:.75}
code{background:rgba(255,255,255,.08);padding:3px 8px;font-size:13px;word-break:break-all}
a.link{color:var(--lightblue)}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:24px}
.pcard{border:1px solid rgba(255,255,255,.14);padding:20px;display:flex;flex-direction:column;gap:14px;background:rgba(255,255,255,.02)}
.phead{display:flex;align-items:center;justify-content:space-between;gap:12px}
.pname{display:flex;align-items:center;gap:10px;font-size:15px;font-weight:600;letter-spacing:.2px}
.pdot{width:14px;height:14px;flex:none;border:1px solid rgba(255,255,255,.3)}
.psum{color:var(--blue200);opacity:.66;font-size:13px;margin:-6px 0 0}
.ptext{color:var(--blue100);opacity:.82;font-size:13.5px;line-height:1.65;max-height:150px;overflow-y:auto;
padding-right:10px;white-space:pre-wrap;border-left:1px solid rgba(255,255,255,.14);padding-left:14px}
.ptext::-webkit-scrollbar{width:5px}
.ptext::-webkit-scrollbar-thumb{background:rgba(255,255,255,.2)}
.copy{min-height:44px;display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:0 18px;
background:transparent;color:#fff;border:1px solid rgba(255,255,255,.3);font:inherit;font-size:13px;
letter-spacing:.4px;cursor:pointer;transition:background .18s,border-color .18s,color .18s;flex:none}
.copy:hover{border-color:var(--lightblue)}
.copy:focus-visible{outline:2px solid var(--lightblue);outline-offset:2px}
.copy[data-copied="1"]{background:var(--electric);border-color:var(--electric)}
.copy svg{width:14px;height:14px;flex:none}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<header>
<p class="eyebrow">AZMX Brand Skill</p>
<h1>Image Library</h1>"""]
    h.append(f'<p class="lede">{total} AZMX-generated brand images. Click any image to open it full size, then save it.</p>')
    h.append('<p class="lede">Nearly all of these are dark surfaces. Set titles in White, body in Blue&nbsp;100 <code>#DDE8FF</code>, eyebrows and accents in Light&nbsp;Blue <code>#5D8FFF</code>. Never set Electric blue as text over them.</p>')
    h.append(f'<p class="meta">{total} images · JPG · 1600px wide</p></header><nav>')
    for s in ORDER:
        if secs.get(s):
            h.append(f'<a href="#{s}">{TITLES[s]} ({len(secs[s])})</a>')
    h.append('<a href="#recolor">Recolour prompts</a>')
    h.append("</nav>")
    h.append(recolour_section())
    for s in ORDER:
        rows = secs.get(s, [])
        if not rows:
            continue
        h.append(f'<section id="{s}"><h2>{TITLES[s]}</h2><p class="sub">{NOTE[s]}</p><div class="grid">')
        for r in rows:
            rel = f"assets/images/{s}/{r['f']}"
            h.append(f'<figure><span class="shot">'
                     f'<a class="card" href="{rel}" target="_blank" rel="noopener">'
                     f'<img loading="lazy" src="{rel}" alt="{r["f"]}"></a>'
                     f'<a class="dl" href="{rel}" download="{r["f"]}" title="Download {r["f"]}">'
                     f'<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" '
                     f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                     f'<path d="M8 2v8M4.5 7.5 8 11l3.5-3.5M2.5 13.5h11"/></svg>Download</a>'
                     f'</span>'
                     f'<figcaption><span>{r["f"]}</span>'
                     f'<span><i class="sw" style="background:{r["dom"]}"></i>{r["dom"]}</span>'
                     f'</figcaption></figure>')
        h.append("</div></section>")
    h.append(f'<footer>Download one image:<br><code>curl -L -O "{RAW}/blue/blue-001.jpg"</code>'
             f'<br><br>Full brand skill and install instructions: '
             f'<a class="link" href="https://github.com/Gamaleldientarek/azmx-brand-skill">github.com/Gamaleldientarek/azmx-brand-skill</a>'
             f'<br><br>Built by <a class="link" href="https://gamaleldien.com">gamaleldien.com</a></footer>')
    with open(os.path.join(ROOT, "index.html"), "w") as fh:
        fh.write("\n".join(h))


def write_prompts_md():
    data = load_prompts()
    if not data:
        return
    L = ["# AZMX Recolour Prompts\n",
         data["note"] + "\n",
         f'**Model:** {data["model"]}\n',
         "Feed the source image to the model together with the prompt for the colour you want. Every prompt holds the same things constant: lighting direction, grain, the frosted highlight, composition, camera angle, and pure white staying pure white. That is what keeps a recoloured image recognisably part of the same set.\n",
         "Browse and copy these from the gallery too: " + GALLERY + "#recolor\n",
         "---\n"]
    for p in data["prompts"]:
        L.append(f'## {p["label"]}  `{p["swatch"]}`\n')
        L.append(f'{p["summary"]}.\n')
        L.append("```text")
        L.append(p["text"])
        L.append("```\n")
    with open(os.path.join(ROOT, "references", "recolor-prompts.md"), "w") as fh:
        fh.write("\n".join(L))


def main():
    secs = analyse()
    if not secs:
        print("No images found under assets/images/")
        return 1
    total = write_index(secs)
    write_gallery(secs, total)
    write_prompts_md()
    for s in ORDER:
        if secs.get(s):
            print(f"  {TITLES[s]:<14} {len(secs[s]):>3}")
    print(f"\nRebuilt references/image-index.md and index.html for {total} images.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
