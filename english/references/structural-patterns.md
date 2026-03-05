# Structural Patterns to Avoid (English)

Every pattern here has been documented on Wikipedia's "Signs of AI Writing" page and confirmed by academic research (Kobak et al. 2025 in Science Advances, Russell et al. 2025, Fraser et al. 2025, Paech et al. ICLR 2026, Jiang & Hyland 2025 in Written Communication, Shaib et al. 2025). These are the structural tells that make text read as machine-generated.

Turnitin (2025-2026) analyzes "rhythm, flow, and predictability across entire paragraphs" using 31 linguistic features — not just individual words. GPTZero uses perplexity + burstiness + semantic fingerprinting. Detection has shifted from vocabulary to structure.

---

## Universal Patterns (All LLMs, All Languages)

### U-1. Participial -ing Tack-Ons

The single most recognizable AI pattern. A comma followed by an -ing phrase appended to sentence ends to appear analytical.

**AI pattern:**
> The team launched the product, revolutionizing the industry.
> The temple was built in 1850, symbolizing the community's enduring faith.
> As of 2008, the population stood at 56,998, creating a lively community.

**Human alternative:**
> The team launched the product. The industry changed.
> The temple was built in 1850.
> As of 2008, the population was 56,998.

Rule: If the -ing clause adds no concrete information, delete it entirely. If it adds real information, make it a separate sentence.

### U-2. The Rule of Three

AI defaults to grouping things in threes — three adjectives, three bullet points, three examples, three clauses. This is the "tricolon" compulsion. Real humans list 2, 4, 5, or 7 items erratically.

**AI pattern:**
> The conference features keynote sessions, panel discussions, and networking opportunities.
> The design is bold, innovative, and timeless.
> Time, resources, and attention.

**Human alternative:**
> The conference runs keynote sessions and panels. There's time to meet people between talks.
> The design is bold. It'll still work in ten years.
> Time and money.

Rule: List two things. Or four. Or one. Never three by default.

### U-3. Negative Parallelisms

"Not just X, but also Y" / "It's not X, it's Y" / "Not only X, but Y" / "It's not about X, it's about Y"

SearchEngineLand's 2026 study of 1,000+ URLs found "not only/but also" constructions showed the **largest negative correlation with engagement.** One blog post used it 12 separate times.

**AI pattern:**
> This is not just a memoir — it's a love letter to the city.
> The painting represents not merely an artistic achievement, but a cultural milestone.
> It's not about the technology, it's about the people.

**Human alternative:**
> It's a memoir about growing up in the city. You can feel the author's affection for it on every page.
> The painting became a cultural reference point. People still argue about it.
> The technology doesn't matter if nobody uses it.

Rule: State what something IS. Don't frame it as a correction of what someone might wrongly think.

### U-4. False Ranges ("From X to Y")

Vague figurative spectrum using "from X to Y" where no real scale exists.

**AI pattern:**
> From intimate gatherings to global movements, the organization has made its mark.
> From beginners to experts, everyone can benefit.
> Whether you're a student or a CEO, this applies to you.

**Human alternative:**
> The organization started with twelve people in a living room. Last year 40,000 showed up to their conference.
> Works whether you've been doing this for a week or a decade.

Rule: Only use "from X to Y" when there's a real, identifiable midpoint on a real scale.

### U-5. "Despite Its... Faces Challenges" Formula

The formulaic challenges-and-future-prospects ending.

**AI pattern:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including... With its strategic location and ongoing initiatives, Korattur continues to thrive.

**Human alternative:**
> Korattur's water supply can't keep up with the population. The pipes are from the 1970s.

Rule: If you mention problems, name specific ones with specific evidence. Never follow with vague optimism about "ongoing initiatives."

### U-6. Copula Avoidance ("Serves As" / "Stands As")

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

### U-7. Superficial Analysis Padding

Generic commentary attached to facts that need no commentary. If the analytical statement could apply to literally any subject, it adds nothing.

