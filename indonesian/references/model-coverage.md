# Cakupan model dan bukti (v4.0)

**Diperiksa:** 27 September 2026. **Versi sebelumnya:** v3.0, 6 Juli 2026 (commit `bffa2a5`). Referensi ini mencatat model teks umum dan pembaruan produk yang relevan setelah batas itu. Ini catatan bertanggal; akses tiap paket bisa berbeda dan rilis mendatang perlu diperiksa lagi.

Baca file ini kalau permintaan menyebut model, menanyakan versi yang dicakup, atau membutuhkan bukti rilis. Untuk menulis biasa, aturan inti skill sudah cukup.

## Riwayat rilis terverifikasi

### ChatGPT / OpenAI

| Tanggal (2026) | Model atau pembaruan | Cakupan dan sumber |
|---|---|---|
| 9 Juli | GPT-5.6 Sol, Terra, Luna | Rilis umum di ChatGPT, Codex, dan API; akses berbeda menurut paket dan produk. [Pengumuman GPT-5.6](https://openai.com/index/gpt-5-6/) |
| 6 Agustus | Pembaruan GPT-5.6 Sol di ChatGPT; perluasan akses Luna | Pembaruan produk dalam generasi yang sama. [Pembaruan ChatGPT](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/) |
| 3 September | GPT-6 Astra | Rilis API dan rollout ChatGPT yang awalnya terbatas untuk organisasi. [Changelog API](https://developers.openai.com/api/docs/changelog), [Catatan rilis ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) |
| 22 September | GPT-6 Sol, Luna | Model API dengan output teks, juga tersedia di ChatGPT Work dan Codex. Akses itu tidak membuktikan bahwa keduanya menjadi default di ChatGPT Chat biasa. [Changelog API](https://developers.openai.com/api/docs/changelog), [Catatan rilis ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) |

GPT-6 Pro di ChatGPT menggunakan Astra; namanya bukan model dasar tambahan. Periksa paket dan produk yang sedang dipakai. [Panduan model/akses ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)

**Bukti terkait tulisan:** OpenAI menyebut pembaruan Sol Agustus menghasilkan jawaban lebih fokus, dan effort penalaran tambahan seharusnya tidak mengubah tone. Ini deskripsi vendor, bukan pengukuran sidik jari bahasa independen. [Pengumuman pembaruan](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)

### Claude / Anthropic

| Tanggal (2026) | Model | Cakupan dan sumber |
|---|---|---|
| 24 Juli | Claude Opus 5 | Dirilis untuk Claude dan developer. [Pengumuman Opus 5](https://www.anthropic.com/news/claude-opus-5) |
| 1 September | Claude Fable 5.1, Mythos 5.1 | Fable tersedia umum; Mythos dibatasi lewat program trusted access. Model dasarnya sama dengan safeguards berbeda. Tanggal tepat tercatat di newsroom; halaman peluncuran hanya menampilkan bulan. [Peluncuran](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Newsroom](https://www.anthropic.com/news) |
| 22 September | Claude Opus 5.5 | Sudah dirilis. Sonnet 5.5 dan Haiku 5.5 masih diumumkan sebagai rilis mendatang pada tanggal pemeriksaan ini. [Pengumuman Opus 5.5](https://www.anthropic.com/claude-opus-5-5) |

**Bukti terkait tulisan:** Anthropic melaporkan komunikasi Opus 5.5 lebih jelas, natural, dan mengikuti instruksi menulis dengan lebih baik. Ini tidak memvalidasi rasio tanda baca v3 atau dialek “Philosopher” untuk seluruh Claude terbaru. [Contoh komunikasi Opus 5.5](https://www.anthropic.com/claude-opus-5-5)

### Gemini / Google

| Tanggal (2026) | Model | Cakupan dan sumber |
|---|---|---|
| 21 Juli | Gemini 3.6 Flash, 3.5 Flash-Lite | Model umum yang mendukung teks. [Peluncuran](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) |
| 13 Agustus | Gemini 3.7 Flash | Rilis Flash berikutnya. [Peluncuran](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) |
| 2 September | Gemini 3.8 Flash | Rilis Flash stabil terbaru untuk penggunaan umum dalam pemeriksaan ini. [Peluncuran](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) |

Registry API mengonfirmasi tanggal-tanggal tersebut dan memisahkan model stabil dari preview. Gemini 3.1 Pro masih tercatat sebagai preview di katalog; namanya tidak membuktikan ada rilis baru setelah v3. Rilis Live, TTS, gambar, embedding, dan Cyber spesialis bukan bukti pola prosa biasa. Label aplikasi bisa berbeda dari ID API. [Registry rilis/deprecation](https://ai.google.dev/gemini-api/docs/deprecations), [Katalog model](https://ai.google.dev/gemini-api/docs/models)

### Grok / xAI

| Tanggal (2026) | Model | Cakupan dan sumber |
|---|---|---|
| 16 Juli | Grok 4.5 | Peluncuran untuk produk developer/agent; rollout konsumen dilakukan terpisah. [Peluncuran](https://x.ai/news/grok-4-5) |
| 12 Agustus | Grok 4.6 | Awalnya diluncurkan di Grok Build dan Cursor; ketersediaan API dicatat terpisah. [Peluncuran](https://x.ai/news/grok-4-6), [Catatan rilis API](https://docs.x.ai/developers/release-notes) |
| 21 September | Grok 4.7 | Rilis umum terbaru yang diperiksa; peluncuran mencakup Grok Build, Cursor, dan API. [Peluncuran](https://x.ai/news/grok-4-7) |

Pengumuman ini menjelaskan kemampuan dan akses, bukan bukti statistik bahwa prosanya selalu sarkastis atau “edgy”. Jangan anggap brand Grok menentukan suara tulisan atau semua aplikasi konsumen memakai model API terbaru. [Berita xAI dan catatan rollout](https://x.ai/news)

## Cek editorial untuk keempat keluarga

Ini panduan editing yang diusulkan skill, bukan hasil perbandingan korpus terkontrol atas model-model di atas. Terapkan kalau masalahnya memang muncul di draf:

- Hapus pembuka asisten, tawaran lanjutan yang tidak diminta, dan narasi proses dari artikel, memo, atau caption. Pertahankan penjelasan penalaran ketika format yang diminta membutuhkannya.
- Potong reassurance, pujian, hook motivasi, dan lelucon tempelan. Ikuti suara yang diminta; empati atau sarkasme bisa tepat kalau konteks mendukung.
- Ganti klaim abstrak dengan detail yang didukung sumber. Jangan mengarang nama, angka, kutipan, sitasi, atau pengalaman pribadi agar tulisan terasa spesifik.
- Pastikan tiap sitasi mendukung klaim di dekatnya, informasinya masih berlaku, dan ketidakpastian tidak hilang setelah rewrite. Snippet pencarian dan ringkasan yang lancar tetap perlu diperiksa.
- Gabungkan klaim berulang dan heading atau bullet yang tidak perlu. Pertahankan daftar, perbandingan, dan template yang diminta pengguna.
- Baca ulang untuk pola kalimat berulang dan penutup template. Perbaiki makna dan alur, tanpa kuota panjang kalimat, jumlah item acak, atau target skor detektor.

Skill ini menyunting bahasa dan struktur. Skill tidak menentukan siapa penulisnya, menjamin hasil detektor, atau membuktikan proses internal suatu model. Tidak ada uji langsung perbandingan model untuk rilis ini. Untuk pembaruan berikutnya, verifikasi rilis resmi bertanggal, catat status aksesnya, lalu uji draf nyata sebelum mengklaim pola khas model tertentu.
