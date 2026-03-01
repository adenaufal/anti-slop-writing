# anti-slop-writing

[Bahasa Indonesia](README.md) | English

A universal skill that helps AI output read more human, specific, and less stiff. Works with Claude.ai (web), Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor, Windsurf, and other tools that support system prompts.

Based on Wikipedia ["Signs of AI Writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and AI text detection research.

Inspired by [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877).

---

## Quick Start (Claude.ai / Claude Web)

> **This is the main path for Claude.ai web users.**
>
> 1. Open [latest release](https://github.com/adenaufal/anti-slop-writing/releases/latest)
> 2. Download `anti-slop-writing.skill`
> 3. In Claude.ai: `Settings -> Skills -> Install from file`
> 4. Select the downloaded `anti-slop-writing.skill`
> 5. Start a new chat and use your prompt as usual

If you use Claude web, this is the fastest setup.

---

## Before vs After

**Without this skill:**
> The festival serves as a vibrant testament to the region's rich cultural heritage, showcasing the intricate tapestry of traditions that have endured through the ages, contributing to the broader social fabric of the community.

**With this skill:**
> The festival has run every April since 1987. Locals build their own stalls. The goat cheese and handmade pottery sell out by noon.

---

## How to Use After Install

Use natural prompts, for example:
- "Rewrite this so it sounds more human."
- "Make this not read like AI."
- "Remove stiff language and make it natural."
- "No slop. Keep it direct."

For Claude Code, you can also trigger with `/anti-slop-writing`.

---

## How to Use in Each AI Agent

This section answers: "I installed it, now how do I use it?"

### Claude.ai / Claude Web

1. Install the `.skill` file first (see Quick Start above).
2. Open a new chat.
3. Paste your draft and ask for rewrite.
4. If needed, mention skill name in prompt: "use anti-slop-writing."

Example prompt:

```text
Use anti-slop-writing. Rewrite this paragraph in natural Indonesian, keep it direct, and avoid AI template phrases.
```

### Claude Code

1. Make sure the skill repo exists at `~/.claude/skills/anti-slop-writing` or `.claude/skills/anti-slop-writing`.
2. In Claude Code chat, use `/anti-slop-writing` or a normal rewrite request.
3. Paste the text you want to rewrite.

Example:

```text
/anti-slop-writing
Rewrite this draft. Make it more human, shorter, and remove AI patterns.
```

### OpenAI Codex CLI

1. Make sure `AGENTS.md` is copied to `~/.codex/AGENTS.md` or project root.
2. Start Codex in the correct project.
3. Ask rewrite as usual.

Example:

```text
Rewrite this landing page copy so it sounds natural, not generic, and readable for Indonesian users.
```

### Gemini CLI

1. Make sure `GEMINI.md` exists in `~/.gemini/GEMINI.md` or project root.
2. Start Gemini from your project folder.
3. Send rewrite instruction.

Example:

```text
Edit this article. Avoid AI-style phrasing and make the Indonesian feel more natural and specific.
```

### GitHub Copilot / Cursor / Windsurf

1. Make sure instruction file is installed:
   - Copilot: `.github/copilot-instructions.md`
   - Cursor: `.cursor/rules/anti-slop-writing.mdc` or `AGENTS.md`
   - Windsurf: `.windsurf/rules/anti-slop-writing.md`
2. Open the target text file.
3. Use chat assistant and ask for anti-slop rewrite.

Example:

```text
Rewrite this section to sound more human, remove AI cliches, and keep the original meaning.
```

### Aider

1. Run Aider with `system-prompt.md`.
2. Ask Aider to edit your target text.

Command:

```bash
aider --system-prompt "$(cat system-prompt.md)"
```

Prompt:

```text
Edit this file. Make the writing style less detectable as AI-generated.
```

### ChatGPT / Other Web AI

1. Copy `system-prompt.md` content.
2. Paste it into System Prompt or Custom Instructions.
3. Send your draft + rewrite instruction.

Example:

```text
Rewrite this text in a natural Indonesian style: varied sentence rhythm, specific details, no AI template phrasing.
```

### Quick Check to Confirm Rules Are Active

Send this test prompt:

```text
Rewrite this paragraph into 2 versions:
1) short formal version
2) casual version
Both must stay natural and avoid AI template phrasing.
```

If output becomes more concrete, less generic, and sentence rhythm varies, the rules are active.

---

## Full Installation

### 1) Claude.ai (Web) - Recommended

Download `anti-slop-writing.skill` from [Releases](https://github.com/adenaufal/anti-slop-writing/releases/latest), then install via:

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

Global:

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

Or place `AGENTS.md` in project root.

### 7) Windsurf

```bash
mkdir -p .windsurf/rules
cp /tmp/anti-slop-writing/AGENTS.md .windsurf/rules/anti-slop-writing.md
```

### 8) Aider

```bash
aider --system-prompt "$(cat system-prompt.md)"
```

Or place `system-prompt.md` content in your Aider config.

### 9) Other tools / Other web AI

Use `system-prompt.md` as base prompt:
1. Open `system-prompt.md`
2. Copy full content
3. Paste into System Prompt / Custom Instructions

---

## Repo Contents

```text
anti-slop-writing/
|- AGENTS.md
|- GEMINI.md
|- SKILL.md
|- system-prompt.md
|- README.md
|- README.en.md
|- LICENSE
|- references/
|  |- vocabulary-banlist.md
|  |- structural-patterns.md
|  `- wikipedia-sign-ai-writing.md

# Released separately (not committed):
anti-slop-writing.skill
```

Notes:
- `AGENTS.md`, `GEMINI.md`, and `system-prompt.md` contain the same core rules.
- `SKILL.md` is for Claude Code skill format.
- `anti-slop-writing.skill` is the install package for Claude.ai.

---

## Indonesian Language Focus

This repo includes Indonesian-specific AI writing patterns, including:
- over-formal style in casual contexts
- formulaic phrase templates like "tidak hanya... tetapi juga"
- forced "Kesimpulan" ending
- heavy nominalization that makes text stiff
- safe but empty word choices

See:
- `references/vocabulary-banlist.md`
- `references/structural-patterns.md`

---

## Sources

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
