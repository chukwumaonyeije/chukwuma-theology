---
marp: true
theme: uncover
paginate: false
---

<style>
/* ─── GOOGLE FONTS ─────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap');

/* ─── DESIGN TOKENS ────────────────────────────────────────────────────── */
:root {
  --primary:      #2d4739;
  --primary-deep: #1a2f26;
  --secondary:    #c26d4b;
  --accent:       #d4af37;
  --accent-dim:   #b8952a;
  --bg-light:     #faf9f6;
  --bg-scripture: #0d1a12;
  --bg-dark:      #1a2f26;
  --bg-tan:       #f5f0e8;
  --text-dark:    #1a1a1a;
  --text-muted:   #555555;
  --text-light:   #f0ece4;
  --border:       #d8d2c8;
  --white:        #ffffff;

  /* ── Lit-room contrast overrides ── */
  --on-dark:      #ffffff;
  --on-dark-dim:  rgba(255,255,255,0.60);
  --on-dark-faint:rgba(255,255,255,0.35);
}

/* ─── GLOBAL BASE ──────────────────────────────────────────────────────── */
/* Fix rem base: Marp's uncover theme defaults to 28px, which inflates everything.
   Explicitly anchor 1rem = 20px so all sizing is predictable.             */
section {
  font-family: 'Inter', sans-serif;
  font-size: 20px;           /* rem anchor — do not remove */
  background: var(--bg-dark);
  color: var(--on-dark);
  padding: 44px 68px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  width: 1280px;
  height: 720px;
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

/* Gold rule — bottom of every slide */
section::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0;
  width: 100%; height: 4px;
  background: linear-gradient(90deg, var(--accent), var(--secondary), var(--accent));
}

h1, h2, h3 {
  font-family: 'Playfair Display', serif;
  color: var(--on-dark);
  margin: 0 0 0.35em 0;
  line-height: 1.18;
}

h1 { font-size: 2.9rem;  font-weight: 700; }
h2 { font-size: 2.0rem;  font-weight: 700; }
h3 { font-size: 1.3rem;  font-weight: 400; font-style: italic; }

p  { font-size: 1.05rem; line-height: 1.65; margin: 0 0 0.5em 0; color: var(--on-dark); }
ul { list-style: none; padding: 0; margin: 0; }
li {
  font-size: 1.0rem; line-height: 1.55;
  padding: 0.25em 0 0.25em 1.4em;
  position: relative; color: var(--on-dark);
}
li::before { content: '—'; position: absolute; left: 0; color: var(--accent); font-weight: 700; }

strong { color: var(--accent); font-weight: 700; }
em     { color: var(--secondary); font-style: italic; }

/* ─── ACCENT LINE UNDER HEADING ────────────────────────────────────────── */
.accent-line {
  width: 56px; height: 3px;
  background: var(--accent);
  margin: 0.45em 0 1em 0;
}

/* ═══════════════════════════════════════════════════════════════════════════
   SLIDE CLASSES
   ═════════════════════════════════════════════════════════════════════════ */

/* ─── TITLE SLIDE ───────────────────────────────────────────────────────── */
section.title {
  background: var(--bg-dark);
  align-items: center;
  text-align: center;
  padding: 44px 100px;
}

section.title::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background:
    radial-gradient(ellipse at 20% 80%, rgba(212,175,55,0.15) 0%, transparent 55%),
    radial-gradient(ellipse at 80% 20%, rgba(194,109,75,0.12) 0%, transparent 50%);
  pointer-events: none;
}

section.title h1 {
  font-family: 'Playfair Display', serif;
  color: var(--white);
  font-size: 3.8rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  margin-bottom: 0.12em;
  text-shadow: 0 2px 24px rgba(0,0,0,0.5);
}

section.title .subtitle {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 1.45rem;
  color: rgba(255,255,255,0.68);
  margin-bottom: 1.4rem;
}

section.title .event-tag {
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.5rem;
}

