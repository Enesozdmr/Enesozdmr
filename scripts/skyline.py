#!/usr/bin/env python3
"""Son 12 ayın katkı takviminden hareketli, izometrik bir şehir silueti üretir.

Kullanım:
    GITHUB_TOKEN=... python3 scripts/skyline.py <github-kullanıcı> <çıktı.svg>

data/ klasöründeki *.json dosyaları ({"YYYY-AA-GG": sayı} biçiminde, örneğin
GitLab katkı takviminin dökümü) gün gün GitHub verisine eklenir. Yalnızca
standart kütüphane kullanır.
"""
import glob
import json
import math
import os
import sys
import urllib.request

AYLAR = ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"]
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"

W, H = 1200, 520
OY = 112.0                # ızgaranın üst köşesinin y konumu
MAX_H = 66.0              # en yoğun günün bina yüksekliği


def github_takvimi(kullanici, token):
    sorgu = (
        "query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{"
        "weeks{contributionDays{date contributionCount}}}}}}"
    )
    istek = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": sorgu, "variables": {"u": kullanici}}).encode(),
        headers={"Authorization": "bearer " + token, "User-Agent": "skyline"},
    )
    with urllib.request.urlopen(istek, timeout=30) as yanit:
        veri = json.load(yanit)
    if veri.get("errors"):
        raise SystemExit("GitHub sorgusu başarısız: %s" % veri["errors"][0].get("message"))
    haftalar = veri["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [[(g["date"], g["contributionCount"]) for g in h["contributionDays"]] for h in haftalar]


def ek_veriler(klasor="data"):
    """data/*.json içindeki günlük sayıları tek sözlükte toplar."""
    toplam = {}
    for yol in sorted(glob.glob(os.path.join(klasor, "*.json"))):
        with open(yol, encoding="utf-8") as f:
            for tarih, sayi in json.load(f).items():
                toplam[tarih] = toplam.get(tarih, 0) + int(sayi)
    return toplam


def renk(t):
    """0..1 yoğunluğu lacivert → camgöbeği → mor geçişine çevirir."""
    duraklar = [(0.0, (37, 67, 150)), (0.5, (56, 189, 248)), (1.0, (196, 140, 255))]
    for (t0, c0), (t1, c1) in zip(duraklar, duraklar[1:]):
        if t <= t1:
            k = (t - t0) / (t1 - t0)
            return tuple(c0[i] + (c1[i] - c0[i]) * k for i in range(3))
    return duraklar[-1][1]


def hex_(c, carpan=1.0):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(v * carpan))) for v in c)


def nokta(*p):
    return " ".join("%.1f,%.1f" % q for q in p)


