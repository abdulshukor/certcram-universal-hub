# ✦ CertCram — Universal Fast-Track Cram Hub

**One lightweight website. Any certification content you ask your VS Code AI coding agent to create.**

A compact, interactive training hub inspired by the *learning interactions* in a reference cram website: six timed study sprints, concept lessons, Exam Blitz, six Multi-Select groups, Golden Triggers, branching decision trees, 5-Second Speed Game, Spot the Trap, Real vs Fake, Head-to-Head comparisons, Code/CLI ordering drills, Magic Numbers, Teacher Rhymes, and a browser voice coach.

Built with **HTML + CSS + JavaScript + JSON**. **No npm, Next.js, database, account, API key, build tool, or paid service required to run.** Designed for VS Code and GitHub Pages.

> **Important:** This download is a **universal engine**, not an AWS/Azure/etc. study course. It intentionally includes **no ready-made certification pack**. A clearly labeled `Interactive Demo` pack lets you click and test the games. **Your VS Code coding agent creates real exam-specific lessons and questions only when you request a certification.** The browser itself does not generate AI content. Generated questions are independently written practice material, not official exam questions or a guarantee of passing.

## 1. Get started in VS Code (3 steps)

1. Extract the ZIP. In VS Code, **File → Open Folder** → open the extracted `certcram-universal-hub` folder. You should see `AGENTS.md`, `index.html`, `app.js`, `styles.css`, `certifications/`, and `README.md`.
2. Open **Terminal → New Terminal** in the folder, then run:

   ```bash
   python3 -m http.server 5500
   ```

   On Windows, use `py -m http.server 5500` instead. Or use VS Code's **Live Server** extension and select **Open with Live Server** on `index.html`.
3. Visit **http://localhost:5500/**. Try the sample sprints and each interactive tab. **Do not** double-click `index.html` using a `file://` URL; most browsers won't fetch external JSON files that way.

**Requirements:** any modern browser, VS Code or another editor, plus Python 3 *or* Live Server to serve files. **Optional**: Node.js to validate content packages; an AI coding agent such as GitHub Copilot Agent Mode or Codex to generate new exam content.

## 2. Create a hub for ANY certification (ONE prompt)

In **VS Code**, open your AI coding agent in **Agent mode**. Optionally select the included workspace agent `CertCram Builder` if your VS Code version supports custom agents. Paste:

```text
Read AGENTS.md.
Create and activate my complete Fast-Track Cram Hub for [CERTIFICATION NAME].
Verify the current official exam guide and code. Write a NEW, original
certification JSON pack with realistic lessons, six study sprints, single-
and multiple-response questions, six Multi-Select exam groups, Golden
Triggers, six branching decision trees, the 5-Second Game, Spot the Trap,
Real vs Fake, Head-to-Head comparisons, six Code/CLI ordering drills,
verified Magic Numbers, ten Teacher Rhymes, and Voice Coach lessons.
Provide reasoning for correct and incorrect options and official links.
Reuse index.html / styles.css / app.js exactly as the common application.
Preserve other exam packs and progress. Update certifications/registry.json,
set the new exam as default, run node tools/validate.mjs, and test every tab.
Do not rebuild the website and do not generate repetitive filler.
```

Change `[CERTIFICATION NAME]` to, for example, `AWS Certified DevOps Engineer – Professional`, `Microsoft Azure Administrator AZ-104`, or `Certified Kubernetes Administrator CKA`.

When finished, refresh the browser. The new exam appears in the **EXAM** selector and should load on startup. Ask the agent to validate the latest official exam version first; an exam code may be retired or revised.

**What the agent really does:** researches official objectives (if browsing is available), creates `certifications/<your-exam>.json`, registers it, and runs tests. This takes coding-agent time and review. Changing the selector to an **already-created** pack is immediate; generating a new pack is not automatic just by typing into the web page.

## 3. What works out of the box

| Module | Real behavior in the generic engine |
|---|---|
| Fast-Track roadmap | Six sprint cards, click to open lesson, mark done, completion bar, locally saved state |
| Main modes | Overview, Exam Blitz, Fast-Learn, Concept Guide, Full Quiz practice |
| Voice Coach | Choose sprint, Play/Pause/Resume/Stop/Next, speed; browser speech support required |
| Golden Triggers | Search and category filters |
| Decision Trees | Branching choices, outcomes, Back and Restart |
| 5-Second Speed Game | Countdown, options 1–4, answer feedback, XP/streak/high score, reset |
| Spot the Trap | Question, select, grade, explanation, next |
| Real vs Fake | Judge claim, keyboard shortcuts, XP, next |
| Head-to-Head | Compare two concepts with previous/next navigation |
| Multi-Select Lab | Exam 1–6 buttons, select a specified number, grade and explain |
| Code & CLI Drills | Move steps up/down, check sequence, reset/reveal |
| Magic Numbers | Search and filter verified fact cards |
| Teacher Rhymes | Card grid and persistent bookmarks |
| Certification selector | Switch published packs; progress isolated by pack ID in localStorage |