section.title .divider-gold {
  width: 72px; height: 2px;
  background: var(--accent);
  margin: 1.2rem auto;
  opacity: 0.85;
}

/* ─── ANCHOR SLIDE ──────────────────────────────────────────────────────── */
section.anchor {
  background: var(--primary-deep);
  align-items: center;
  text-align: center;
  padding: 44px 110px;
}

section.anchor blockquote {
  font-family: 'Playfair Display', serif;
  font-size: 2.15rem;
  font-style: italic;
  color: var(--white);
  line-height: 1.45;
  margin: 0 0 0.9rem 0;
  border: none;
  padding: 0;
}

section.anchor blockquote strong {
  color: var(--accent);
  font-style: normal;
  font-weight: 700;
}

section.anchor .anchor-label {
  font-family: 'Inter', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 1.2rem;
}

section.anchor .anchor-note {
  font-size: 0.88rem;
  color: var(--on-dark-dim);
  font-style: italic;
  margin-top: 1.2rem;
}

/* ─── SCRIPTURE SLIDES ──────────────────────────────────────────────────── */
section.scripture {
  background: var(--bg-scripture);
  align-items: flex-start;
  padding: 56px 88px;
}

section.scripture .ref-tag {
  font-family: 'Inter', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 1.2rem;
  display: block;
}

section.scripture blockquote {
  font-family: 'Playfair Display', serif;
  font-size: 2.0rem;
  font-style: italic;
  color: var(--white);
  line-height: 1.5;
  border-left: 5px solid var(--accent);
  padding-left: 28px;
  margin: 0 0 1rem 0;
}

section.scripture .context-note {
  font-size: 0.95rem;
  color: var(--on-dark-dim);
  font-style: italic;
  margin-top: 1rem;
}

section.scripture .arc-label {
  font-family: 'Inter', sans-serif;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--on-dark-faint);
  position: absolute;
  bottom: 20px;
  right: 68px;
}

/* ─── DARK STATEMENT SLIDES ─────────────────────────────────────────────── */
section.dark-statement {
  background: var(--primary-deep);
  align-items: center;
  text-align: center;
  padding: 44px 90px;
}

section.dark-statement p {
  font-family: 'Playfair Display', serif;
  font-size: 2.0rem;
  font-style: italic;
  color: var(--white);
  line-height: 1.5;
  margin: 0;
}

section.dark-statement p strong {
  color: var(--accent);
  font-style: normal;
  font-weight: 700;
}

section.dark-statement .sub-note {
  font-family: 'Inter', sans-serif;
  font-size: 0.88rem;
  color: var(--on-dark-dim);
  margin-top: 1.6rem;
  font-style: normal;
}

/* ─── GOLD STATEMENT (key theological declarations) ─────────────────────── */
section.gold-statement {
  background: var(--accent);
  align-items: center;
  text-align: center;
  padding: 44px 90px;
}

section.gold-statement::after { background: var(--primary-deep); }

section.gold-statement p {
  font-family: 'Playfair Display', serif;
  font-size: 2.2rem;
  font-style: italic;
  color: var(--primary-deep);
  line-height: 1.4;
  margin: 0;
  font-weight: 700;
}

section.gold-statement .sub-note {
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  color: rgba(26,47,38,0.7);
  margin-top: 1.4rem;
  font-style: normal;
  font-weight: 600;
}

/* ─── POLL / QR SLIDES ───────────────────────────────────────────────────── */
/* Dark background — projects clearly in lit rooms.
   Compact vertical rhythm so all 4 options always fit.                      */
section.poll {
  background: var(--primary-deep);
  padding: 36px 68px;
  justify-content: flex-start;
}

section.poll .poll-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}

section.poll .poll-badge {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  background: var(--secondary);
  color: var(--white);
  padding: 5px 12px;
  border-radius: 4px;
}

section.poll .mentimeter-tag {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--on-dark-dim);
  border: 1px solid rgba(255,255,255,0.25);
  padding: 4px 10px;
  border-radius: 4px;
}

