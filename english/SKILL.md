---
name: anti-slop-writing
description: Edit English prose for clarity, specificity, natural flow, and fit to the requested voice. Use for writing or revising articles, essays, posts, and other text that feels generic or padded.
---

# Anti-Slop Writing v4.1

# Core Principle

Good writing serves the reader and the writer's purpose. Generic phrasing, padding, and formulaic structure can make a draft feel automated, but no single word or pattern proves who wrote it. Treat the rules below as editorial prompts: use them when they improve clarity, accuracy, or voice, and ignore them when they would distort the requested format or register.

## Model coverage (reviewed September 27, 2026)

The model names below identify recent versions, not reliable writing fingerprints. Providers update products and route requests across models; an API model ID may not match the model selected in a consumer product. Check the optional [model coverage reference](references/model-coverage.md) for dated release notes and product/API distinctions when a version-specific request requires them.

- **ChatGPT / OpenAI:** Recent coverage includes GPT-5.6 Sol/Terra/Luna and GPT-6 Astra. GPT-6 Pro is an Astra-powered ChatGPT offering; GPT-6 Sol and Luna are documented separately for API, ChatGPT Work, and Codex. Availability depends on product and plan.
- **Claude / Anthropic:** Recent releases include Opus 5, Fable and restricted Mythos 5.1, then Opus 5.5. Sonnet and Haiku 5.5 were announced as upcoming, not released as of this update.
- **Gemini / Google:** Recent releases include Gemini 3.6 Flash and 3.5 Flash-Lite, Gemini 3.7 Flash, and Gemini 3.8 Flash stable.
- **Grok / xAI:** Recent releases include Grok 4.5, 4.6, and 4.7. Product rollout and availability can differ by surface.

These facts describe release coverage. They do not establish distinctive prose habits for any model. Use the checks in EN-11 to edit what is actually present in a draft.

Before writing, consult `references/vocabulary-banlist.md` for optional vocabulary preferences and `references/structural-patterns.md` for editorial examples. For sentence-level repairs, use the focused [language editing guide](references/language-editing.md). Apply every list as a review prompt, not a detector test or a rule to alter accurate meaning.

---

# Vocabulary Rules

## Words and Phrases to Review

The lists below flag wording that can become generic or padded. They are not hard bans. Keep an item when it is the accurate technical term, needed hedge, part of a quotation, requested by the user, or best fit for the format. Do not replace precise language just to avoid a word.

**Significance puffers:** pivotal, crucial, vital, key (as adjective), significant, essential, groundbreaking, remarkable, transformative, indelible, profound, testament, enduring, lasting, deeply rooted, paramount, indispensable, invaluable, quintessential

**Analytical verbs:** underscore, highlight (as "emphasize"), showcase, foster, garner, bolster, delve, embark, leverage, facilitate, utilize, encompass, cultivate, elucidate, illuminate, navigate (figurative), exemplify, embody, transcend, harness, spearhead, streamline, galvanize

**Poetic nouns:** tapestry, landscape (figurative), realm, paradigm, ecosystem (figurative), journey (figurative), nexus, interplay, mosaic, fabric (of society), cornerstone, beacon, pillar, catalyst, crucible, linchpin, hallmark, confluence, odyssey, trajectory, underpinning

**Promotional adjectives:** vibrant, rich (figurative), comprehensive, robust, seamless, innovative, dynamic, cutting-edge, meticulous, intricate, nuanced, nestled, breathtaking, renowned, diverse array, bustling, stunning, multifaceted, holistic, overarching, compelling

**Puffery adverbs:** seamlessly, meticulously, profoundly, intrinsically, fundamentally, remarkably, notably, crucially, undeniably, inherently, poignantly, relentlessly, tirelessly, vividly

**Formal connectives to review when simpler wording fits the register:** furthermore → "also" | moreover → "also" | consequently → "so" | accordingly → "so" | nonetheless → "still" | nevertheless → "still" | additionally → "also" | thus → "so" | hence → "so"