**AI pattern:**
> The city has a population of 56,998, creating a lively community within its borders.
> The inscriptions offer valuable insights into the construction of the mosque.
> These citations illustrate the enduring relevance of his work.

**Human alternative:**
> The city has a population of 56,998.
> The inscriptions name the craftsmen who built the mosque.
> His work keeps getting cited.

Rule: If the analytical statement could apply to literally any subject, it adds nothing. Delete it.

### U-8. Elegant Variation (Synonym Cycling)

AI avoids repeating the same word by cycling through synonyms, even when repetition would be clearer. One text might use: protagonist → main character → central figure → hero → lead.

**AI pattern:**
> Soviet artistic constraints... non-conformist artists... their creativity... the confines of state-imposed artistic norms... the artistic aspirations...

**Human alternative:**
> The Soviet government told artists what they could and couldn't paint. Yankilevsky painted what he wanted anyway.

Rule: Repeat words when clarity demands it. Don't cycle through "constraints / confines / norms / limitations" to avoid saying the same word twice.

### U-9. Em Dash Overuse

AI uses em dashes (—) where humans use commas, parentheses, periods, or nothing. The em dash has been called "the ChatGPT dash" — AI training data skews toward 19th/20th century prose that used ~30% more em dashes than contemporary writing.

**AI pattern:**
> The article complies with policies — including WP:V, WP:RS, and WP:BLP — with all claims supported by multiple sources.

**Human alternative:**
> The article complies with WP:V, WP:RS, and WP:BLP. All claims have sources.

Rule: Maximum one em dash per 500 words. When in doubt, use a period and start a new sentence.

### U-10. Vertical Lists with Bold Inline Headers

Formatting everything as bullet points with **Bold Header:** description.

**AI pattern:**
> - **SEO:** Traditional methods for improving visibility...
> - **AEO:** Techniques focused on optimizing content...
> - **GIO:** Strategies for ensuring businesses are cited...

**Human alternative:**
Write it as prose. If a list is genuinely needed, keep it simple without bold headers and colon separators.

### U-11. Undue Emphasis on Notability/Media Coverage

Painstakingly listing every source that covered the topic to prove it matters.

**AI pattern:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu.
> The mall maintains a strong digital presence, particularly on Instagram.

**Human alternative:**
> She wrote a piece for the Times about it. [cite the actual piece]

Rule: Cite sources inline as references. Don't make the existence of coverage into content.

### U-12. Overuse of Boldface

Mechanically bolding every key term, proper noun, or concept.

**AI pattern:**
> A **leveraged buyout (LBO)** uses **debt financing** to let **private equity firms** control businesses using the company's **assets and future cash flows** as collateral.

**Human alternative:**
> A leveraged buyout uses debt to buy a company. The company's own assets and cash flow back the loans.

Rule: Bold sparingly. In most prose, bold nothing at all.

### U-13. Uniform Syntactic Depth

AI produces sentences of remarkably consistent medium complexity — never very simple, never deeply nested. Humans swing between extremes.

**AI pattern (all sentences medium depth):**
> The government has allocated funds for a training program. The program is designed to improve the skills of local workers. Participants will receive certificates after completing all training modules.

**Human alternative (depth varies wildly):**
> Budget: $2 million. From that, 200 people get trained over three months — mostly single mothers who'd never touched a computer before, most of them from villages at the foot of Mount Rainier where broadband only arrived two years ago. Result? 147 got jobs.

Rule: Mix very shallow sentences (subject-verb-object) with very deep ones (multiple subordinate clauses, parenthetical asides, embedded thoughts). AI sticks to the middle.

### U-14. Formulaic Transition Repetition

AI uses the same transitions repeatedly: "Additionally," "Furthermore," "Moreover," "However," "In addition." Real writing uses implicit transitions, questions, fragments, and sudden topic shifts.

**Human alternatives to formulaic transitions:**
- Implicit transition (no connector — let the idea sequence guide the reader)
- Question as transition ("So what does that mean in practice?")
- Fragment as transition ("Same problem. Different decade.")
- Sudden topic shift that earns its context in the next sentence

