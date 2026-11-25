"""Kişisel projeler kart görselini (assets/projeler.svg) üretir.

Yeni proje eklemek ya da birini güncellemek için PROJELER listesini düzenleyip
çalıştır:  python3 scripts/projeler.py
Logolar data/ikonlar.json içinde (simple-icons, CC0). Logosu olmayan
teknoloji yalnızca adıyla gösterilir.
"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

KOK = Path(__file__).resolve().parent.parent
IKON = json.loads((KOK / "data/ikonlar.json").read_text())["ikonlar"]

# (ad, alan, vurgu rengi, açıklama, [(teknoloji adı, ikon slug'ı ya da None)])
PROJELER = [
    ("Fasppegent", "Ajan · Mobil", "#d2a8ff",
     "iPhone'dan yönettiğim kişisel asistan: ajanların düşünme adımları ve araç "
     "çağrıları canlı akar, riskli adımda onay ister, push bildirim gönderir.",
     [("Rust", "rust"), ("PostgreSQL", "postgresql"), ("Expo", "expo")]),
    ("Yerel yapay zekâ platformu", "Yapay zekâ", "#79c0ff",
     "Kendi sunucumda yerel LLM'ler, RAG araması ve araç çağıran ajanlar; "
     "dışarıya veri göndermeyen, politika ve onay akışıyla sınırlı altyapı.",
     [("Ollama", "ollama"), ("pgvector", "postgresql"), ("Docker", "docker")]),
    ("İkinci beyin", "RAG", "#56d4dd",
     "Link ya da metni alıp konuşmayı yazıya, içeriği Türkçe özete çeviren "
     "ve anlamsal aramaya açan kişisel bilgi hattı.",
     [("Python", "python"), ("faster-whisper", None), ("Ollama", "ollama")]),
    ("TABAK", "Sağlık", "#7ee787",
     "Diyetisyenler için platform; tek kod tabanından web ve mobil, "
     "1.299 otomatik test.",
     [("FastAPI", "fastapi"), ("PostgreSQL", "postgresql"), ("Expo", "expo")]),
    ("Filo takip ve telemetri", "IoT · Telemetri", "#ffa657",
     "Teltonika cihazlarından CAN telemetrisi; sefer üretimi ve yakıt "
     "anomalisi tespiti, modelin cümlesi sayılarla doğrulanır.",
     [("TypeScript", "typescript"), ("TimescaleDB", "timescale"), ("Redis", "redis")]),
    ("DOKUM", "Belge işleme", "#f778ba",
     "e-Fatura PDF/XML dosyalarını Excel'e çevirir; okunan her değeri belge "
     "metnine karşı doğrular, yerel modelle çalışır.",
     [("Python", "python"), ("FastAPI", "fastapi"), ("Ollama", "ollama")]),
    ("D&D Companion", "Oyun", "#a5b4fc",
     "Birim testli kural motoru, karakter sihirbazı ve 3D zar.",
     [("Next.js", "nextdotjs"), ("Supabase", "supabase")]),
    ("Programatik video hattı", "Medya", "#ffd33d",
     "Ham çekimlerden otomatik vlog kurgusu.",
     [("Remotion", None), ("FFmpeg", "ffmpeg")]),
]

MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
W, PAD, GAP, KW, KH = 1200, 32, 16, 560, 136


def parlaklik(hexrenk: str) -> float:
    r, g, b = (int(hexrenk[i:i + 2], 16) / 255 for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def teknoloji(x: float, y: float, ad: str, slug: str | None) -> tuple[list[str], float]:
    """Logo karosu + ad hapı; (svg satırları, genişlik)."""
    yazi_x = x + (34 if slug else 12)
    gen = (yazi_x - x) + len(ad) * 7.3 + 12
    s = [f'    <rect x="{x}" y="{y}" width="{gen:.0f}" height="28" rx="8" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.10"/>']
    if slug:
        renk = IKON[slug]["renk"]
        koyu = parlaklik(renk) < 0.12
        zemin = "#30363d" if koyu else renk
        logo = "#ffffff" if koyu or parlaklik(renk) < 0.6 else "#1f2328"
        s.append(f'    <rect x="{x + 4}" y="{y + 4}" width="20" height="20" rx="5" fill="{zemin}"/>')
        s.append(f'    <path transform="translate({x + 7} {y + 7}) scale(0.5833)" fill="{logo}" d="{IKON[slug]["yol"]}"/>')
    s.append(f'    <text x="{yazi_x}" y="{y + 18.5}" font-family="{MONO}" font-size="12" fill="#c9d1d9">{escape(ad)}</text>')
    return s, gen


def uret() -> str:
    satir = (len(PROJELER) + 1) // 2
    H = PAD * 2 + satir * KH + (satir - 1) * GAP
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         f'aria-label="Kişisel projeler: {escape(", ".join(p[0] for p in PROJELER))}">',
         '  <title>Kişisel projeler</title>',
         f'''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0b1022"/><stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
    <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#ffffff" fill-opacity="0.05"/>
    </pattern>
  </defs>
  <rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#dots)"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#ffffff" stroke-opacity="0.09"/>''']
    for i, (ad, alan, vurgu, aciklama, teknolojiler) in enumerate(PROJELER):
        x = PAD + (i % 2) * (KW + 16)
        y = PAD + (i // 2) * (KH + GAP)
        gecikme = i * 0.6
        o.append('  <g>')
        o.append(f'    <rect x="{x}" y="{y}" width="{KW}" height="{KH}" rx="14" fill="#161b22" fill-opacity="0.85" stroke="{vurgu}" stroke-opacity="0.22"/>')
        o.append(f'    <rect x="{x}" y="{y + 18}" width="4" height="{KH - 36}" rx="2" fill="{vurgu}">')
        o.append(f'      <animate attributeName="opacity" values="1;0.35;1" dur="4.8s" begin="{gecikme}s" repeatCount="indefinite"/>')
        o.append('    </rect>')
        o.append(f'    <text x="{x + 24}" y="{y + 36}" font-family="{SANS}" font-size="19" font-weight="700" fill="#f0f6fc">{escape(ad)}</text>')
        eg = len(alan) * 6.9 + 20
        o.append(f'    <rect x="{x + KW - 20 - eg:.0f}" y="{y + 18}" width="{eg:.0f}" height="24" rx="12" fill="{vurgu}" fill-opacity="0.12" stroke="{vurgu}" stroke-opacity="0.45"/>')
        o.append(f'    <text x="{x + KW - 20 - eg / 2:.1f}" y="{y + 34.5}" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{vurgu}">{escape(alan)}</text>')
        for j, s in enumerate(textwrap.wrap(aciklama, 74)[:2]):
            o.append(f'    <text x="{x + 24}" y="{y + 62 + j * 19}" font-family="{SANS}" font-size="13.5" fill="#9da7b3">{escape(s)}</text>')
        tx = x + 24
        for tad, slug in teknolojiler:
            s, gen = teknoloji(tx, y + KH - 44, tad, slug)
            o += s
            tx += gen + 8
        o.append('  </g>')
    o.append('</svg>')
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    (KOK / "assets/projeler.svg").write_text(uret())
    print("assets/projeler.svg yazıldı")
