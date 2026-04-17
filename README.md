# anti-slop-writing

Bahasa Indonesia (default) | [English](README.en.md)

Skill universal biar output AI gak terdengar kayak AI. Lebih manusia, lebih spesifik, gak kaku.

Cocok untuk **Claude.ai, ChatGPT, Gemini, Copilot, Claude Code, Codex CLI, Gemini CLI, Cursor, Windsurf, Ollama, LM Studio**, dan tool lain yang support system prompt.

👉 **Butuh panduan install per platform?** Lihat [INSTALL.md](INSTALL.md) (panduan lengkap ChatGPT, Gemini, Copilot, API, local LLM).

Berdasarkan Wikipedia ["Signs of AI Writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) + riset deteksi teks AI. Terinspirasi dari [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877).

---

## Sebelum vs Sesudah

**Tanpa skill ini:**
> The festival serves as a vibrant testament to the region's rich cultural heritage, showcasing the intricate tapestry of traditions that have endured through the ages, contributing to the broader social fabric of the community.

**Dengan skill ini:**
> The festival has run every April since 1987. Locals build their own stalls. The goat cheese and handmade pottery sell out by noon.

---

## Mulai Cepat

### Claude.ai (Web) — Cara Paling Gampang

1. Download `anti-slop-writing.skill` dari [Releases terbaru](https://github.com/adenaufal/anti-slop-writing/releases/latest)
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

### ChatGPT / Gemini / Copilot / Lainnya

Lihat [INSTALL.md](INSTALL.md) untuk panduan lengkap per platform. Ringkasnya:

- **ChatGPT Custom Instructions** (karakter terbatas): pakai versi Lite `indonesian/SKILL-lite.md`
- **ChatGPT Projects / Gemini Gems / Copilot Agents**: pakai Full `indonesian/system-prompt.md`
- **CLI tools & editor**: lihat [Instalasi Lengkap](#instalasi-lengkap) di bawah

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
| **ChatGPT / tool lain** | Copy isi `indonesian/system-prompt.md` → paste ke System Prompt |

> Ganti `indonesian/` dengan `english/` kalau mau versi English.

---

## Isi Repo

```text
anti-slop-writing/
├── english/
│   ├── SKILL.md              ← Full version (~16 KB)
│   ├── SKILL-lite.md         ← Lite version (~4 KB, buat ChatGPT Custom Instructions)
│   ├── AGENTS.md
│   ├── GEMINI.md
│   ├── system-prompt.md
│   └── references/
│       ├── vocabulary-banlist.md
│       └── structural-patterns.md
├── indonesian/
│   ├── SKILL.md              ← Full version dengan 3-tier tone (formal/semi-formal/informal)
│   ├── SKILL-lite.md         ← Lite version (~4 KB)
│   ├── AGENTS.md
│   ├── GEMINI.md
│   ├── system-prompt.md
│   └── references/
│       ├── vocabulary-banlist.md
│       └── structural-patterns.md
├── references/               ← legacy (gabungan)
├── INSTALL.md                ← Panduan install per platform (bilingual)
├── README.md
├── README.en.md
└── LICENSE
```

- `AGENTS.md`, `GEMINI.md`, `system-prompt.md` isinya sama — beda format aja sesuai tool.
- `SKILL.md` khusus format skill Claude Code.
- `anti-slop-writing.skill` dirilis terpisah via [Releases](https://github.com/adenaufal/anti-slop-writing/releases).

---

## Fokus Bahasa Indonesia

Repo ini punya aturan khusus buat pola AI dalam teks Bahasa Indonesia:
- Gaya terlalu baku di konteks santai
- Frasa template ("tidak hanya... tetapi juga")
- Selalu menutup dengan "Kesimpulan"
- Nominalisasi berlebihan
- Absennya partikel wacana (nah/sih/dong/kan)
- "Anda" yang kaku tanpa lihat konteks
- Em dash dan en dash (dilarang total, jadi sinyal AI nomor satu)

Pakai file dari folder `indonesian/`.

### 3 Tier Tone

Versi ID dukung tiga tier register:
- **Formal**: makalah, laporan, dokumen kantor. Kata ganti: saya, Anda. Tanpa partikel wacana.
- **Semi-formal** (default): blog, opini, newsletter, LinkedIn. Kata ganti: saya/aku, kamu. Partikel wacana sesekali.
- **Informal**: Twitter, IG caption, blog santai, TikTok. Kata ganti: aku/gw, kamu/lo. Partikel wacana natural.

Pilih tier di prompt lo: "Pakai tier semi-formal" atau "Tulis dalam tier informal". Default: semi-formal.

---

## Sumber

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
