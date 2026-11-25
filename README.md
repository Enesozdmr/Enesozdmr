<img src="./assets/hero.svg" width="100%" alt="Muhammed Özdemir — Backend, platform, yapay zekâ ve ağ. OSI yığınının yedi katmanında yaptığı işler: fiziksel kurulumdan ağa, oturumdan uygulamaya, RAG ve fine-tuning'e.">

Backend ve platform mühendisiyim. Üç yıldır production'da çalışan sistemler
geliştiriyorum: API tasarımı, veritabanı, dağıtım ve sunucu işletimi dahil
işin tamamını üstleniyorum. Veri merkezi ve sistem/ağ operasyonu geçmişim
sayesinde yazdığım sistemin barındırmasını, ağını, yedeğini ve izlemesini de
kendim kurup işletiyorum.

<img src="./assets/metrics.svg" width="100%" alt="Öne çıkan sonuçlar: 430+ REST endpoint, 375 kat hızlanan sorgu, 5.000+ otomatik test, 7 dilde 6 production sitesi">

## Bir yazma isteğinin yolculuğu

Yazma uçlarını nasıl kurduğumun kısa hali. İstek ağda tekrarlanabilir, dış
sistem çökebilir, uygulama katmanında hata olabilir; hiçbiri veriyi bozmamalı.

<img src="./assets/akis.svg" width="100%" alt="Bir yazma isteğinin yolculuğu: kimlik ve hız sınırı, idempotency, RLS ile korunan transaction, outbox, worker ve imzalı webhook">

## Nasıl çalışırım

- **Yetki veritabanında zorlanır.** Uygulama kodundaki bir hata başka kiracının
  verisini açmamalı; erişim kuralı PostgreSQL RLS'te durur.
- **Her yazma ucu idempotent.** İstemci aynı isteği iki kez gönderdiğinde ikinci
  kayıt oluşmaz.
- **Dış sistem çökünce akış durmaz.** Olay veriyle aynı transaction'da outbox'a
  yazılır; worker kuyruktan alır, başarısız olursa geri çekilerek yeniden dener.
- **Önce ölçerim, sonra hızlandırırım.** Tahminle değil sorgu planıyla; 1,5 sn
  süren bir sorgunun 4 ms'ye inmesi tek bir doğru indeksti.
- **Geri dönüşü denenmemiş dağıtım yapmam.** Yedekten dönüş ve önceki sürüme
  dönüş, canlıya çıkmadan önce provası yapılmış adımlardır.
- **Test, işin parçası.** Her değişiklik CI'da birim ve entegrasyon
  testlerinden geçer; geçmeyen birleşmez.

## Şu an

**Pandassist**'te medikal distribütörler için stok, satış, satın alma ve
CRM operasyonlarını yürüten çok kiracılı B2B platformun backend'ini ve
altyapısını geliştiriyorum (Fastify, Next.js, PostgreSQL, Docker).

<img src="./assets/katki-sehri.svg" width="100%" alt="Katkılar: her bina bir gün, yüksekliği o günkü katkı sayısı">

## Neler yaptım

- **Telemedicine API'si:** doktor, hemşire ve hasta uygulamalarına hizmet
  veren 430+ endpoint'lik backend; ödeme, randevu, uzaktan hasta izleme.
- **Canlı çevirili görüntülü görüşme:** doktor ve hastanın farklı diller
  konuşabildiği platformun FastAPI + LiveKit (WebRTC) backend'ini tek
  başıma tasarlayıp geliştirdim.
- **Klinik işletim platformu:** CRM, randevu, muayene ve faturalama;
  ulusal sağlık altyapısıyla entegre (Django REST Framework).
- **Çok dilli web siteleri:** 7 dile kadar yerelleştirme ve teknik SEO
  içeren altı production sitesi (Next.js).
- **Veri merkezi operasyonu:** 7/24 izleme, fiziksel sunucu kurulumu ve
  ağ yapılandırması.

## Kişisel projeler

<img src="./assets/projeler.svg" width="100%" alt="Kişisel projeler: Fasppegent, yerel yapay zekâ platformu, ikinci beyin, TABAK, filo takip ve telemetri, DOKUM, D&amp;D Companion, programatik video hattı">

<details>
<summary>Metin olarak</summary>

| Proje | Ne yapıyor | Teknoloji |
|---|---|---|
| **Fasppegent** | iPhone'dan yönettiğim kişisel asistan: ajanlara iş verip düşünme adımlarını ve araç çağrılarını canlı izleme, riskli adımlarda onay akışı, not yakalama, hatırlatıcı ve push bildirim | Rust (axum, sqlx), PostgreSQL, Expo |
| **Yerel yapay zekâ platformu** | Kendi sunucumda yerel LLM'ler, RAG araması ve araç çağıran ajanlar; dışarıya veri göndermeyen, politika ve onay akışıyla sınırlandırılmış altyapı | Ollama, pgvector, Docker |
| **İkinci beyin** | Link ya da metni alıp konuşmayı yazıya, içeriği Türkçe özete çeviren ve anlamsal aramaya açan kişisel bilgi hattı | faster-whisper, yerel LLM |
| **TABAK** | Diyetisyenler için platform; tek kod tabanından web ve mobil, 1.299 otomatik test | FastAPI, PostgreSQL, Expo |
| **Filo takip ve telemetri** | Konum akışından sefer üretimi ve yakıt anomalisi tespiti | TypeScript, TimescaleDB, Redis |
| **DOKUM** | e-Fatura PDF/XML dosyalarını Excel'e çevirir; okunan her değeri belge metnine karşı doğrular | Python |
| **D&D Companion** | Birim testli kural motoru, karakter sihirbazı ve 3D zar | Next.js, Supabase |
| **Programatik video hattı** | Ham çekimlerden otomatik vlog kurgusu | Remotion, ffmpeg |

</details>

Depolarımın çoğu gizli; merak ettiğin bir proje olursa yazabilirsin.

## Kullandıklarım

**Diller:** TypeScript/Node.js, Python, Rust, C#/.NET, SQL, Bash<br>
**Backend:** Fastify, FastAPI, Django REST Framework, Express, OpenAPI<br>
**Veri:** PostgreSQL (RLS, pgvector, TimescaleDB), MongoDB, Redis<br>
**Altyapı:** Linux, Docker, GitHub Actions, GitLab CI/CD, Nginx<br>
**Yapay zekâ:** OpenAI API, Ollama, RAG, konuşma-metin<br>
**Frontend:** React, Next.js, React Native/Expo, Tailwind CSS<br>
**Test:** pytest, Vitest, Playwright

## İletişim

[LinkedIn](https://www.linkedin.com/in/muhammed-%C3%B6zdemir-891967194)

<sub>Bu sayfadaki görseller bu depodaki SVG dosyalarıdır; katkı şehri her gün <a href="./scripts/skyline.py">kendi betiğimle</a> yeniden üretilir, proje kartları ve üst görsel <a href="./scripts/projeler.py">projeler.py</a> ve <a href="./scripts/hero.py">hero.py</a> ile. Logolar: simple-icons (CC0).</sub>
