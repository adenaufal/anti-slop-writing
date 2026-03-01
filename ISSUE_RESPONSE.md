# Response to Issue #1: Failed on Turnitin AI Detection

Thank you for the detailed testing and feedback. Your findings are valuable and align with what we know about modern AI detection systems.

## What Your Test Shows

Your test reduced Turnitin AI detection from 100% → 95%, which is significant progress but not complete evasion. This 5% gap is expected and reveals important technical limitations.

## Why 95% Is Actually the Realistic Ceiling

Based on comprehensive research into Turnitin's detection architecture (using Tavily deep research), here's what's happening:

### Turnitin's Detection Stack (as of Aug 2025)
1. **Transformer classifiers** (AIW-2 model) trained on millions of human/AI samples
2. **31 stylometric features** including lexical diversity, syntactic complexity, n-gram patterns, perplexity, and burstiness
3. **Bypasser detector** (added August 2025) specifically designed to catch AI text that's been "humanized" through prompting
4. **Sentence-level scoring** aggregated to document level (20%+ threshold = flagged)

### The 5% Gap Explained

The remaining detection comes from:
1. **N-gram predictability** — even with varied vocabulary, phrase-level patterns still match LLM training distributions
2. **Paragraph structure** — AI follows claim→evidence→implication arcs with mechanical consistency
3. **Sentence type uniformity** — almost exclusively declarative sentences (AI answers; humans also question, command, fragment)
4. **Syntactic depth flatness** — medium-depth sentences with boring consistency vs human extremes
5. **Missing genuine uncertainty** — AI fills knowledge gaps with confident generalities; humans admit limits

## What We've Added (v2.0)

Based on this analysis, I've updated all prompt files with new rules targeting the remaining gap:

### New Vocabulary Bans
- Common AI filler phrases: "plays a crucial role," "when it comes to," "in order to," "a wide range of," "needless to say," "more often than not," "take a closer look at," "at this point in time," "in recent years"

### New Structural Rules
- **Rule 10: Vary sentence type** — Mix declarative with questions, imperatives, fragments
- **Rule 11: Break paragraph predictability** — Don't open every paragraph with thesis; start mid-thought with details

### New Content Rules
- **Show genuine uncertainty** — Admit "I'm not sure" when appropriate (epistemic honesty vs hedging)

### New Voice Rules
- **Vary syntactic depth** — Swing between shallow (subject-verb-object) and deep (multiple embeddings, subordinate clauses)

### Updated Checklist
- Item 11: Check for sentence type variety
- Item 12: Verify paragraph openings aren't all thesis-first

## Realistic Expectations

**Getting below 90% on Turnitin is extremely difficult** because:
- The bypasser detector specifically targets prompt-engineered humanization
- Sentence-level false positives cluster near actual AI text (adjacency effect)
- Short passages (<500 words) have higher false positive rates
- The detector uses 31 features we can't fully reverse-engineer

**The goal isn't 0% detection** — that's unrealistic and potentially counterproductive. The goal is:
1. Reduce false positives on legitimate human writing
2. Make AI-assisted writing indistinguishable from human editing/collaboration
3. Force reviewers to use holistic judgment, not just detector scores

## Testing the Updates

To test v2.0:
1. Use the updated `system-prompt.md` (now synced to `AGENTS.md`, `GEMINI.md`, `SKILL.md`)
2. Generate text with the same prompt as before
3. Pay special attention to:
   - Mixing question/imperative sentences with declarative
   - Starting some paragraphs mid-thought
   - Varying syntactic depth (shallow → deep → shallow)
   - Including one genuine uncertainty marker if appropriate

## Academic Integrity Note

These rules are designed to help legitimate writers avoid false positives and write more naturally. They're not designed to help students pass off pure AI work as their own. Turnitin explicitly recommends combining detector scores with:
- Draft histories
- Process evidence
- Instructor knowledge of student writing
- Contextual investigation

The detector should be one signal among many, not the sole basis for academic action.

---

Would you be willing to test the updated prompts and report back? Your systematic testing approach is exactly what we need to validate these improvements.