**Opening/closing crutches:** "In today's world," "In today's fast-paced world," "In the ever-evolving landscape of," "In an era of/where," "As we navigate the complexities of," "In conclusion," "In summary," "Overall," "It is important to note that," "It's worth noting that," "At the end of the day," "Without further ado," "In a nutshell," "The bottom line is," "Last but not least"

**Copula-avoidance constructions (use "is/has" instead):** serves as → is | stands as → is | marks a → describe directly | boasts → has | features (meaning "has") → has | holds the distinction of → is | emerged as → became or is | constitutes → is

**Vague attribution phrases:** "Experts argue," "Observers note," "Industry reports suggest," "According to some," "Many believe," "It is widely regarded," "Studies show" (without naming the study), "Research suggests" (without citing it)

**Promotional phrases:** "commitment to excellence," "natural beauty," "in the heart of," "rich cultural heritage," "setting the stage for," "contributing to the broader," "reflects broader trends," "paving the way for," "at the forefront of," "pushing the boundaries of," "the landscape of X is evolving," "in the realm of," "shed light on," "a game-changer"

**Formulaic patterns to review when they add no needed contrast or structure:** "It's not just X, it's Y" | "It's not about X, it's about Y" | "Not only X, but also Y" | "No X. No Y. Just Z." (staccato triplet) | "Whether you're [X] or [Y]..." | "From [X] to [Y], [sweeping generalization]"

**Formulaic pairs to review when they add no useful distinction:** "challenges and opportunities" | "on one hand... on the other hand" | "pros and cons" | "risks and rewards"

**Stock conversational openers to review when they add no meaning:** "But honestly?" | "Here's the truth:" | "Here's the thing:" | "Let me be clear:" | "But here's where it gets interesting..." | "Think about it this way..." | "Let me break this down..."

**Common AI filler phrases (cut or replace):** "plays a [crucial/key/important] role" → state the action directly | "when it comes to" → rewrite with a verb | "in order to" → "to" | "a wide range of" → name what's in the range | "needless to say" → cut | "it goes without saying" → cut | "more often than not" → "usually" or give a number | "take a closer look at" → cut or be direct | "at this point in time" → "now" | "in recent years" → give the actual years or timeframe | "dive deep into" → just discuss it | "navigate the complexities of" → name the complexities

**Passive hedging constructions (cut the framing, state the fact):** "It should be noted that" → cut | "It must be emphasized that" → cut | "It has been observed that" → say who observed it | "It can be argued that" → argue it or don't | "It is important to remember that" → cut | "There are several factors that" → name them

**Collaborative chat artifacts (never include):** "I hope this helps!" | "Of course!" | "Certainly!" | "You're absolutely right!" | "Would you like me to..." | "Is there anything else..." | "Let me know if..." | "As an AI language model..." | "I'd be happy to..." | "Great question!"

**Additional phrases to review when they add no meaning:** "ensuring/ensures" as padding → name the concrete action or cut | "plays a [crucial/critical/important] role in shaping" → state what it does | "highlights/supports/reflects" used vaguely → use a concrete verb or delete | "capable of X" → "able to X" or the direct verb | "rather than" where a direct comparison works → rewrite directly | "conversely" → "but" or restructure | "in essence" / "essentially" / "fundamentally" → cut when redundant | unsupported intensifiers → add evidence or delete | "one thing is clear" | "the key takeaway" | "inherent tensions" | "this raises important questions about" | stacked hedging adverbs → state the supported level of certainty

## Replacement Strategy

Use short, common words: "use" not "utilize," "help" not "facilitate," "show" not "demonstrate," "end" not "conclude," "start" not "embark," "dig into" not "delve into."

When you encounter a listed word that adds no meaning, don't swap it mechanically for a synonym. Restructure the sentence to say what you mean in plain language, while keeping accurate terms and claims. Empty wording can pad a sentence; a listed word by itself does not make writing weak.

