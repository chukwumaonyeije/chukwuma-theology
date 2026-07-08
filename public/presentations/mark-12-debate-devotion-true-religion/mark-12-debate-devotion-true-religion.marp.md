---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: "Mark 12:18-44 — Debate, Devotion, and True Religion"
description: "A Chukwuma Theology Wednesday Night Prayer Meeting study on Mark 12:18-44 — five temple-court encounters that move from hostile debate to true devotion."
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --navy: #10161f;
  --navy-deep: #0a0e15;
  --gold: #d9ac54;
  --gold-deep: #b3862f;
  --ember: #b96a35;
  --linen: #f3ede0;
  --dim: rgba(243,237,224,0.72);
  --line: rgba(243,237,224,0.16);
}

section {
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  background:
    radial-gradient(circle at 82% 14%, rgba(217,172,84,0.24), transparent 30%),
    radial-gradient(circle at 12% 86%, rgba(185,106,53,0.16), transparent 34%),
    linear-gradient(150deg, var(--navy), var(--navy-deep));
  color: var(--linen);
  padding: 40px 64px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  overflow: hidden;
}

section::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, var(--gold), var(--ember), var(--gold));
}

h1, h2, h3 {
  font-family: 'Playfair Display', serif;
  margin: 0 0 0.2em 0;
  color: var(--linen);
  line-height: 1.14;
}

h1 { font-size: 2.7rem; max-width: 1040px; }
h2 { font-size: 1.9rem; max-width: 1040px; }
h3 { font-size: 1.15rem; }

p {
  font-size: 1rem;
  line-height: 1.5;
  margin: 0.2em 0 0.5em 0;
  color: var(--linen);
}

ul, ol {
  list-style: none;
  padding: 0;
  margin: 0.35em 0 0 0;
  max-width: 980px;
}

li {
  position: relative;
  padding: 0.2em 0 0.2em 1.3em;
  line-height: 1.44;
}

li::before {
  content: '-';
  position: absolute;
  left: 0;
  color: var(--gold);
  font-weight: 800;
}

strong { color: var(--gold); }
em { color: #e0b184; }

.eyebrow {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 0.7rem;
}

.accent-line {
  width: 54px;
  height: 3px;
  background: var(--gold);
  margin: 0.4rem 0 1rem 0;
}

.subtitle {
  max-width: 900px;
  font-family: 'Playfair Display', serif;
  font-size: 1.24rem;
  font-style: italic;
  line-height: 1.5;
  color: var(--dim);
}

.reference, .credit {
  font-size: 0.85rem;
  color: rgba(243,237,224,0.6);
  letter-spacing: 0.02em;
  line-height: 1.4;
}

section.title, section.quote, section.blessing {
  text-align: center;
  align-items: center;
  padding: 34px 62px;
}

section.title h1 {
  font-size: 3rem;
  max-width: 1080px;
}

section.title .accent-line,
section.quote .accent-line,
section.blessing .accent-line {
  margin-left: auto;
  margin-right: auto;
}

section.light {
  background:
    radial-gradient(circle at 78% 18%, rgba(255,255,255,0.32), transparent 24%),
    linear-gradient(140deg, #e6d3ac, #8a5e34 46%, var(--navy-deep));
}

section.split {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 22px;
  align-items: center;
}

.panel {
  background: rgba(10,14,21,0.6);
  border: 1px solid var(--line);
  border-left: 5px solid var(--gold);
  padding: 14px 18px;
  width: 100%;
  box-sizing: border-box;
}

.panel.soft {
  background: rgba(243,237,224,0.08);
  border-left-color: var(--ember);
}

.panel h3, .panel .label {
  font-family: 'Inter', sans-serif;
  color: var(--gold);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin: 0 0 0.5rem 0;
}

.qa-list {
  counter-reset: qa;
  margin-top: 0.4rem;
}

.qa-list li {
  counter-increment: qa;
  padding-left: 1.9rem;
  font-size: 0.95rem;
  line-height: 1.4;
  margin-bottom: 0.5rem;
}

.qa-list li::before {
  content: counter(qa);
  left: 0;
  top: 0.1em;
  width: 1.3rem;
  height: 1.3rem;
  border-radius: 50%;
  border: 1px solid var(--gold);
  color: var(--gold);
  font-weight: 800;
  font-size: 0.72rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
}

.grid {
  display: grid;
  gap: 12px;
  width: 100%;
  margin-top: 12px;
}

.grid.five { grid-template-columns: repeat(5, 1fr); }
.grid.two { grid-template-columns: 1fr 1fr; }

.card {
  background: rgba(243,237,224,0.08);
  border: 1px solid var(--line);
  border-top: 4px solid var(--gold);
  border-radius: 8px;
  padding: 12px 12px;
  box-sizing: border-box;
}

.card .num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.6rem;
  height: 1.6rem;
  border-radius: 50%;
  background: var(--gold);
  color: var(--navy-deep);
  font-weight: 800;
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
}

.card h4 {
  font-family: 'Playfair Display', serif;
  font-size: 0.92rem;
  margin: 0 0 0.3rem 0;
  line-height: 1.2;
  color: var(--linen);
}

.card p {
  font-size: 0.78rem;
  color: var(--dim);
  margin: 0;
  line-height: 1.32;
}

.small-list li {
  font-size: 0.92rem;
}

.wide { max-width: 960px; }

.statement {
  font-family: 'Playfair Display', serif;
  font-size: 1.8rem;
  line-height: 1.16;
  font-weight: 700;
  max-width: 1040px;
}

section.quote .statement { font-style: italic; }

.closing-summary {
  font-family: 'Playfair Display', serif;
  font-size: 2.1rem;
  line-height: 1.14;
  max-width: 1040px;
}

.dim { color: var(--dim); }

.chain {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 14px;
  flex-wrap: wrap;
}

.chain .step {
  background: rgba(243,237,224,0.08);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 6px 14px;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--linen);
  letter-spacing: 0.03em;
}

