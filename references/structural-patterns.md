# Structural Patterns to Avoid

Every pattern here has been documented on Wikipedia's "Signs of AI Writing" page and confirmed by academic research (Kobak et al. 2024, Russell et al. 2025, Fraser et al. 2025). These are the structural tells that make text read as machine-generated.

## 1. Participial -ing Tack-Ons

The single most recognizable AI pattern. A comma followed by an -ing phrase appended to the end of a sentence to appear analytical.

**AI pattern:**
> The team launched the product, revolutionizing the industry.
> The temple was built in 1850, symbolizing the community's enduring faith.
> As of 2008, the population stood at 56,998, creating a lively community.

**Human alternative:**
> The team launched the product. The industry changed.
> The temple was built in 1850.
> As of 2008, the population was 56,998.

Rule: If the -ing clause adds no concrete information, delete it entirely. If it adds real information, make it a separate sentence.

## 2. The Rule of Three

AI defaults to grouping things in threes — three adjectives, three bullet points, three examples, three clauses.

**AI pattern:**
> The conference features keynote sessions, panel discussions, and networking opportunities.
> The design is bold, innovative, and timeless.

**Human alternative:**
> The conference runs keynote sessions and panels. There's time to meet people between talks.
> The design is bold. It'll still work in ten years.

Rule: List two things. Or four. Or one. Never three by default.

## 3. Negative Parallelisms

"Not just X, but also Y" / "It's not X, it's Y" / "Not only X, but Y"

**AI pattern:**
> This is not just a memoir — it's a love letter to the city.
> The painting represents not merely an artistic achievement, but a cultural milestone.

**Human alternative:**
> It's a memoir about growing up in the city. You can feel the author's affection for it on every page.
> The painting became a cultural reference point. People still argue about it.

Rule: State what something IS. Don't frame it as a correction of what someone might wrongly think.

## 4. False Ranges ("From X to Y")

Vague figurative spectrum using "from X to Y" where no real scale exists.

**AI pattern:**
> From intimate gatherings to global movements, the organization has made its mark.
> From beginners to experts, everyone can benefit.
> From the singularity of the Big Bang to the grand cosmic web...

**Human alternative:**
> The organization started with twelve people in a living room. Last year 40,000 showed up to their conference.
> Works whether you've been doing this for a week or a decade.

Rule: Only use "from X to Y" when there's a real, identifiable midpoint on a real scale.

## 5. "Despite Its... Faces Challenges" Formula

The formulaic challenges-and-future-prospects ending.

**AI pattern:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including... With its strategic location and ongoing initiatives, Korattur continues to thrive.

**Human alternative:**
> Korattur's water supply can't keep up with the population. The pipes are from the 1970s.

Rule: If you mention problems, name specific ones with specific evidence. Never follow with vague optimism about "ongoing initiatives."

## 6. Copula Avoidance ("Serves As" / "Stands As")

AI substitutes elaborate verb phrases for simple "is/are/has."

**AI pattern:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art.
> The gallery features four separate spaces.
> She holds the distinction of being the first female director.

**Human alternative:**
> Gallery 825 is LAAA's exhibition space.
> The gallery has four separate spaces.
> She was the first female director.

Rule: Use "is," "are," "has," "was." Simple copulas are not boring — they're clear.

## 7. Superficial Analysis Padding

Generic commentary attached to facts that need no commentary.

**AI pattern:**
> The city has a population of 56,998, creating a lively community within its borders.
> The inscriptions offer valuable insights into the construction of the mosque.
> These citations illustrate the enduring relevance of his work.

**Human alternative:**
> The city has a population of 56,998.
> The inscriptions name the craftsmen who built the mosque.
> His work keeps getting cited.

Rule: If the analytical statement could apply to literally any subject, it adds nothing. Delete it.

## 8. Elegant Variation (Synonym Cycling)

AI avoids repeating the same word by cycling through synonyms, even when repetition would be clearer.

**AI pattern:**
> Soviet artistic constraints... non-conformist artists... their creativity... the confines of state-imposed artistic norms... the artistic aspirations...

**Human alternative:**
> The Soviet government told artists what they could and couldn't paint. Yankilevsky painted what he wanted anyway.

Rule: Repeat words when clarity demands it. Don't cycle through "constraints / confines / norms / limitations" to avoid saying the same word twice.

## 9. Em Dash Overuse

AI uses em dashes (—) where humans use commas, parentheses, periods, or nothing.

**AI pattern:**
> The article complies with policies — including WP:V, WP:RS, and WP:BLP — with all claims supported by multiple sources.

**Human alternative:**
> The article complies with WP:V, WP:RS, and WP:BLP. All claims have sources.

Rule: Maximum one em dash per 500 words. When in doubt, use a period and start a new sentence.

## 10. Vertical Lists with Bold Inline Headers

Formatting everything as bullet points with **Bold Header:** description.

**AI pattern:**
> - **SEO:** Traditional methods for improving visibility...
> - **AEO:** Techniques focused on optimizing content...
> - **GIO:** Strategies for ensuring businesses are cited...

**Human alternative:**
Write it as prose. If a list is genuinely needed, keep it simple without bold headers and colon separators.

## 11. Undue Emphasis on Notability/Media Coverage

Painstakingly listing every source that covered the topic to prove it matters.

**AI pattern:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu.
> The mall maintains a strong digital presence, particularly on Instagram.

**Human alternative:**
> She wrote a piece for the Times about it. [cite the actual piece]

Rule: Cite sources inline as references. Don't make the existence of coverage into content.

## 12. Overuse of Boldface

Mechanically bolding every key term, proper noun, or concept.

**AI pattern:**
> A **leveraged buyout (LBO)** uses **debt financing** to let **private equity firms** control businesses using the company's **assets and future cash flows** as collateral.

**Human alternative:**
> A leveraged buyout uses debt to buy a company. The company's own assets and cash flow back the loans.

Rule: Bold sparingly. In most prose, bold nothing at all.

## Detection Metrics (Why This Matters)

AI detectors measure two primary things:

1. **Perplexity** — how predictable word choices are. AI produces low-perplexity text (smooth, unsurprising). Human text has higher perplexity (unexpected metaphors, unusual phrasing, creative choices).

2. **Burstiness** — variation in sentence length and structure. AI has low burstiness (sentences cluster around 10-20 words with consistent structure). Human text has high burstiness (3-word sentences mixed with 30-word sentences).

Every structural rule above increases perplexity and burstiness — making text statistically indistinguishable from human writing.