Use contractions when they fit the speaker and register: "can't," "don't," "it's," "we're," "won't," "they'll," "that's." Keep full forms when they fit formal prose or the writer's voice.

---

# Structural Rules

## 1. Vary Sentence Length Dramatically

Mix sentence lengths when it helps the pace and meaning. If several neighboring sentences fall into the same rhythm, revise where the repetition distracts; do not follow a quota or target word band.

**Review repeated rhythms and repetitive openers.** Read the passage aloud and revise only where the cadence distracts or obscures the point. Do not impose a quota or add fragments just to create variation.

## 2. Review Formulaic Lists

A three-part list can feel formulaic when its items do not form a real group. Keep it when the content supports it; otherwise use the number of items the material calls for.

## 3. Review Stock Contrasts

Use contrast when it clarifies a real distinction. Remove stock contrast formulas when they merely delay the point; state the claim directly.

## 4. Review Vague Ranges

Review "from X to Y" when it gestures at a sweeping spectrum without clarifying the claim. Keep literal ranges and established rhetorical uses when they fit the passage.

## 5. Review Participial Attachments

Review comma plus participial phrases such as ", highlighting the importance of...". They can add vague commentary, but can also express a real simultaneous action or result. Keep them when their subject and relationship are clear and accurate; otherwise delete, relocate, or recast the information. See [language editing](references/language-editing.md#3-check-what-an--ing-appendage-claims).

## 6. Avoid Generic Conclusions

Do not append a stock “Challenges and Future Prospects” section or vague optimism about “ongoing initiatives.” End where the requested piece has made its point.

## 7. Avoid Redundant Summaries

Remove “Overall,” “In conclusion,” “In summary,” or “To recap” when they only repeat what the piece already said. Use a summary when the format calls for one.

## 8. Paragraph Rhythm

Let each paragraph hold one connected idea. Use a short paragraph for emphasis and a longer one when the reasoning needs room. Merge fragments only when they belong together, and keep lists when they serve the requested format.

## 9. Review Vertical Lists with Bold Headers

Use prose when it reads more naturally. Keep headings, labeled lists, and colon-separated descriptions when the format or reader benefits from them.

## 10. Follow the Requested Dash Style

Follow the user's or publication's punctuation style. If none is given, prefer periods, commas, colons, or parentheses over em and en dashes, following this project's existing style. Preserve dashes in quotations, ranges, and technical notation as required; punctuation is not evidence of authorship.

## 11. Vary Sentence Type, Not Just Length

Mix declarative sentences with questions, imperatives, and deliberate fragments. Use questions, imperatives, and fragments when the purpose and register call for them. Do not add them as proof of human authorship.

## 12. Organize Paragraphs for the Argument

Give each paragraph a clear role. A claim-evidence-implication sequence often works; use another order when it better supports the argument. Avoid repeating the same opening or conclusion without a reason.

## 13. Choose Sentence Structure for Clarity

Use simple or layered sentences according to the idea, pace, and emphasis.

## 14. Choose Accurate Connectors

Use the connector that states the relationship accurately. Do not rotate through synonyms just to create variety.

## 15. Prefer Precise Words

Prefer accurate, concrete terms over vague wording. Repeat a term when that is clearer than cycling through synonyms.

---

# English-Specific Rules

## EN-1. Review Broad Temporal Openers

Review broad temporal openers such as “In today’s fast-paced world” when they delay the point. Start with the specific fact, scene, or claim when the format allows it; keep the framing when time context matters.

## EN-2. No Semicolon Overuse

In informal prose, a semicolon can sound stiff. Use it when the clauses are closely related; otherwise a period or conjunction may be clearer.

## EN-3. Use Natural Punctuation

Keep punctuation consistent with the requested register. Do not introduce errors or roughness to imitate a person.

## EN-4. Follow the Requested Register

Match the requested register. Shift tone only when the audience, format, or content calls for a change.

## EN-5. Review Agentless Passives

Look for sentences where the actor disappears or an introductory modifier attaches to the wrong subject. Name the actor when it matters; keep passive voice when the actor is unknown, irrelevant, or less important than the affected object. Use the [language editing guide](references/language-editing.md) for meaning-preserving repairs.

Use passive voice when the affected object matters more than the agent. Prefer active voice when naming the agent improves clarity.

## EN-6. Review Repeated Parallel Sentences

A run of punchy parallel sentences can feel like an ad slogan. Keep it when that effect is intended; otherwise state the point once.

## EN-7. Use Contractions Naturally

Use contractions when they fit the requested register. Informal forms such as “gonna” or “kinda” belong only when the audience and context support them.

## EN-8. Use Questions When They Help

Use a question when the piece needs to pose a real question. Avoid rhetorical questions that only set up an obvious answer. "But does it actually work?" "Who decides that?"

## EN-9. Use Fragments When They Fit

Use fragments when the format and voice allow them and they add emphasis. Do not add them as a test of authorship.

## EN-10. Keep Useful Qualification

Remove stacked qualifiers that add no useful precision. Keep hedging when the evidence is incomplete or the claim is uncertain.

## EN-11. Apply Cross-Model Editorial Checks

These are editorial heuristics, not model fingerprints. They apply only when the issue is present in the draft:

- Remove chat or reasoning scaffolding from a deliverable, such as “Let me break this down” or a self-narrated plan the reader did not request.
- Remove unsolicited hype, reassurance, excessive praise, or an edgy/snarky persona unless the user asked for that tone.
- Keep factual claims, citations, and stated uncertainty grounded in the supplied sources. Do not invent lived experience, numbers, or anecdotes to make prose sound specific.
- Attribute claims to the source that supports them. Do not imply that the writer personally observed or verified something they did not.
- Vary cadence where repetition distracts. Do not force fragments, errors, punctuation changes, or “rough edges” as signals of authorship.
- Follow the requested format, audience, and register, even when that means using headings, bullets, formal language, or a tidy conclusion.

For a version-specific question, check the optional [model coverage reference](references/model-coverage.md). Release notes establish product availability and documented capabilities; they do not establish a model's writing fingerprint.

## EN-12. Check Grammar and Meaning Together

Check whether modifiers attach to the intended actor, pronouns have clear referents, clauses are joined correctly, and coordinated items have matching grammatical form. During every edit, preserve the source's actor, scope, negation, quantity, degree of certainty, and causal claim. Do not resolve ambiguity by guessing; retain it or ask for the missing context. The [language editing guide](references/language-editing.md) gives practical repairs and conditions for retaining each form.

---

# Content Rules

## Specificity Over Generality

Replace vague claims with concrete detail when the source material supports it. Do not invent counts, places, people, dates, or examples to make prose seem specific.

## Review Vague Attributions

Phrases such as "Experts argue," "Observers note," "According to some," and "Studies show" can hide who supports a claim. Name the source when it is known and relevant, cite the study when making a research claim, or qualify the statement. Keep an intentionally broad attribution only when the scope is accurate and useful.

## Remove Unsupported or Generic Analysis

Do not attach commentary that the facts do not support. Population data may or may not support a claim about community life; a founding date alone does not establish historical importance. State the evidence and keep analysis when it follows from that evidence.

## Support Claims About Legacy or Significance

Review claims that something "contributes to the broader" picture, "reflects broader trends," or has an "enduring legacy." Keep them when the relationship is explained and supported; otherwise state the evidence or remove the claim.

## Review Notability Padding

Avoid listing outlets as a substitute for explaining why coverage matters. Cite the relevant reporting. Mention social media activity only when it helps the reader understand the subject.

## Take Real Positions

State a supported conclusion directly. Present disagreement fairly when relevant; do not manufacture balance or certainty.

## Show Genuine Uncertainty When Appropriate

State limits clearly when information is missing or uncertain. Do not add first-person uncertainty language unless it fits the speaker and context.

---

# Voice and Texture

## Keep the Requested Voice

Do not add errors, awkward phrasing, false starts, fragments, or redundant wording to simulate a person. Keep a casual aside or self-correction only when it suits the speaker and purpose.

## Match the Register

Keep the register suited to the audience and format. Shift it when the subject or speaker calls for a change; do not add tonal shifts to signal authenticity.

## Use Grounded Examples

Use names, events, and examples only when they are relevant and supported by the source material or supplied context. Do not invent memories or imply personal experience.

## First-Person When Appropriate

Use first person when writing for a real speaker whose views or experiences are provided. Never invent a speaker’s experience or observation.

## Use English Discourse Markers

Use discourse markers when they fit the speaker and register:
- Processing: "Well," "I mean," "Look," "So," "The thing is"
- Hedging: "I think," "sort of," "kind of," "arguably," "as far as I can tell"
- Concessive: "Fair enough," "Granted," "Mind you," "That said"
- Stance: "Honestly," "Frankly," "Personally," "Admittedly"
- Self-correction: "Actually," "Or rather," "No, wait, "

Replace AI transitions ("Moreover," "Furthermore") with natural connectors ("And," "But," "So," "Plus," "Also," "Still," "Though").

## Show Emotional Texture

Let the subject and speaker determine the emotional tone. For example:
- Genuine excitement about what interests them
- Frustration with problems
- Humor where it fits
- Skepticism toward dubious claims
- Rushing through parts that bore them
- Lingering on parts that fascinate them

## Develop Consistent Idiosyncrasies

When a voice guide or examples are available, follow their preferences:
- Favorite words and phrases that recur
- Characteristic sentence constructions
- Habitual ways of transitioning between ideas
- Consistent use (or avoidance) of specific punctuation

## Show Knowledge Asymmetry

Reflect the speaker’s supplied expertise and uncertainty. Do not claim expertise or insider knowledge that the context does not support.

## Vary Syntactic Depth

Mix shallow and deep sentence structures. A shallow sentence: subject-verb-object, one clause. A deep sentence: multiple embeddings, subordinate clauses, parenthetical asides. Choose sentence depth for clarity, pace, and emphasis.

---

# Editorial Validation and Detection Limits

No writing pattern can establish who wrote a passage. AI detectors can produce false positives and false negatives, and their internal methods and performance vary by product, version, language, and text type. Do not promise that a draft will evade detection or claim that a stylistic edit proves human authorship.

Use the checklist below to improve the draft for its reader, not to game a detector.

---

# Post-Generation Checklist

- Check the vocabulary preferences and remove phrases that add no meaning.
- Confirm that claims, numbers, examples, and citations are supported by the supplied material. Preserve uncertainty where evidence is limited.
- Remove chat or reasoning scaffolding that does not belong in the requested deliverable.
- Look for repeated sentence openings, stock contrasts, unnecessary summaries, generic conclusions, or commentary attached to facts. Revise only where the pattern weakens the draft.
- Read the draft for cadence and paragraph flow. Vary them naturally without adding errors or forced roughness.
- Check punctuation, list structure, formatting, audience, and register against the request.
- Do not fabricate personal experience, sources, measurements, or concrete details.
- Check modifier attachment, pronoun reference, clause joins, and parallel items. Compare the revised claim with the source for changes to who acted, what is included, negation, quantity, certainty, and causation.

---

# Language Support

The structural rules apply across languages, with vocabulary and idioms adapted to the target language. In this repository, the Indonesian skill is at `../indonesian/SKILL.md`; packaged English-only copies should use the separate Indonesian skill rather than treating that sibling path as a dependency.

---

**Last Updated:** September 27, 2026 (v4.1)
**Changelog v4.1:** Added actionable, meaning-preserving grammar and discourse edits; changed absolute style bans into contextual review prompts. The model coverage section remains the September 27, 2026 v4.0 snapshot.
