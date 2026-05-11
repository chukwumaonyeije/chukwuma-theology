---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: The Text and the Canon of Scripture
description: A Chukwuma Theology elder-study presentation on Gerald A. Klingbeil's chapter on canon, textual transmission, and Scripture's authority.
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --primary: #2d4739;
  --primary-deep: #172d24;
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

h1 { font-size: 2.85rem; }
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
  content: '-';
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

section.anchor,
section.statement {
  text-align: center;
  align-items: center;
  background: var(--primary-deep);
  padding: 48px 106px;
}

section.anchor blockquote,
section.statement .statement,
section.gold .statement,
section.closing .statement {
  font-family: 'Playfair Display', serif;
}

section.anchor blockquote {
  font-size: 2.06rem;
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
  max-width: 790px;
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
  font-size: 2.06rem;
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

# The Text and the Canon of Scripture

<div class="subtitle">Gerald A. Klingbeil, the church under the Word, and the question of a preserved canon</div>

<div class="accent-line" style="margin:1.1rem auto 1rem auto;"></div>

<p>Why the Bible's authority depends on God speaking, not the church granting permission.</p>

<div class="deck-credit">Prepared for Chukwuma Theology · Chukwuma I. Onyeije, MD, FACOG</div>

---

<!-- _class: anchor -->

<div class="eyebrow">The controlling issue</div>

> "Canonization is not the church creating divine authority. It is the church recognizing the authority God has already placed in His Word."

<p class="context-note">The church does not stand over Scripture with a stamp. The church stands under Scripture with open ears.</p>

---

<!-- _class: scripture -->

<div class="eyebrow">The biblical claim</div>

<div class="two-note">
  <div class="panel">
    <h3>2 Timothy 3:16</h3>
    <p><strong>All Scripture is God-breathed</strong> and therefore useful for doctrine, correction, and formation.</p>
  </div>
  <div class="panel">
    <h3>2 Peter 1:20-21</h3>
    <p>Prophets did not speak from private impulse. They spoke as they were <strong>moved by the Holy Spirit</strong>.</p>
  </div>
</div>

<p class="context-note">For Klingbeil, canon, inspiration, transmission, and interpretation belong in the same theological conversation.</p>

---

<!-- _class: section-intro -->

<div class="section-kicker">Start Here</div>

# Canon Is a Question of Authority

<div class="accent-line" style="margin:0.7rem auto 1rem auto;"></div>

<p class="section-note">The word canon points to a measuring rod. Scripture becomes the measure for faith and practice because it is God-breathed, not because religious leaders later made it powerful.</p>

---

<div class="eyebrow">A diagnostic distinction</div>

## Two very different accounts of the Bible's authority

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Recognition</h3>
    <p>The believing community receives writings that already bear divine authority because God has spoken through prophets and apostles.</p>
  </div>
  <div class="card alt">
    <h3>Creation</h3>
    <p>The community, council, or tradition grants authority to certain writings by ecclesiastical decision.</p>
  </div>
</div>

<p class="context-note">Adventist theology depends on the first account. Scripture judges the church; the church does not judge Scripture.</p>

---

<!-- _class: statement -->

<div class="statement">"The church is healthiest when its authority is most visibly submitted to the written Word."</div>

<div class="sub-note">That is not weakness. That is the proper posture of the people of God.</div>

---

<div class="eyebrow">The Old Testament canon</div>

## Jesus treated the Hebrew Scriptures as settled authority

<div class="accent-line"></div>

<div class="grid three">
  <div class="card">
    <h3>Law</h3>
    <p>The Torah formed Israel's covenant memory and moral center.</p>
  </div>
  <div class="card alt">
    <h3>Prophets</h3>
    <p>The prophets carried God's covenant lawsuit, warning, hope, and historical interpretation.</p>
  </div>
  <div class="card">
    <h3>Writings</h3>
    <p>The Writings preserved worship, wisdom, lament, history, and apocalyptic expectation.</p>
  </div>
</div>

<p class="context-note">Jesus' repeated "It is written" shows Scripture functioning as decisive authority, not devotional ornament.</p>

---

<div class="eyebrow">The New Testament canon</div>

## The church gathered around apostolic witness to Christ

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>What gave authority</h3>
    <ul>
      <li>Apostolic witness</li>
      <li>Faithful testimony to Jesus</li>
      <li>Spirit-given authority</li>
      <li>Continuity with the Old Testament</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>What councils did</h3>
    <ul>
      <li>They did not make books inspired</li>
      <li>They ratified what the church had already received</li>
      <li>They clarified boundaries against confusion</li>
      <li>They gave public recognition to an existing reality</li>
    </ul>
  </div>
</div>

---

<!-- _class: gold -->

<div class="statement">"History matters, but history does not outrank inspiration."</div>

<p>The canon is historically recognized because Scripture is theologically given.</p>

---

<div class="eyebrow">Protestant and Catholic canons</div>

## The Apocrypha question is not merely a footnote

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>The historical issue</h3>
    <p>The deuterocanonical books were not part of the Hebrew canon and were not used by New Testament writers as inspired Scripture.</p>
  </div>
  <div class="card alt">
    <h3>The theological issue</h3>
    <p>Some teachings connected to these books conflict with biblical anthropology, death, judgment, and salvation.</p>
  </div>
</div>

<p class="context-note">The deeper question: does tradition expand Scripture, or does Scripture judge tradition?</p>

---

<div class="eyebrow">An Adventist concern</div>

## Canon affects doctrine

<div class="accent-line"></div>

<div class="application-list">
  <div class="app-item">
    <span class="label">Death</span>
    <p>Adventist anthropology resists the idea of an inherently immortal soul.</p>
  </div>
  <div class="app-item">
    <span class="label">Judgment</span>
    <p>Scripture, not postbiblical speculation, must govern how we speak of judgment and hope.</p>
  </div>
  <div class="app-item">
    <span class="label">Salvation</span>
    <p>The gospel cannot be supplemented by a tradition that Scripture itself does not authorize.</p>
  </div>
  <div class="app-item">
    <span class="label">Authority</span>
    <p>The final norm is the whole biblical canon, not ecclesiastical habit or inherited preference.</p>
  </div>
</div>

---

<div class="eyebrow">A subtle danger</div>

## Rejecting the "canon within the canon"

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>What it sounds like</h3>
    <p>Some books, themes, or passages become functionally more inspired because they fit our preferred theological center.</p>
  </div>
  <div class="card alt">
    <h3>Why it matters</h3>
    <p>The interpreter becomes the measuring rod. Scripture is no longer the canon; our selected emphasis is.</p>
  </div>
</div>

<p class="context-note">The whole Bible must be allowed to speak, even when some books play a larger role in specific doctrines.</p>

---

<!-- _class: statement -->

<div class="statement">"Different functions in Scripture do not require different levels of inspiration."</div>

<div class="sub-note">Genesis, Daniel, Romans, Hebrews, and Revelation may carry special doctrinal weight for Adventists, but they are not more inspired than Ruth, Mark, James, or Philemon.</div>

---

<div class="eyebrow">Textual criticism</div>

## A servant of faith, not an enemy of faith

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>The honest admission</h3>
    <ul>
      <li>Scripture was copied by hand for centuries</li>
      <li>Minor variants and copyist errors exist</li>
      <li>Most questions concern names, numbers, or places</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>The mature confidence</h3>
    <ul>
      <li>Doctrines do not collapse under manuscript variation</li>
      <li>The Bible is exceptionally well attested</li>
      <li>Textual study helps recover the most reliable wording</li>
    </ul>
  </div>
</div>

---

<!-- _class: gold -->

<div class="statement">"God preserved the message of Scripture without requiring us to pretend every copyist was miraculously protected from every minor error."</div>

<p>This is confidence without brittleness.</p>

---

<div class="eyebrow">Translations and study aids</div>

## Useful tools require wise readers

<div class="accent-line"></div>

<div class="application-list">
  <div class="app-item">
    <span class="label">Compare translations</span>
    <p>Every translation makes choices. Comparing reliable translations exposes those choices.</p>
  </div>
  <div class="app-item">
    <span class="label">Respect genre</span>
    <p>Doctrine should not be built on a paraphrase, a loose rendering, or an isolated phrase.</p>
  </div>
  <div class="app-item">
    <span class="label">Use scholarship</span>
    <p>Manuscripts, lexicons, commentaries, and dictionaries can serve the church when Scripture remains supreme.</p>
  </div>
  <div class="app-item">
    <span class="label">Stay under the Spirit</span>
    <p>Tools are not a substitute for reverence, prayer, humility, and obedience.</p>
  </div>
</div>

---

<div class="eyebrow">A needed Adventist clarification</div>

## Ellen White and the closed canon

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>What Adventists affirm</h3>
    <p>The Spirit of Prophecy is a genuine gift to the remnant church and must be received seriously.</p>
  </div>
  <div class="card alt">
    <h3>What Adventists do not claim</h3>
    <p>Ellen White's writings do not become part of the biblical canon. They point back to Scripture rather than adding a new canonical rule.</p>
  </div>
</div>

<p class="context-note">A prophetic gift can be real without becoming canonical Scripture.</p>

---

<!-- _class: application -->

<div class="eyebrow">Implications for elders</div>

## How this should change our leadership

<div class="accent-line"></div>

<div class="application-list">
  <div class="app-item">
    <span class="label">Preaching</span>
    <p>Let the text govern the sermon rather than using Scripture as a decorative launchpad.</p>
  </div>
  <div class="app-item">
    <span class="label">Teaching</span>
    <p>Explain why the Bible can be trusted without flattening its history or human texture.</p>
  </div>
  <div class="app-item">
    <span class="label">Counseling</span>
    <p>Bring people under the Word with patience, not personal preference dressed up as authority.</p>
  </div>
  <div class="app-item">
    <span class="label">Church life</span>
    <p>Test tradition, culture, denominational habit, and personality by Scripture's total witness.</p>
  </div>
</div>

---

<!-- _class: discussion -->

<div class="eyebrow">Reading group discussion</div>

## Four questions worth carrying into the room

<div class="question-box">
  <div class="question">Where are we most tempted to let tradition, personality, or culture function as canon?</div>
  <div class="question">What parts of Scripture do we quietly treat as less authoritative because they are less useful to our preferred emphasis?</div>
  <div class="question">How can elders teach textual criticism in a way that builds confidence instead of anxiety?</div>
  <div class="question">How do we honor Ellen White while keeping the Bible as the only canonical rule of faith and doctrine?</div>
</div>

---

<!-- _class: closing -->

<div class="eyebrow">Closing burden</div>

<div class="statement">"The Bible is not an ancient religious library waiting for the church to authorize it.<br><br>It is the preserved Word of God, given to measure the people of God."</div>

<p class="closing-note">The question is not whether we admire Scripture. The question is whether our preaching, teaching, doctrine, and church life still sit under its authority.</p>