section.poll h2 {
  font-family: 'Playfair Display', serif;
  font-size: 1.45rem;     /* controlled size — was 1.9rem which inflated */
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0;
  line-height: 1.3;
  max-width: 960px;
}

/* Horizontal gold rule between question and options */
section.poll .poll-rule {
  width: 100%;
  height: 1px;
  background: rgba(212,175,55,0.35);
  margin: 12px 0;
}

section.poll .poll-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 10px;
  width: 100%;
  flex: 1;
}

section.poll .poll-option {
  background: rgba(255,255,255,0.07);
  border: 1.5px solid rgba(255,255,255,0.18);
  border-radius: 8px;
  padding: 12px 18px;
  font-family: 'Inter', sans-serif;
  font-size: 0.92rem;
  font-weight: 500;
  color: var(--white);
  display: flex;
  align-items: center;
  gap: 14px;
  line-height: 1.35;
}

section.poll .poll-option .opt-letter {
  width: 32px;
  height: 32px;
  min-width: 32px;
  background: var(--accent);
  color: var(--primary-deep);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 0.82rem;
  flex-shrink: 0;
}

section.poll .poll-qr-note {
  font-size: 0.72rem;
  color: var(--on-dark-faint);
  font-style: italic;
  margin-top: 8px;
}

/* ─── POLL TWO-COLUMN BODY (options left, QR right) ────────────────────── */
section.poll .poll-body {
  display: grid;
  grid-template-columns: 1fr 220px;
  gap: 28px;
  width: 100%;
  flex: 1;
  align-items: start;
}

section.poll .poll-left {
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* QR panel — right column */
section.poll .poll-qr-panel,
section.poll-open .poll-qr-panel {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--white);
  border-radius: 12px;
  padding: 16px 14px 14px;
  gap: 10px;
  align-self: center;
}

section.poll .poll-qr-panel img,
section.poll-open .poll-qr-panel img {
  width: 160px;
  height: 160px;
  display: block;
  border-radius: 6px;
}

section.poll .poll-qr-panel .qr-go,
section.poll-open .poll-qr-panel .qr-go {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--primary-deep);
  text-align: center;
}

section.poll .poll-qr-panel .qr-url,
section.poll-open .poll-qr-panel .qr-url {
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  font-weight: 800;
  color: var(--primary-deep);
  text-align: center;
  letter-spacing: 0.04em;
}

section.poll .poll-qr-panel .qr-code-num,
section.poll-open .poll-qr-panel .qr-code-num {
  font-family: 'Inter', sans-serif;
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--primary);
  text-align: center;
  letter-spacing: 0.12em;
  border: 2px solid var(--primary);
  border-radius: 6px;
  padding: 4px 10px;
  width: 100%;
  box-sizing: border-box;
}

/* poll-open two-col layout */
section.poll-open .poll-open-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: 100%;
}

section.poll-open .poll-open-row {
  display: grid;
  grid-template-columns: 1fr 220px;
  gap: 28px;
  width: 100%;
  align-items: center;
}

/* ─── OPEN POLL (single large question) ─────────────────────────────────── */
section.poll-open {
  background: var(--primary-deep);
  align-items: center;
  text-align: center;
  padding: 44px 100px;
}

section.poll-open .poll-badge {
  font-family: 'Inter', sans-serif;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  background: var(--secondary);
  color: var(--white);
  padding: 6px 14px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 1.4rem;
}

section.poll-open h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2.1rem;
  color: var(--white);
  line-height: 1.4;
  max-width: 860px;
}

section.poll-open .poll-sub {
  font-size: 0.85rem;
  color: var(--on-dark-faint);
  font-style: italic;
  margin-top: 1.2rem;
}

/* ─── QUESTION SLIDES (pivotal unanswered questions) ────────────────────── */
/* Dark background — legible in lit rooms; italic gold text for weight       */
section.question {
  background: var(--bg-dark);
  align-items: center;
  text-align: center;
  padding: 44px 110px;
}

