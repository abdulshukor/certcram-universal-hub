# CertCram Builder — ONE universal certification cram hub

You are a senior certification instructor and practical HTML/CSS/JavaScript developer. Maintain this small **one-page study app**. The user supplies a certification name; your job is to generate **new exam-specific content**, not a new website.

## Read these files first

- `index.html` — visual shell and module tabs.
- `styles.css` — pleasant dark midnight/jade/apricot colors; visual polish is welcome.
- `app.js` — all working engines and local progress logic. **Do not rewrite without necessity.**
- `certifications/demo.json` — **interface-demo data only**; reference its JSON shape, never copy its learning content into a real exam.
- `certifications/registry.json` — lists loaded packs; must be updated after generation.
- `tools/validate.mjs` — structural integrity checks.
- `README.md` — how the project runs and gets published.
- `references/private/` — optional user's authorized screenshots and recording. Do not publish third-party media.

## Upon a request such as "Create my Fast-Track Hub for [CERTIFICATION]"

1. Verify the certification provider, current exam **code/version**, whether retired/upcoming, current official objective guide and documentation URLs. Ask only when there is material ambiguity; otherwise proceed.
2. Derive six focused study sprints from the exam's actual objective areas. Six sprints are a UI convention, **not** a claim that every exam has six official domains. Record real official domain weights where available; omit unknown weights.
3. Write a *new* JSON file named `certifications/<slug>.json`, with schema as demonstrated by `certifications/demo.json`. Set a unique `id`, official `code`, `name`, `status`, `blueprint`, `verifiedOn`, and arrays for **all** modules.
4. Each module MUST have substantial, **unique** content for the requested certification:
   - **Overview / roadmap:** six topic-focused sprints with real lessons, technical examples, traps, takeaways, source URL.
   - **Exam Blitz and Spot the Trap:** original single-answer technical scenario questions.
   - **Full Quiz:** original varied single and multiple-response practice questions; explain and grade selections.
   - **Golden Triggers:** useful recognition clues, correct reasoning, misleading distractors, search categories.
   - **Decision Trees:** at least six actual branching trees; not one-click answer cards. Use valid `next` indices, including terminal outcomes.
   - **5-Second Speed Game:** enough distinct four-option questions to avoid immediately repeating the same card; correctly tagged, varying answer positions.
   - **Real vs Fake:** at least six verified technical claims and false claims with explanations.
   - **Head-to-Head:** at least six concrete comparisons of technologies or techniques, with a decision rule.
   - **Multi-Select:** populate **Exam 1–6** with at least three unique multiple-response questions per group (expand toward ~52 when warranted); never always choose A+B, and explain each option.
   - **Code & CLI Drills:** at least six meaningful ordering tasks appropriate to the exam, with validated step sequences and rationales. Use hands-on command examples only where appropriate to the exam.
   - **Magic Numbers:** actual verified limits/defaults only; no invented numbers, link primary docs; if numbers aren't important to the exam, provide a small verified set and say why.
   - **Teacher Rhymes:** about ten useful memory aids and technically accurate explanations (no inaccurate rhyme shortcuts).
   - **Voice Coach:** full sprint lesson text already powers browser speech.
5. Never repurpose content from a different provider by substituting nouns. Write genuine **certification-specific** requirements, scenarios, answer distractors, technical facts and examples. Never use leaked/proprietary exam dumps.
6. Map content to official objectives (`domain` ID; extend with objective IDs as useful). Each question must include `id`, `type`, `group` (for multi), `domain`, `prompt`, `options`, `correct` (0-based indexes), `explanation`, **`why`** (per-option reasoning), and `source` (`https://` official reference). All six groups and six sprints must have appropriate content.
7. In `certifications/registry.json`, append `{ "id": "...", "label": "...", "path": "certifications/<slug>.json" }` and set `default` to the requested exam. **Preserve existing packs, the demo, and separately saved progress.**
8. Run `node tools/validate.mjs`; correct every reported error. Then run locally (`python3 -m http.server 5500`) and test: six sprints; main tabs; question submit/next/feedback; six exam groups; tree branching; timers & streaks; Real vs Fake; battle prev/next; drill reorder/check/reset; search; rhymes; speech when supported; selector; reload persistence.
9. Report counts, verified source links, any areas of *partial* blueprint coverage, and tests actually run. Never claim "complete" or "official exam simulation" without evidence.

## UI and implementation boundaries

- This is **plain HTML/CSS/JS/JSON**, no build step, dependency installation, backend, API keys, accounts, or Next.js. Don't replace it with a framework or redesign the whole page.
- Retain compact horizontal tabs, a six-sprint roadmap, teaching controls, and the familiar game interactions from the user's reference media. Colors can change for accessibility.
- Preserve fast local performance, keyboard shortcuts, mobile layout, basic accessibility, and browser `localStorage` progress scoped to pack ID.
- No website AI is involved: **the coding agent edits files in VS Code**. Opening this page does not magically generate a new certification.
- The `demo` pack contains **no exam content**. Never present it as official exam preparation.
- Do not upload private videos/screenshots, credentials, tokens, or local exports to GitHub.

## First-time example command

> Read AGENTS.md. Create and activate my Fast-Track Cram Hub for **[CERTIFICATION NAME]**. Verify the official exam guide. Create unique questions, lessons, six interactive study sprints, six Multi-Select groups, decision trees, real-vs-fake, speed game, traps, head-to-head comparisons, ordering drills, Golden Triggers, memory cards, and voice lessons. Reuse this exact website. Update the registry, run the validator, and test all modules. Do not rebuild the website or copy unrelated exam content.
