---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: "Elements of Biblical Hermeneutics"
description: "A Chukwuma Theology presentation on Frank M. Hasel's chapter, Elements of Biblical Hermeneutics in Harmony with Scripture's Self-Claims."
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
  --text-light: #f4efe7;
  --text-dim: rgba(255,255,255,0.72);
  --border: rgba(255,255,255,0.16);
}

section {
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  letter-spacing: normal;
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

h1, h2, h3 {
  font-family: 'Playfair Display', serif;
  margin: 0 0 0.2em 0;
  color: var(--text-light);
  line-height: 1.18;
}

h1 { font-size: 2.78rem; }
h2 { font-size: 1.96rem; }
h3 { font-size: 1.24rem; font-style: italic; }

p {
  font-size: 1rem;
  line-height: 1.55;
  margin: 0.2em 0 0.5em 0;
  color: var(--text-light);
}

ul {
  list-style: none;
  padding: 0;
  margin: 0.35em 0 0 0;
}

li {
  position: relative;
  padding: 0.2em 0 0.2em 1.3em;
  line-height: 1.48;
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
  max-width: 930px;
  font-family: 'Playfair Display', serif;
  font-size: 1.22rem;
  line-height: 1.52;
  font-style: italic;
  color: var(--text-dim);
}

.deck-credit {
  font-size: 0.82rem;
  color: rgba(255,255,255,0.48);
  letter-spacing: 0.07em;
  margin-top: 1rem;
}

section.title {
  text-align: center;
  align-items: center;
  padding: 48px 96px;
  background:
    radial-gradient(circle at 18% 84%, rgba(212,175,55,0.17), transparent 31%),
    radial-gradient(circle at 83% 18%, rgba(194,109,75,0.13), transparent 29%),
    var(--bg-dark);
}

section.anchor,
section.statement {
  text-align: center;
  align-items: center;
  background: var(--primary-deep);
  padding: 48px 104px;
}

section.anchor blockquote,
section.statement .statement,
section.gold .statement,
section.closing .statement {
  font-family: 'Playfair Display', serif;
}

section.anchor blockquote {
  font-size: 2.04rem;
  line-height: 1.45;
  border: none;
  margin: 0;
  padding: 0;
  font-style: italic;
}

section.anchor blockquote p {
  font-size: 2.04rem;
  line-height: 1.45;
}

.context-note {
  font-size: 0.91rem;
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
  max-width: 850px;
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
  font-size: 0.84rem;
  font-style: normal;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.7rem;
}

.card.alt h3 { color: #f0b39b; }
.card p, .card li { font-size: 0.9rem; }

.principles {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  width: 100%;
  margin-top: 0.8rem;
}

.principle {
  min-height: 132px;
  padding: 18px 14px;
  border-top: 3px solid var(--accent);
  background: rgba(255,255,255,0.06);
}

.principle .label {
  display: block;
  font-size: 0.69rem;
  font-weight: 800;
  color: var(--accent);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 0.55rem;
}

.principle p {
  font-size: 0.78rem;
  line-height: 1.45;
}

section.gold {
  background: var(--accent);
  align-items: center;
  text-align: center;
  padding: 48px 96px;
  color: var(--primary-deep);
}

section.gold::after { background: var(--primary-deep); }
section.gold p, section.gold .statement { color: var(--primary-deep); }

section.gold .statement {
  font-size: 2.04rem;
  line-height: 1.45;
  font-style: italic;
  font-weight: 700;
}

.stack {
  display: grid;
  grid-template-columns: 1fr;
  gap: 13px;
  width: 100%;
  margin-top: 0.55rem;
}

.rung {
  display: grid;
  grid-template-columns: 210px 1fr;
  gap: 18px;
  align-items: center;
  background: rgba(255,255,255,0.07);
  border-left: 4px solid var(--accent);
  padding: 14px 18px;
}

.rung .label {
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--accent);
}

.rung p {
  font-size: 0.9rem;
  margin: 0;
}

.process {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  width: 100%;
  margin-top: 0.85rem;
}

.process-step {
  min-height: 148px;
  background: rgba(255,255,255,0.07);
  border-top: 4px solid var(--accent);
  padding: 18px 15px;
}

.process-step .label {
  display: block;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.55rem;
}

.process-step p {
  font-size: 0.8rem;
  line-height: 1.45;
  margin: 0;
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
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.45rem;
}

.app-item p { font-size: 0.9rem; margin: 0; }

section.discussion {
  justify-content: flex-start;
  padding-top: 40px;
}

.question {
  background: rgba(255,255,255,0.07);
  border-left: 4px solid var(--accent);
  border-radius: 0 10px 10px 0;
  padding: 15px 20px;
  margin: 11px 0;
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  line-height: 1.48;
  font-style: italic;
}

section.closing {
  text-align: center;
  align-items: center;
  padding: 48px 108px;
  background: linear-gradient(145deg, var(--primary-deep), var(--bg-dark));
}

section.closing .statement {
  font-size: 2rem;
  line-height: 1.48;
  font-style: italic;
}

.closing-note {
  max-width: 860px;
  margin-top: 1rem;
  color: var(--text-dim);
}
</style>

<!-- _class: title -->

<div class="eyebrow">Biblical Hermeneutics Study Series | Chapter 2</div>

# Elements of Biblical<br>Hermeneutics

<div class="subtitle">In harmony with Scripture's self-claims: how the nature of the Bible determines the way the church reads the Bible.</div>

<div class="accent-line" style="margin:1.1rem auto 0.95rem auto;"></div>

<div class="deck-credit">Based on Frank M. Hasel, "Elements of Biblical Hermeneutics in Harmony with Scripture's Self-Claims" | Chukwuma Theology</div>

---

<!-- _class: anchor -->

<div class="eyebrow">The controlling question</div>

> "Do we choose a method first, then force Scripture to fit it, or do we let Scripture's own nature teach us how it must be read?"

<p class="context-note">Hermeneutics begins before interpretation. It begins with what we believe the Bible is.</p>

---

<div class="eyebrow">Why this chapter matters</div>

## Every method is determined by its object

<div class="accent-line"></div>

<div class="grid three">
  <div class="card">
    <h3>The Object</h3>
    <p>Scripture is not merely an ancient religious artifact. It claims to be God's written Word in human language.</p>
  </div>
  <div class="card alt">
    <h3>The Method</h3>
    <p>The Bible should not be studied by assumptions that deny the kind of reality Scripture itself presents.</p>
  </div>
  <div class="card">
    <h3>The Reader</h3>
    <p>The faithful interpreter comes ready to be corrected by the Word, not merely to control it.</p>
  </div>
</div>

---

<!-- _class: section-intro -->

<div class="section-kicker">Foundation One</div>

# Scripture's Self-Claims Matter

<div class="accent-line" style="margin:0.7rem auto 1rem auto;"></div>

<p class="section-note">Hasel begins with the premise that the Bible must be interpreted in harmony with what Scripture says about itself: its divine source, its human form, its authority, and its purpose.</p>

---

<div class="eyebrow">No blank minds</div>

## Presuppositions are unavoidable, but they are not untouchable

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>The honest admission</h3>
    <ul>
      <li>No one studies Scripture with a blank mind</li>
      <li>Sin shapes even our best intentions</li>
      <li>Presuppositionless exegesis is self-deception</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>The hopeful correction</h3>
    <ul>
      <li>God can challenge distorted assumptions</li>
      <li>The written Word corrects the reader</li>
      <li>Faithful interpretation remains possible</li>
    </ul>
  </div>
</div>

<p class="context-note">The goal is not neutrality. The goal is conversion of the reader's assumptions under Scripture.</p>

---

<div class="eyebrow">Jesus and the apostles</div>

## The Bible's authority is not an abstract doctrine

<div class="accent-line"></div>

<div class="stack">
  <div class="rung">
    <span class="label">Jesus</span>
    <p>He searched, obeyed, fulfilled, and appealed to Scripture as the Word that cannot be broken.</p>
  </div>
  <div class="rung">
    <span class="label">The Apostles</span>
    <p>They treated Scripture as God-breathed, profitable, hope-giving, and normative for teaching and correction.</p>
  </div>
  <div class="rung">
    <span class="label">The Church</span>
    <p>The apostolic community devoted itself to the apostles' teaching and tested claims by the written Word.</p>
  </div>
</div>

---

<div class="eyebrow">Canon and covenant</div>

## Written revelation preserves God's address

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Old Testament Witness</h3>
    <p>God's covenant words are proclaimed, written, preserved, and passed on to rule and direct His people.</p>
  </div>
  <div class="card alt">
    <h3>New Testament Witness</h3>
    <p>Jesus and the apostles use the Old Testament canon normatively, while apostolic writings come to carry comparable authority.</p>
  </div>
</div>

<p class="context-note">The recurring logic is simple and searching: what Scripture says, God says.</p>

---

<!-- _class: gold -->

<div class="statement">If Scripture is God's Word in human words, then interpretation is never merely technical.</div>

<p>It is an encounter with the God who speaks.</p>

---

<!-- _class: section-intro -->

<div class="section-kicker">Foundation Two</div>

# The Divine-Human Bible

<div class="accent-line" style="margin:0.7rem auto 1rem auto;"></div>

<p class="section-note">Scripture is neither a merely human religious record nor a heavenly message detached from history. It is divine revelation communicated through real human language, authors, settings, and literary forms.</p>

---

<div class="eyebrow">The Christological analogy</div>

## The Word made flesh and the Word written

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>The Parallel</h3>
    <p>As Christ's divine glory came in true humanity, Scripture's divine message comes in true human language.</p>
  </div>
  <div class="card alt">
    <h3>The Caution</h3>
    <p>The Bible is not the incarnation. We are saved by Christ, yet we know Christ savingly through the written Word.</p>
  </div>
</div>

<p class="context-note">The human form of Scripture is not an argument against faith. It is the form God chose for address.</p>

---

<div class="eyebrow">Why a written Word?</div>

## God makes His message accessible across time

<div class="accent-line"></div>

<div class="principles">
  <div class="principle">
    <span class="label">Reference</span>
    <p>A stable point for covenant memory and obedience.</p>
  </div>
  <div class="principle">
    <span class="label">Preservation</span>
    <p>Protection against forgetfulness, corruption, and drift.</p>
  </div>
  <div class="principle">
    <span class="label">Transmission</span>
    <p>A message copied, multiplied, and carried beyond one place.</p>
  </div>
  <div class="principle">
    <span class="label">Continuity</span>
    <p>A norm available to later generations of readers.</p>
  </div>
  <div class="principle">
    <span class="label">Correction</span>
    <p>A standard by which teaching and experience are tested.</p>
  </div>
</div>

---

<div class="eyebrow">Interpretive consequence</div>

## We reject methods that silence Scripture's own worldview

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Not naturalism</h3>
    <p>A method that reads as if God does not exist cannot do justice to a text that repeatedly claims God speaks and acts.</p>
  </div>
  <div class="card alt">
    <h3>Not anti-history</h3>
    <p>A faithful method still attends carefully to language, culture, context, genre, and historical setting.</p>
  </div>
</div>

<p class="context-note">Adventist interpretation takes both realities seriously: God acts in history, and Scripture comes through history.</p>

---

<!-- _class: section-intro -->

<div class="section-kicker">The Method</div>

# Historical-Grammatical Care

<div class="accent-line" style="margin:0.7rem auto 1rem auto;"></div>

<p class="section-note">Because God has spoken in words, faithful readers attend to the words. Because those words came in history, faithful readers attend to context. Because the whole canon is God's Word, faithful readers read Scripture with Scripture.</p>

---

<div class="eyebrow">Literary meaning</div>

## The text itself must govern the interpretation

<div class="accent-line"></div>

<div class="process">
  <div class="process-step">
    <span class="label">Words</span>
    <p>Study usage, grammar, syntax, translation, and the range of meaning.</p>
  </div>
  <div class="process-step">
    <span class="label">Context</span>
    <p>Read the passage in its literary, historical, and cultural setting.</p>
  </div>
  <div class="process-step">
    <span class="label">Genre</span>
    <p>Let prose be prose, poetry be poetry, parable be parable, symbol be symbol.</p>
  </div>
  <div class="process-step">
    <span class="label">Canon</span>
    <p>Let Scripture in its totality clarify Scripture's particular claims.</p>
  </div>
</div>

---

<div class="eyebrow">Clarity without laziness</div>

## Scripture can be understood, but it must be read carefully

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>External clarity</h3>
    <p>God communicates meaning through human language, and the meaning of the text is accessible to faithful readers.</p>
  </div>
  <div class="card alt">
    <h3>Real difficulty</h3>
    <p>Some passages remain hard, disputed, or mysterious, but difficulty does not make meaning arbitrary.</p>
  </div>
</div>

<p class="context-note">The answer to difficult texts is not speculation. It is more careful listening.</p>

---

<div class="eyebrow">Common distortions</div>

## Ways readers lose the text while still using the Bible

<div class="accent-line"></div>

<div class="application-list">
  <div class="app-item">
    <span class="label">Subjectivism</span>
    <p>Asking only, "What does this mean to me?" before asking what the text says.</p>
  </div>
  <div class="app-item">
    <span class="label">Loose Association</span>
    <p>Stringing words together without letting context define meaning.</p>
  </div>
  <div class="app-item">
    <span class="label">Speculation</span>
    <p>Prioritizing hypothetical layers behind the text over the canonical text itself.</p>
  </div>
  <div class="app-item">
    <span class="label">Modern Control</span>
    <p>Allowing Scripture to answer only the questions the modern reader permits.</p>
  </div>
</div>

---

<!-- _class: gold -->

<div class="statement">The Bible is not raw material for religious creativity.<br><br>It is the Word that judges our creativity.</div>

<p>The reader does not grant Scripture authority. The reader receives it.</p>

---

<!-- _class: section-intro -->

<div class="section-kicker">The Posture</div>

# Obedient Understanding

<div class="accent-line" style="margin:0.7rem auto 1rem auto;"></div>

<p class="section-note">Hasel insists that interpretation aims beyond correct analysis. The Word of God was given to be believed, obeyed, proclaimed, and lived.</p>

---

<div class="eyebrow">Knowing and doing</div>

## Understanding is incomplete until it becomes following

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Analysis is necessary</h3>
    <p>We must study grammar, history, syntax, genre, and context with patience and rigor.</p>
  </div>
  <div class="card alt">
    <h3>Analysis is not enough</h3>
    <p>If the house is burning, it is not enough to parse the warning. The words require response.</p>
  </div>
</div>

<p class="context-note">The final word in interpretation belongs not to standing over the text, but to following the Word.</p>

---

<div class="eyebrow">Faith and thinking</div>

## The intellect is sanctified, not sacrificed

<div class="accent-line"></div>

<div class="stack">
  <div class="rung">
    <span class="label">Not anti-intellectual</span>
    <p>Biblical faith does not require us to abandon careful thought, study, or scholarly discipline.</p>
  </div>
  <div class="rung">
    <span class="label">Not autonomous</span>
    <p>Christian thinking happens coram Deo: before God, under God, and accountable to God.</p>
  </div>
  <div class="rung">
    <span class="label">Not self-protective</span>
    <p>The mind must be renewed, not enthroned as a final court above Scripture.</p>
  </div>
</div>

---

<div class="eyebrow">Humility</div>

## The interpreter is a receiver before being a critic

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Why humility matters</h3>
    <ul>
      <li>Our experience is limited</li>
      <li>Our logic may be too narrow</li>
      <li>Our questions are not exhaustive</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>What humility protects</h3>
    <ul>
      <li>Confidence without arrogance</li>
      <li>Conviction without carelessness</li>
      <li>Inquiry without suspicion as a habit</li>
    </ul>
  </div>
</div>

<p class="context-note">We believe so that we may understand. Faith is not the end of thinking; it is the beginning of rightly ordered thought.</p>

---

<!-- _class: section-intro -->

<div class="section-kicker">Biblical Presuppositions</div>

# What Must a Biblical Hermeneutic Assume?

<div class="accent-line" style="margin:0.7rem auto 1rem auto;"></div>

<p class="section-note">A method in harmony with Scripture must be open to the reality Scripture presents: God exists, God is supernatural, God acts in time and space, God is personal, and sin affects the interpreter.</p>

---

<div class="eyebrow">Reality according to Scripture</div>

## The Bible's worldview sets the reading frame

<div class="accent-line"></div>

<div class="principles">
  <div class="principle">
    <span class="label">God Exists</span>
    <p>The biblical writers assume the living God from the beginning.</p>
  </div>
  <div class="principle">
    <span class="label">God Transcends</span>
    <p>He is not trapped inside ordinary cause and effect.</p>
  </div>
  <div class="principle">
    <span class="label">God Acts</span>
    <p>He enters time and space, performs miracles, and reveals the future.</p>
  </div>
  <div class="principle">
    <span class="label">God Speaks</span>
    <p>The triune God communicates personally and meaningfully.</p>
  </div>
  <div class="principle">
    <span class="label">God Unifies</span>
    <p>New light does not contradict old light; Scripture interprets Scripture.</p>
  </div>
</div>

---

<div class="eyebrow">The noetic effect of sin</div>

## The problem is not only in the text we read

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Sin bends the reader</h3>
    <ul>
      <li>Thinking becomes self-centered</li>
      <li>Truth is resisted or distorted</li>
      <li>Obedience feels optional</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>The Spirit restores sight</h3>
    <ul>
      <li>Illumines the inspired Word</li>
      <li>Creates willingness to obey</li>
      <li>Leads us to Christ through Scripture</li>
    </ul>
  </div>
</div>

<p class="context-note">Without the Spirit, a reader may grasp linguistic meaning while missing spiritual significance.</p>

---

<div class="eyebrow">Spirit and Word</div>

## Illumination never supersedes Scripture

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>The Spirit's work</h3>
    <p>The Holy Spirit makes the written Word come alive, persuades the heart, and leads the reader toward faithful obedience.</p>
  </div>
  <div class="card alt">
    <h3>The Spirit's boundary</h3>
    <p>The Spirit does not lead away from Scripture. The Word remains the standard by which teaching and experience are tested.</p>
  </div>
</div>

<p class="context-note">We do not worship the Bible. We receive Scripture as the Spirit's appointed witness to the living Christ.</p>

---

<div class="eyebrow">Implications for Adventist reading</div>

## What this chapter asks of the church

<div class="accent-line"></div>

<div class="application-list">
  <div class="app-item">
    <span class="label">Teaching</span>
    <p>Let Scripture's self-claims shape the method before modern assumptions shape the result.</p>
  </div>
  <div class="app-item">
    <span class="label">Preaching</span>
    <p>Move from text to theology to summons, not from preference to proof text.</p>
  </div>
  <div class="app-item">
    <span class="label">Doctrine</span>
    <p>Test every conclusion by tota Scriptura, the whole canonical witness.</p>
  </div>
  <div class="app-item">
    <span class="label">Discipleship</span>
    <p>Read with intellectual care, prayerful humility, and willingness to obey.</p>
  </div>
</div>

---

<!-- _class: discussion -->

<div class="eyebrow">Discussion</div>

## Questions worth carrying into the room

<div class="question">Which interpretive habits quietly assume that God cannot speak, act, reveal, or correct?</div>
<div class="question">Where do we most need historical-grammatical care: context, genre, language, canon, or application?</div>
<div class="question">How can Adventists defend Scripture's authority without becoming careless, suspicious, or merely defensive?</div>
<div class="question">What would change if Bible study aimed not only at understanding the Word, but following it?</div>

---

<!-- _class: closing -->

<div class="eyebrow">Closing burden</div>

<div class="statement">Faithful hermeneutics begins when Scripture is allowed to tell us what Scripture is.</div>

<p class="closing-note">The Adventist reader comes to the Bible with open eyes, a renewed mind, a teachable spirit, and a surrendered will. We read carefully because God has spoken clearly. We read humbly because sin still clouds us. We read obediently because the Word was never given merely to be analyzed. It was given to lead us to Christ.</p>
