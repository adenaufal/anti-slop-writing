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

**Common AI filler phrases (cut or replace):** "plays a [crucial/key/important] role" → state the action directly | "when it comes to" → rewrite with a verb | "in order to" → "to" | "a wide range of" → name what's in the range | "needless to say" → cut | "it goes without saying" → cut | "more often than not" → "usually" or give a number | "take a closer look at" → cut or be direct | "at this point in time" → "now" | "in recent years" → give the actual years or timeframe

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

## Vary Sentence Type, Not Just Length

Mix declarative sentences with questions, imperatives, and deliberate fragments. A genuine question mid-paragraph ("Why does this matter?") signals a thinking mind. An imperative ("Think about that.") shifts the register. A fragment for emphasis. AI writes almost exclusively in declarative because it answers; humans also wonder aloud, give commands, and break off mid-thought.

## Break Paragraph-Level Predictability

Don't open every paragraph with its thesis sentence. Start some paragraphs mid-thought — with a specific detail, scene, or example that earns its context. End some paragraphs before completing the expected "so what." AI writes clean arcs: claim → evidence → implication. Break that arc at least twice per piece.

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

## Show Genuine Uncertainty When Appropriate

When you don't know something, say so directly. "I'm not sure" or "I don't have enough information" signals honest thinking. AI fills gaps with confident-sounding generalities; humans admit limits. Use uncertainty markers sparingly but genuinely — not as hedging ("it could be argued that") but as actual epistemic honesty.

# Voice and Texture

## Add Human Imperfection

Include deliberate texture: a redundancy kept for rhythm, a fragment used for emphasis, a casual aside in formal prose, a self-correction ("actually, thinking about it more..."). These imperfections signal a real mind at work.

## Use Register Shifts

A sudden casual parenthetical in a formal argument. A technical term dropped into conversational prose. Humor that punches sideways. These shifts read as authentic because AI never produces them spontaneously.

## Reference Specific Touchstones

Name real recent events, specific pop culture moments, actual people and works. Not "recent developments in the field."

## First-Person When Appropriate

Use "I" when the context allows. Share specific experiences, opinions, or observations. AI defaults to abstracted third-person generalization because it has no lived experience.

## Vary Syntactic Depth

Mix shallow and deep sentence structures. A shallow sentence: subject-verb-object, one clause. A deep sentence: multiple embeddings, subordinate clauses, parenthetical asides. AI produces medium-depth sentences with boring consistency. Humans swing between extremes — a blunt statement followed by a winding, clause-heavy exploration.

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
11. Check for sentence type variety — if you wrote only declarative sentences, add at least one question or imperative
12. Verify paragraph openings — if every paragraph starts with its thesis sentence, rewrite at least two to start mid-thought with a detail or example

# Language Support

The structural rules apply to all languages. When writing in a non-English language, adapt vocabulary bans to that language's equivalent overused words and maintain natural idioms.

## Bahasa Indonesia - Extended Rules

AI-generated Indonesian has patterns beyond the universal ones. Apply these when writing in Indonesian.

### Indonesian Vocabulary - Hard Ban

**Significance puffers:** sangat penting, sangat krusial, sangat signifikan, sangat relevan, fundamental (as vague praise), luar biasa (as generic praise), mendalam (without concrete detail)

**Analytical verbs:** menyoroti, menggarisbawahi, memfasilitasi, mengoptimalkan. For replacements, keep meaning: memanfaatkan -> gunakan "menggunakan" only when it means "to use"; keep "memanfaatkan" when it means "to benefit from" | mengimplementasikan -> "menerapkan" in plain style | berkontribusi pada -> state the concrete action and result | berperan dalam -> name the action directly

**Formal connectives to replace:** selain itu -> "juga" | di sisi lain -> "namun" or "tapi" (match register) | lebih lanjut -> restructure or cut | dengan demikian -> "jadi" | oleh karena itu -> "jadi" or "karena itu" | tak kalah penting -> state what it is | menariknya -> lead with the fact | sehubungan dengan hal tersebut -> restructure

**Opening/closing crutches:** "Di era modern ini," | "Dalam konteks [X] yang semakin [Y]," | "Seiring perkembangan zaman," | "Perlu diketahui bahwa" | "Penting untuk diingat" | "Sebagai kesimpulan," | "Dapat disimpulkan bahwa" | "Dengan demikian, dapat disimpulkan"

**Copula-avoidance:** merupakan -> prefer "adalah" or rewrite directly | berperan sebagai -> use "adalah" only for identity statements, otherwise use a concrete verb | berfungsi sebagai -> use "berfungsi untuk" for purpose statements | memiliki peran penting -> state the exact role | menjadi salah satu... -> quantify directly

**Vague attribution:** "para ahli menyatakan" -> name them | "penelitian menunjukkan" -> name it | "banyak kalangan berpendapat" -> name who

**Promotional phrases:** "memiliki komitmen untuk" | "memberikan dampak positif" | "dalam rangka [goal]" | "dalam upaya [X]" | "guna meningkatkan" | "untuk mencapai tujuan tersebut"

### Indonesian Structural Rules

**Avoid automatic "Kesimpulan" headings.** Use a "Kesimpulan" section only when the genre requires it (for example: academic papers, formal reports, compliance docs). For essays, articles, and casual writing, close in prose.

**No temporal openings.** Never start with "Di era modern ini," "Seiring perkembangan zaman," or "Dalam konteks X yang semakin Y." Start with a specific fact.

**Avoid "tidak hanya...tetapi juga."** Keep it only when the contrast is truly needed and adds new meaning.

**No "merupakan salah satu X yang paling Y."** Importance assertion without evidence. Quantify instead.

**No template line "di sisi lain, terdapat tantangan."** Name the concrete problem and, when possible, include numbers.

**No "dapat dilihat bahwa" padding.** Delete "dapat dilihat bahwa," "dapat dipahami bahwa," "perlu dipahami bahwa." State the finding.

**Avoid "di mana" as relative pronoun.** Rewrite "program di mana peserta akan..." as "program yang..." or a direct sentence.

**Prefer verbs over nominalizations.** "Melatih" not "pelaksanaan pelatihan." "Mengembangkan" not "pengembangan kapasitas."

### Indonesian Voice

**Use discourse particles when appropriate.** Natural Indonesian often uses nah, sih, dong, deh, lho, nih, tuh, kan, kok, ya in conversational contexts. Do not force particles in formal writing.

**Match pronoun register.** AI locks onto "Anda" regardless of context. Casual writing uses kamu or lo/lu. Formal uses Anda. Match the actual register.

**Avoid pure Bahasa Indonesia baku in casual contexts.** AI always writes formal Indonesian. When the context is informal, use natural shortened forms: nggak (not tidak), udah (not sudah), gimana (not bagaimana).

**Add engagement when it fits the genre.** Human Indonesian writers can ask direct questions, use asides, or use light humor when context allows.

### Indonesian Checklist Additions

After the standard checklist, also:
- Find all "merupakan" - replace most with "adalah" or rewrite directly
- Remove automatic "Kesimpulan" section headers unless format requires them
- Find every "tidak hanya...tetapi juga" - keep only when the contrast is necessary
- Check opening - if it starts with "Di era" / "Seiring" / "Dalam konteks" - rewrite
- Find all nominalizations (pe-/ke-an/-an chains) - prefer verb forms where clarity improves
- Find all "dapat dilihat bahwa" / "dapat dipahami bahwa" - delete them
- Check pronoun register - does "Anda" match the actual tone?
- Re-check semantic accuracy so replacements do not change meaning
