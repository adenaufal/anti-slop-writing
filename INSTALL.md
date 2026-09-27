# Installation Guide / Panduan Instalasi

**Bahasa Indonesia (default)** | [English](#english)

Repo ini berisi skill anti-slop-writing yang bisa dipakai di banyak platform AI, bukan cuma Claude. Halaman ini jelasin cara install di tiap platform.

## Pilih Versi yang Tepat

Repo ini punya dua versi:

| Versi | Ukuran | Untuk Platform |
|---|---|---|
| **Full** (`SKILL.md` / `system-prompt.md`) | sekitar 23 KB (English) / 38 KB (Indonesia), di luar referensi | Projects, Gems, agents, API, atau platform yang menerima file referensi |
| **Lite** (`SKILL-lite.md`) | sekitar 3,5 KB (English) / 4 KB (Indonesia) | Chat atau kolom instruksi dengan batas lebih ketat; periksa batas karakter |

Lite tetap lebih dari 1.500 karakter, jadi mungkin tidak muat di kolom instruksi akun ChatGPT Free/Go. Pilih dan tempel hanya aturan yang sesuai dengan batas platform, atau unggah Full sebagai file referensi bila platform mendukungnya. Tidak ada versi yang dijamin muat di semua kolom instruksi.

Bahasa: pilih folder `indonesian/` (Bahasa Indonesia) atau `english/` (English).

Cakupan model dan sumber rilis v4: [Bahasa Indonesia](indonesian/references/model-coverage.md) | [English](english/references/model-coverage.md).

Panduan tata bahasa v4.1: [Bahasa Indonesia](indonesian/references/language-editing.md) | [English](english/references/language-editing.md). Saat menyalin adapter Full (`AGENTS.md`, `GEMINI.md`, atau `system-prompt.md`), sediakan juga folder `references/` dari bahasa yang sama di lokasi relatif yang diminta, atau unggah referensinya sebagai sumber proyek. Untuk kolom yang hanya menerima teks, Lite memuat pemeriksaan inti; referensi menambah contoh jika platform mendukung file.

Untuk membangun empat paket dari checkout ini, jalankan `python scripts/build_skills.py`; gunakan `python scripts/build_skills.py --check` untuk memeriksa paket tanpa menulis ulang. Perintah ini hanya memakai pustaka standar Python dan tidak memanggil API model.

---

## ChatGPT

### Custom Instructions (gratis + Plus + Team)

1. Buka **Settings → Personalization → Custom Instructions** (nama/menu dapat berbeda antar perangkat).
2. Tempel aturan pilihan. Batas resmi saat ini: Free dan Go hingga 1.500 karakter; Plus, Pro, Enterprise, Business, dan Education hingga 5.000 karakter. Lite v4.1 English sekitar 3.500 karakter dan Indonesia sekitar 4.000 karakter; keduanya melampaui 1.500 karakter. Pilih beberapa aturan utama agar sesuai dengan batas akun Anda.
3. Klik **Save**
4. Tiap chat baru otomatis pakai instruksi ini

Sumber batas dan langkah UI: [ChatGPT Custom Instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions).

### ChatGPT Projects (Plus + Team + Enterprise)

1. Bikin Project baru: sidebar kiri → **New project**
2. Klik Project → **Instructions** (atau "Add instructions")
3. Tambahkan aturan pilihan ke Project instructions.
4. Upload `indonesian/SKILL.md` atau `english/SKILL.md`, serta file referensi yang diperlukan, sebagai project sources.

Project instructions berlaku di dalam project; file sumber dapat dipakai sebagai referensi. Batas bergantung pada akun. [Panduan Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

### ChatGPT Custom GPTs (Plus + Team)

1. **Explore GPTs** → **Create**
2. Di tab **Configure**, tambahkan aturan pilihan ke **Instructions**.
3. Di **Knowledge**, unggah Full dan file referensi bila tersedia dan sesuai batas akun.
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

Jangan mengandalkan batas karakter tetap; periksa batas akun Anda. Jika Full tidak muat, tambahkan aturan pilihan dan unggah berkas sebagai sumber bila tersedia.

### Gemini API (developers)

Kalau lo pakai Gemini via API:

```python
from google import genai
from google.genai import types

with open("english/system-prompt.md", encoding="utf-8") as f:
    sp = f.read()

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(system_instruction=sp),
    contents="Tulis artikel tentang kopi specialty di Bandung, 600 kata.",
)
```

Model ID: [Gemini API model catalog](https://ai.google.dev/gemini-api/docs/models).

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

## Generic/API (OpenAI, Anthropic, xAI, Local LLM)

### OpenAI API

```python
from openai import OpenAI

with open("english/system-prompt.md", encoding="utf-8") as f:
    sp = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-6-sol",
    messages=[
        {"role": "system", "content": sp},
        {"role": "user", "content": "Tulis artikel 500 kata tentang kopi Aceh Gayo."}
    ]
)
```

Model ID: [`gpt-6-sol` API docs](https://developers.openai.com/api/docs/models/gpt-6-sol).

Untuk Indonesian: pakai `indonesian/system-prompt.md`.

### Anthropic API (Claude)

```python
import anthropic

with open("english/system-prompt.md", encoding="utf-8") as f:
    sp = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    system=sp,
    messages=[{"role": "user", "content": "Tulis essay 800 kata..."}]
)
```

Model ID: [Claude Opus 5.5](https://www.anthropic.com/claude/opus).

### xAI API (Grok)

Pakai model API `grok-4.7` dengan klien OpenAI-compatible. Simpan API key di environment variable `XAI_API_KEY`; jangan tempel key langsung di kode.

```python
import os
from openai import OpenAI

with open("indonesian/system-prompt.md", encoding="utf-8") as f:
    sp = f.read()

client = OpenAI(base_url="https://api.x.ai/v1", api_key=os.environ["XAI_API_KEY"])
response = client.chat.completions.create(
    model="grok-4.7",
    messages=[
        {"role": "system", "content": sp},
        {"role": "user", "content": "Tulis artikel 500 kata tentang kopi Aceh Gayo."},
    ],
)
print(response.choices[0].message.content)
```

Model ID dan contoh klien: [Grok 4.7 API docs](https://docs.x.ai/developers/grok-4-7).

### Grok (chat konsumen)

Di awal chat, tempel isi `indonesian/SKILL-lite.md` sebagai instruksi menulis. Jika akun atau aplikasi Anda menyediakan kolom instruksi khusus, Anda juga bisa menaruh aturan pilihan di sana. Nama menu dan ketersediaannya dapat berbeda; bila teks terlalu panjang, pilih aturan yang paling penting.

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

1. Unduh paket Full atau Lite untuk bahasa yang dipilih dari [Release v4.1](https://github.com/adenaufal/anti-slop-writing/releases/tag/v4.1).
2. Di Claude.ai, buka **Customize → Skills → + Create skill → Upload a skill**, lalu unggah paket dan aktifkan skill. Jika kolom unggah hanya menerima `.zip`, ganti ekstensi `.skill` menjadi `.zip` tanpa membongkar isinya.
3. Ikuti [panduan resmi Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) untuk mengaktifkan fitur yang diperlukan. Setelah skill aktif, minta Claude menulis atau menyunting teks.

### Claude Code

```bash
git clone https://github.com/adenaufal/anti-slop-writing anti-slop-writing
mkdir -p ~/.claude/skills/anti-slop-writing-id
cp -R anti-slop-writing/indonesian/. ~/.claude/skills/anti-slop-writing-id/
```

Contoh Bash untuk macOS/Linux/Git Bash. Salin seluruh folder bahasa beserta `references/`; jangan menempatkan root repo sebagai satu skill karena `SKILL.md` ada di subfolder bahasa. Untuk English, gunakan folder `english/` dan tujuan `anti-slop-writing`.

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
| **Full** (`SKILL.md` / `system-prompt.md`) | about 20 KB (English) / 40 KB (Indonesian) currently | Projects, Gems, agents, APIs, or platforms that accept reference files |
| **Lite** (`SKILL-lite.md`) | about 2 KB (English) / 4 KB (Indonesian) | Chats or instruction fields with tighter limits; check the character limit |

Lite still exceeds 1,500 characters, so it may not fit ChatGPT Free/Go instruction fields. Select and paste only rules that fit the platform's displayed limit, or upload Full as a reference file where supported. No version is guaranteed to fit every instruction field.

Language: pick `english/` or `indonesian/` folder.

For v4 model coverage and release sources, see [English](english/references/model-coverage.md) | [Bahasa Indonesia](indonesian/references/model-coverage.md).

---

## ChatGPT

### Custom Instructions (Free + Plus + Team)

1. Open **Settings → Personalization → Custom Instructions** (menu labels may vary by device).
2. Paste selected rules. Current official limits: up to 1,500 characters for Free and Go; up to 5,000 for Plus, Pro, Enterprise, Business, and Education. The English Lite file is about 2 KB and the Indonesian Lite file about 4 KB; both exceed 1,500 characters. Select a few core rules that fit your account's limit.
3. Click **Save**
4. Every new chat uses these instructions

Source for current limits and steps: [ChatGPT Custom Instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions).

### ChatGPT Projects (Plus + Team + Enterprise)

1. Create a new Project: sidebar, **New project**
2. Click Project, **Instructions** (or "Add instructions")
3. Add selected rules to Project instructions.
4. Upload `english/SKILL.md` and needed reference files as project sources.

Project instructions apply inside the project; uploaded sources can provide reference material. Limits depend on your account. [Projects guide](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

### ChatGPT Custom GPTs (Plus + Team)

1. **Explore GPTs**, **Create**
2. In **Configure**, add selected rules to **Instructions**.
3. In **Knowledge**, upload Full and reference files where available and supported by your account limits.
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

Do not assume a fixed character limit. Check what your account accepts. If the full skill does not fit, add selected rules and attach the file as a source if the interface supports it.

### Gemini API (developers)

```python
from google import genai
from google.genai import types

with open("english/system-prompt.md", encoding="utf-8") as f:
    sp = f.read()

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(system_instruction=sp),
    contents="Write a 600-word essay on specialty coffee.",
)
```

Model ID: [Gemini API model catalog](https://ai.google.dev/gemini-api/docs/models).

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

## Generic/API (OpenAI, Anthropic, xAI, Local LLM)

### OpenAI API

```python
from openai import OpenAI

with open("english/system-prompt.md", encoding="utf-8") as f:
    sp = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-6-sol",
    messages=[
        {"role": "system", "content": sp},
        {"role": "user", "content": "Write a 500-word article on specialty coffee."}
    ]
)
```

Model ID: [`gpt-6-sol` API docs](https://developers.openai.com/api/docs/models/gpt-6-sol).

### Anthropic API (Claude)

```python
import anthropic

with open("english/system-prompt.md", encoding="utf-8") as f:
    sp = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    system=sp,
    messages=[{"role": "user", "content": "Write an 800-word essay..."}]
)
```

Model ID: [Claude Opus 5.5](https://www.anthropic.com/claude/opus).

### xAI API (Grok)

Use the `grok-4.7` model through the OpenAI-compatible client. Store your API key in the `XAI_API_KEY` environment variable; do not paste the key into code.

```python
import os
from openai import OpenAI

with open("english/system-prompt.md", encoding="utf-8") as f:
    sp = f.read()

client = OpenAI(base_url="https://api.x.ai/v1", api_key=os.environ["XAI_API_KEY"])
response = client.chat.completions.create(
    model="grok-4.7",
    messages=[
        {"role": "system", "content": sp},
        {"role": "user", "content": "Write a 500-word article on specialty coffee."},
    ],
)
print(response.choices[0].message.content)
```

For the model ID and client example, see [Grok 4.7 API docs](https://docs.x.ai/developers/grok-4-7).

### Grok (consumer chat)

At the start of a chat, paste `english/SKILL-lite.md` as your writing instruction. If your account or app provides a custom-instructions field, you can put selected rules there too. Menu names and availability may vary; if the text is too long, select the rules that matter most.

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

1. Download the Full or Lite package for your language from [Release v4.1](https://github.com/adenaufal/anti-slop-writing/releases/tag/v4.1).
2. In Claude.ai, open **Customize → Skills → + Create skill → Upload a skill**, upload the package, and enable it. If the uploader accepts only `.zip`, rename the `.skill` extension to `.zip` without unpacking it.
3. Follow [Claude's official guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude) to enable the required features. Once the skill is enabled, ask Claude to write or edit your text.

### Claude Code

```bash
git clone https://github.com/adenaufal/anti-slop-writing anti-slop-writing
mkdir -p ~/.claude/skills/anti-slop-writing
cp -R anti-slop-writing/english/. ~/.claude/skills/anti-slop-writing/
```

Bash example for macOS/Linux/Git Bash. Copy the entire language folder, including `references/`; the repository root itself is not one skill because its `SKILL.md` files live in language subfolders. For Indonesian, use `indonesian/` and the destination `anti-slop-writing-id`.

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
3. Test a concrete edit that preserves meaning, such as: "Rewrite this notice as exactly three bullets: only the trial is delayed; the launch has not been cancelled; no new date has been set." Check the format and qualifiers. A single failed instruction does not prove the skill is inactive, and punctuation alone is not an activation test.

### Output still uses "Anda" in casual Indonesian contexts
Add to your prompt: "Use [semi-formal/informal] tier. No 'Anda'."