.chain .arrow {
  color: var(--gold);
  font-size: 0.9rem;
}

</style>

<!-- _class: title -->

<div class="eyebrow">Wednesday Night Prayer Meeting</div>

# Mark 12:18-44

<div class="subtitle">Debate, Devotion, and True Religion in the Temple Courts</div>

<div class="accent-line"></div>

<p class="reference">Key Scripture: Mark 12:18-44</p>

<p class="credit">A Seventh-day Adventist reading of Jesus' final temple debates during Holy Week — Dr. Chukwuma I. Onyeije, MD, FACOG</p>

---

<div class="eyebrow">Setting the scene</div>

## Where We Are in Mark

<div class="accent-line"></div>

<ul>
  <li>Mark is <strong>urgent and fast-paced</strong> — Jesus presented as the suffering Servant-Messiah.</li>
  <li>The narrative turns deliberately toward <strong>Jerusalem and the cross</strong>.</li>
  <li>Setting: <strong>Holy Week</strong> — Jesus teaching daily in the temple courts.</li>
  <li>Hostile encounters: <strong>Pharisees, Sadducees, and scribes</strong> attempt to trap Him.</li>
</ul>

---

<!-- _class: light -->

<div class="eyebrow">Five encounters, one movement</div>

## The Shape of the Passage

<div class="accent-line"></div>

<p class="wide"><strong>Mark 12:18-44</strong> moves through five encounters — from hostile debate to true devotion.</p>

<div class="grid five">
  <div class="card"><div class="num">1</div><h4>Truth Tested by Debate</h4><p>vv. 18-27</p></div>
  <div class="card"><div class="num">2</div><h4>Truth Affirmed by a Seeker</h4><p>vv. 28-34</p></div>
  <div class="card"><div class="num">3</div><h4>Jesus Reframes Messiah</h4><p>vv. 35-37</p></div>
  <div class="card"><div class="num">4</div><h4>False Piety Exposed</h4><p>vv. 38-40</p></div>
  <div class="card"><div class="num">5</div><h4>True Piety Modeled</h4><p>vv. 41-44</p></div>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Encounter 1 · vv. 18-27</div>
  <h2>Truth Tested by Debate</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>The Sadducees, who deny the resurrection, pose a marriage riddle to mock the doctrine.</li>
    <li>Jesus answers plainly: they know <strong>neither the Scriptures nor the power of God</strong>.</li>
    <li>He cites Exodus 3:6 — "I am the God of Abraham... of Isaac... of Jacob" — present tense, spoken centuries after they died.</li>
  </ul>
  <div class="panel soft">
    <p class="label">SDA Perspective</p>
    <p>"God of the living" affirms the certainty of a future bodily resurrection — consistent with the sleep of the dead and the hope of 1 Thessalonians 4:16.</p>
  </div>
</div>

<div class="panel">
  <p class="label">Discussion Questions</p>
  <ol class="qa-list">
    <li>Sincere inquiry, or a rhetorical trap?</li>
    <li>Which error is more common today — not knowing Scripture, or not knowing God's power?</li>
    <li>How does belief in the resurrection change the way we grieve?</li>
  </ol>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Encounter 2 · vv. 28-34</div>
  <h2>Truth Affirmed by a Seeker</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>A scribe asks Jesus which commandment is first of all.</li>
    <li>Jesus joins the Shema — <em>love God</em> (Deut. 6:4-5) — with Leviticus 19:18 — <em>love your neighbor</em> — as a single, undivided law.</li>
    <li>The scribe agrees, adding this is worth more than all burnt offerings and sacrifices.</li>
    <li>Jesus tells him: <strong>"You are not far from the kingdom of God."</strong></li>
  </ul>