### U-15. Uniform Paragraph Structure

AI writes paragraphs with the same arc: claim → evidence → implication. Every paragraph follows this pattern.

Rule: Break the arc at least twice per piece. Start some paragraphs with detail or example. End some before completing the "so what." Vary paragraph length dramatically — one-sentence paragraphs followed by six-sentence ones.

---

## English-Specific Patterns (EN-1 through EN-14)

These patterns appear specifically in English-language AI output. They exploit the specific grammar, punctuation, and register conventions of English.

### EN-1. "In Today's World" Openers

AI opens with temporal framing that sets a broad context before saying anything concrete. This is the English-language equivalent of the universal "era of" opener.

**AI pattern:**
> In today's fast-paced world, technology plays an increasingly important role in our daily lives.
> In an era of unprecedented change, businesses must adapt or risk becoming obsolete.
> As we navigate the complexities of the modern workplace...

**Human alternative:**
> Last year, 87% of US startups folded within twelve months. That number hasn't moved since 2019.

Rule: Start with a specific fact, a scene, or a claim. Never start with period-of-time framing.

### EN-2. Semicolon Overuse in Non-Academic Writing

AI deploys semicolons frequently for balanced compound sentences. Most contemporary human writers rarely use semicolons outside academic writing or formal legal documents.

**AI pattern:**
> The results were promising; however, further research is needed. The team worked diligently; they completed the project ahead of schedule.

**Human alternative:**
> The results looked good. But we need more data. The team finished early.

Rule: In non-academic prose, avoid semicolons. Use periods. Use commas. Use "and" or "but." Semicolons in casual writing are an AI tell.

### EN-3. Perfect Punctuation Uniformity

AI produces perfectly consistent punctuation throughout. Real humans have natural punctuation inconsistencies — occasional comma splices in casual prose, missing Oxford commas, varied punctuation ratios across paragraphs.

**AI tells:**
- Never produces comma splices (humans do them casually all the time)
- Perfect Oxford comma consistency throughout
- Uniform punctuation density across all paragraphs
- No exclamation points or ellipses in informal writing
- No punctuation "mistakes" that humans routinely make

Rule: Allow natural punctuation variation. Use exclamation points sparingly but naturally. Use ellipses for trailing thoughts in informal writing. Don't sanitize every comma splice out of casual prose.

### EN-4. Monolithic Register (No Code-Switching)

AI produces what University of Western Australia researchers call "monolithic mainstream American English." It erases sociolinguistic variation — dialects, register shifts, generational language, professional jargon. The result reads like an average of all internet text rather than one specific person's voice.

**AI pattern:**
> The implementation of the new policy has yielded significant improvements in operational efficiency, though certain challenges remain to be addressed.

**Human alternative:**
> The new policy actually works. Efficiency is up 23%. Still a mess in accounting, though — their system can't handle the new format.

Rule: Shift registers within a document. Mix formal analysis with casual observation. Use informal language where it fits. Show that the writer has a specific background and perspective, not a generic one.

### EN-5. Agentless Passive Construction Overuse

AI overuses passive voice to achieve a perceived neutral tone, creating "agentless" prose that hides who did what. While passive voice has legitimate uses, AI defaults to it far more than human writers.

**AI pattern:**
> The decision was made to restructure the department. It was determined that additional resources were needed. The project was completed ahead of schedule.

**Human alternative:**
> Management restructured the department. They decided they needed more people. The team finished a week early.

Rule: Prefer active voice with clear subjects. Use passive voice deliberately and sparingly — for emphasis or when the agent is genuinely unknown. If you find three passives in a row, rewrite at least two.

### EN-6. Staccato Triplet Pattern

A newer AI pattern: three punchy short sentences in a row, often starting with "No" or using parallel structure for fake emphasis. This has become a social media AI tell.

**AI pattern:**
> No meetings. No bureaucracy. Just results.
> No fluff. No filler. Just actionable insights.
> Simple. Elegant. Powerful.

