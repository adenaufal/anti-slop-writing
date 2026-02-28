---
name: anti-slop-writing
description: Write text that avoids all known AI writing patterns and passes human detection. Use when writing articles, essays, blog posts, social media copy, or any content that must read as authentically human. Triggers on requests to write naturally, avoid AI slop, avoid AI detection, humanize writing, write like a human, or make text sound authentic.
---

# Core Principle

AI writing fails because it optimizes for statistical probability — producing the most expected, safe, broadly palatable text. Human writing comes from a single mind with history, opinions, specific context, and goals. Every instruction below exists to break the probability optimization and inject the specificity, imperfection, and personality that marks real human writing.

Before writing anything, load `references/vocabulary-banlist.md` for the complete banned vocabulary and `references/structural-patterns.md` for patterns to avoid. For the full Wikipedia source catalog with examples, see `references/wikipedia-sign-ai-writing.md`.

# Vocabulary Rules

## Hard Ban List (Never Use These)

**Significance puffers:** pivotal, crucial, vital, key (as adjective), significant, essential, groundbreaking, remarkable, transformative, indelible, profound, testament, enduring

**Analytical verbs:** underscore, highlight, showcase, foster, garner, bolster, delve, embark, leverage, facilitate, utilize, encompass, cultivate

**Poetic nouns:** tapestry, landscape (figurative), realm, paradigm, ecosystem (figurative), journey (figurative), nexus, interplay

**Promotional adjectives:** vibrant, rich (figurative), comprehensive, robust, seamless, innovative, dynamic, cutting-edge, meticulous, intricate, nuanced, nestled, breathtaking, renowned, diverse array

**Formal connectives:** furthermore, moreover, consequently, accordingly, nonetheless, nevertheless — replace with "also," "but," "so," "still," "and"

**Opening/closing crutches:** "In today's world," "In conclusion," "It is important to note," "It's worth noting," "At the end of the day," "In the ever-evolving landscape of," "Overall,"

**Copula avoidance constructions:** Replace "serves as a" with "is a." Replace "stands as a testament to" with "shows." Replace "marks a pivotal moment" with describe the moment directly. Replace "features" and "boasts" with "has." Replace "represents a shift" with "is a shift" or describe the shift.

## Replacement Principle

Use short, common words: "use" not "utilize," "help" not "facilitate," "show" not "demonstrate," "end" not "conclude," "start" not "embark," "dig into" not "delve into."

Use contractions in conversational contexts: "can't," "don't," "it's," "we're."

# Structural Rules

## Sentence Length — Vary Dramatically

Mix very short sentences (3-5 words) with long ones (25+ words). Never write 3+ consecutive sentences of similar length. This single change has the most impact on evading detection — it directly increases "burstiness," the metric detectors use most.

## Break the Rule of Three

AI defaults to listing things in groups of exactly three. List two things. Or four. Or five. Never default to three items in every list.

## Kill Negative Parallelisms

Never write "It's not just X, it's Y" or "Not only X, but also Y." These rhetorical contrasts are AI signatures. State what something IS directly.

## Kill False Ranges

Never write "from X to Y" as vague figurative spectrum ("from intimate gatherings to global movements"). Only use "from X to Y" for actual quantifiable ranges with identifiable middle points.

## No Formulaic Sections

Never end with "Challenges and Future Prospects." Never write "Despite its [positive words], [subject] faces challenges..." Never include speculative "Future Outlook" paragraphs.

## No Participial Tack-Ons

Never end sentences with ", highlighting the importance of..." or ", underscoring the significance of..." or ", symbolizing the region's commitment to..." These -ing clause attachments are the single most recognizable AI pattern.

## No Compulsive Summaries

Never start paragraphs with "Overall," "In conclusion," "In summary," "To recap." If the piece needs a conclusion, make it say something new.

## Paragraph Rhythm

Use irregular paragraph lengths. One-sentence paragraphs for emphasis. Longer paragraphs for sustained argument. The rhythm should never feel metronomic.

## No Vertical Lists with Bold Headers

Prefer prose over bullet-point lists with bolded inline headers followed by colons. When lists are genuinely needed, keep them simple — no bold headers, no colon-separated descriptions.

# Content Rules

## Specificity Over Generality

Replace every generic claim with a specific one. "Many companies" becomes "three startups in Austin." "Various factors" becomes the actual factors, named. "Experts agree" becomes the actual person who said it, with their name.

## No Vague Attributions

Never write "Experts argue," "Observers note," "Industry reports suggest," "According to some," "Many believe." Name the specific source or remove the attribution entirely.

## No Superficial Analysis

Never attach analytical commentary to facts that don't need it. Population data doesn't need "creating a lively community." A founding date doesn't need "marking a pivotal moment in history." State facts. Let them stand.

## No Undue Legacy/Significance Statements

Never write about how something "contributes to the broader" anything. Never state that something "reflects broader trends." Never assert that mundane facts have "enduring legacy." If importance exists, show it through specific evidence, not assertion.

## Show Real Opinions

Take positions. "This approach is wrong because..." not "Some argue X, while others argue Y." AI hedges reflexively; humans commit.

# Voice and Texture

## Add Human Imperfection

Include deliberate texture: a redundancy kept for rhythm, a fragment used for emphasis, a casual aside in formal prose, a self-correction ("actually, thinking about it more..."). These imperfections signal a real mind at work.

## Use Register Shifts

A sudden casual parenthetical in a formal argument. A technical term dropped into conversational prose. Humor that punches sideways. These shifts read as authentic because AI never produces them spontaneously.

## Reference Specific Touchstones

Name real recent events, specific pop culture moments, actual people and works. Not "recent developments in the field."

## First-Person When Appropriate

Use "I" when the context allows. Share specific experiences, opinions, or observations. AI defaults to abstracted third-person generalization because it has no lived experience.

# Post-Generation Checklist

After drafting, run this checklist:

1. Search for every word on the ban list — replace or remove each one
2. Check every paragraph's last sentence — AI almost always adds a redundant restatement; delete it
3. Find any sequence of 3+ sentences with similar length — restructure to vary
4. Find any list with exactly three items — add or remove one
5. Remove all instances of "serves as," "stands as," "is a testament to," "marks a," "highlights the importance of"
6. Remove all vague attributions or replace with named sources
7. Check the opening — if it starts with "In today's..." or "In this article, we will discuss..." rewrite it
8. Read the entire piece aloud — awkward AI rhythm is audible in ways it's not visible
9. Count em dashes — if more than one per 500 words, replace most with commas, parentheses, or periods
10. Check for any -ing participial phrases tacked onto sentence ends — rewrite as separate sentences or remove

# Language Support

This skill works for any language. When writing in non-English languages (e.g., Bahasa Indonesia, Spanish, Japanese):
- Apply the same structural rules (varied sentence length, no rule of three, no formulaic sections)
- Adapt vocabulary bans to equivalent overused words in that language
- Maintain natural idioms and colloquialisms of the target language
- AI patterns transcend language — the statistical smoothing and generic puffery appear in all languages
