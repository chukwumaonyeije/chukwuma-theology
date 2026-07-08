---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: "Under the Broom Tree — Elijah, Depression, and the God Who Still Speaks"
description: "A Chukwuma Theology sermon presentation on 1 Kings 19 — how God ministers to His exhausted prophet with care, presence, truth, and a future."
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --dusk: #1c2438;
  --dusk-deep: #11162350;
  --dusk-deeper: #0d1120;
  --sand: #d9b98a;
  --terracotta: #bf6e42;
  --ember: #e0a458;
  --linen: #f5eee1;
  --dim: rgba(245,238,225,0.72);
  --line: rgba(245,238,225,0.16);
}

section {
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  background:
    radial-gradient(circle at 85% 12%, rgba(224,164,88,0.26), transparent 30%),
    radial-gradient(circle at 10% 88%, rgba(191,110,66,0.18), transparent 34%),
    linear-gradient(150deg, var(--dusk), var(--dusk-deeper));
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
  background: linear-gradient(90deg, var(--ember), var(--terracotta), var(--ember));
}

h1, h2, h3 {
  font-family: 'Playfair Display', serif;
  margin: 0 0 0.2em 0;
  color: var(--linen);
  line-height: 1.14;
}

h1 { font-size: 2.6rem; max-width: 1040px; }
h2 { font-size: 1.85rem; max-width: 1040px; }
h3 { font-size: 1.1rem; }

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
  color: var(--ember);
  font-weight: 800;
}

strong { color: var(--ember); }
em { color: #e8c199; }

.eyebrow {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ember);
  margin-bottom: 0.7rem;
}

.accent-line {
  width: 54px;
  height: 3px;
  background: var(--ember);
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
  color: rgba(245,238,225,0.6);
  letter-spacing: 0.02em;
  line-height: 1.4;
}

section.title, section.quote, section.blessing {
  text-align: center;
  align-items: center;
  padding: 34px 62px;
}

section.title h1 {
  font-size: 2.9rem;
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
    radial-gradient(circle at 78% 18%, rgba(255,255,255,0.3), transparent 24%),
    linear-gradient(140deg, #e7cfa4, #93602f 46%, var(--dusk-deeper));
}

section.split {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 22px;
  align-items: center;
}

.panel {
  background: rgba(13,17,32,0.6);
  border: 1px solid var(--line);
  border-left: 5px solid var(--ember);
  padding: 14px 18px;
  width: 100%;
  box-sizing: border-box;
}

.panel.soft {
  background: rgba(245,238,225,0.08);
  border-left-color: var(--terracotta);
}

.panel h3, .panel .label {
  font-family: 'Inter', sans-serif;
  color: var(--ember);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin: 0 0 0.5rem 0;
}

.grid {
  display: grid;
  gap: 12px;
  width: 100%;
  margin-top: 12px;
}

.grid.two { grid-template-columns: 1fr 1fr; }
.grid.four { grid-template-columns: repeat(4, 1fr); }

.card {
  background: rgba(245,238,225,0.08);
  border: 1px solid var(--line);
  border-top: 4px solid var(--ember);
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
  background: var(--ember);
  color: var(--dusk-deeper);
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
  font-size: 1.75rem;
  line-height: 1.18;
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
  background: rgba(245,238,225,0.08);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 6px 14px;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--linen);
  letter-spacing: 0.03em;
}

.chain .arrow {
  color: var(--ember);
  font-size: 0.9rem;
}

</style>

<!-- _class: title -->

<div class="eyebrow">Chukwuma Theology &middot; Sermon Presentation</div>

# Under the Broom Tree

<div class="subtitle">Elijah, Depression, and the God Who Still Speaks</div>

<div class="accent-line"></div>

<p class="reference">Primary Text: 1 Kings 19:1-18</p>

<p class="credit">Opening Hymn: "What a Friend We Have in Jesus" &middot; Closing Hymn: "He Hideth My Soul"</p>

---

<div class="eyebrow">Sermon Frame</div>

## Theme &amp; Preaching Burden

<div class="accent-line"></div>

<div class="panel">
  <p class="label">Theme</p>
  <p class="wide">God does not abandon His exhausted servants; He meets them tenderly, corrects their distorted vision, and restores them to hope and mission.</p>
</div>

<div class="panel soft" style="margin-top: 12px;">
  <p class="label">Preaching Burden</p>
  <p class="wide">Spiritual victory does not make us invulnerable. Seasons of depression, burnout, and despair are not proof that God has left us.</p>
</div>

---