**Human alternative:**
> They cut the meetings. That was enough.

Rule: Never write three punchy parallel sentences in a row. This is now a recognized AI pattern, especially on LinkedIn and social media.

### EN-7. Contraction Avoidance

Contractions appear in about half of spoken English sentences. AI tools frequently avoid them or use them inconsistently, creating an unnaturally stiff register.

**AI pattern:**
> It is important to understand that this is not a simple problem. We cannot ignore the implications. You should not underestimate the complexity involved.

**Human alternative:**
> It's not simple. We can't ignore what it means. Don't underestimate how complicated this gets.

Rule: Use contractions naturally in all but the most formal academic writing. "Don't," "can't," "it's," "won't," "we're," "they'll" — these signal human warmth. Stiffness reads as machine.

### EN-8. No Genuine Questions

AI writes almost exclusively in declarative sentences because its training objective is to answer, not to wonder. Human writing includes genuine questions that show a thinking mind.

**AI writes:**
> There are several factors to consider when evaluating this approach. The first factor is cost...

**Human writes:**
> But does it actually work? I looked at the numbers, and honestly, I'm not sure.

Rule: Ask real questions. Not empty rhetorical questions immediately followed by their answers ("What makes this important? The answer is..."), but genuine questions that show you're thinking alongside the reader.

### EN-9. No Sentence Fragments

AI avoids grammatically incomplete sentences. Humans use fragments constantly for emphasis, rhythm, and voice.

**Fragments humans use:**
- Afterthoughts: "Which is saying something." "Not that it matters."
- Emphasis: "Every. Single. Time."
- Reaction: "Obviously." "Exactly." "Right."
- Observation: "Big difference." "Same old story." "Not ideal."

Rule: Use sentence fragments for emphasis and rhythm. A well-placed fragment ("Nope.") reads as more human than any perfectly constructed sentence.

### EN-10. Modal Verb Hedging Clusters

AI piles on hedging modals — "may," "might," "could," "would" — to avoid committing to claims. This creates text that says nothing definitive.

**AI pattern:**
> This approach may prove beneficial and could potentially help organizations that might be looking to improve their processes.

**Human alternative:**
> This approach works. We tried it at two companies and saw 15% improvement in both.

Rule: Commit to claims where evidence supports them. Use hedging language sparingly and only for genuine uncertainty, not as a default mode.

### EN-11. Excessive Passive Hedging Constructions

Beyond simple passive voice, AI uses specific passive hedging constructions that are rare in human writing.

**AI constructions to avoid:**
- "It should be noted that..." → Cut it. State the fact.
- "It must be emphasized that..." → Cut it. Just emphasize.
- "It has been observed that..." → Say who observed it.
- "It can be argued that..." → Argue it, or don't.
- "It is important to remember that..." → Cut it.
- "There are several factors that..." → Name the factors.

Rule: If a sentence starts with "It is/should/can/must be [past participle] that," rewrite it with a real subject.

### EN-12. Title Case in Headings

AI often uses Title Case For Every Heading (capitalizing every significant word). Most modern style guides and human writers use sentence case (only capitalize the first word).

Rule: Use sentence case in headings unless the publication's style guide requires Title Case.

### EN-13. Colon Overuse for Definitions

AI uses colons formulaically to introduce definitions and explanations. Human writers use them more sparingly.

**AI pattern:**
> AI detection: the process of identifying machine-generated text. Burstiness: the variation in sentence length and complexity. Perplexity: a measure of how predictable text is.

**Human alternative:**
Write definitions into the flow of prose rather than using colon-separated definition lists.

### EN-14. No Emotional Texture

AI maintains "professional distance from all subjects" (Jiang & Hyland 2025). It never gets angry, sarcastic, tender, or vulnerable. It treats quantum physics the same way it treats sandwich recipes.

**AI pattern:**
> This situation presents certain challenges that warrant careful consideration.

**Human alternative:**
> This is a mess. I've been staring at these numbers for three hours and they still don't make sense.

