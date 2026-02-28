# anti-slop-writing

A universal AI agent skill that makes generated text read as authentically human. Works with Claude Code, Gemini CLI, OpenAI Codex CLI, GitHub Copilot, Cursor, Windsurf, and any web-based AI interface.

Based on Wikipedia's ["Signs of AI Writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and peer-reviewed LLM detection research.

Inspired by [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877) — the original insight of using the Wikipedia AI writing catalog as a writing ruleset.

---

## Before vs. After

**Without this skill:**
> The festival serves as a vibrant testament to the region's rich cultural heritage, showcasing the intricate tapestry of traditions that have endured through the ages, contributing to the broader social fabric of the community.

**With this skill:**
> The festival has run every April since 1987. Locals build their own stalls. The goat cheese and handmade pottery sell out by noon.

---

## Installation

### Claude.ai

Download `anti-slop-writing.skill` from the [Releases](https://github.com/adenaufal/anti-slop-writing/releases) page, then install it in Claude.ai via **Settings → Skills → Install from file**.

---

### Claude Code

```bash
git clone https://github.com/adenaufal/anti-slop-writing ~/.claude/skills/anti-slop-writing
```

Or project-level:
```bash
git clone https://github.com/adenaufal/anti-slop-writing .claude/skills/anti-slop-writing
```

Trigger with: *"write this without AI patterns"*, *"make this sound human"*, *"no slop"*, or `/anti-slop-writing`

---

### OpenAI Codex CLI

Global (applies to all projects):
```bash
git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing
cp /tmp/anti-slop-writing/AGENTS.md ~/.codex/AGENTS.md
```

Project-level:
```bash
cp /tmp/anti-slop-writing/AGENTS.md ./AGENTS.md
```

Codex reads `AGENTS.md` automatically from `~/.codex/` and the project root.

---

### Gemini CLI

Global:
```bash
git clone https://github.com/adenaufal/anti-slop-writing /tmp/anti-slop-writing
cp /tmp/anti-slop-writing/GEMINI.md ~/.gemini/GEMINI.md
```

Project-level (Gemini CLI traverses up from the current directory):
```bash
cp /tmp/anti-slop-writing/GEMINI.md ./GEMINI.md
```

---

### GitHub Copilot

```bash
mkdir -p .github
cp /tmp/anti-slop-writing/AGENTS.md .github/copilot-instructions.md
```

Copilot reads `.github/copilot-instructions.md` automatically. It also supports `AGENTS.md` directly in the repo root.

---

### Cursor

```bash
mkdir -p .cursor/rules
cp /tmp/anti-slop-writing/AGENTS.md .cursor/rules/anti-slop-writing.mdc
```

Or drop `AGENTS.md` in the project root — Cursor imports it as an agent-mode rule.

---

### Windsurf

```bash
mkdir -p .windsurf/rules
cp /tmp/anti-slop-writing/AGENTS.md .windsurf/rules/anti-slop-writing.md
```

---

### Aider

Pass the system prompt inline at startup:
```bash
aider --system-prompt "$(cat system-prompt.md)"
```

Or add to your Aider config profile in `~/.aider/.aider.conf.yml`:
```yaml
system_prompt_prefix: |
  # anti-slop-writing rules
  [paste contents of system-prompt.md here]
```

---

### Any web-based AI (ChatGPT, Claude.ai, Gemini, Grok, etc.)

1. Open `system-prompt.md` from this repo
2. Copy the full contents
3. Paste into the **System Prompt** or **Custom Instructions** field of your AI interface
4. Or paste at the start of any conversation before your writing request

---

### Any other tool

Copy `system-prompt.md` — it's a self-contained, plain-text prompt with no platform dependencies. Paste it wherever your tool accepts system-level instructions.

---

## What's in this repo

```
anti-slop-writing/
├── AGENTS.md             ← Codex CLI, GitHub Copilot, Cursor (copy to project or config dir)
├── GEMINI.md             ← Gemini CLI (copy to ~/.gemini/ or project root)
├── SKILL.md              ← Claude Code skill with file references
├── system-prompt.md      ← Universal — copy-paste into any AI interface
├── README.md
├── LICENSE
└── references/
    ├── vocabulary-banlist.md        ← Full banned word list, organized by AI model era
    ├── structural-patterns.md       ← 12 structural patterns with before/after examples
    └── wikipedia-sign-ai-writing.md ← Offline copy of the Wikipedia source

# Released separately (not committed to git):
anti-slop-writing.skill             ← Claude.ai installable package (zip of the above)
```

`AGENTS.md`, `GEMINI.md`, and `system-prompt.md` are **identical in content** — self-contained with all rules inline. The different filenames exist because different tools look for different filenames.

`SKILL.md` is Claude Code-specific: it uses YAML frontmatter for skill metadata and references the `references/` files for extended context.

---

## What the rules target

AI text detection relies on two primary metrics:

**Perplexity** — how predictable the word choices are. AI produces low-perplexity text: smooth, statistically safe, unsurprising. The vocabulary ban list directly increases perplexity by eliminating the words AI defaults to most.

**Burstiness** — variance in sentence length and structure. AI text clusters around 10–20 word sentences with consistent structure throughout a passage. The structural rules force dramatic variation — 4-word sentences next to 30-word ones.

Every rule in this skill targets one or both of these metrics.

---

## Sources

- Wikipedia: [Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup)
- Kobak et al. (2024): *Delving into LLM-assisted writing in biomedical publications through excess vocabulary* — Science Advances ([arXiv:2406.07016](https://arxiv.org/abs/2406.07016))
- Russell, Karpinska & Iyyer (2025): *People who frequently use ChatGPT are accurate detectors of AI-generated text* — ACL 2025
- Fraser, Dawkins & Kiritchenko (2025): *Detecting AI-generated text: factors influencing detectability* — JAIR 82:2233-2278

---

## Credits

- Original insight by [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877) — using Wikipedia's AI writing catalog as a system prompt
- Wikipedia [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) editors who compiled the Signs of AI Writing guide

---

## License

MIT
