---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: Revelation and Inspiration
description: A Chukwuma Theology elder-study presentation on Fernando Canale's doctrine of revelation and inspiration.
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --primary: #2d4739;
  --primary-deep: #1a2f26;
  --secondary: #c26d4b;
  --accent: #d4af37;
  --bg-dark: #1a2f26;
  --bg-deeper: #102018;
  --bg-light: #f5f0e8;
  --text-light: #f4efe7;
  --text-dim: rgba(255,255,255,0.72);
  --text-dark: #1f1f1f;
  --border: rgba(255,255,255,0.16);
}

section {
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  background: var(--bg-dark);
  color: var(--text-light);
  padding: 48px 72px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

section::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, var(--accent), var(--secondary), var(--accent));
}

h1,
h2,
h3 {
  font-family: 'Playfair Display', serif;
  margin: 0 0 0.2em 0;
  color: var(--text-light);
  line-height: 1.18;
}

h1 { font-size: 2.9rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.3rem; font-style: italic; }

p {
  font-size: 1rem;
  line-height: 1.6;
  margin: 0.2em 0 0.5em 0;
  color: var(--text-light);
}

ul {
  list-style: none;
  padding: 0;
  margin: 0.4em 0 0 0;
}

li {
  position: relative;
  padding: 0.22em 0 0.22em 1.3em;
  line-height: 1.5;
}

li::before {
  content: '—';
  position: absolute;
  left: 0;
  color: var(--accent);
  font-weight: 700;
}

strong { color: var(--accent); }
em { color: var(--secondary); }

.eyebrow {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.8rem;
}

.accent-line {
  width: 58px;
  height: 3px;
  background: var(--accent);
  margin: 0.45rem 0 1rem 0;
}

.subtitle {
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
  font-style: italic;
  color: rgba(255,255,255,0.68);
}

.deck-credit {
  font-size: 0.86rem;
  color: rgba(255,255,255,0.46);
  letter-spacing: 0.08em;
  margin-top: 0.9rem;
}

section.title {
  text-align: center;
  align-items: center;
  padding: 48px 104px;
  background:
    radial-gradient(circle at 20% 80%, rgba(212,175,55,0.15), transparent 30%),
    radial-gradient(circle at 80% 20%, rgba(194,109,75,0.12), transparent 28%),
    var(--bg-dark);
}

section.anchor {
  text-align: center;
  align-items: center;
  background: var(--primary-deep);
  padding: 48px 112px;
}

section.anchor blockquote,
section.scripture blockquote,
section.statement .statement,
section.gold .statement,
section.closing .statement {
  font-family: 'Playfair Display', serif;
}

section.anchor blockquote {
  font-size: 2.1rem;
  line-height: 1.45;
  border: none;
  margin: 0;
  padding: 0;
  font-style: italic;
}

section.scripture {
  background: var(--bg-deeper);
  padding: 54px 86px;
}

section.scripture blockquote {
  font-size: 1.65rem;
  line-height: 1.5;
  border-left: 5px solid var(--accent);
  padding-left: 24px;
  margin: 0.25em 0 0.6em 0;
  font-style: italic;
}

.context-note {
  font-size: 0.92rem;
  color: var(--text-dim);
  font-style: italic;
}

section.section-intro {
  background: linear-gradient(140deg, var(--primary-deep), var(--bg-dark));
  align-items: center;
  text-align: center;
  padding: 48px 104px;
}

.section-kicker {
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.7rem;
}

.section-note {
  max-width: 760px;
  color: var(--text-dim);
}

.grid {
  display: grid;
  gap: 18px;
  width: 100%;
  margin-top: 0.6rem;
}

.grid.two { grid-template-columns: 1fr 1fr; }
.grid.three { grid-template-columns: 1fr 1fr 1fr; }

.card {
  background: rgba(255,255,255,0.07);
  border: 1px solid var(--border);
  border-top: 4px solid var(--accent);
  border-radius: 12px;
  padding: 20px 22px;
}

.card.alt {
  border-top-color: var(--secondary);
  background: rgba(194,109,75,0.11);
}

.card h3 {
  font-family: 'Inter', sans-serif;
  font-size: 0.86rem;
  font-style: normal;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.75rem;
}

