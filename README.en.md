# anti-slop-writing

**v4.1 · September 27, 2026**

[Bahasa Indonesia](README.md)

anti-slop-writing is a reusable set of writing and editing instructions. It helps AI produce clearer, more specific writing that fits the writer's voice.

Use the text directly in a writing conversation, or import a `.skill` package if your platform supports skill imports.

## Download or view Lite

Choose a language and size. For most people, choose **Full** if your platform can import a package; choose **Lite** to paste text into a chat or instruction field.

| Package | Bahasa Indonesia | English |
|---|---|---|
| Full | [Download `.skill`](https://github.com/adenaufal/anti-slop-writing/releases/download/v4.1/anti-slop-writing-id.skill) · [View SKILL.md](indonesian/SKILL.md) | [Download `.skill`](https://github.com/adenaufal/anti-slop-writing/releases/download/v4.1/anti-slop-writing-en.skill) · [View SKILL.md](english/SKILL.md) |
| Lite | [Download `.skill`](https://github.com/adenaufal/anti-slop-writing/releases/download/v4.1/anti-slop-writing-id-lite.skill) · [View Lite text](indonesian/SKILL-lite.md) | [Download `.skill`](https://github.com/adenaufal/anti-slop-writing/releases/download/v4.1/anti-slop-writing-en-lite.skill) · [View Lite text](english/SKILL-lite.md) |

See the changes and all packages in the [v4.1 release](https://github.com/adenaufal/anti-slop-writing/releases/tag/v4.1).

## Choose Full or Lite

| | Full | Lite |
|---|---|---|
| Includes | Complete guide and language-specific references | Core guidance in a shorter form |
| Suited to | Skill imports, projects, Gems, or instructions that support reference files | Pasting into a chat or a smaller instruction field |
| Keep in mind | Longer; file support and limits depend on the platform | Can still exceed some field limits; select and paste what fits |

Not every chat accepts files or has a custom-instructions field. Projects and Gems also depend on the features and limits of your account. If unsure, paste the Lite text into the conversation you are using.

## Start without installing

1. Open [English Lite](english/SKILL-lite.md) or [Bahasa Indonesia Lite](indonesian/SKILL-lite.md).
2. Copy from the main `# Anti-Slop...` heading onward. Skip the metadata block at the top, between the `---` lines.
3. Paste it at the start of a writing conversation, then add your draft or request.

Ready-to-use prompt:

> Use the writing guide above to edit this draft. Preserve its facts, meaning, level of certainty, and the writer's voice. Change only what makes it less clear or natural.

If you use Claude.ai, download a package from the table and follow [Claude's official instructions for importing a skill](https://support.claude.com/en/articles/12512180-use-skills-in-claude). A `.skill` package is a ZIP archive; if the uploader accepts only `.zip`, change the file extension to `.zip` without extracting or repacking it. Other platforms may use a different import process or may not support skill imports.

## Editing example

Constructed editorial exercise. Source facts: only the trial is delayed; the launch has not been cancelled; a new date has not been set.

**Before:** “A postponement of the trial has been carried out by the team, while a cancellation of the launch has not been carried out and a determination of a new date has not been made.”

**After:** “The team has postponed the trial. The launch has not been cancelled, and a new date has not been set.”

“Has not been” remains part of the meaning. Changing it to “the launch will not be cancelled” would add a promise absent from the source.

## What's new in v4.1

- Adds language-editing guidance and examples for English and Bahasa Indonesia.
- Clarifies checks for actors, references, chronology, causation, and the scope of words such as “only,” “not yet,” and “may.”
- Preserves the writer's voice: revise the parts that need work; do not automatically formalize casual writing or add slang to formal writing.
- Aligns Full, Lite, and adapters; constructed examples have been reviewed for factual drift.

## For technical users

### Install as a skill

Each skill has its own folder containing `SKILL.md`. To install from source:

1. Clone the repository to a working location, then choose **one language folder**: `english/` or `indonesian/`.
2. Copy `SKILL.md` for Full, or copy `SKILL-lite.md` and name it `SKILL.md` for Lite. Include the `references/` folder for the same language.
3. Use the skill folder name in the table below. It matches the `name` in the file's metadata.

| Language | Full folder | Lite folder |
|---|---|---|
| Bahasa Indonesia | `anti-slop-writing-id` | `anti-slop-writing-id-lite` |
| English | `anti-slop-writing` | `anti-slop-writing-lite` |

Claude Code reads personal skills from `~/.claude/skills/<skill-name>/SKILL.md` and project skills from `.claude/skills/<skill-name>/SKILL.md`. Other platforms have their own locations and activation rules. This repository's root holds the source; its skill files live inside the language folders.

For the `AGENTS.md`, `GEMINI.md`, and `system-prompt.md` adapters, follow the [platform installation guide](INSTALL.md) and include the same language's `references/`. Merge the rules with your existing instructions to preserve them.

### Source map

- `english/` and `indonesian/`: Full and Lite skills, adapters, and language references.
- `*/references/language-editing.md`: language-editing route and examples.
- `*/references/model-coverage.md`: historical model release notes and sources.
- `evaluations/`: synthetic scenarios, outputs, and the v4.1 evaluation record.
- `scripts/build_skills.py`: validates sources and builds or checks the four packages.

Build packages with `python scripts/build_skills.py`. Check existing packages without rewriting them with `python scripts/build_skills.py --check`.

## Evaluation limits

The [v4.1 evaluation record](evaluations/v4.1.md) covers 8 scenarios (4 per language) and 16 Full/Lite outputs from `gpt-6-luna` at medium reasoning. This is a small check of the instructions, not a benchmark of all providers or models. The guide cannot guarantee detector results, and detectors cannot reliably establish authorship. Model coverage in the [reference](english/references/model-coverage.md) is the v4.0 release history, not a v4.1 evaluation.

## Sources and credits

- Language guidance: [English](english/references/language-editing.md) · [Bahasa Indonesia](indonesian/references/language-editing.md)
- Historical model notes: [releases, dates, and sources](english/references/model-coverage.md)
- [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Kobak et al. (2024), [Delving into LLM-assisted writing](https://arxiv.org/abs/2406.07016)
- [@mkbijaksana](https://x.com/mkbijaksana/status/2027714311330627877) · Wikipedia [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)

## License

MIT. See [LICENSE](LICENSE).