section.question h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2.1rem;
  font-style: italic;
  color: var(--white);
  line-height: 1.45;
  max-width: 900px;
}

section.question .q-note {
  font-size: 0.85rem;
  color: var(--on-dark-dim);
  margin-top: 1.6rem;
  font-style: italic;
}

/* ─── DISCUSSION SLIDES ──────────────────────────────────────────────────── */
section.discussion {
  background: var(--bg-dark);
  padding: 40px 68px;
  justify-content: flex-start;
}

section.discussion .disc-badge {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  background: var(--primary);
  color: var(--accent);
  border: 1px solid var(--accent);
  padding: 6px 14px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 0.9rem;
}

section.discussion h2 {
  font-size: 1.5rem;
  color: var(--white);
  margin-bottom: 0.2em;
}

section.discussion .disc-questions {
  margin-top: 1rem;
  width: 100%;
}

section.discussion .disc-q {
  background: rgba(255,255,255,0.07);
  border-left: 4px solid var(--accent);
  padding: 16px 22px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 12px;
  font-family: 'Playfair Display', serif;
  font-size: 1.05rem;
  font-style: italic;
  color: var(--white);
  line-height: 1.5;
}

section.discussion .disc-time {
  font-size: 0.75rem;
  color: var(--on-dark-dim);
  font-style: italic;
  margin-top: 0.8rem;
}

/* ─── QUOTE SLIDES (Ellen White) ─────────────────────────────────────────── */
/* Dark background with bright quote text — high contrast for lit rooms      */
section.quote {
  background: var(--bg-dark);
  padding: 48px 80px;
  align-items: flex-start;
}

section.quote .quote-source {
  font-family: 'Inter', sans-serif;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--secondary);
  margin-bottom: 1rem;
}

section.quote blockquote {
  font-family: 'Playfair Display', serif;
  font-size: 1.55rem;
  font-style: italic;
  color: var(--white);
  line-height: 1.6;
  border: none;
  margin: 0;
  padding: 0 0 0 24px;
  border-left: 4px solid var(--accent);
  max-width: 1020px;
  position: relative;
}

section.quote blockquote::before {
  content: '\201C';
  font-size: 6rem;
  color: var(--accent);
  opacity: 0.2;
  position: absolute;
  top: -20px;
  left: -10px;
  line-height: 1;
  font-family: 'Playfair Display', serif;
}

section.quote .quote-attr {
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  color: var(--on-dark-dim);
  margin-top: 1.1rem;
  font-style: italic;
}

/* ─── TENSION SLIDE (two-column statements) ─────────────────────────────── */
section.tension {
  background: var(--bg-dark);
  padding: 40px 68px;
  align-items: flex-start;
}

section.tension .tension-label {
  font-family: 'Inter', sans-serif;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--on-dark-dim);
  margin-bottom: 1rem;
}

section.tension .tension-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: 100%;
}

section.tension .tension-card {
  padding: 28px 26px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 160px;
}

section.tension .tension-card.card-a {
  background: rgba(212,175,55,0.12);
  border-top: 4px solid var(--accent);
  border: 1.5px solid rgba(212,175,55,0.4);
  border-top: 4px solid var(--accent);
}

section.tension .tension-card.card-b {
  background: rgba(194,109,75,0.12);
  border: 1.5px solid rgba(194,109,75,0.35);
  border-top: 4px solid var(--secondary);
}

section.tension .tension-card p {
  font-family: 'Playfair Display', serif;
  font-size: 1.3rem;
  line-height: 1.5;
  margin: 0;
}

section.tension .tension-card.card-a p { color: var(--white); }
section.tension .tension-card.card-b p { color: var(--white); }

section.tension .tension-footnote {
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  color: var(--on-dark-dim);
  font-style: italic;
  margin-top: 1rem;
  width: 100%;
}

/* ─── SABBATH SLIDES ─────────────────────────────────────────────────────── */
section.sabbath {
  background: var(--primary-deep);
  padding: 40px 80px;
  align-items: flex-start;
  justify-content: flex-start;
}

