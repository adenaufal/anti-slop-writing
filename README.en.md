# anti-slop-writing

**v4.0** — September 27, 2026

[Bahasa Indonesia](README.md) | English

A universal skill that makes AI output read more human, specific, and less stiff.

Works with **ChatGPT, Claude, Gemini, Grok, Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor, Windsurf**, and tools that support writing instructions.

Based on Wikipedia ["Signs of AI Writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) + AI text detection research. Inspired by [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877).

---

## What's New in v4.0

- **Four-provider coverage:** updates after v3.0 (July 6, 2026) through September 27, 2026, with official sources and access status.
- **Checks for current model output:** assistant scaffolding, hype/reassurance, unwanted personas, citations, repetition, and requested formatting.
- **Clear evidence limits:** release facts are separate from editing heuristics. Unsupported legacy vocabulary/punctuation ratios and model fingerprint claims are removed.
- **Facts survive editing:** do not fabricate details, numbers, quotes, or experiences to sound human. The skill does not guarantee AI detector results.
- **Synchronized Full, Lite, and adapters:** English and Indonesian versions, including `AGENTS.md`, `GEMINI.md`, and `system-prompt.md`.

| Provider | Text releases covered since v3.0 |
|---|---|
| ChatGPT / OpenAI | GPT-5.6 Sol/Terra/Luna; GPT-6 Astra; GPT-6 Sol/Luna in API, Work, and Codex. GPT-6 Pro uses Astra. |
| Claude / Anthropic | Opus 5, Fable 5.1, Mythos 5.1 (restricted access), Opus 5.5. |
| Gemini / Google | 3.6 Flash, 3.5 Flash-Lite, 3.7 Flash, 3.8 Flash. |
| Grok / xAI | 4.5, 4.6, 4.7. |

Chat product labels and access can differ from API models. Sonnet/Haiku 5.5 were upcoming at review time. See [model coverage, dates, and sources](english/references/model-coverage.md). This is an instruction update based on official documentation; no live model comparison was run.

---

## Before vs After

**Without this skill:**
> The festival serves as a vibrant testament to the region's rich cultural heritage, showcasing the intricate tapestry of traditions that have endured through the ages, contributing to the broader social fabric of the community.

**With this skill:**
> The festival has run every April since 1987. Locals build their own stalls. The goat cheese and handmade pottery sell out by noon.

---

## Quick Start

### Claude.ai (Web) — Easiest

The Full and Lite v4.0 packages are available from [Release v4.0](https://github.com/adenaufal/anti-slop-writing/releases/tag/v4.0).

1. Download `anti-slop-writing-en.skill` (English) or `anti-slop-writing-id.skill` (Indonesian) from the [latest release](https://github.com/adenaufal/anti-slop-writing/releases/latest)
2. In Claude.ai: `Settings → Skills → Install from file`
3. Select the downloaded file
4. Start a new chat and go

### Claude Code

```bash
# Global
git clone https://github.com/adenaufal/anti-slop-writing ~/.claude/skills/anti-slop-writing

# Or per-project
git clone https://github.com/adenaufal/anti-slop-writing .claude/skills/anti-slop-writing
```

Skill file: `english/SKILL.md` (English) or `indonesian/SKILL.md` (Bahasa Indonesia).

### Other Tools (Codex CLI, Gemini CLI, Copilot, Cursor, Windsurf, Aider, ChatGPT, Grok)

See [Full Installation](#full-installation) below.

---

## How to Use

Use natural prompts:
- "Rewrite this so it sounds more human."
- "Make this not read like AI."
- "No slop. Keep it direct."

In Claude Code you can also use `/anti-slop-writing`.

### Quick Check

Send this test prompt:

```text
Rewrite this paragraph into 2 versions:
1) short formal version
2) casual version
Both must stay natural and avoid AI template phrasing.
```

If output is more concrete and sentence rhythm varies, the rules are active.

---

## Full Installation

> All tools besides Claude.ai need a repo clone first:
> ```bash
> git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing
> ```
> Then pick files from `english/` (English) or `indonesian/` (Bahasa Indonesia).

| Tool | File & Location |
|------|-----------------|
| **Codex CLI** (global) | `cp /tmp/anti-slop-writing/english/AGENTS.md ~/.codex/AGENTS.md` |
| **Codex CLI** (project) | `cp /tmp/anti-slop-writing/english/AGENTS.md ./AGENTS.md` |
| **Gemini CLI** (global) | `cp /tmp/anti-slop-writing/english/GEMINI.md ~/.gemini/GEMINI.md` |
| **Gemini CLI** (project) | `cp /tmp/anti-slop-writing/english/GEMINI.md ./GEMINI.md` |
| **GitHub Copilot** | `cp /tmp/anti-slop-writing/english/AGENTS.md .github/copilot-instructions.md` |
| **Cursor** | `cp /tmp/anti-slop-writing/english/AGENTS.md .cursor/rules/anti-slop-writing.mdc` |
| **Windsurf** | `cp /tmp/anti-slop-writing/english/AGENTS.md .windsurf/rules/anti-slop-writing.md` |
| **Aider** | `aider --system-prompt "$(cat english/system-prompt.md)"` |
| **ChatGPT / Grok / other** | Use writing instructions from `english/SKILL-lite.md`; for APIs or projects that support them, use `system-prompt.md` and references. Check the field limit. |

> Replace `english/` with `indonesian/` for Bahasa Indonesia.

---

## Repo Contents

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
├── references/              ← legacy (combined)
├── anti-slop-writing-en.skill   ← Full English package (local build)
├── anti-slop-writing-id.skill   ← Full Indonesian package (local build)
├── anti-slop-writing-en-lite.skill
├── anti-slop-writing-id-lite.skill
├── README.md
├── README.en.md
└── LICENSE
```

- `AGENTS.md`, `GEMINI.md`, `system-prompt.md` share the same core rules — just different formats per tool.
- `SKILL.md` is for Claude Code skill format.
- `anti-slop-writing-*.skill` are released separately via [Releases](https://github.com/adenaufal/anti-slop-writing/releases).
- Release v4.0 includes four packages: Full and Lite for English and Indonesian.

---

## Indonesian Language Support

This repo includes rules specific to AI patterns in Bahasa Indonesia text:
- Over-formal style in casual contexts
- Formulaic templates ("tidak hanya... tetapi juga")
- Forced "Kesimpulan" endings
- Heavy nominalization
- Missing discourse particles (nah/sih/dong/kan)
- Always-formal "Anda" regardless of register
- Translationese (English-calqued sentence structures)
- Symmetric two-clause hooks ("Banyak orang mengira X. Kenyataannya Y.")
- Prompt keyword repetition

Use files from the `indonesian/` folder.

---

## Sources

- July-September 2026 model releases: [four-provider timeline and official sources](english/references/model-coverage.md).
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
