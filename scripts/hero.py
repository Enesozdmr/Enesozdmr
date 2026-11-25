"""Hero görselini (assets/hero.svg) üretir: kimlik, dil/sistem logoları ve OSI yığını.

Çalıştır: python3 scripts/hero.py
"""
W, H = 1200, 500
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
LAYERS = [  # (no, ad, işler, renk)
  (7, "Uygulama",        "REST · Next.js · RAG · fine-tuning · ajan", "#d2a8ff"),
  (6, "Sunum",           "TLS · JSON · UBL-TR · Codec 8",             "#bc8cff"),
  (5, "Oturum",          "WebSocket · SSE · JWT · çerez",             "#a5b4fc"),
  (4, "Taşıma",          "TCP ingest · Nginx · yük dengeleme",        "#79c0ff"),
  (3, "Ağ",              "IP · VPN · Tailscale · güvenlik duvarı",    "#56d4dd"),
  (2, "Veri bağlantısı", "switch · VLAN · MAC",                       "#4ac26b"),
  (1, "Fiziksel",        "rack · kablolama · sunucu kurulumu",        "#7ee787"),
]
X0, X1 = 652, 1148          # satır kutusu
Y0, RH, GAP = 46, 46, 12    # ilk satır, satır yüksekliği, aralık
RAIL = 624                  # paket rayı
DUR = 8.4                   # bir tur (iniş + çıkış) saniye
n = len(LAYERS)
cy = [Y0 + i*(RH+GAP) + RH/2 for i in range(n)]
seq = cy + cy[-2::-1]                        # aşağı sonra yukarı: 13 durak
kt = [round(k/(len(seq)-1), 4) for k in range(len(seq))]

def blink(times):
    """Belirtilen anlarda (0-1) yanıp sönen opaklık animasyonu değerleri."""
    pts = [(0.0, 0)]
    for t in times:
        a, b, c = max(t-0.035, 0.0001), t, min(t+0.075, 0.9999)
        pts += [(a, 0), (b, 1), (c, 0)]
    pts.append((1.0, 0))
    pts = sorted(set(pts))
    return ";".join(f"{v}" for _, v in pts), ";".join(f"{k:.4f}" for k, _ in pts)

o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Muhammed Özdemir — Backend, platform, yapay zekâ ve ağ. Fiziksel katmandan uygulama katmanına OSI yığınının yedi katmanında yaptığı işler; bir paket katmanlardan inip geri çıkıyor.">')
o.append('  <title>Muhammed Özdemir — L1\'den L7\'ye</title>')
o.append(f'''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0b1022"/><stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
    <radialGradient id="blob" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#3b82f6" stop-opacity="0.30"/><stop offset="1" stop-color="#3b82f6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="blob2" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#a371f7" stop-opacity="0.22"/><stop offset="1" stop-color="#a371f7" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="name" gradientUnits="userSpaceOnUse" x1="64" y1="0" x2="664" y2="0" spreadMethod="reflect">
      <stop offset="0" stop-color="#f0f6fc"/><stop offset="0.45" stop-color="#79c0ff"/>
      <stop offset="0.75" stop-color="#d2a8ff"/><stop offset="1" stop-color="#f0f6fc"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="1200 0" dur="9s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="rail" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#d2a8ff"/><stop offset="0.5" stop-color="#79c0ff"/><stop offset="1" stop-color="#7ee787"/>
    </linearGradient>
    <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#ffffff" fill-opacity="0.055"/>
    </pattern>
    <filter id="glow" x="-300%" y="-300%" width="700%" height="700%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    <circle cx="900" cy="250" r="340" fill="url(#blob)">
      <animate attributeName="cy" values="230;290;230" dur="13s" repeatCount="indefinite"/>
    </circle>
    <circle cx="220" cy="470" r="300" fill="url(#blob2)">
      <animate attributeName="cx" values="200;320;200" dur="17s" repeatCount="indefinite"/>
    </circle>
    <rect width="{W}" height="{H}" fill="url(#dots)"/>
  </g>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="#ffffff" stroke-opacity="0.09"/>''')

# Sol: kimlik
o.append(f'''  <g font-family="{MONO}">
    <text x="64" y="86" font-size="17" fill="#3fb950">$ whoami</text>
  </g>
  <text x="62" y="150" font-family="{SANS}" font-size="52" font-weight="700" letter-spacing="-1" fill="url(#name)">Muhammed Özdemir</text>
  <g font-family="{MONO}">
    <text x="64" y="192" font-size="20" fill="#e6edf3">Backend · Platform · AI · Network</text>
    <text x="64" y="228" font-size="15" fill="#8b949e">Rack kurulumundan RAG'e,</text>
    <text x="64" y="250" font-size="15" fill="#8b949e">OSI'nin her katmanında iş çıkardım.</text>
  </g>''')
# dil ve sistem logoları
import json as _json
from pathlib import Path as _P
_KOK = _P(__file__).resolve().parent.parent
_IKON = _json.loads((_KOK / 'data/ikonlar.json').read_text())['ikonlar']
def _yol(slug): return _IKON[slug]['yol']
def logos(y, items):
    """Marka renginde karo + beyaz (ya da koyu) logo. items: (slug, zemin, logo rengi, ad)"""
    x = 64; s = []
    for slug, zemin, renk, ad in items:
        s.append(f'    <g><title>{ad}</title>')
        s.append(f'      <rect x="{x}" y="{y}" width="42" height="42" rx="10" fill="{zemin}"/>')
        s.append(f'      <rect x="{x}" y="{y}" width="42" height="42" rx="10" fill="none" stroke="#ffffff" stroke-opacity="0.14"/>')
        s.append(f'      <path transform="translate({x+10} {y+10}) scale(0.9167)" fill="{renk}" d="{_yol(slug)}"/>')
        s.append(f'      <text x="{x+21}" y="{y+56}" text-anchor="middle" font-size="10" fill="#8b949e" fill-opacity="0.55">{ad}</text>')
        s.append('    </g>')
        x += 62
    return s