section.sabbath h2 {
  font-family: 'Playfair Display', serif;
  color: var(--white);
  font-size: 1.9rem;
  margin-bottom: 0.1em;
}

section.sabbath .sabbath-tag {
  font-family: 'Inter', sans-serif;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.8rem;
}

section.sabbath .sabbath-not-rule {
  font-family: 'Playfair Display', serif;
  font-size: 1.3rem;
  font-style: italic;
  color: var(--on-dark-dim);
  margin-top: 0.2rem;
  margin-bottom: 1.2rem;
}

section.sabbath .sabbath-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  width: 100%;
  margin-top: 0.4rem;
  flex: 1;
}

section.sabbath .s-col-label {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  margin-bottom: 0.6rem;
}

section.sabbath .s-col-label.interrupts { color: var(--secondary); }
section.sabbath .s-col-label.recenters  { color: var(--accent); }

section.sabbath .s-col li {
  font-size: 0.95rem;
  color: var(--on-dark-dim);
  padding: 0.22em 0 0.22em 1.4em;
}

section.sabbath .s-col li::before { color: var(--accent); }

/* ─── REFLECTION SLIDE ────────────────────────────────────────────────────── */
section.reflection {
  background: var(--bg-dark);
  align-items: center;
  text-align: center;
  padding: 44px 110px;
}

section.reflection .ref-badge {
  font-family: 'Inter', sans-serif;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 1.4rem;
  display: block;
}

section.reflection h2 {
  font-family: 'Playfair Display', serif;
  font-size: 1.9rem;
  font-style: italic;
  color: var(--white);
  line-height: 1.5;
  margin-bottom: 0;
  max-width: 860px;
}

section.reflection .ref-note {
  font-size: 0.82rem;
  color: var(--on-dark-faint);
  margin-top: 1.4rem;
  font-style: italic;
}

/* ─── LINGERING QUESTION (closing) ──────────────────────────────────────── */
section.lingering {
  background: var(--primary-deep);
  align-items: center;
  text-align: center;
  padding: 44px 90px;
}

section.lingering .ling-pre {
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  color: var(--on-dark-dim);
  font-style: italic;
  margin-bottom: 1.2rem;
}

section.lingering h2 {
  font-family: 'Playfair Display', serif;
  font-size: 1.9rem;
  color: var(--white);
  line-height: 1.5;
  margin-bottom: 0;
  max-width: 880px;
}

section.lingering .ling-verse-a {
  font-family: 'Inter', sans-serif;
  font-size: 0.85rem;
  color: var(--accent);
  font-weight: 700;
  letter-spacing: 0.08em;
  margin-top: 1.2rem;
}

section.lingering .ling-verse-b {
  font-family: 'Inter', sans-serif;
  font-size: 0.85rem;
  color: var(--on-dark-faint);
  letter-spacing: 0.08em;
  margin-top: 0.35rem;
}

/* ─── SECTION INTRO SLIDES ───────────────────────────────────────────────── */
section.section-intro {
  background: var(--bg-dark);
  align-items: flex-start;
  padding: 56px 88px;
}

section.section-intro .sec-number {
  font-family: 'Inter', sans-serif;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--secondary);
  margin-bottom: 0.4rem;
}

section.section-intro h1 {
  font-size: 2.7rem;
  color: var(--white);
  margin-bottom: 0.1em;
}

section.section-intro p {
  font-size: 1.05rem;
  color: var(--on-dark-dim);
  max-width: 700px;
  margin-top: 0.4rem;
}

section.section-intro .sec-bar {
  width: 56px;
  height: 3px;
  background: var(--accent);
  margin: 0.6rem 0 0.8rem 0;
}
</style>

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 1 — TITLE
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: title -->

<div class="event-tag">Atlanta North Vespers</div>

# Demas and the Drift

<div class="subtitle">When Good Work Replaces First Love</div>

<div class="divider-gold"></div>

