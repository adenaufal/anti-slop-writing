# anti-slop-writing

**v4.1 · 27 September 2026**

[English](README.en.md)

anti-slop-writing adalah panduan yang bisa dipakai ulang untuk membantu AI menulis dan menyunting dengan lebih jelas, spesifik, dan sesuai suara penulis.

Anda bisa memakai teksnya langsung di percakapan menulis, atau mengimpor paket `.skill` jika platform Anda mendukung impor skill.

## Unduh atau lihat versi Lite

Pilih bahasa dan ukuran. Untuk kebanyakan orang, pilih **Full** jika platform bisa mengimpor paket; pilih **Lite** untuk menyalin teks ke chat atau kolom instruksi.

| Paket | Bahasa Indonesia | English |
|---|---|---|
| Full | [Unduh `.skill`](https://github.com/adenaufal/anti-slop-writing/releases/download/v4.1/anti-slop-writing-id.skill) · [Lihat SKILL.md](indonesian/SKILL.md) | [Download `.skill`](https://github.com/adenaufal/anti-slop-writing/releases/download/v4.1/anti-slop-writing-en.skill) · [View SKILL.md](english/SKILL.md) |
| Lite | [Unduh `.skill`](https://github.com/adenaufal/anti-slop-writing/releases/download/v4.1/anti-slop-writing-id-lite.skill) · [Lihat teks Lite](indonesian/SKILL-lite.md) | [Download `.skill`](https://github.com/adenaufal/anti-slop-writing/releases/download/v4.1/anti-slop-writing-en-lite.skill) · [View Lite text](english/SKILL-lite.md) |

Lihat catatan perubahan dan semua paket di [rilis v4.1](https://github.com/adenaufal/anti-slop-writing/releases/tag/v4.1).

## Pilih Full atau Lite

| | Full | Lite |
|---|---|---|
| Isinya | Panduan lengkap dan referensi per bahasa | Inti panduan untuk pemakaian ringkas |
| Cocok untuk | Impor skill, proyek, Gem, atau instruksi yang mendukung berkas referensi | Ditempel di chat atau kolom instruksi yang lebih terbatas |
| Perlu diketahui | Lebih panjang; batas dan dukungan berkas bergantung platform | Tetap bisa melebihi batas kolom tertentu; pilih dan tempel bagian yang muat |

Tidak semua chat menerima berkas atau punya kolom instruksi khusus. Projects dan Gem juga mengikuti batas serta fitur akun masing-masing. Bila ragu, salin teks Lite ke percakapan yang sedang dipakai.

## Mulai tanpa instalasi

1. Buka [teks Lite Bahasa Indonesia](indonesian/SKILL-lite.md) atau [Lite English](english/SKILL-lite.md).
2. Salin teks mulai dari judul utama `# Anti-Slop...`. Lewati blok metadata di bagian paling atas yang dimulai dan diakhiri dengan `---`.
3. Tempel di awal percakapan menulis, lalu sertakan draf atau permintaan Anda.

Contoh prompt:

> Pakai panduan menulis di atas untuk menyunting draf ini. Pertahankan fakta, maksud, tingkat kepastian, dan suara penulis. Ubah hanya bagian yang membuatnya kurang jelas atau alami.

Jika menggunakan Claude.ai, unduh paket dari tabel dan ikuti [petunjuk resmi untuk mengimpor skill](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Paket `.skill` adalah arsip ZIP; jika pengunggah hanya menerima `.zip`, ubah ekstensi file menjadi `.zip` tanpa mengekstrak atau mengemas ulang. Platform lain mungkin punya cara impor berbeda atau tidak mendukung impor skill.

## Contoh suntingan

Contoh buatan untuk latihan editorial. Fakta sumber: hanya uji coba yang ditunda; peluncuran belum dibatalkan; tanggal baru belum ditentukan.

**Sebelum:** “Penundaan pelaksanaan uji coba telah dilakukan oleh tim, sementara pembatalan peluncuran belum dilakukan dan penentuan tanggal baru belum dilakukan.”

**Sesudah:** “Tim menunda uji coba. Peluncuran belum dibatalkan, dan tanggal baru belum ditentukan.”

Kata “belum” tetap dipertahankan. Mengubahnya menjadi “peluncuran tidak akan dibatalkan” akan menambahkan janji yang tidak ada di sumber.

## Perubahan v4.1

- Menambahkan rute pemeriksaan tata bahasa dan contoh penyuntingan untuk Bahasa Indonesia dan English.
- Memperjelas pemeriksaan pelaku, rujukan kata, urutan peristiwa, sebab-akibat, serta cakupan kata seperti “hanya”, “belum”, dan “mungkin”.
- Menjaga suara penulis: revisi bagian yang perlu saja; jangan otomatis memformalkan tulisan santai atau menambahkan slang ke tulisan formal.
- Menyelaraskan panduan Full, Lite, dan adapter; contoh buatan diperiksa agar tidak mengubah fakta.

## Bagi pengguna teknis

### Pasang sebagai skill

Setiap skill memakai folder khusus dengan `SKILL.md` di dalamnya. Untuk memasang dari source:

1. Clone repo ke lokasi kerja, lalu pilih **satu folder bahasa**: `english/` atau `indonesian/`.
2. Salin `SKILL.md` untuk Full, atau salin `SKILL-lite.md` lalu beri nama `SKILL.md` untuk Lite. Sertakan folder `references/` dari bahasa yang sama.
3. Gunakan nama folder skill sesuai tabel berikut. Nama ini mengikuti nilai `name` di metadata file.

| Bahasa | Folder Full | Folder Lite |
|---|---|---|
| Bahasa Indonesia | `anti-slop-writing-id` | `anti-slop-writing-id-lite` |
| English | `anti-slop-writing` | `anti-slop-writing-lite` |

Claude Code membaca skill pribadi dari `~/.claude/skills/<nama-skill>/SKILL.md`, atau skill proyek dari `.claude/skills/<nama-skill>/SKILL.md`. Platform lain punya lokasi dan cara aktivasi masing-masing. Root repo ini adalah tempat source; file skill ada di dalam folder bahasa.

Untuk adapter `AGENTS.md`, `GEMINI.md`, dan `system-prompt.md`, ikuti [panduan instalasi per platform](INSTALL.md) dan sertakan `references/` dari bahasa yang sama. Gabungkan aturan dengan instruksi yang sudah Anda punya agar tetap terjaga.

### Peta sumber

- `english/` dan `indonesian/`: skill Full, Lite, adapter, dan referensi untuk tiap bahasa.
- `*/references/language-editing.md`: rute bahasa dan contoh suntingan.
- `*/references/model-coverage.md`: catatan historis rilis model dan sumbernya.
- `evaluations/`: skenario sintetis, output, dan catatan batas evaluasi v4.1.
- `scripts/build_skills.py`: validasi sumber serta build atau pemeriksaan empat paket.

Bangun paket dengan `python scripts/build_skills.py`. Periksa paket yang ada tanpa menulis ulang dengan `python scripts/build_skills.py --check`.

## Batas evaluasi

Catatan [evaluasi v4.1](evaluations/v4.1.md) mencakup 8 skenario (4 per bahasa) dan 16 output Full/Lite dari `gpt-6-luna` pada reasoning medium. Ini pemeriksaan kecil atas instruksi, bukan benchmark semua provider atau semua model. Tidak ada jaminan tulisan akan lolos detektor AI atau bahwa detektor dapat menentukan penulisnya. Cakupan model yang dicatat di [referensi model](indonesian/references/model-coverage.md) adalah riwayat rilis v4.0, bukan hasil evaluasi v4.1.

## Sumber dan kredit

- Panduan bahasa: [Bahasa Indonesia](indonesian/references/language-editing.md) · [English](english/references/language-editing.md)
- Catatan model historis: [rilis, tanggal, dan sumber](indonesian/references/model-coverage.md)
- [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Kobak et al. (2024), [Delving into LLM-assisted writing](https://arxiv.org/abs/2406.07016)
- [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877) · Wikipedia [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)

## Lisensi

MIT. Lihat [LICENSE](LICENSE).
