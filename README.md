# anti-slop-writing

**v4.0** — 27 September 2026

Bahasa Indonesia (default) | [English](README.en.md)

Skill universal biar output AI gak terdengar kayak AI. Lebih manusia, lebih spesifik, gak kaku.

Cocok untuk **ChatGPT, Claude, Gemini, Grok, Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor, Windsurf**, dan tool lain yang support instruksi menulis.

Berdasarkan Wikipedia ["Signs of AI Writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) + riset deteksi teks AI. Terinspirasi dari [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877).

---

## Yang Baru di v4.0

- **Cakupan empat provider:** pembaruan setelah v3.0 (6 Juli 2026) sampai 27 September 2026, dengan sumber resmi dan status akses.
- **Panduan untuk output model terbaru:** cek scaffolding asisten, hype/reassurance, persona tempelan, sitasi, repetisi, dan format sesuai permintaan.
- **Batas bukti diperjelas:** fakta rilis dipisahkan dari panduan editing. Rasio kosakata/tanda baca dan klaim sidik jari lama yang tidak didukung sumber dihapus.
- **Fakta tetap utuh:** detail, angka, kutipan, dan pengalaman tidak boleh dikarang untuk membuat tulisan terasa manusiawi. Skill tidak menjamin lolos detektor AI.
- **Full, Lite, dan adapter sinkron:** versi English dan Indonesia, termasuk `AGENTS.md`, `GEMINI.md`, dan `system-prompt.md`.

| Provider | Rilis teks yang dicakup sejak v3.0 |
|---|---|
| ChatGPT / OpenAI | GPT-5.6 Sol/Terra/Luna; GPT-6 Astra; GPT-6 Sol/Luna di API, Work, dan Codex. GPT-6 Pro memakai Astra. |
| Claude / Anthropic | Opus 5, Fable 5.1, Mythos 5.1 (akses terbatas), Opus 5.5. |
| Gemini / Google | 3.6 Flash, 3.5 Flash-Lite, 3.7 Flash, 3.8 Flash. |
| Grok / xAI | 4.5, 4.6, 4.7. |

Nama dan akses aplikasi chat bisa berbeda dari API. Sonnet/Haiku 5.5 masih rilis mendatang pada tanggal pemeriksaan. Lihat [cakupan model, tanggal, dan sumber](indonesian/references/model-coverage.md). Ini pembaruan instruksi berdasarkan dokumentasi resmi; belum ada uji langsung perbandingan model.

---

## Sebelum vs Sesudah

**Tanpa skill ini:**
> The festival serves as a vibrant testament to the region's rich cultural heritage, showcasing the intricate tapestry of traditions that have endured through the ages, contributing to the broader social fabric of the community.

**Dengan skill ini:**
> The festival has run every April since 1987. Locals build their own stalls. The goat cheese and handmade pottery sell out by noon.

---

## Mulai Cepat

### Claude.ai (Web) — Cara Paling Gampang

Paket Full dan Lite v4.0 tersedia lewat [Release v4.0](https://github.com/adenaufal/anti-slop-writing/releases/tag/v4.0).

1. Download `anti-slop-writing-id.skill` (Indonesia) atau `anti-slop-writing-en.skill` (English) dari [Releases terbaru](https://github.com/adenaufal/anti-slop-writing/releases/latest)
2. Di Claude.ai: `Settings → Skills → Install from file`
3. Pilih file yang barusan di-download
4. Mulai chat baru, langsung pakai

### Claude Code

```bash
# Global
git clone https://github.com/adenaufal/anti-slop-writing ~/.claude/skills/anti-slop-writing

# Atau per-project
git clone https://github.com/adenaufal/anti-slop-writing .claude/skills/anti-slop-writing
```

Skill: `indonesian/SKILL.md` (Bahasa Indonesia) atau `english/SKILL.md` (English).

### Tool Lain (Codex CLI, Gemini CLI, Copilot, Cursor, Windsurf, Aider, ChatGPT, Grok)

Lihat [Instalasi Lengkap](#instalasi-lengkap) di bawah.

---

## Cara Pakai

Pakai perintah natural:
- "Tolong rewrite biar lebih manusiawi."
- "Bikin tulisan ini gak keliatan AI."
- "No slop, langsung to the point."

Di Claude Code bisa juga pakai `/anti-slop-writing`.

### Cek Cepat

Kirim prompt ini buat tes:

```text
Ubah paragraf ini jadi 2 versi:
1) versi formal ringkas
2) versi santai
Keduanya harus tetap natural dan hindari frasa AI template.
```

Kalau hasilnya lebih konkret dan ritme kalimatnya bervariasi, berarti aturannya aktif.

---

## Instalasi Lengkap

> Semua tool selain Claude.ai perlu clone repo dulu:
> ```bash
> git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing
> ```
> Lalu pilih file dari `indonesian/` (Bahasa Indonesia) atau `english/` (English).

| Tool | File & Lokasi |
|------|---------------|
| **Codex CLI** (global) | `cp /tmp/anti-slop-writing/indonesian/AGENTS.md ~/.codex/AGENTS.md` |
| **Codex CLI** (project) | `cp /tmp/anti-slop-writing/indonesian/AGENTS.md ./AGENTS.md` |
| **Gemini CLI** (global) | `cp /tmp/anti-slop-writing/indonesian/GEMINI.md ~/.gemini/GEMINI.md` |
| **Gemini CLI** (project) | `cp /tmp/anti-slop-writing/indonesian/GEMINI.md ./GEMINI.md` |
| **GitHub Copilot** | `cp /tmp/anti-slop-writing/indonesian/AGENTS.md .github/copilot-instructions.md` |
| **Cursor** | `cp /tmp/anti-slop-writing/indonesian/AGENTS.md .cursor/rules/anti-slop-writing.mdc` |
| **Windsurf** | `cp /tmp/anti-slop-writing/indonesian/AGENTS.md .windsurf/rules/anti-slop-writing.md` |
| **Aider** | `aider --system-prompt "$(cat indonesian/system-prompt.md)"` |
| **ChatGPT / Grok / tool lain** | Pakai instruksi menulis dari `indonesian/SKILL-lite.md`; untuk API atau proyek yang mendukungnya, gunakan `system-prompt.md` beserta referensi. Sesuaikan dengan batas kolom. |

> Ganti `indonesian/` dengan `english/` kalau mau versi English.

---

## Isi Repo

```text
anti-slop-writing/
├── english/
│   ├── SKILL.md
│   ├── SKILL-lite.md
│   ├── AGENTS.md
│   ├── GEMINI.md
│   ├── system-prompt.md
│   └── references/
│       ├── vocabulary-banlist.md
│       ├── structural-patterns.md
│       └── model-coverage.md
├── indonesian/
│   ├── SKILL.md
│   ├── SKILL-lite.md
│   ├── AGENTS.md
│   ├── GEMINI.md
│   ├── system-prompt.md
│   └── references/
│       ├── vocabulary-banlist.md
│       ├── structural-patterns.md
│       └── model-coverage.md
├── references/              ← legacy (gabungan)
├── anti-slop-writing-en.skill   ← paket Full English (build lokal)
├── anti-slop-writing-id.skill   ← paket Full Indonesia (build lokal)
├── anti-slop-writing-en-lite.skill
├── anti-slop-writing-id-lite.skill
├── README.md
├── README.en.md
└── LICENSE
```

- `AGENTS.md`, `GEMINI.md`, `system-prompt.md` isinya sama — beda format aja sesuai tool.
- `SKILL.md` khusus format skill Claude Code.
- `anti-slop-writing-*.skill` dirilis terpisah via [Releases](https://github.com/adenaufal/anti-slop-writing/releases).
- Release v4.0 menyertakan empat paket: Full dan Lite untuk English dan Indonesia.

---

## Fokus Bahasa Indonesia

Repo ini punya aturan khusus buat pola AI dalam teks Bahasa Indonesia:
- Gaya terlalu baku di konteks santai
- Frasa template ("tidak hanya... tetapi juga")
- Selalu menutup dengan "Kesimpulan"
- Nominalisasi berlebihan
- Absennya partikel wacana (nah/sih/dong/kan)
- "Anda" yang kaku tanpa lihat konteks
- Translationese (struktur kalimat kalke Inggris)
- Hook dua klausa simetris ("Banyak orang mengira X. Kenyataannya Y.")
- Repetisi kata kunci prompt

Pakai file dari folder `indonesian/`.

---

## Sumber

- Rilis model Juli-September 2026: [riwayat dan sumber resmi empat provider](indonesian/references/model-coverage.md).
- Wikipedia: [Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Kobak et al. (2024): *Delving into LLM-assisted writing* ([arXiv:2406.07016](https://arxiv.org/abs/2406.07016))
- Russell, Karpinska & Iyyer (2025): *People who frequently use ChatGPT are accurate detectors of AI-generated text*
- Fraser, Dawkins & Kiritchenko (2025): *Detecting AI-generated text: factors influencing detectability*
- Wang et al. (2024): *M4: Multi-generator, Multi-domain, Multi-lingual Black-Box MGT Detection*
- Lovenia et al. (2024): *SEACrowd* ([arXiv:2406.10118](https://arxiv.org/abs/2406.10118))
- Ilman Akbar (2024): *Cara gampang mendeteksi konten buatan AI secara manual*
- The Conversation Indonesia (2024): *Mengapa tulisan asli bisa terdeteksi buatan AI*

## Credits

- [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877)
- Wikipedia [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)

## License

MIT
