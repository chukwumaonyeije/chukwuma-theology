---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: The Power That Changed the Universe
description: A Chukwuma Theology Sabbath School study on First Corinthians — why the cross redefines strength, and how it settles the Great Controversy's argument over God's power.
---

<style>
:root {
  --stone: #201915;
  --cave: #151d22;
  --cave-deep: #10161a;
  --ember: #c87532;
  --gold: #d6ab55;
  --linen: #f5efe5;
  --muted: rgba(245,239,229,0.72);
  --line: rgba(245,239,229,0.18);
}

section {
  box-sizing: border-box;
  font-family: "Segoe UI", Arial, sans-serif;
  background:
    radial-gradient(circle at 78% 20%, rgba(214,171,85,0.28), transparent 32%),
    radial-gradient(circle at 20% 80%, rgba(200,117,50,0.18), transparent 34%),
    linear-gradient(135deg, var(--cave), var(--stone));
  color: var(--linen);
  padding: 32px 46px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
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

h1,
h2,
h3 {
  font-family: Georgia, "Times New Roman", serif;
  color: var(--linen);
  margin: 0 0 10px 0;
  line-height: 1.04;
  letter-spacing: 0;
}

h1 { font-size: 46px; max-width: 1040px; }
h2 { font-size: 34px; max-width: 1040px; }
h3 { font-size: 22px; }

p {
  font-size: 20px;
  line-height: 1.34;
  color: var(--linen);
  margin: 5px 0 10px 0;
}

ul {
  list-style: none;
  padding: 0;
  margin: 8px 0 0 0;
  max-width: 980px;
}

li {
  position: relative;
  padding: 4px 0 4px 24px;
  line-height: 1.24;
  font-size: 20px;
}

li::before {
  content: '-';
  position: absolute;
  left: 0;
  color: var(--gold);
  font-weight: 800;
}

strong { color: var(--gold); }
em { color: #e5b08e; }

.eyebrow {
  color: var(--gold);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  margin-bottom: 10px;
}

.accent-line {
  width: 50px;
  height: 3px;
  background: var(--gold);
  margin: 6px 0 12px 0;
}

.subtitle {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 24px;
  font-style: italic;
  color: var(--muted);
  max-width: 860px;
}

.credit,
.reference {
  color: rgba(245,239,229,0.58);
  font-size: 16px;
  line-height: 1.3;
  letter-spacing: 0.5px;
}

section.title,
section.quote,
section.blessing {
  text-align: center;
  align-items: center;
  padding: 34px 62px;
}

section.title h1 {
  font-size: 50px;
  text-transform: uppercase;
  max-width: 1080px;
}

section.title .accent-line {
  margin-left: auto;
  margin-right: auto;
}

section.light {
  background:
    radial-gradient(circle at 75% 22%, rgba(255,255,255,0.36), transparent 22%),
    linear-gradient(140deg, #e7d3b0, #81583a 48%, var(--cave-deep));
}

section.split {
  display: grid;
  grid-template-columns: 0.95fr 1.05fr;
  gap: 22px;
  align-items: center;
}

.panel {
  background: rgba(16,22,26,0.62);
  border: 1px solid var(--line);
  border-left: 5px solid var(--gold);
  padding: 14px 18px;
  width: 100%;
  box-sizing: border-box;
}

.panel.soft {
  background: rgba(245,239,229,0.08);
  border-left-color: var(--ember);
}

.grid {
  display: grid;
  gap: 12px;
  width: 100%;
  margin-top: 10px;
}

.grid.two { grid-template-columns: 1fr 1fr; }
.grid.five { grid-template-columns: repeat(5, 1fr); }

.card {
  background: rgba(245,239,229,0.08);
  border: 1px solid var(--line);
  border-top: 4px solid var(--gold);
  border-radius: 8px;
  padding: 13px 16px;
  box-sizing: border-box;
}

.card.alt {
  border-top-color: var(--ember);
  background: rgba(200,117,50,0.13);
}

.card h3,
.label {
  font-family: "Segoe UI", Arial, sans-serif;
  color: var(--gold);
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  margin: 0 0 8px 0;
}

.card p {
  font-size: 16px;
  margin: 0;
}

.statement {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 36px;
  line-height: 1.14;
  font-weight: 700;
  max-width: 1040px;
}

section.quote .statement {
  font-size: 38px;
  font-style: italic;
}

.small-list li {
  font-size: 18px;
}

.wide {
  max-width: 960px;
}

.closing-summary {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 40px;
  line-height: 1.12;
  max-width: 1040px;
}

.dim {
  color: var(--muted);
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 18px;
}

th, td {
  border: 1px solid var(--line);
  padding: 8px 12px;
  text-align: left;
}

th {
  color: var(--gold);
  font-size: 13px;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.qmark {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--gold);
  color: var(--cave-deep);
  font-weight: 800;
  font-size: 15px;
  margin-right: 10px;
  flex-shrink: 0;
}

.q-item {
  display: flex;
  align-items: flex-start;
  gap: 4px;
  padding: 6px 0;
  font-size: 19px;
  line-height: 1.28;
  border-bottom: 1px solid var(--line);
  max-width: 1040px;
}

.q-item:last-child { border-bottom: none; }

</style>

<!-- _class: title -->

<div class="eyebrow">Chukwuma Theology &middot; Sabbath School Study</div>

# The Power That Changed the Universe

<div class="subtitle">Why the cross redefines strength</div>

<div class="accent-line"></div>

<p class="reference">Key Text: 1 Corinthians 1:18, 4:20</p>

<p class="credit">A study through First Corinthians on power, the cross, and the Great Controversy</p>

---

<div class="eyebrow">Where we begin</div>

## Power has two definitions

<div class="accent-line"></div>

<p class="wide">First Corinthians confronts two rival visions of power. <strong>What does true power actually look like?</strong></p>

<div class="grid two">
  <div class="card">
    <h3>Worldly Power (Corinth)</h3>
    <ul class="small-list">
      <li>Wealth</li>
      <li>Rhetoric</li>
      <li>Visibility</li>
      <li>Status</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>True Power</h3>
    <p style="font-size:22px; font-family: Georgia, serif; color: var(--linen);">The Cross.</p>
  </div>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Sunday</div>
  <h2>When the church mirrors Corinth</h2>
  <div class="accent-line"></div>
  <p class="reference">1 Corinthians 1:10-17; 3:1-9; 11:17-22</p>
</div>

<div class="panel">
  <div class="grid two">
    <div>
      <h3 style="color: var(--gold); font-size: 13px; text-transform: uppercase; letter-spacing: 1.2px;">Worldly Measure</h3>
      <ul class="small-list">
        <li>Visibility and applause</li>
        <li>Charisma and eloquence</li>
        <li>Control and influence</li>
      </ul>
    </div>
    <div>
      <h3 style="color: var(--gold); font-size: 13px; text-transform: uppercase; letter-spacing: 1.2px;">Gospel Measure</h3>
      <ul class="small-list">
        <li>Faithfulness to Christ</li>
        <li>Character and truth</li>
        <li>Service and sacrifice</li>
      </ul>
    </div>
  </div>
</div>

<p class="dim" style="font-style: italic; margin-top: 10px;">A church can confess Christ while still imitating the world's methods of power.</p>

---

<!-- _class: quote -->

<div class="eyebrow">Monday &middot; The cross redefines strength</div>

<div class="statement">The cross is not divine power temporarily hidden. The cross is divine power fully revealed.</div>

<p class="dim">"For the message of the cross is foolishness to those who are perishing, but to us who are being saved it is the power of God." &mdash; 1 Corinthians 1:18</p>

---

<div class="eyebrow">Tuesday</div>

## The Spirit makes truth transformative

<div class="accent-line"></div>

<p class="reference">1 Corinthians 2:1-5; 6:9-11</p>

<ul>
  <li>Information instructs the mind, but the Holy Spirit converts the heart.</li>
  <li>Grace changes both standing and character.</li>
</ul>

<table>
  <tr><th>Truth Alone</th><th></th><th>Truth by the Spirit</th></tr>
  <tr><td>Inform</td><td>vs.</td><td><strong>Transforms</strong></td></tr>
  <tr><td>Forgive</td><td>vs.</td><td><strong>Sanctifies</strong></td></tr>
  <tr><td>Impress</td><td>vs.</td><td><strong>Converts</strong></td></tr>
</table>

<p class="dim" style="font-style: italic; margin-top: 8px;">Adventist integration: sanctification demonstrates the continuing work of Christ.</p>

---

<!-- _class: light -->

<div class="eyebrow">Wednesday</div>

# Love is the highest power

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Worldly Coercion</h3>
    <ul class="small-list">
      <li>Relies on force and control</li>
      <li>Seeks personal elevation</li>
      <li>Produces fear, resentment, and bondage</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>Divine Love</h3>
    <ul class="small-list">
      <li>Flows from truth and freedom</li>
      <li>Leads in humility and self-giving</li>
      <li>Produces peace, joy, and transformation</li>
    </ul>
  </div>
</div>

<p class="dim" style="font-style: italic; margin-top: 10px;">The cross is love made visible.</p>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Thursday</div>
  <h2>Resurrection is power over death</h2>
  <div class="accent-line"></div>
  <p class="reference">"Death is swallowed up in victory." &mdash; 1 Corinthians 15:54</p>
</div>

<div class="panel soft">
  <ul>
    <li>Immortality is God's gift, not a natural possession.</li>
    <li>The final triumph is abolishing death itself.</li>
    <li>The Creator's answer to death is resurrection, restoration, and everlasting life in Christ.</li>
  </ul>
</div>

---

<div class="eyebrow">Inside the story</div>

## A church learning a new kingdom

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Corinth's Instinct</h3>
    <ul class="small-list">
      <li>Exalt yourself</li>
      <li>Protect your status</li>
      <li>Display your gift</li>
      <li>Preserve power</li>
    </ul>
  </div>
  <div class="card alt">
    <h3>Paul's Invitation</h3>
    <ul class="small-list">
      <li>Boast in the Lord</li>
      <li>Honor the weaker member</li>
      <li>Serve the whole body</li>
      <li>Take the way of love</li>
    </ul>
  </div>
</div>

<p class="dim" style="font-style: italic; margin-top: 10px;">Mission takeaway: the credibility of the church's witness depends on whether its life together resembles the crucified Christ.</p>

---

<div class="eyebrow">Synthesis</div>

## One gospel, five expressions of power

<div class="accent-line"></div>

<div class="grid five">
  <div class="card">
    <h3>01 &middot; The Cross</h3>
    <p>Conquers through sacrifice.</p>
  </div>
  <div class="card">
    <h3>02 &middot; The Spirit</h3>
    <p>Transforms the human heart.</p>
  </div>
  <div class="card">
    <h3>03 &middot; Sanctification</h3>
    <p>Re-forms character in Christ.</p>
  </div>
  <div class="card">
    <h3>04 &middot; Love</h3>
    <p>Orders gifts toward service.</p>
  </div>
  <div class="card">
    <h3>05 &middot; Resurrection</h3>
    <p>Defeats death and restores creation.</p>
  </div>
</div>

<p class="dim" style="font-style: italic; margin-top: 12px;">Genuine spiritual power is measured by Christlikeness, not applause or control.</p>

---

<div class="eyebrow">Reflect, discuss, apply</div>

## Questions for the group

<div class="accent-line"></div>

<div class="q-item"><span class="qmark">1</span> Where is the modern church most tempted to confuse visibility with spiritual power?</div>
<div class="q-item"><span class="qmark">2</span> How does the cross answer Satan's claim that authority must depend on force?</div>
<div class="q-item"><span class="qmark">3</span> Why can impressive gifts coexist with spiritual immaturity?</div>
<div class="q-item"><span class="qmark">4</span> What would change if love&mdash;not recognition&mdash;became the measure of ministry?</div>
<div class="q-item"><span class="qmark">5</span> Which expression of God's power do you most need today?</div>

---

<!-- _class: blessing -->

<div class="eyebrow">The kingdom is revealed in power</div>

<div class="statement">"For the kingdom of God is not in word but in power." &mdash; 1 Corinthians 4:20</div>

<p class="closing-summary" style="font-size: 26px; margin-top: 16px;">May the Spirit of the crucified and risen Christ free us from the need to control, teach us to serve in love, transform our character, and keep us faithful in resurrection hope.</p>

<p class="credit" style="margin-top: 14px;">Chukwuma Theology &middot; Rooted in Scripture. Grounded in Grace.</p>