def uret(haftalar):
    gunler = [g for h in haftalar for g in h]
    sayilar = [c for _, c in gunler]
    toplam = sum(sayilar)
    toplam_s = f"{toplam:,}".replace(",", ".")
    en_cok = max(sayilar) or 1
    aktif = sum(1 for c in sayilar if c)
    ortalama = round(toplam / aktif) if aktif else 0

    # Baştaki boş haftaları at; kalan dönemi tuvalin genişliğine yay.
    ilk = next((i for i, h in enumerate(haftalar) if any(c for _, c in h)), 0)
    haftalar = haftalar[max(0, min(ilk - 1, len(haftalar) - 12)):]
    n = len(haftalar)
    A = min(40.0, 1080.0 / (n + 7))
    B = A / 3
    OX = 60 + 7 * A
    zirve_tarih = max(gunler, key=lambda g: g[1])[0]
    zirve = "%d %s" % (int(zirve_tarih[8:10]), AYLAR[int(zirve_tarih[5:7]) - 1])

    # Hücreleri arkadan öne (köşegen köşegen) sırala.
    kosegenler = {}
    for w, hafta in enumerate(haftalar):
        for d, (tarih, c) in enumerate(hafta):
            kosegenler.setdefault(w + d, []).append((w, d, c))
    son_k = max(kosegenler)

    govde = []
    for k in sorted(kosegenler):
        bina, parilti = [], []
        for w, d, c in kosegenler[k]:
            x = OX + (w - d) * A
            y = OY + (w + d) * B
            if c == 0:
                bina.append(
                    '<polygon points="%s" fill="#161b22" stroke="#21262d" stroke-width="0.6"/>'
                    % nokta((x, y - B), (x + A, y), (x, y + B), (x - A, y))
                )
                continue
            t = math.sqrt(c / en_cok)
            h = 5 + MAX_H * t
            c0 = renk(t)
            ust = nokta((x, y - h - B), (x + A, y - h), (x, y - h + B), (x - A, y - h))
            bina.append('<polygon points="%s" fill="%s"/>'
                        % (nokta((x - A, y - h), (x, y - h + B), (x, y + B), (x - A, y)), hex_(c0, 0.62)))
            bina.append('<polygon points="%s" fill="%s"/>'
                        % (nokta((x, y - h + B), (x + A, y - h), (x + A, y), (x, y + B)), hex_(c0, 0.40)))
            bina.append('<polygon points="%s" fill="%s"/>' % (ust, hex_(c0)))
            parilti.append('<polygon points="%s"/>' % ust)
        gecikme = 0.3 + k * 0.035
        s = 0.08 + 0.72 * k / son_k
        govde.append(
            '<g opacity="0">'
            '<animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="%.2fs" fill="freeze"/>'
            '<animateTransform attributeName="transform" type="translate" from="0 -26" to="0 0" dur="0.7s" '
            'begin="%.2fs" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.16 0.84 0.3 1"/>'
            "%s"
            '<g fill="#ffffff" opacity="0"><animate attributeName="opacity" dur="7s" begin="3.5s" '
            'repeatCount="indefinite" values="0;0;0.5;0;0" keyTimes="0;%.3f;%.3f;%.3f;1"/>%s</g>'
            "</g>" % (gecikme, gecikme, "".join(bina), s, s + 0.03, s + 0.12, "".join(parilti))
        )

    # Ön kenar boyunca ay etiketleri.
    etiketler, onceki = [], None
    for w, hafta in enumerate(haftalar):
        ay = hafta[0][0][5:7]
        if ay != onceki and len(hafta) == 7 and w < len(haftalar) - 1:
            x = OX + (w - 7.9) * A
            y = OY + (w + 7.9) * B + 6
            etiketler.append('<text x="%.1f" y="%.1f">%s</text>' % (x, y, AYLAR[int(ay) - 1]))
        onceki = ay

    lejant = "".join(
        '<rect x="%d" y="462" width="14" height="14" rx="3" fill="%s"/>' % (98 + i * 20, f)
        for i, f in enumerate(["#161b22"] + [hex_(renk(t)) for t in (0.15, 0.45, 0.75, 1.0)])
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Son 12 ayda {toplam} katkı; en yoğun gün {zirve}, {en_cok} katkı. Her bina bir günü, yüksekliği o günkü katkı sayısını gösterir.">
<title>Son 12 ayda {toplam} katkı</title>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1022"/><stop offset="1" stop-color="#0d1117"/></linearGradient>
<radialGradient id="isik" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#3b82f6" stop-opacity="0.26"/><stop offset="1" stop-color="#3b82f6" stop-opacity="0"/></radialGradient>
<linearGradient id="sayi" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#79c0ff"/><stop offset="1" stop-color="#d2a8ff"/></linearGradient>
<pattern id="nokta" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#ffffff" fill-opacity="0.05"/></pattern>
<clipPath id="cerceve"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#cerceve)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<ellipse cx="620" cy="300" rx="560" ry="250" fill="url(#isik)"><animate attributeName="cx" values="520;720;520" dur="16s" repeatCount="indefinite"/></ellipse>
<rect width="{W}" height="{H}" fill="url(#nokta)"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#ffffff" stroke-opacity="0.09"/>
{"".join(govde)}
<g font-family="{MONO}" font-size="12" fill="#6e7681" text-anchor="middle">{"".join(etiketler)}</g>
<g text-anchor="end">
<text x="1136" y="70" font-family="{MONO}" font-size="14" letter-spacing="2" fill="#7ee787">SON 12 AY</text>
<text x="1136" y="140" font-family="{SANS}" font-size="72" font-weight="800" letter-spacing="-2" fill="url(#sayi)">{toplam_s}</text>
<text x="1136" y="170" font-family="{MONO}" font-size="16" fill="#c9d1d9">katkı</text>
<text x="1136" y="192" font-family="{MONO}" font-size="12" fill="#6e7681">GitHub + GitLab</text>
</g>
<g font-family="{MONO}" font-size="14" fill="#8b949e">
<text x="64" y="430">en yoğun gün <tspan fill="#f0f6fc" font-weight="700">{zirve}</tspan> · {en_cok} katkı</text>
<text x="64" y="452">çalışılan günlerde ortalama <tspan fill="#f0f6fc" font-weight="700">{ortalama}</tspan> katkı</text>
<text x="64" y="474" font-size="12">az</text>{lejant}<text x="204" y="474" font-size="12">çok</text>
</g>
</svg>
"""


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    kullanici, cikti = sys.argv[1], sys.argv[2]
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN gerekli")
    haftalar = github_takvimi(kullanici, token)
    ek = ek_veriler()
    haftalar = [[(t, c + ek.get(t, 0)) for t, c in h] for h in haftalar]
    svg = uret(haftalar)
    os.makedirs(os.path.dirname(cikti) or ".", exist_ok=True)
    with open(cikti, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)


if __name__ == "__main__":
    main()