<div class="subtitle" style="font-size:1rem; opacity:0.5; font-style:normal; letter-spacing:0.1em;">2 Timothy 4:10</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 2 — ANCHOR / THESIS
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: anchor -->

<div class="anchor-label">Facilitator Anchor — Keep This in View All Evening</div>

> "Demas did not stop **working.**
> He stopped **loving** rightly."

<div class="anchor-note">Everything tonight builds toward that sentence. Everything after it flows from it.</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 3 — QR PULSE #1
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: poll -->

<div class="poll-header">
  <span class="poll-badge">QR Pulse #1</span>
  <span class="mentimeter-tag">Mentimeter Poll</span>
</div>

## Right now, what gets most of your daily attention?

<div class="poll-rule"></div>

<div class="poll-body">
  <div class="poll-left">
    <div class="poll-options">
      <div class="poll-option"><span class="opt-letter">A</span>Christ and devotional life</div>
      <div class="poll-option"><span class="opt-letter">B</span>Career and professional growth</div>
      <div class="poll-option"><span class="opt-letter">C</span>Relationships and family</div>
      <div class="poll-option"><span class="opt-letter">D</span>Personal goals and self-development</div>
    </div>
    <p class="poll-qr-note">Scan code or visit menti.com — results display live</p>
  </div>
  <div class="poll-qr-panel">
    <img src="mentimeter_qr_code.png" alt="Mentimeter QR Code" />
    <div class="qr-go">Go to</div>
    <div class="qr-url">menti.com</div>
    <div class="qr-code-num">3461 4656</div>
  </div>
</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 4 — PIVOTAL QUESTION #1
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: question -->

## "Which of these could slowly replace Christ —
without you even noticing?"

<p class="q-note">Don't answer out loud. Just sit with it.</p>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 5 — SECTION INTRO: THE THREE MENTIONS
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: section-intro -->

<div class="sec-number">Scripture</div>

# The Three Mentions of Demas

<div class="sec-bar"></div>

The arc is the whole point.

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 6 — SCRIPTURE: COLOSSIANS 4:14
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: scripture -->

<span class="ref-tag">Colossians 4:14</span>

> "Luke the beloved physician, and **Demas,**
> greet you."

<p class="context-note">The co-laborer. Present. Trusted. Named.</p>

<span class="arc-label">1 of 3</span>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 7 — SCRIPTURE: PHILEMON 1:24
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: scripture -->

<span class="ref-tag">Philemon 1:24</span>

> "Marcus, Aristarchus, **Demas,** Lucas,
> my fellow labourers."

<p class="context-note">Still in the inner circle. Still working.</p>

<span class="arc-label">2 of 3</span>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 8 — SCRIPTURE: 2 TIMOTHY 4:10
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: scripture -->

<span class="ref-tag">2 Timothy 4:10</span>

> "For **Demas** hath forsaken me, having loved
> this present world."

<p class="context-note">Paul doesn't say Demas became wicked. He says Demas loved something else more.</p>

<span class="arc-label">3 of 3</span>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 9 — PAIRS DISCUSSION
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: discussion -->

<div class="disc-badge">Pairs Discussion — 2 Minutes</div>

## Did Demas fall suddenly — or drift gradually?

<div class="disc-questions">
  <div class="disc-q">"What do you think happened between Colossians and 2 Timothy?"</div>
</div>

<p class="disc-time">Turn to one person near you. Two minutes. Then we share back.</p>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 10 — KEY INSIGHT: CHRONIC CONDITION
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: dark-statement -->

*"This was not an acute collapse.*

*This was a **chronic condition** of the soul."*

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 11 — QR PULSE #2
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: poll -->

<div class="poll-header">
  <span class="poll-badge">QR Pulse #2</span>
  <span class="mentimeter-tag">Word Cloud</span>
</div>

## What do you think is the primary diagnosis for Demas?

<div class="poll-rule"></div>