<!-- _class: quote -->

<div class="eyebrow">The sermon hook</div>

<div class="statement wide">"Sometimes the devil does not attack you before Mount Carmel. He waits until after the fire has fallen — after the prayer has been answered, after everybody around you assumes you should be strong."</div>

<p class="wide dim">Some of the deepest collapses in life happen not in open defeat, but in the strange silence that follows a public victory.</p>

---

<!-- _class: light -->

<div class="eyebrow">The big idea</div>

# God Answers Despair With Care, Not Shame

<div class="accent-line"></div>

<p class="wide">When Elijah collapses under the broom tree, God does not answer his despair with shame. He answers with <strong>care, presence, truth, and a future.</strong></p>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">I &middot; 1 Kings 19:1-4</div>
  <h2>Even Prophets Can Break Down</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Elijah moves from triumph on Carmel to fear, flight, isolation, and death-wish language — in the space of a single threat from Jezebel.</li>
    <li>Spiritual usefulness does not equal emotional invincibility.</li>
    <li>The prophet who stood before kings cannot stand before his own despair.</li>
  </ul>
</div>

<div class="panel soft">
  <p class="label">Adventist Application</p>
  <p class="wide">Remnant people are not superhuman people. The most spiritually useful season of your life does not inoculate you against collapse.</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">II &middot; 1 Kings 19:5-8</div>
  <h2>God Cares for the Whole Person First</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Before a single word of correction, God gives Elijah <strong>food, water, sleep, touch, and time.</strong></li>
    <li>An angel comes twice — not to rebuke him, but to feed him.</li>
    <li>God addresses Elijah's body before He addresses Elijah's theology.</li>
  </ul>
</div>

<div class="panel soft">
  <p class="label">Adventist Application</p>
  <p class="wide">Whole-person ministry matters. Body, mind, and spirit belong together — care for the exhausted is not a detour from the gospel, it is part of it.</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">III &middot; 1 Kings 19:9-13</div>
  <h2>Not in the Earthquake — in the Whisper</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Wind, earthquake, and fire pass by Horeb — spectacular, but God is not in them.</li>
    <li>The healing word comes quietly, in "a still small voice."</li>
    <li>God still speaks to discouraged people, and He often speaks gently.</li>
  </ul>
</div>

<div class="panel soft">
  <p class="label">Great Controversy Emphasis</p>
  <p class="wide">God's government is not built on coercion, noise, or manipulation. He wins hearts the same way He wins Elijah's — by whisper, not by force.</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">IV &middot; 1 Kings 19:14-18</div>
  <h2>God Corrects the Isolation, Restores the Mission</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Elijah insists: <em>"I alone am left."</em></li>
    <li>God reveals the seven thousand who have not bowed to Baal — a remnant Elijah could not see.</li>
    <li>God gives Elijah a fresh assignment. Restoration ends in mission, not just comfort.</li>
  </ul>
</div>

<div class="panel soft">
  <p class="label">Adventist Application</p>
  <p class="wide">The remnant is bigger than your despair can see. Isolation lies; God's family is wider than your worst moment lets you believe.</p>
</div>

---

<!-- _class: light -->

<div class="eyebrow">Four movements, one mercy</div>

# Closing Synthesis

<div class="accent-line"></div>

<div class="chain">
  <div class="step">1. Breakdown</div>
  <span class="arrow">&rarr;</span>
  <div class="step">2. Whole-Person Care</div>
  <span class="arrow">&rarr;</span>
  <div class="step">3. The Whisper</div>
  <span class="arrow">&rarr;</span>
  <div class="step">4. Restored Mission</div>
</div>

<div class="panel soft" style="margin-top: 16px;">
  <p class="label">Concluding Thought</p>
  <p class="wide">God does not rush from Elijah's collapse to Elijah's commission. He feeds him first, lets him rest, meets him gently, and only then sends him back out. Restoration has an order — and God will not skip it in you either.</p>
</div>

---

<!-- _class: blessing -->

<div class="eyebrow">The Appeal</div>

<div class="closing-summary">Come Out From Under the Broom Tree</div>

<p class="wide">Lord, some of us are sitting exactly where Elijah sat — not after defeat, but after victory nobody saw cost us anything. Teach us to come honestly to You instead of hiding in shame. Make Your church a people who bring bread, rest, presence, and truth to the exhausted among us. Help us to listen for Your whisper, and when You speak, give us the courage to rise and go. In Jesus' name, Amen.</p>

<p class="statement">You are not alone under the tree. Come out — He is already calling your name.</p>