</div>

<div class="panel">
  <p class="label">Discussion Questions</p>
  <ol class="qa-list">
    <li>Why does this scribe receive a different response than the Sadducees?</li>
    <li>Where do we split loving God and loving neighbor in practice?</li>
    <li>What does "not far from the kingdom" imply — and what would close the gap?</li>
  </ol>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Encounter 3 · vv. 35-37</div>
  <h2>Jesus Reframes the Messiah</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Jesus turns the questioning around: how can Messiah be David's son, if David himself — speaking by the Holy Spirit — calls Him "Lord"? (<strong>Psalm 110:1</strong>)</li>
    <li>A purely political or genealogical Messiah falls short of who Christ actually is.</li>
    <li>He is <strong>both David's son and David's Lord</strong> — fully human, fully divine.</li>
  </ul>
</div>

<div class="panel">
  <p class="label">Discussion Questions</p>
  <ol class="qa-list">
    <li>Why raise this riddle right after being complimented for His answers?</li>
    <li>What does a "David's son" view of Messiah alone leave out?</li>
    <li>How does this tie to the crowd's incomplete expectations of Jesus during Holy Week?</li>
  </ol>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Encounter 4 · vv. 38-40</div>
  <h2>False Piety Exposed</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Jesus warns against scribes who love long robes, greetings in the marketplace, and the best seats.</li>
    <li>They <strong>"devour widows' houses"</strong> and make long prayers for show.</li>
    <li>This warning sets up a sharp, deliberate contrast with the scene that follows.</li>
  </ul>
</div>

<div class="panel">
  <p class="label">Discussion Questions</p>
  <ol class="qa-list">
    <li>What's the common thread in robes, greetings, seats, and prayers?</li>
    <li>What does it mean for religious status to become cover for exploitation?</li>
    <li>Why does Mark place this warning immediately before the widow's offering?</li>
  </ol>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Encounter 5 · vv. 41-44</div>
  <h2>True Piety Modeled</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Jesus sits opposite the temple treasury, watching how people give. The rich contribute large sums from their abundance.</li>
    <li>A poor widow puts in two small copper coins — <strong>"all she had to live on."</strong></li>
    <li>Jesus declares she gave more than all of them, because she gave <em>out of her poverty</em>, not her surplus.</li>
  </ul>
</div>

<div class="panel">
  <p class="label">Discussion Questions</p>
  <ol class="qa-list">
    <li>Jesus watches <em>how</em> people give, not just how much. What does that say about God's evaluation?</li>
    <li>Why is "she gave out of her poverty" the point, not just the smallness of the amount?</li>
    <li>How does the resurrection hope of vv. 18-27 make this sacrificial trust reasonable, not foolish?</li>
  </ol>
</div>

---

<!-- _class: light -->

<div class="eyebrow">Main question</div>

# Closing Synthesis

<div class="accent-line"></div>

<p class="wide">Across all five encounters, what does Mark 12 teach us about the difference between religion that <strong>argues</strong> and religion that <strong>trusts</strong>?</p>

<div class="chain">
  <div class="step">1. Debate</div>
  <span class="arrow">&rarr;</span>
  <div class="step">2. Right Belief</div>
  <span class="arrow">&rarr;</span>
  <div class="step">3. Christ's True Identity</div>
  <span class="arrow">&rarr;</span>
  <div class="step">4. False Piety Unmasked</div>
  <span class="arrow">&rarr;</span>
  <div class="step">5. True Piety Lived</div>
</div>

<div class="panel soft" style="margin-top: 16px;">
  <p class="label">Concluding Thought</p>
  <p class="wide">The widow gives all she has to live on, immediately after Jesus defends the resurrection of the dead. Trust in a God who raises the dead is what makes such total surrender reasonable, not foolish.</p>
</div>

---

<!-- _class: blessing -->

<div class="eyebrow">Closing Prayer</div>

<div class="closing-summary">Lord, Search Our Hearts</div>

<p class="wide">Lord Jesus, in the temple courts You met debate with truth, sincerity with grace, and false piety with holy correction. You saw a widow the crowd overlooked and called her offering greater than all the rest. Teach us to love You with all our heart, and our neighbor as ourselves — not as an argument to win, but as a life to give. Where we have offered You our surplus, teach us to offer You our trust. In Your holy name, Amen.</p>

<p class="statement">What does it cost you to trust God the way she did?</p>