<div class="poll-body">
  <div class="poll-left">
    <div class="poll-options">
      <div class="poll-option"><span class="opt-letter">A</span>Burnout and spiritual exhaustion</div>
      <div class="poll-option"><span class="opt-letter">B</span>Gradual distraction by success</div>
      <div class="poll-option"><span class="opt-letter">C</span>Loss of devotional discipline</div>
      <div class="poll-option"><span class="opt-letter">D</span>Misplaced love — loving a good thing too much</div>
    </div>
    <p class="poll-qr-note">Scan code or visit menti.com — word cloud displays live</p>
  </div>
  <div class="poll-qr-panel">
    <img src="mentimeter_qr_code.png" alt="Mentimeter QR Code" />
    <div class="qr-go">Go to</div>
    <div class="qr-url">menti.com</div>
    <div class="qr-code-num">3461 4656</div>
  </div>
</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 12 — ELLEN WHITE: ABSORBED IN BUSINESS
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: quote -->

<div class="quote-source">Ellen White &nbsp;·&nbsp; Testimonies for the Church, Vol. 5, p. 161</div>

> "Many are so absorbed in business that they have no time for prayer, no time for the study of the Bible… The cares of this life crowd out the things of eternity."

<div class="quote-attr">— Ellen G. White</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 13 — SECTION INTRO: CORE TENSION
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: section-intro -->

<div class="sec-number">The Core Tension</div>

# Good Work vs. First Love

<div class="sec-bar"></div>

Both truths are real. The tension is the point.

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 14 — TENSION: TWO STATEMENTS
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: tension -->

<div class="tension-label">Hold both of these at the same time</div>

<div class="tension-grid">
  <div class="tension-card card-a">
    <p>God calls us to meaningful work in the world.</p>
  </div>
  <div class="tension-card card-b">
    <p>The world can quietly replace God in our hearts.</p>
  </div>
</div>

<p class="tension-footnote">The tension between them is not a contradiction. It is the permanent condition of the Christian professional life.</p>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 15 — GREAT CONTROVERSY QUOTE
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: quote -->

<div class="quote-source">Ellen White &nbsp;·&nbsp; The Great Controversy, p. 508</div>

> "Satan works to distort the character of God — often making Him seem harsh or unloving — to distract humans, breaking their focus and preventing a close, personal relationship with Him."

<div class="quote-attr">— Ellen G. White</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 16 — SMALL GROUP DISCUSSION
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: discussion -->

<div class="disc-badge">Small Groups — 3 to 4 People — 4 Minutes</div>

## Two questions for your group:

<div class="disc-questions">
  <div class="disc-q">"How do you know when your work is still worship — and when it has become replacement?"</div>
  <div class="disc-q">"What does loving Christ practically look like in a busy professional life?"</div>
</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 17 — ADVENTIST STAKES
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: dark-statement -->

*"If the final crisis is about **worship and allegiance** —
not activity — then Demas is not a cautionary tale
about slacking off.*

*He is a cautionary tale about
what we **worship** while we work."*

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 18 — STEPS TO CHRIST QUOTE
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: quote -->

<div class="quote-source">Ellen White &nbsp;·&nbsp; Steps to Christ, p. 44</div>

> "It is not so much the fear of punishment, or the hope of everlasting reward, that leads the disciples of Christ to follow Him. They behold the Saviour's matchless love… and to them duty becomes a delight and sacrifice a pleasure."

<div class="quote-attr">— Ellen G. White</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 19 — SECTION INTRO: REORIENTATION
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: section-intro -->

<div class="sec-number">Biblical Reorientation</div>

# Christ at the Center

<div class="sec-bar"></div>

Two texts. Let them breathe.

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 20 — MATTHEW 6:21
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: scripture -->

<span class="ref-tag">Matthew 6:21</span>

> "For where your treasure is,
> there will your **heart** be also."

<p class="context-note">The heart follows what you value. The treasure reveals what you love.</p>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 21 — REVELATION 2:4
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: scripture -->

<span class="ref-tag">Revelation 2:4 — To the Church at Ephesus</span>