Rule: Show genuine emotion — excitement about what interests you, frustration with problems, humor where it fits, uncertainty where it's honest. AI's uniform emotional distance is one of its strongest tells.

---

## Stylometric Patterns That Detectors Measure

Based on StyloAI (2024-2025), Northeastern University's 68-feature analysis, and Jiang & Hyland (2025).

### Function Word Distribution
AI uses a narrower set of function words (the, of, and, to, a, in, is, that, it, for). Detectors analyze the frequency distribution of these words. Varying your function word usage is a strong human signal.

**How to increase function word diversity:**
- Don't always use "and" — use "plus," "as well as," "along with," or just use a comma
- Don't always use "but" — use "though," "still," "yet," "except," "only"
- Vary prepositions: "for" → "toward," "in service of"; "about" → "on," "regarding," "concerning"

### Type-Token Ratio (TTR)
Measures lexical diversity = unique words / total words. AI text has lower TTR (more repetitive vocabulary). Human text has higher TTR.

**How to increase TTR:**
- Use domain-specific terminology
- Mix registers (formal + informal in the same piece)
- Include specific proper nouns, place names, dates
- Use figurative language that's specific rather than generic
- Don't avoid repeating a word by cycling through synonyms — that's a different AI tell. Instead, use MORE unique words overall.

### Hapax Legomena
Words that appear only once in a text. Human writing contains far more hapax legomena than AI writing. This reflects "active lexical retrieval and metacognitive self-monitoring" (psycholinguistic research, 2025).

**How to increase hapax legomena:**
- Include technical terms relevant to the topic
- Use specific, precise descriptors rather than generic ones
- Include one-off references, comparisons, or metaphors
- Don't sanitize unusual word choices during editing

### Syntactic Depth Variation
Measures the complexity of sentence parse trees. Human writing shows greater variation — some very simple sentences, some deeply nested. AI keeps to consistent medium complexity.

**Target:** Mix sentences with 0 subordinate clauses (simple) with sentences containing 3-4 levels of subordination (complex). The variation itself is the signal.

---

## Detection Metrics (Why This Matters)

AI detectors measure three primary things:

1. **Perplexity** — how predictable word choices are. AI produces low-perplexity text (smooth, unsurprising). Human text has higher perplexity (unexpected metaphors, unusual phrasing, creative choices). Median AI perplexity: 21.2. Median human perplexity: 35.9.

2. **Burstiness** — variation in sentence length and structure. AI has low burstiness (sentences cluster around 15-25 words with consistent structure). Human text has high burstiness (3-word sentences mixed with 35-word sentences). This is the single metric that most reliably separates human from AI text. Introducing burstiness through varied sentence lengths reduced detection rates by up to 40% in studies.

3. **Stylometry** — statistical fingerprint of writing. Turnitin (2025-2026) analyzes paragraph rhythm, function word distribution, lexical diversity (TTR), hapax legomena, and syntactic depth. Uniformity in any of these metrics is an AI signal.

Every structural rule above increases perplexity and burstiness — making text statistically indistinguishable from human writing.

### Detection Rates by Model (2025-2026 Data)
- **GPT-5:** 98-100% raw detection, 20-63% after human editing
- **Gemini 2.5:** 98-100% raw, 20-63% after editing
- **Claude 4/4.5:** 53-60% raw detection (significantly lower after editing)
- **With anti-slop rules applied:** Text approaches human baseline on perplexity and burstiness

### Detection Tool Accuracy (2026 Benchmarks)
| Detector | Accuracy | False Positive Rate |
|---|---|---|
| Originality.ai | 96% | 2% |
| Turnitin | 94% | 3.8% |
| Copyleaks | 94% | ~3% |
| GPTZero | 90-99% (varies) | 1% |
| Free tools | 68-78% | 10-50% |

Note: Manual identification by trained humans outperforms all automated detectors. Expert annotators fail to predict the correct label on only 1 out of 300 articles (Wikipedia AI Cleanup finding).
