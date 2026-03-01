# anti-slop-writing

Bahasa Indonesia (default) | [English](README.en.md)

Skill universal untuk bantu output AI terasa lebih manusia, lebih spesifik, dan tidak kaku. Cocok untuk Claude.ai (web), Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor, Windsurf, dan tool lain yang bisa pakai system prompt.

Dasarnya dari Wikipedia ["Signs of AI Writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) plus riset deteksi teks AI.

Terinspirasi dari [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877).

---

## Mulai Cepat (Claude.ai / Claude Web)

> **Ini jalur utama buat mayoritas user Indonesia.**
>
> 1. Buka [Releases terbaru](https://github.com/adenaufal/anti-slop-writing/releases/latest)
> 2. Download file `anti-slop-writing.skill`
> 3. Di Claude.ai: `Settings -> Skills -> Install from file`
> 4. Pilih file `anti-slop-writing.skill` yang barusan di-download
> 5. Mulai chat baru dan pakai prompt kamu seperti biasa

Kalau kamu pakai Claude web, ini cara paling cepat dan paling rapi.

---

## Sebelum vs Sesudah

**Tanpa skill ini:**
> The festival serves as a vibrant testament to the region's rich cultural heritage, showcasing the intricate tapestry of traditions that have endured through the ages, contributing to the broader social fabric of the community.

**Dengan skill ini:**
> The festival has run every April since 1987. Locals build their own stalls. The goat cheese and handmade pottery sell out by noon.

---

## Cara Pakai Setelah Install

Pakai perintah natural, misalnya:
- "Tolong rewrite biar lebih manusiawi."
- "Bikin tulisan ini gak keliatan AI."
- "Hapus gaya bahasa kaku, bikin lebih natural."
- "No slop, langsung to the point."

Untuk Claude Code, kamu juga bisa trigger dengan `/anti-slop-writing`.

---

## Cara Pakai di Tiap AI Agent

Bagian ini jawab pertanyaan: "udah install, terus pakenya gimana?"

### Claude.ai / Claude Web

1. Install file `.skill` dulu (lihat "Mulai Cepat" di atas).
2. Buka chat baru.
3. Langsung kirim naskah kamu + instruksi rewrite.
4. Kalau perlu, sebut nama skill di prompt: "pakai anti-slop-writing."

Contoh prompt:

```text
Pakai anti-slop-writing. Rewrite paragraf ini biar natural bahasa Indonesia, tetap tegas, jangan pakai frasa template AI.
```

### Claude Code

1. Pastikan repo skill sudah ada di `~/.claude/skills/anti-slop-writing` atau `.claude/skills/anti-slop-writing`.
2. Di chat Claude Code, pakai `/anti-slop-writing` atau instruksi natural.
3. Tempel teks yang mau direwrite.

Contoh:

```text
/anti-slop-writing
Rewrite draft ini. Bikin lebih manusia, lebih ringkas, dan jangan pakai pola AI.
```

### OpenAI Codex CLI

1. Pastikan `AGENTS.md` sudah disalin ke `~/.codex/AGENTS.md` atau root project.
2. Start session Codex dari project yang benar.
3. Minta rewrite seperti biasa.

Contoh:

```text
Rewrite copy landing page ini biar terdengar natural, nggak generik, dan enak dibaca orang Indonesia.
```

### Gemini CLI

1. Pastikan `GEMINI.md` sudah ada di `~/.gemini/GEMINI.md` atau root project.
2. Start session Gemini dari folder project.
3. Kirim instruksi rewrite.

Contoh:

```text
Tolong edit artikel ini. Hindari gaya AI, pakai bahasa Indonesia yang lebih hidup dan spesifik.
```

### GitHub Copilot / Cursor / Windsurf

1. Pastikan file instruksi sudah dipasang:
   - Copilot: `.github/copilot-instructions.md`
   - Cursor: `.cursor/rules/anti-slop-writing.mdc` atau `AGENTS.md`
   - Windsurf: `.windsurf/rules/anti-slop-writing.md`
2. Buka file teks yang mau diedit.
3. Jalankan chat assistant dan minta rewrite dengan gaya anti-slop.

Contoh:

```text
Rewrite section ini biar lebih manusia, hilangkan frasa klise AI, dan pertahankan makna aslinya.
```

### Aider

1. Jalankan Aider dengan `--system-prompt` pakai `system-prompt.md`.
2. Minta edit naskah target.

Contoh command:

```bash
aider --system-prompt "$(cat system-prompt.md)"
```

Contoh prompt di Aider:

```text
Edit file ini. Rapikan gaya bahasanya biar tidak terdeteksi sebagai tulisan AI.
```

### ChatGPT / tool web lain

1. Copy isi `system-prompt.md`.
2. Tempel ke System Prompt atau Custom Instructions.
3. Kirim naskah + instruksi rewrite.

Contoh:

```text
Tolong rewrite tulisan ini dengan gaya manusia Indonesia: kalimat bervariasi, spesifik, tidak kaku, tanpa frase AI.
```

### Cek cepat apakah aturan aktif

Kirim satu prompt uji ini:

```text
Ubah paragraf ini jadi 2 versi:
1) versi formal ringkas
2) versi santai
Keduanya harus tetap natural dan hindari frasa AI template.
```

Kalau hasilnya lebih konkret, nggak generik, dan ritme kalimatnya bervariasi, berarti aturannya kebaca.

---

## Instalasi Lengkap

### 1) Claude.ai (Web) - Recommended

Download `anti-slop-writing.skill` dari [Releases](https://github.com/adenaufal/anti-slop-writing/releases/latest), lalu install via:

`Settings -> Skills -> Install from file`

### 2) Claude Code

Global:

```bash
git clone https://github.com/adenaufal/anti-slop-writing ~/.claude/skills/anti-slop-writing
```

Project-level:

```bash
git clone https://github.com/adenaufal/anti-slop-writing .claude/skills/anti-slop-writing
```

### 3) OpenAI Codex CLI

Global (semua project):

```bash
git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing
cp /tmp/anti-slop-writing/AGENTS.md ~/.codex/AGENTS.md
```

Project-level:

```bash
cp /tmp/anti-slop-writing/AGENTS.md ./AGENTS.md
```

### 4) Gemini CLI

Global:

```bash
git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing
cp /tmp/anti-slop-writing/GEMINI.md ~/.gemini/GEMINI.md
```

Project-level:

```bash
cp /tmp/anti-slop-writing/GEMINI.md ./GEMINI.md
```

### 5) GitHub Copilot

```bash
mkdir -p .github
cp /tmp/anti-slop-writing/AGENTS.md .github/copilot-instructions.md
```

### 6) Cursor

```bash
mkdir -p .cursor/rules
cp /tmp/anti-slop-writing/AGENTS.md .cursor/rules/anti-slop-writing.mdc
```

Atau taruh `AGENTS.md` di root repo.

### 7) Windsurf

```bash
mkdir -p .windsurf/rules
cp /tmp/anti-slop-writing/AGENTS.md .windsurf/rules/anti-slop-writing.md
```

### 8) Aider

```bash
aider --system-prompt "$(cat system-prompt.md)"
```

Atau masukin isi `system-prompt.md` ke config Aider kamu.

### 9) Tool lain / Web AI lain

Pakai `system-prompt.md` sebagai base prompt:
1. Buka file `system-prompt.md`
2. Copy semua isinya
3. Paste ke System Prompt / Custom Instructions tool kamu

---

## Isi Repo

```text
anti-slop-writing/
|- AGENTS.md
|- GEMINI.md
|- SKILL.md
|- system-prompt.md
|- README.md
|- LICENSE
|- references/
|  |- vocabulary-banlist.md
|  |- structural-patterns.md
|  `- wikipedia-sign-ai-writing.md

# Dirilis terpisah (tidak di-commit):
anti-slop-writing.skill
```

Catatan:
- `AGENTS.md`, `GEMINI.md`, dan `system-prompt.md` isinya sama.
- `SKILL.md` dipakai untuk format skill Claude Code.
- `anti-slop-writing.skill` adalah paket install untuk Claude.ai.

---

## Fokus Bahasa Indonesia

Repo ini sudah cover pola AI yang sering muncul di teks Indonesia, termasuk:
- gaya terlalu baku untuk konteks santai
- frasa template seperti "tidak hanya... tetapi juga"
- kebiasaan menutup tulisan dengan "Kesimpulan"
- nominalisasi berlebihan yang bikin kalimat berat
- pilihan kata yang terasa aman tapi kosong

Referensi lengkap ada di:
- `references/vocabulary-banlist.md`
- `references/structural-patterns.md`

---

## Sumber

- Wikipedia: [Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Kobak et al. (2024): *Delving into LLM-assisted writing in biomedical publications through excess vocabulary* ([arXiv:2406.07016](https://arxiv.org/abs/2406.07016))
- Russell, Karpinska & Iyyer (2025): *People who frequently use ChatGPT are accurate detectors of AI-generated text*
- Fraser, Dawkins & Kiritchenko (2025): *Detecting AI-generated text: factors influencing detectability*
- Wang et al. (2024): *M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection*
- Lovenia et al. (2024): *SEACrowd* ([arXiv:2406.10118](https://arxiv.org/abs/2406.10118))
- Ilman Akbar (2024): *Cara gampang mendeteksi konten buatan AI secara manual*
- The Conversation Indonesia (2024): *Mengapa tulisan asli bisa terdeteksi buatan AI*

---

## Credits

- Original insight by [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877)
- Wikipedia [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)

---

## License

MIT