def chips(y, items, color):
    x = 64; s = []
    for it in items:
        w = len(it)*7.9 + 22
        s.append(f'    <rect x="{x}" y="{y}" width="{w:.0f}" height="26" rx="13" fill="{color}" fill-opacity="0.10" stroke="{color}" stroke-opacity="0.45"/>')
        s.append(f'    <text x="{x + w/2:.1f}" y="{y+17.5}" text-anchor="middle" font-size="13" fill="#e6edf3">{it}</text>')
        x += w + 8
    return s
o.append(f'  <g font-family="{MONO}">')
o.append(f'    <text x="64" y="294" font-size="12" fill="#6e7681" letter-spacing="1.5">DİLLER</text>')
o += logos(304, [("typescript","#3178C6","#ffffff","TypeScript"),("python","#3776AB","#FFD43B","Python"),("rust","#1f2328","#ffffff","Rust"),("dotnet","#512BD4","#ffffff","C#/.NET"),("gnubash","#2b3137","#4EAA25","Bash")])
o.append(f'    <text x="64" y="388" font-size="12" fill="#6e7681" letter-spacing="1.5">SİSTEMLER</text>')
o += logos(398, [("postgresql","#336791","#ffffff","Postgres"),("redis","#FF4438","#ffffff","Redis"),("docker","#2496ED","#ffffff","Docker"),("linux","#FCC624","#1f2328","Linux"),("ollama","#1f2328","#ffffff","Ollama")])
o.append('  </g>')
o.append(f'''  <g font-family="{MONO}" font-size="14" fill="#8b949e">
    <circle cx="70" cy="483" r="5" fill="#3fb950">
      <animate attributeName="opacity" values="1;0.35;1" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text x="84" y="488">Ankara, Türkiye · NOC'tan production'a</text>
  </g>''')

# Sağ: OSI yığını
o.append(f'  <line x1="{RAIL}" y1="{cy[0]}" x2="{RAIL}" y2="{cy[-1]}" stroke="url(#rail)" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="3 5"/>')
for i, (no, ad, isler, renk) in enumerate(LAYERS):
    y = Y0 + i*(RH+GAP)
    t_down, t_up = kt[i], kt[len(seq)-1-i]
    vals, kts = blink(sorted({t_down, t_up}))
    o.append(f'  <g>')
    o.append(f'    <line x1="{RAIL}" y1="{cy[i]}" x2="{X0}" y2="{cy[i]}" stroke="{renk}" stroke-opacity="0.3"/>')
    o.append(f'    <circle cx="{RAIL}" cy="{cy[i]}" r="3.5" fill="#0d1117" stroke="{renk}" stroke-opacity="0.7"/>')
    o.append(f'    <rect x="{X0}" y="{y}" width="{X1-X0}" height="{RH}" rx="10" fill="#161b22" fill-opacity="0.82" stroke="#ffffff" stroke-opacity="0.08"/>')
    # yanma katmanı
    o.append(f'    <rect x="{X0}" y="{y}" width="{X1-X0}" height="{RH}" rx="10" fill="{renk}" fill-opacity="0.13" stroke="{renk}" stroke-opacity="0.9" opacity="0">')
    o.append(f'      <animate attributeName="opacity" values="{vals}" keyTimes="{kts}" dur="{DUR}s" repeatCount="indefinite"/>')
    o.append(f'    </rect>')
    o.append(f'    <rect x="{X0}" y="{y+10}" width="3" height="{RH-20}" rx="1.5" fill="{renk}"/>')
    o.append(f'    <text x="{X0+18}" y="{y+29}" font-family="{MONO}" font-size="14" font-weight="700" fill="{renk}">L{no}</text>')
    o.append(f'    <text x="{X0+50}" y="{y+29}" font-family="{SANS}" font-size="15" font-weight="600" fill="#e6edf3">{ad}</text>')
    o.append(f'    <text x="{X1-16}" y="{y+29}" text-anchor="end" font-family="{MONO}" font-size="13" fill="#9da7b3">{isler}</text>')
    o.append(f'  </g>')

# paket
cvals = ";".join(f"{v:.1f}" for v in seq)
ktimes = ";".join(f"{k:.4f}" for k in kt)
o.append(f'''  <g filter="url(#glow)">
    <circle cx="{RAIL}" cy="{cy[0]}" r="6" fill="#f0f6fc">
      <animate attributeName="cy" values="{cvals}" keyTimes="{ktimes}" dur="{DUR}s" calcMode="spline" keySplines="{';'.join(['0.45 0 0.55 1']*(len(seq)-1))}" repeatCount="indefinite"/>
      <animate attributeName="fill" values="#d2a8ff;#79c0ff;#7ee787;#79c0ff;#d2a8ff" keyTimes="0;0.25;0.5;0.75;1" dur="{DUR}s" repeatCount="indefinite"/>
    </circle>
  </g>''')
o.append('</svg>')
open(_KOK / 'assets/hero.svg', 'w').write("\n".join(o) + "\n")
