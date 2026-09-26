# Model coverage and evidence (v4.0)

**Reviewed:** September 27, 2026. **Previous version:** v3.0, July 6, 2026 (commit `bffa2a5`). This reference tracks general-purpose text models and relevant product updates after that baseline. It is a dated snapshot, not a promise of future model coverage or identical access on every plan.

Read this file when a request names a model, asks which versions are covered, or needs release evidence. Ordinary writing can use the core skill without loading this timeline.

## Verified release timeline

### ChatGPT / OpenAI

| Date (2026) | Model or update | Scope and source |
|---|---|---|
| July 9 | GPT-5.6 Sol, Terra, Luna | General availability across ChatGPT, Codex and API; access differs by tier and surface. [GPT-5.6 announcement](https://openai.com/index/gpt-5-6/) |
| August 6 | GPT-5.6 Sol ChatGPT update; Luna access expansion | A product update within the generation, not a new base model. [ChatGPT update](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/) |
| September 3 | GPT-6 Astra | API release and an initially limited organizational ChatGPT rollout. [API changelog](https://developers.openai.com/api/docs/changelog), [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) |
| September 22 | GPT-6 Sol, Luna | Text-output API models, also in ChatGPT Work and Codex. Their availability there does not establish a default in ordinary ChatGPT Chat. [API changelog](https://developers.openai.com/api/docs/changelog), [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) |

GPT-6 Pro is a ChatGPT offering powered by Astra, not another base model. Check the current plan and surface rather than assuming a model from the ChatGPT brand. [ChatGPT model/access guide](https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)

**Writing evidence:** OpenAI describes the August Sol update as more focused and says extra reasoning effort should not change the writing tone. That is vendor-described behavior, not an independent prose fingerprint. [Update announcement](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)

### Claude / Anthropic

| Date (2026) | Model | Scope and source |
|---|---|---|
| July 24 | Claude Opus 5 | Released for Claude and developer use. [Opus 5 announcement](https://www.anthropic.com/news/claude-opus-5) |
| September 1 | Claude Fable 5.1, Mythos 5.1 | Fable is generally available; Mythos has restricted trusted access. They share an underlying model with different safeguards. The newsroom supplies the exact date; the launch page displays only the month. [Launch](https://www.anthropic.com/claude-fable-and-mythos-5-1), [Newsroom](https://www.anthropic.com/news) |
| September 22 | Claude Opus 5.5 | Released. Sonnet 5.5 and Haiku 5.5 were announced as upcoming, not released by this review date. [Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5) |

**Writing evidence:** Anthropic reports clearer, more natural communication and better adherence to writing instructions for Opus 5.5. This does not validate the old v3 punctuation ratios or a universal “Philosopher” dialect for current Claude models. [Opus 5.5 communication examples](https://www.anthropic.com/claude-opus-5-5)

### Gemini / Google

| Date (2026) | Model | Scope and source |
|---|---|---|
| July 21 | Gemini 3.6 Flash, 3.5 Flash-Lite | General text-capable models. [Launch](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) |
| August 13 | Gemini 3.7 Flash | Next Flash release. [Launch](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) |
| September 2 | Gemini 3.8 Flash | Latest general-purpose stable Flash release in this review. [Launch](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) |

The API registry confirms these dates and lists stable models separately from previews. Gemini 3.1 Pro remains a preview entry in the current catalog; its name is not evidence of a new post-v3 release. Live, TTS, image, embedding and specialist Cyber releases do not establish ordinary prose behavior. App labels and API IDs can differ. [Release/deprecation registry](https://ai.google.dev/gemini-api/docs/deprecations), [Model catalog](https://ai.google.dev/gemini-api/docs/models)

### Grok / xAI

| Date (2026) | Model | Scope and source |
|---|---|---|
| July 16 | Grok 4.5 | Launch for developer/agent surfaces; consumer rollout followed separately. [Launch](https://x.ai/news/grok-4-5) |
| August 12 | Grok 4.6 | Initial launch in Grok Build and Cursor; API availability is documented separately. [Launch](https://x.ai/news/grok-4-6), [API release notes](https://docs.x.ai/developers/release-notes) |
| September 21 | Grok 4.7 | Latest general-purpose release reviewed; launch includes Grok Build, Cursor and API. [Launch](https://x.ai/news/grok-4-7) |

These releases describe capabilities and distribution, not a measured sarcastic or “edgy” prose signature. Do not equate the Grok brand with a requested voice or assume every consumer surface uses the newest API model. [xAI news and rollout records](https://x.ai/news)

## Editorial checks for all four families

These are editing heuristics proposed by this skill. They are not findings from a controlled comparison of the listed models. Apply a check only when the draft exhibits the problem:

- Remove assistant preambles, unsolicited follow-up offers and process narration from an article, memo or caption. Keep an explanation of the reasoning when the requested format needs it.
- Cut stock reassurance, praise, motivational hooks and forced jokes. Match the requested voice; sarcasm and empathy can be appropriate when the context earns them.
- Replace abstract claims with supported details. Never invent names, numbers, quotes, citations or lived experiences to make text seem specific.
- Check whether each citation supports its nearby claim, whether information is current, and whether uncertainty survived the rewrite. Retrieved snippets and polished summaries still need verification.
- Merge repeated claims and unnecessary headings or bullets. Keep requested lists, comparisons and templates intact.
- Read for repeated sentence shapes and canned endings. Revise for meaning and flow, not a fixed sentence-length quota, arbitrary list size or punctuation detector score.

The skill edits language and structure. It does not identify authorship, guarantee detector results, or prove that a provider's internal writing process works a particular way. No live comparison of these models was run for this release. For future model updates, verify a dated official release, record its access status, and test actual drafts before adding a claimed model-specific pattern.