The included demo has **30 non-certification practice questions** and representative content across the interface. It exists to prove the controls work, **not** to prepare you for an exam. The new certification pack's depth/accuracy depends on the content the agent writes and validates. `Full Quiz` is currently a timed practice navigator, **not** a full official exam emulator, and the voice coach uses browser synthesis rather than a live conversational AI.

## 4. How it works (simple file structure)

```text
certcram-universal-hub/
├── index.html                       # One-page interface, tabs, forms
├── styles.css                       # Modern midnight / jade / apricot colors
├── app.js                           # All working game and study logic
├── AGENTS.md                        # Rules the coding agent must follow
├── certifications/
│   ├── registry.json                # List of available content packs
│   └── demo.json                    # Interactive DEMO, not certification content
├── tools/validate.mjs               # Content structure validation (Node, optional)
├── tests/smoke.py                   # Optional Playwright interaction checks
├── .github/agents/                  # Optional VS Code custom agent
├── references/README.md            # Notes for authorized private media
├── .gitignore
├── LICENSE
└── README.md
```

The engine is generic. **All exam-specific content is stored in JSON.** The AI agent uses `demo.json` only to understand the data shape and creates a new file with **actual exam-specific** questions, answers, comparisons, labs/drills, and lessons. Progress is stored under a certification-specific localStorage key; it is not uploaded anywhere.

## 5. Testing

**Quick checks:** Start the local server, select **Interactive Demo**, click all modules, answer a question, run the five-second timer, switch the Multi-Select exam group, reorder a drill, browse comparisons, test a tree, bookmark a rhyme, refresh to confirm progress, and try voice playback if supported.

**Validate data** after an agent generates a certification (Node.js is optional for normal use):

```bash
node tools/validate.mjs
```

This checks schema, IDs, six sprints and six exam groups, response indexes, ordering steps, and branching links. **Validation does not prove the technical answers are correct.** They must be reviewed against the official provider documentation.

**Optional browser smoke tests** (for contributors with Python Playwright + Chromium installed):

```bash
# Terminal 1
python3 -m http.server 5500
# Terminal 2
python3 tests/smoke.py
```

For a new certification, check whether all official exam objectives are covered, not merely whether the pack passes structural validation. Report partial coverage honestly.

## 6. Publish on GitHub

This repository is a static site. It can be hosted on **GitHub Pages** using `main` branch `/ (root)` as the Pages source, or another static host. It needs no backend and no paid server. Public viewers can use whatever certification packs are committed to the repo; **they do not get an automatic coding agent inside the website**.

1. Create an **empty** GitHub repository named `certcram-universal-hub` (don't initialize it with a second README).
2. In the extracted folder, run:

   ```bash
   git init
   git add .
   git status               # Review every staged file carefully
   git commit -m "Initial universal Fast-Track Cram Hub"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/certcram-universal-hub.git
   git push -u origin main
   ```

3. Replace `YOUR_USERNAME`. Enable **Settings → Pages → Deploy from a branch → main → / (root)**. View the resulting site URL after deployment.
4. Before posting the repository, confirm rights to distribute its code and any third-party material. The included `LICENSE` is MIT for the original template code; review attribution and rights before publication.

### What to commit and what to ignore

| **Commit (share)** | **Do not commit (private/generated)** |
|---|---|
| `index.html`, `styles.css`, `app.js` | `.env`, `.env.local`, API keys, credentials, private keys |
| `AGENTS.md`, `README.md`, `.gitignore` | `node_modules/`, `.next/`, `dist/`, `coverage/` |
| `certifications/registry.json` and approved public exam packs | private study exports, backups, tokens, credential JSON files |
| `tools/`, `tests/`, `.github/` | private reference video/screenshots without redistribution permission |

An included **`.gitignore`** already covers those categories. `.gitignore` does *not* remove files previously committed: use `git rm --cached <file>` and, for leaked secrets, revoke/rotate the credentials and clean Git history as appropriate. To preview what is staged before pushing, run `git diff --cached --stat` and `git status`.

**Original reference media:** A third party created the sample website shown in the user's images/video. Those assets are intentionally **not included** in this public ZIP. Put your own authorized references under `references/private/`, which Git ignores. The shipped UI is an original implementation of the observed *learning interaction pattern*, not the original site's source code.

## 7. Change the colors

The UI already uses a comfortable **midnight-blue, soft jade, and warm apricot** theme. To customize it, edit the first `:root` variables in `styles.css`. No images, libraries or font downloads are necessary.

## 8. Limitations and ethics

- The initial demo is not an exam pack. Ask the VS Code agent for any specific certification before relying on the content.
- New content needs a current official exam guide and technical review. An unavailable source must be marked unverified. Never call generated questions "official" or use exam dumps.
- This project is not affiliated with or endorsed by certification providers. Names and trademarks belong to their owners.
- Scoring here is for *practice*; it does not predict provider-scaled results. Browser localStorage stays on your device/browser and is not a multi-device sync.
- Browser voice functionality depends on browser/system voices and may not work in every environment.

**The workflow to remember:** Open VS Code → ask your coding agent for a certification → it creates a new JSON pack → validate and review it → refresh the same website → study with all the familiar learning tools.