.card.alt h3 { color: #f0b39b; }

.card p,
.card li {
  font-size: 0.92rem;
  color: var(--text-light);
}

.two-note {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  width: 100%;
  margin-top: 0.8rem;
}

.panel {
  background: rgba(255,255,255,0.06);
  border-radius: 12px;
  border-left: 4px solid var(--accent);
  padding: 18px 20px;
}

.panel h3 {
  font-family: 'Inter', sans-serif;
  font-size: 0.8rem;
  font-style: normal;
  font-weight: 800;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.7rem;
}

.panel p,
.panel li {
  font-size: 0.92rem;
}

section.statement {
  background: var(--primary-deep);
  align-items: center;
  text-align: center;
  padding: 48px 96px;
}

section.statement .statement {
  font-size: 2.02rem;
  line-height: 1.5;
  font-style: italic;
}

section.statement .sub-note {
  font-size: 0.88rem;
  color: var(--text-dim);
  margin-top: 1.2rem;
}

section.gold {
  background: var(--accent);
  align-items: center;
  text-align: center;
  padding: 48px 96px;
  color: var(--primary-deep);
}

section.gold::after { background: var(--primary-deep); }

section.gold h1,
section.gold h2,
section.gold p,
section.gold .statement {
  color: var(--primary-deep);
}

section.gold .statement {
  font-size: 2.12rem;
  line-height: 1.45;
  font-style: italic;
  font-weight: 700;
}

section.application {
  justify-content: flex-start;
  padding-top: 42px;
}

.application-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 18px;
  width: 100%;
  margin-top: 0.8rem;
}

.app-item {
  background: rgba(255,255,255,0.07);
  border-radius: 10px;
  padding: 16px 18px;
  border-left: 4px solid var(--accent);
}

.app-item .label {
  display: block;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.5rem;
}

.app-item p {
  font-size: 0.92rem;
  margin: 0;
}

section.discussion {
  justify-content: flex-start;
  padding-top: 40px;
}

.question-box {
  width: 100%;
  margin-top: 0.8rem;
}

.question {
  background: rgba(255,255,255,0.07);
  border-left: 4px solid var(--accent);
  border-radius: 0 10px 10px 0;
  padding: 16px 20px;
  margin-bottom: 12px;
  font-family: 'Playfair Display', serif;
  font-size: 1.02rem;
  line-height: 1.5;
  font-style: italic;
}

section.closing {
  text-align: center;
  align-items: center;
  padding: 48px 110px;
  background: linear-gradient(145deg, var(--primary-deep), var(--bg-dark));
}

section.closing .statement {
  font-size: 2rem;
  line-height: 1.5;
  font-style: italic;
}

.closing-note {
  max-width: 820px;
  margin-top: 1rem;
  color: var(--text-dim);
}
</style>

<!-- _class: title -->

<div class="eyebrow">Atlanta North Elders' Reading Group</div>

# Revelation and Inspiration

<div class="subtitle">Fernando Canale, Scripture, and the question beneath all interpretation</div>

<div class="accent-line" style="margin:1.1rem auto 1rem auto;"></div>

<p>Why our doctrine of Scripture determines how we read, preach, teach, and defend the Bible.</p>

<div class="deck-credit">Prepared for Chukwuma Theology · Chukwuma I. Onyeije, MD, FACOG</div>

---

<!-- _class: anchor -->

<div class="eyebrow">The controlling issue</div>

> "Before inspiration is a doctrinal debate, it is a **hermeneutical decision**."

<p class="context-note">How we answer "What is the Bible?" determines how we handle every text that follows.</p>

---

<!-- _class: scripture -->

<div class="eyebrow">Biblical foundation</div>

<div class="two-note">
  <div class="panel">
    <h3>2 Timothy 3:16</h3>
    <p><strong>All scripture is given by inspiration of God</strong> — God-breathed, not merely religious reflection.</p>
  </div>
  <div class="panel">
    <h3>2 Peter 1:20-21</h3>
    <p>Holy men <strong>spake as they were moved by the Holy Ghost</strong> — genuinely human speakers, but not self-originating ones.</p>
  </div>
</div>

<p class="context-note">Canale's balance: the Bible is fully divine in origin and fully human in expression.</p>

---

<!-- _class: section-intro -->

<div class="section-kicker">The Diagnostic Work</div>

# Three Inadequate Models

<div class="accent-line" style="margin:0.7rem auto 1rem auto;"></div>

<p class="section-note">Canale's argument is not that every model gets everything wrong. It is that each one distorts something essential about Scripture.</p>

---

<div class="eyebrow">Where the models fail</div>

<div class="grid three">
  <div class="card">
    <h3>Verbal Inspiration</h3>
    <p>Protects authority, but can flatten prophets into passive instruments and ignore genre, history, and authorial personality.</p>
  </div>
  <div class="card alt">
    <h3>Encounter Revelation</h3>
    <p>Protects relationship, but reduces Scripture to witness about God instead of reliable communication from God.</p>
  </div>
  <div class="card">
    <h3>Radical Thought Inspiration</h3>
    <p>Rejects dictation, but becomes dangerous when inspired ideas are detached from the actual words we possess.</p>
  </div>
</div>

---

<!-- _class: statement -->

<div class="statement">"Adventism cannot afford a Bible that is either <strong>mechanically dictated</strong> or <strong>merely human</strong>."</div>

<div class="sub-note">The first collapses the human texture of Scripture. The second dissolves its authority.</div>

---

<div class="eyebrow">A necessary distinction</div>