> "Nevertheless I have somewhat against thee,
> because thou hast **left thy first love.**"

<p class="context-note">A church that worked harder than any other. But the heart had moved.</p>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 22 — ACTS OF APOSTLES QUOTE
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: quote -->

<div class="quote-source">Ellen White &nbsp;·&nbsp; The Acts of the Apostles, p. 547</div>

> "The church of Ephesus had let slip her first love. She was more intent on carrying on the forms and ceremonies of religion than on possessing its spirit. She was more anxious to win the approval of men than to win the approval of God."

<div class="quote-attr">— Ellen G. White</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 23 — THE SABBATH: MAIN DECLARATION
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: gold-statement -->

*"The Sabbath is God's built-in resistance against becoming Demas."*

<div class="sub-note">Not a rule. A rescue.</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 24 — SABBATH REFRAME: INTERRUPTS / RECENTERS
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: sabbath -->

<div class="sabbath-tag">The Sabbath as Corrective</div>

## It interrupts. It recenters.

<div class="sabbath-not-rule">Not a rule. A rescue.</div>

<div class="sabbath-grid">
  <div class="s-col">
    <div class="s-col-label interrupts">It interrupts</div>
    <ul>
      <li>Identity through achievement</li>
      <li>Constant striving</li>
      <li>Replacement of God by good things</li>
    </ul>
  </div>
  <div class="s-col">
    <div class="s-col-label recenters">It recenters</div>
    <ul>
      <li>Relationship over performance</li>
      <li>Trust over productivity</li>
      <li>Devotion over deliverables</li>
    </ul>
  </div>
</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 25 — DEMAS KEPT WORKING
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: dark-statement -->

*"Demas kept working.*

*He lost the **Sabbath of the soul** first."*

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 26 — QR PULSE #3
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: poll-open -->

<span class="poll-badge">QR Pulse #3 — Open Response</span>

<div class="poll-open-row">
  <h2>"What is competing with Christ for your deepest affection right now?"</h2>
  <div class="poll-qr-panel">
    <img src="mentimeter_qr_code.png" alt="Mentimeter QR Code" />
    <div class="qr-go">Go to</div>
    <div class="qr-url">menti.com</div>
    <div class="qr-code-num">3461 4656</div>
  </div>
</div>

<div class="poll-sub">Your answer is anonymous — word cloud displays live</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 27 — CLOSER TO DEMAS
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: anchor -->

<div class="anchor-label">After the word cloud</div>

> "I think what we're seeing here…
> is that we are all **closer to Demas**
> than we thought."

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 28 — PRIVATE REFLECTION
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: reflection -->

<span class="ref-badge">Private Reflection — 2 Minutes — Not for Sharing</span>

## "What would it look like to choose Christ first this week? Not in general. **This week.**"

<p class="ref-note">On your phone or a piece of paper — answer this for yourself and God only.</p>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 29 — LINGERING QUESTION
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: lingering -->

<div class="ling-pre">Before we close — a question to carry home:</div>

## "If someone wrote one sentence about your spiritual life five years from now — would it sound more like Colossians… or 2 Timothy?"

<div class="ling-verse-a">Colossians 4:14 — co-laborer, present, trusted</div>
<div class="ling-verse-b">2 Timothy 4:10 — having loved this present world</div>

---

<!-- ═══════════════════════════════════════════════════════════════════════
     SLIDE 30 — CLOSING
     ══════════════════════════════════════════════════════════════════════ -->
<!-- _class: title -->

<div class="event-tag">Atlanta North Vespers</div>

# Demas and the Drift

<div class="subtitle">*Close in prayer. Not for success. Not for productivity. For reordered love.*</div>

<div class="divider-gold"></div>

<div class="subtitle" style="font-size:0.88rem; opacity:0.4; font-style:normal; letter-spacing:0.08em;">Chukwuma Onyeije &nbsp;·&nbsp; chukwumaonyeije.github.io/chukwuma-theology</div>
