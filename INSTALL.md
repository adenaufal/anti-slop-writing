# Installation Guide / Panduan Instalasi

**Bahasa Indonesia (default)** | [English](#english)

Repo ini berisi skill anti-slop-writing yang bisa dipakai di banyak platform AI, bukan cuma Claude. Halaman ini jelasin cara install di tiap platform.

## Pilih Versi yang Tepat

Repo ini punya dua versi:

| Versi | Ukuran | Untuk Platform |
|---|---|---|
| **Full** (`SKILL.md` / `system-prompt.md`) | ~12-16 KB | Claude Projects, Gemini Gems, Copilot agents, API dengan system prompt besar |
| **Lite** (`SKILL-lite.md`) | ~4 KB | ChatGPT Custom Instructions, platform dengan batas karakter ketat |

Aturan umum: **coba Full dulu**. Kalau dapat error "system prompt too long" atau kepotong, ganti ke Lite.

Bahasa: pilih folder `indonesian/` (Bahasa Indonesia) atau `english/` (English).

---

## ChatGPT

### Custom Instructions (gratis + Plus + Team)

1. Buka ChatGPT → klik avatar kanan atas → **Customize ChatGPT**
2. Di kolom **"What traits should ChatGPT have?"** atau **"Anything else ChatGPT should know"**: paste isi file.
   - **Disarankan pakai Lite**: `indonesian/SKILL-lite.md` atau `english/SKILL-lite.md`
   - Kalau muat (biasanya limit 1500-3000 karakter per kolom), isi Full `system-prompt.md`
3. Klik **Save**
4. Tiap chat baru otomatis pakai instruksi ini

**Catatan**: ChatGPT Custom Instructions punya batas karakter. Kalau kena "too long", pakai Lite.

### ChatGPT Projects (Plus + Team + Enterprise)

Projects punya sistem prompt yang lebih longgar (sekitar 8000 karakter).

1. Bikin Project baru: sidebar kiri → **New project**
2. Klik Project → **Instructions** (atau "Add instructions")
3. Paste isi `indonesian/system-prompt.md` atau `english/system-prompt.md` (Full version muat di sini)
4. Upload juga file `references/vocabulary-banlist.md` dan `references/structural-patterns.md` kalau mau aturan lebih komplit (via **Files** di Project)

Tiap chat dalam Project itu otomatis pakai instructions-nya.

### ChatGPT Custom GPTs (Plus + Team)

1. **Explore GPTs** → **Create**
2. Di tab **Configure**, kolom **Instructions**: paste `system-prompt.md`
3. Di **Knowledge**, upload file `references/` kalau perlu
4. Set nama, deskripsi, publish

---

## Gemini (Google)

### Gems (gemini.google.com)

Gems = custom Gemini dengan system instructions.

1. Buka [gemini.google.com](https://gemini.google.com)
2. Sidebar kiri → **Gems** → **+ New Gem**
3. Di **Instructions**: paste isi `indonesian/GEMINI.md` atau `english/GEMINI.md`
4. Kasih nama (misal: "Anti-Slop Writer ID"), deskripsi singkat
5. **Save**

Pakai Gem itu tiap kali mau nulis tanpa slop.

**Catatan**: Gemini Gems support system instructions yang cukup panjang (sekitar 8000 karakter). Full version muat.

### Gemini API (developers)

Kalau lo pakai Gemini via API:

```python
from google import genai
from google.genai import types

with open("english/system-prompt.md") as f:
    sp = f.read()

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-pro",
    config=types.GenerateContentConfig(system_instruction=sp),
    contents="Tulis artikel tentang kopi specialty di Bandung, 600 kata.",
)
```

Untuk Bahasa Indonesia, pakai `indonesian/system-prompt.md`.

### Gemini Advanced (di Google Workspace)

1. Buka Gemini di Google Workspace (Docs, Gmail, dll)
2. Di panel Gemini, sayangnya belum ada custom system prompt untuk user biasa
3. Workaround: copy isi skill, paste di awal prompt lo tiap kali mau nulis

---

## GitHub Copilot / Microsoft 365

### Copilot Chat (VS Code, Visual Studio)

GitHub Copilot Chat baca `.github/copilot-instructions.md` dari root repo:

```bash
git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing
mkdir -p .github
cp /tmp/anti-slop-writing/indonesian/AGENTS.md .github/copilot-instructions.md
```

Atau untuk English: ganti `indonesian/` dengan `english/`.

Copilot Chat di repo itu otomatis pakai instructions-nya.

### Copilot Custom Instructions (per-user)

Di VS Code:
1. Command Palette → **Preferences: Open Settings (JSON)**
2. Tambah:
```json
{
  "github.copilot.chat.customInstructions": "paste isi SKILL-lite.md di sini sebagai satu baris"
}
```

### Microsoft 365 Copilot (Word, Outlook, dll)

1. Di Copilot side panel → **Settings** → **Custom instructions** (kalau tersedia di tenant lo)
2. Paste isi `SKILL-lite.md`

Kalau Custom Instructions belum available di tenant lo, workaround: mulai prompt dengan "Pakai aturan anti-slop: [paste ringkas aturan utama]..."

### Microsoft 365 Copilot Agents (Copilot Studio)

1. Buka Copilot Studio
2. Bikin **New agent** atau edit existing
3. Di **Instructions**: paste `english/system-prompt.md`
4. Publish

---

## Generic/API (OpenAI, Anthropic, Local LLM)

### OpenAI API

```python
from openai import OpenAI

with open("english/system-prompt.md") as f:
    sp = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": sp},
        {"role": "user", "content": "Tulis artikel 500 kata tentang kopi Aceh Gayo."}
    ]
)
```

Untuk Indonesian: pakai `indonesian/system-prompt.md`.

### Anthropic API (Claude)

```python
import anthropic

with open("english/system-prompt.md") as f:
    sp = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    system=sp,
    messages=[{"role": "user", "content": "Tulis essay 800 kata..."}]
)
```

### Ollama (local LLM)

```bash
# Clone repo
git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing

# Bikin Modelfile
cat > Modelfile <<EOF
FROM llama3.2
SYSTEM """
$(cat /tmp/anti-slop-writing/english/system-prompt.md)
"""
EOF

# Bikin model custom
ollama create anti-slop -f Modelfile

# Jalanin
ollama run anti-slop
```

### LM Studio

1. Download model via LM Studio
2. Di chat window → **System Prompt** icon (kiri atas)
3. Paste isi `english/system-prompt.md` atau `indonesian/system-prompt.md`
4. Save

### Kobold.cpp / Text Generation WebUI

Biasanya ada field **System Prompt** atau **Character Card**. Paste isi `system-prompt.md` di situ.

### Open WebUI

1. Settings → **Default Models** → **System Prompt**
2. Paste isi skill
3. Save

---

## Claude (recap)

### Claude.ai Web

1. Download `anti-slop-writing.skill` dari [Releases](https://github.com/adenaufal/anti-slop-writing/releases/latest)
2. Claude.ai → **Settings** → **Skills** → **Install from file**
3. Upload file → langsung jalan

### Claude Code

```bash
git clone https://github.com/adenaufal/anti-slop-writing ~/.claude/skills/anti-slop-writing
```

### Claude Projects

1. Bikin Project baru
2. **Custom Instructions** → paste `english/system-prompt.md` atau `indonesian/system-prompt.md`
3. Upload file referensi via **Project Knowledge**

---

## Troubleshooting

### "System prompt too long"
Ganti dari `SKILL.md` ke `SKILL-lite.md`. Kalau masih kepanjangan, potong bagian yang nggak perlu (misal bagian checklist bisa dipotong, tier tone bisa dipilih satu aja).

### Output masih kedengaran AI
1. Cek platform lo support system prompt dengan benar. Beberapa tool chat web nggak support.
2. Kalau Custom Instructions kepotong, mungkin cuma sebagian yang kepake.
3. Test dengan prompt kayak: "Tulis ulang paragraf ini biar lebih natural, zero em dash." Kalau hasilnya masih pakai em dash, system prompt nggak aktif.

### Output di Indonesian masih pakai "Anda" di konteks santai
Tambahkan di prompt lo: "Pakai tier [semi-formal/informal], jangan pakai 'Anda'."

---

<a name="english"></a>

# English

**English** | [Bahasa Indonesia](#installation-guide--panduan-instalasi)

This repo contains the anti-slop-writing skill that works across many AI platforms, not just Claude. This page covers installation per platform.

## Choose the Right Version

This repo has two versions:

| Version | Size | Best For |
|---|---|---|
| **Full** (`SKILL.md` / `system-prompt.md`) | ~12-16 KB | Claude Projects, Gemini Gems, Copilot agents, APIs with generous system prompts |
| **Lite** (`SKILL-lite.md`) | ~4 KB | ChatGPT Custom Instructions, platforms with strict char limits |

General rule: **try Full first**. If you get "system prompt too long" or it gets truncated, switch to Lite.

Language: pick `english/` or `indonesian/` folder.

---

## ChatGPT

### Custom Instructions (Free + Plus + Team)

1. Open ChatGPT, click your avatar top-right, **Customize ChatGPT**
2. In **"What traits should ChatGPT have?"** or **"Anything else ChatGPT should know"**: paste contents.
   - **Recommended: Lite** (`english/SKILL-lite.md`)
   - If it fits (1500-3000 char limit per field), try `english/system-prompt.md`
3. Click **Save**
4. Every new chat uses these instructions

**Note**: ChatGPT Custom Instructions has a character limit. If you hit "too long", switch to Lite.

### ChatGPT Projects (Plus + Team + Enterprise)

Projects have a much larger system prompt (around 8000 chars).

1. Create a new Project: sidebar, **New project**
2. Click Project, **Instructions** (or "Add instructions")
3. Paste `english/system-prompt.md` (Full version fits)
4. Upload `references/vocabulary-banlist.md` and `references/structural-patterns.md` via **Files** for complete coverage

Every chat inside the Project uses these instructions.

### ChatGPT Custom GPTs (Plus + Team)

1. **Explore GPTs**, **Create**
2. In **Configure** tab, **Instructions** field: paste `system-prompt.md`
3. In **Knowledge**, upload `references/` files if needed
4. Set name, description, publish

---

## Gemini (Google)

### Gems (gemini.google.com)

Gems are custom Gemini personalities with system instructions.

1. Go to [gemini.google.com](https://gemini.google.com)
2. Left sidebar, **Gems**, **+ New Gem**
3. In **Instructions**: paste `english/GEMINI.md`
4. Name it (e.g., "Anti-Slop Writer"), add brief description
5. **Save**

Use that Gem whenever you want non-slop writing.

**Note**: Gemini Gems support fairly long instructions (~8000 chars). Full version fits.

### Gemini API (developers)

```python
from google import genai
from google.genai import types

with open("english/system-prompt.md") as f:
    sp = f.read()

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-pro",
    config=types.GenerateContentConfig(system_instruction=sp),
    contents="Write a 600-word essay on specialty coffee.",
)
```

### Gemini in Workspace (Docs, Gmail, etc)

No per-user system prompt currently available. Workaround: paste the skill at the start of each prompt.

---

## GitHub Copilot / Microsoft 365

### Copilot Chat (VS Code, Visual Studio)

GitHub Copilot Chat reads `.github/copilot-instructions.md`:

```bash
git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing
mkdir -p .github
cp /tmp/anti-slop-writing/english/AGENTS.md .github/copilot-instructions.md
```

Copilot Chat in that repo will automatically use these instructions.

### Copilot Custom Instructions (per-user)

In VS Code:
1. Command Palette, **Preferences: Open Settings (JSON)**
2. Add:
```json
{
  "github.copilot.chat.customInstructions": "paste SKILL-lite.md content as one line"
}
```

### Microsoft 365 Copilot (Word, Outlook, etc)

1. In Copilot side panel, **Settings**, **Custom instructions** (if available in your tenant)
2. Paste `SKILL-lite.md` contents

If Custom Instructions isn't available, workaround: start prompts with "Use anti-slop rules: [paste key rules summary]..."

### Microsoft 365 Copilot Agents (Copilot Studio)

1. Open Copilot Studio
2. Create **New agent** or edit existing
3. In **Instructions**: paste `english/system-prompt.md`
4. Publish

---

## Generic/API (OpenAI, Anthropic, Local LLM)

### OpenAI API

```python
from openai import OpenAI

with open("english/system-prompt.md") as f:
    sp = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": sp},
        {"role": "user", "content": "Write a 500-word article on specialty coffee."}
    ]
)
```

### Anthropic API (Claude)

```python
import anthropic

with open("english/system-prompt.md") as f:
    sp = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    system=sp,
    messages=[{"role": "user", "content": "Write an 800-word essay..."}]
)
```

### Ollama (local LLM)

```bash
git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing

cat > Modelfile <<EOF
FROM llama3.2
SYSTEM """
$(cat /tmp/anti-slop-writing/english/system-prompt.md)
"""
EOF

ollama create anti-slop -f Modelfile
ollama run anti-slop
```

### LM Studio

1. Download model via LM Studio
2. In chat, click **System Prompt** icon (top-left)
3. Paste `english/system-prompt.md`
4. Save

### Kobold.cpp / Text Generation WebUI

Look for **System Prompt** or **Character Card** field. Paste `system-prompt.md` there.

### Open WebUI

1. Settings, **Default Models**, **System Prompt**
2. Paste the skill
3. Save

---

## Claude (recap)

### Claude.ai Web

1. Download `anti-slop-writing.skill` from [Releases](https://github.com/adenaufal/anti-slop-writing/releases/latest)
2. Claude.ai, **Settings**, **Skills**, **Install from file**
3. Upload and go

### Claude Code

```bash
git clone https://github.com/adenaufal/anti-slop-writing ~/.claude/skills/anti-slop-writing
```

### Claude Projects

1. Create a new Project
2. **Custom Instructions**, paste `english/system-prompt.md`
3. Upload reference files via **Project Knowledge**

---

## Troubleshooting

### "System prompt too long"
Switch from `SKILL.md` to `SKILL-lite.md`. If still too long, trim sections (the checklist can be removed; pick only one tier for Indonesian).

### Output still reads as AI
1. Check that your platform actually supports system prompts. Some web chat tools don't.
2. If Custom Instructions got truncated, only part of the rules may be active.
3. Test with a prompt like: "Rewrite this paragraph to sound natural, with zero em dashes." If output still has em dashes, the system prompt isn't active.

### Output still uses "Anda" in casual Indonesian contexts
Add to your prompt: "Use [semi-formal/informal] tier. No 'Anda'."
