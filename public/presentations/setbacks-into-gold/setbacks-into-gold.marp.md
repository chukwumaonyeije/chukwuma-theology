---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: Setbacks into Gold
description: A Sabbath School presentation on growing in a relationship with God through setbacks. Atlanta North Seventh-day Adventist Church, June 13, 2026.
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
  font-size: 52px;
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
.grid.three { grid-template-columns: 1fr 1fr 1fr; }
.grid.four { grid-template-columns: 1fr 1fr 1fr 1fr; }

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

.card.dark {
  background: rgba(16,22,26,0.72);
  border-top-color: var(--ember);
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

.application {
  font-size: 32px;
  line-height: 1.2;
  max-width: 980px;
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
  border-collapse: collapse;
  width: 100%;
  font-size: 18px;
  margin-top: 10px;
}

thead th {
  background: rgba(214,171,85,0.22);
  color: var(--gold);
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 1.4px;
  text-transform: uppercase;
  padding: 10px 14px;
  border-bottom: 2px solid var(--gold);
  text-align: left;
}

tbody td {
  padding: 9px 14px;
  border-bottom: 1px solid var(--line);
  vertical-align: top;
  line-height: 1.3;
  font-size: 17px;
}

tbody tr:last-child td {
  border-bottom: none;
}

tbody td:first-child {
  color: var(--gold);
  font-weight: 700;
}

.takeaway {
  background: rgba(214,171,85,0.14);
  border: 1px solid rgba(214,171,85,0.38);
  border-left: 5px solid var(--gold);
  padding: 12px 18px;
  margin-top: 14px;
  font-size: 18px;
  line-height: 1.38;
  border-radius: 4px;
}

.step-row {
  display: flex;
  gap: 18px;
  width: 100%;
  margin-top: 12px;
}

.step {
  flex: 1;
  background: rgba(245,239,229,0.07);
  border: 1px solid var(--line);
  border-top: 4px solid var(--gold);
  border-radius: 8px;
  padding: 14px 14px;
  text-align: center;
}

.step.highlight {
  border-top-color: #f0d878;
  background: rgba(214,171,85,0.18);
}

.step .step-num {
  color: var(--gold);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 1.4px;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.step h3 {
  font-size: 20px;
  margin: 4px 0 6px 0;
  color: var(--linen);
}

.step p {
  font-size: 15px;
  color: var(--muted);
  margin: 0;
  line-height: 1.3;
}

</style>

<!-- _class: title -->

<div class="eyebrow">Atlanta North Seventh-day Adventist Church · Sabbath School · June 13, 2026</div>

# Setbacks: Growing in a Relationship with God

<div class="subtitle">Navigating life's storms through a divine lens.</div>

<div class="accent-line"></div>

<p class="reference">Key Texts: Romans 5:3–5 · Mark 4 · Mark 5 · Job 1 · Job 23 · Luke 24</p>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">The lens of adversity</div>
  <h2>A question of perspective</h2>
  <div class="accent-line"></div>
  <p>A young girl was walking home as a severe thunderstorm broke. Drenched and hurrying, her father watched her through the window.</p>
  <p>With every terrifying flash of lightning, she stopped, looked up at the sky, and <em>smiled.</em></p>
</div>

<div class="panel">
  <p><strong>"Why did you do that?"</strong> her father asked.</p>
  <p><em>"Because God was taking my picture."</em></p>
  <br/>
  <div class="takeaway">Setbacks are a matter of perspective. When the storm hits, are we cowering from the thunder, or looking up for God's light?</div>
</div>

---

<div class="eyebrow">Romans 5:3–5</div>

## The Biblical Framework of Refinement

<div class="accent-line"></div>

<p>Romans 5 reveals that setbacks are not roadblocks — they are the active machinery God uses to manufacture spiritual endurance.</p>

<div class="step-row">
  <div class="step">
    <div class="step-num">Step 1</div>
    <h3>Tribulation</h3>
    <p>The raw material: setbacks, storms, and suffering.</p>
  </div>
  <div class="step">
    <div class="step-num">Step 2</div>
    <h3>Perseverance</h3>
    <p>The mechanical friction: enduring the unexplainable.</p>
  </div>
  <div class="step">
    <div class="step-num">Step 3</div>
    <h3>Character</h3>
    <p>The forged product: a resilient, tested spiritual identity.</p>
  </div>
  <div class="step highlight">
    <div class="step-num">Step 4</div>
    <h3>Hope</h3>
    <p>The golden output: an unshakeable trust in God's love.</p>
  </div>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Archetype 1 · Mark 4</div>
  <h2>The Sudden Storm</h2>
  <div class="accent-line"></div>
  <p><strong>Context:</strong> A sudden, violent squall on the Sea of Galilee terrifies experienced, professional fishermen.</p>
  <p><em>"Teacher, do You not care that we are perishing?"</em> — questioning God's character in crisis.</p>
</div>

<div class="panel">
  <p><strong>The Paradox:</strong> Jesus is asleep on the only pillow in the boat — located at the stern, the exact position of the helmsman.</p>
  <br/>
  <p><strong>The Divine Reality:</strong> The Helmsman is at rest. When we feel the urge to save ourselves, Jesus commands peace to the storm we cannot control.</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Archetype 2 · Mark 5</div>
  <h2>The Chronic Burden</h2>
  <div class="accent-line"></div>
  <p><strong>Context:</strong> A woman suffers from a flow of blood for 12 years.</p>
  <p><strong>The Depletion:</strong> She spent all her money on physicians, found no cure, and grew steadily worse. Fatigued, isolated, and culturally labeled unclean.</p>
</div>

<div class="panel soft">
  <p><strong>The Action:</strong> Despite physical exhaustion and social stigma, she intentionally pushes through the suffocating crowd with a singular belief:</p>
  <br/>
  <p><em>"If only I may touch His clothes."</em></p>
</div>

---

<div class="eyebrow">Mark 5 · Desire of Ages</div>

## Diagnostic Matrix: Proximity vs. Faith

<div class="accent-line"></div>

| &nbsp; | **The Careless Throng** | **The True Seeker** |
|---|---|---|
| **Action** | Casual contact, pushed by the crowd. | Intentional, deliberate reach for the Savior's hem. |
| **Expectation** | No expectation of a miracle; just observing. | Absolute belief that a single touch will heal a 12-year affliction. |
| **Jesus' Response** | "People are pressing You all around." | "Who touched my clothes?" — recognizing the specific transfer of healing power. |

<div class="takeaway"><em>"The Savior could distinguish the touch of faith from the casual contact of the careless throng."</em> — The Desire of Ages</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Archetype 3 · Job 1</div>
  <h2>The Inexplicable Loss</h2>
  <div class="accent-line"></div>
  <p><strong>Context:</strong> A faithful man systematically loses everything in a cosmic controversy he cannot see or understand.</p>
  <p><strong>The Danger of Miserable Comforters:</strong> Friends who apply human reasoning to spiritual warfare, falsely insisting Job must have hidden sins to deserve this setback.</p>
</div>

<div class="panel">
  <p><strong>The Core Reaction (Job 1:21):</strong></p>
  <br/>
  <p><em>"Naked I came from my mother's womb... The Lord gave, and the Lord has taken away; blessed be the name of the Lord."</em></p>
  <br/>
  <p>Even stripped of wealth, children, and health — the golden core of trust remained unshaken.</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Job 23:8–10</div>
  <h2>The Crucible of Gold</h2>
  <div class="accent-line"></div>
  <p><strong>The Darkness of Confusion:</strong></p>
  <ul>
    <li>I go forward, but He is not there...</li>
    <li>Backward, but I cannot perceive Him...</li>
    <li>I cannot see Him... (Job 23:8–9)</li>
  </ul>
</div>

<div class="panel">
  <p><strong>The Certainty of Refinement:</strong></p>
  <br/>
  <p><em>"But He knows the way that I take... When He has tested me, I shall come forth as gold."</em> (Job 23:10)</p>
  <br/>
  <div class="takeaway">The key to triumphing in trials is not necessarily understanding the "why," but trusting that the Refiner has not abandoned the crucible.</div>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Archetype 4 · Luke 24</div>
  <h2>Shattered Expectations</h2>
  <div class="accent-line"></div>
  <p><strong>Walking Away — 7 miles to Emmaus.</strong></p>
  <p>The disciples are discouraged, confused, and retreating after the crucifixion.</p>
  <p><em>"We were hoping it was He who was going to redeem Israel."</em></p>
</div>

<div class="panel soft">
  <p><strong>The Pivot Point:</strong> A Stranger opens the Word — Jesus illuminates prophecies (Gen 3:15, Micah 5, Isaiah 53), shifting their focus from political victory to divine salvation.</p>
  <br/>
  <p><strong>Running Back:</strong> The breaking of bread reveals His identity. Their perspective shifts entirely; they run 7 miles back to Jerusalem in the dark, fueled by renewed faith and joy.</p>
</div>

---

<div class="eyebrow">Master Synthesis</div>

## The Two Perspectives of Setbacks

<div class="accent-line"></div>

| **Archetype** | **The Human Perspective** | **The Divine Reality** |
|---|---|---|
| The Sudden Storm (Disciples) | Fear & Panic — "Do you not care?" | **Complete Sovereignty** — Sleeping at the helm; commanding peace. |
| The Chronic Burden (Bleeding Woman) | Exhaustion & Isolation — 12 years depleted | **Infinite Compassion** — Recognizing the specific touch of faith. |
| The Inexplicable Loss (Job) | Despair & Confusion — "Why is this happening?" | **Unseen Refinement** — Forging character to come forth as gold. |
| Shattered Expectations (Emmaus) | Disappointment — "He didn't act as we hoped" | **Prophetic Fulfillment** — Executing a grander, eternal plan. |

---

<!-- _class: split -->

<div>
  <div class="eyebrow">A Modern Story</div>
  <h2>The Ripple Effect of a Setback</h2>
  <div class="accent-line"></div>
  <p>Zeth, a literature evangelist, loses his livelihood entirely due to a sudden pandemic lockdown.</p>
</div>

<div class="panel">
  <ul>
    <li><strong>The Pivot:</strong> Instead of despairing, Zeth and his wife pivot to volunteer Bible work in their immediate sphere of influence.</li>
    <li><strong>The Action:</strong> They build a prayer list of 50 friends, visiting three families daily by motorcycle to study the Word.</li>
    <li><strong>The Harvest:</strong> 14% of the people on that list are baptized.</li>
  </ul>
  <div class="takeaway">A closed door often forces us to redirect our energy toward life's most important work.</div>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Ellen G. White</div>
  <h2>Leaving the Baggage at the Door</h2>
  <div class="accent-line"></div>
  <p>In a dream, Ellen G. White found herself climbing a steep, frail stairway carrying all her possessions. At the top, a guide told her to leave everything outside the door.</p>
  <p>Upon entering, she stood before Jesus, whose smile filled her with inexpressible peace.</p>
</div>

<div class="panel soft">
  <p><em>"The heavier your burdens, the more blessed the rest in casting them upon the Burden Bearer."</em></p>
  <br/>
  <div class="takeaway">We are invited to stop carrying the crushing weight of our setbacks and lay them at the feet of the One who already knows our every circumstance.</div>
</div>

---

<div class="eyebrow">Practical Tools</div>

## The Believer's Toolkit for Setbacks

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>1. Assess Your Picture of God</h3>
    <p>The enemy's primary goal in a setback is to distort your view of God's character. Actively reject the voice that says God is punishing you.</p>
  </div>
  <div class="card alt">
    <h3>2. Immerse in the Word</h3>
    <p>Faith comes by hearing (Rom. 10:17). When your own faith is weak, let the promises of Scripture illuminate your darkness, just as Jesus did on the Emmaus road.</p>
  </div>
  <div class="card">
    <h3>3. Cultivate a Humble Heart</h3>
    <p>Acknowledge that God is sovereign. We often cannot see the cosmic controversy behind our trials; humility trusts His goodness anyway.</p>
  </div>
  <div class="card alt">
    <h3>4. Cry Out to the Counselor</h3>
    <p>Do not suffer in silence. Spread your anxieties before the Lord in prayer. When weak, pray: <em>"Lord, I believe; help my unbelief!"</em></p>
  </div>
</div>

---

<!-- _class: quote -->

<div class="eyebrow">Closing Word</div>

<div class="statement">The Storm is Temporary. The Gold is Eternal.</div>

<ul style="text-align:left; margin-top:16px;">
  <li>He is in your boat when the storm is sudden.</li>
  <li>He feels your touch when the burden is chronic.</li>
  <li>He knows your way when the loss is unexplainable.</li>
  <li>He walks your road when expectations shatter.</li>
</ul>

---

<!-- _class: blessing -->

<div class="eyebrow">The Promise</div>

<div class="closing-summary">Your setbacks are not the end of the story; they are the exact locations where God is forging your faith into gold.</div>

<p class="dim">Look up, and smile for the camera.</p>