## Revelation and inspiration are distinguishable, but inseparable

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Revelation</h3>
    <p>How the content comes to the prophet or apostle: vision, speech, history, wisdom, memory, research, lived encounter.</p>
  </div>
  <div class="card alt">
    <h3>Inspiration</h3>
    <p>How that content is faithfully communicated: orally, textually, historically, and providentially under the Spirit's guidance.</p>
  </div>
</div>

<p class="context-note">God gives the message, and God also guides its communication.</p>

---

<div class="eyebrow">Canale's crucial warning</div>

## We must take both the doctrine and the phenomena of Scripture seriously

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Doctrine of Scripture</h3>
    <ul>
      <li>God-breathed</li>
      <li>Prophetic</li>
      <li>Truthful and authoritative</li>
      <li>Given for the church</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>Phenomena of Scripture</h3>
    <ul>
      <li>Different genres and voices</li>
      <li>Historical settings and literary methods</li>
      <li>Distinct personalities and styles</li>
      <li>Real human texture without loss of divine authority</li>
    </ul>
  </div>
</div>

---

<!-- _class: gold -->

<div class="statement">"If the thoughts are inspired but the words are unreliable, then the church has no reliable access to the inspired thoughts."</div>

<p>The Spirit did not bypass human language. He used it.</p>

---

<div class="eyebrow">Canale's positive model</div>

## A biblical model of revelation-inspiration

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>How God works</h3>
    <ul>
      <li>Personally and historically</li>
      <li>Without erasing human freedom</li>
      <li>Through language, memory, research, and literary skill</li>
      <li>Across prophecy, wisdom, history, poetry, and apocalypse</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>What the church receives</h3>
    <ul>
      <li>A reliable written revelation</li>
      <li>Truth in human language</li>
      <li>Authority without dictation theory</li>
      <li>Trustworthiness without brittle perfectionism</li>
    </ul>
  </div>
</div>

---

<!-- _class: statement -->

<div class="statement">"The Bible is not a transcript dropped from heaven.<br><br>It is God's trustworthy word, given in history, through human beings, for the salvation of His people."</div>

<div class="sub-note">That is why apparent variations do not destroy Scripture's reliability. God did not promise a lab manual. He gave a saving revelation.</div>

---

<div class="eyebrow">Why this fits Adventism</div>

## The model harmonizes with our strongest theological instincts

<div class="accent-line"></div>

<div class="application-list">
  <div class="app-item">
    <span class="label">Authority</span>
    <p>Scripture remains the church's supreme written authority, not a negotiable witness among other witnesses.</p>
  </div>
  <div class="app-item">
    <span class="label">Humanity</span>
    <p>The Bible's human features are not defects. They are part of God's chosen method.</p>
  </div>
  <div class="app-item">
    <span class="label">Great Controversy</span>
    <p>God reveals Himself in history, covenant, incarnation, judgment, and restoration rather than outside history in abstraction.</p>
  </div>
  <div class="app-item">
    <span class="label">Mature confidence</span>
    <p>We need not choose between rigid fundamentalism and critical reductionism.</p>
  </div>
</div>

---

<!-- _class: application -->

<div class="eyebrow">Implications for elders</div>

## How this should change our teaching

<div class="accent-line"></div>

<div class="application-list">
  <div class="app-item">
    <span class="label">When preaching</span>
    <p>Take genre, authorial purpose, and historical setting seriously without surrendering authority.</p>
  </div>
  <div class="app-item">
    <span class="label">When teaching</span>
    <p>Avoid implying either dictation theory or the idea that only vague religious ideas matter.</p>
  </div>
  <div class="app-item">
    <span class="label">When answering skeptics</span>
    <p>Acknowledge the Bible's human features without conceding unreliability.</p>
  </div>
  <div class="app-item">
    <span class="label">When handling Ellen White</span>
    <p>Use her writings as a serious Adventist conversation partner, not as a flattened slogan.</p>
  </div>
</div>

---

<!-- _class: discussion -->

<div class="eyebrow">Reading group discussion</div>

## Four questions worth carrying into the room

<div class="question-box">
  <div class="question">Which model of inspiration did most of us inherit without ever naming it?</div>
  <div class="question">How do we defend full trustworthiness without retreating into dictation theory?</div>
  <div class="question">What changes when we say that God reveals Himself <strong>in history</strong> rather than outside it?</div>
  <div class="question">How should this reshape the way we teach difficult passages, apparent discrepancies, and distinctive Adventist doctrines?</div>
</div>

---

<!-- _class: closing -->

<div class="eyebrow">Closing burden</div>

<div class="statement">"Our doctrine of inspiration is never abstract for long.<br><br>It becomes the way we read the text, the way we preach the gospel, and the way we teach the church to trust the voice of God."</div>

<p class="closing-note">The question is not simply whether we affirm revelation and inspiration. The question is whether our hermeneutics actually behaves as though Scripture is God's reliable written word.</p>
