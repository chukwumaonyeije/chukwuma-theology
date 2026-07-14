---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: "The Door of Reconciliation — Chancing Our Arms for the Peace of Christ"
description: "A Chukwuma Theology sermon presentation by Pastor Evan Knott on the historic 'chancing your arm' story at St. Patrick's Cathedral and Ephesians 2 — how Christ's cross opens the door between enemies and calls the church to become partners of peace."
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --wood: #241a12;
  --wood-deep: #150f0a;
  --wood-deeper: #0d0a06;
  --gold: #d9b06a;
  --amber: #c8863f;
  --ember: #e2a75a;
  --parchment: #f3e9d2;
  --dim: rgba(243,233,210,0.72);
  --line: rgba(243,233,210,0.16);
}

section {
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
  font-size: 20px;
  background:
    radial-gradient(circle at 88% 10%, rgba(226,167,90,0.24), transparent 32%),
    radial-gradient(circle at 6% 92%, rgba(200,134,63,0.16), transparent 34%),
    linear-gradient(155deg, var(--wood), var(--wood-deeper));
  color: var(--parchment);
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
  background: linear-gradient(90deg, var(--ember), var(--amber), var(--gold));
}

h1, h2, h3 {
  font-family: 'Playfair Display', serif;
  margin: 0 0 0.2em 0;
  color: var(--parchment);
  line-height: 1.14;
}

h1 { font-size: 2.5rem; max-width: 1040px; }
h2 { font-size: 1.8rem; max-width: 1040px; }
h3 { font-size: 1.1rem; }

p {
  font-size: 1rem;
  line-height: 1.5;
  margin: 0.2em 0 0.5em 0;
  color: var(--parchment);
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
  content: '\2020';
  position: absolute;
  left: 0;
  color: var(--ember);
  font-weight: 800;
  font-size: 0.85em;
}

strong { color: var(--ember); }
em { color: #e8c78f; }

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
  color: rgba(243,233,210,0.6);
  letter-spacing: 0.02em;
  line-height: 1.4;
}

section.title, section.quote, section.blessing {
  text-align: center;
  align-items: center;
  padding: 34px 62px;
}

section.title h1 {
  font-size: 2.85rem;
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
    radial-gradient(circle at 80% 16%, rgba(255,241,214,0.28), transparent 26%),
    linear-gradient(140deg, #e9d3a4, #8a5a2c 48%, var(--wood-deeper));
}

section.split {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 22px;
  align-items: center;
}

.panel {
  background: rgba(13,10,6,0.6);
  border: 1px solid var(--line);
  border-left: 5px solid var(--ember);
  padding: 14px 18px;
  width: 100%;
  box-sizing: border-box;
}

.panel.soft {
  background: rgba(243,233,210,0.08);
  border-left-color: var(--amber);
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
  background: rgba(243,233,210,0.08);
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
  color: var(--wood-deeper);
  font-weight: 800;
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
}

.card h4 {
  font-family: 'Playfair Display', serif;
  font-size: 0.92rem;
  margin: 0 0 0.3rem 0;
  line-height: 1.2;
  color: var(--parchment);
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
  font-size: 1.7rem;
  line-height: 1.2;
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

.door-mark {
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  color: var(--ember);
  margin-bottom: 0.3rem;
}

</style>

<!-- _class: title -->

<div class="eyebrow">Chukwuma Theology &middot; Sermon Presentation</div>

<div class="door-mark">&#10022;</div>

# The Door of Reconciliation

<div class="subtitle">Chancing Our Arms for the Peace of Christ</div>

<div class="accent-line"></div>

<p class="reference">Primary Texts: Ephesians 2:14-19 &middot; Galatians 3:26-29 &middot; Matthew 5:44</p>

<p class="credit">Sermon by Pastor Evan Knott &middot; Atlanta North Seventh-day Adventist Church &middot; July 11, 2026</p>

---

<div class="eyebrow">I &middot; A History Lesson</div>

## A Feud at the Cathedral Door

<div class="accent-line"></div>

<ul>
  <li>In 1492, the rival Fitzgerald and Butler families brought their conflict to Dublin.</li>
  <li>Defeated Butler forces sought sanctuary inside St. Patrick's Cathedral.</li>
  <li>A bolted chapter-house door became the final barrier between enemies.</li>
  <li>The question was no longer who would win, but whether the bloodshed would ever end.</li>
</ul>

---

<!-- _class: light -->

<div class="eyebrow">How division hardens</div>

# When Rivalry Becomes Hostility

<div class="accent-line"></div>

<ul class="small-list">
  <li>Competition for land, influence, and political office hardened into generational hatred.</li>
  <li>Each family believed its claim was right and the other side could not be trusted.</li>
  <li>Threats, posturing, and violence replaced dialogue.</li>
  <li>Division became self-sustaining: every injury justified the next.</li>
</ul>

---

<div class="eyebrow">II &middot; The Turning Point</div>

## An Arm Extended in Peace

<div class="accent-line"></div>

<ul>
  <li>Gerald Fitzgerald reconsidered the cost of continuing the feud.</li>
  <li>He cut a hole through the cathedral door and pushed his unprotected arm through it.</li>
  <li>James Butler recognized the vulnerability as proof that the offer of peace was genuine.</li>
  <li>The enemies shook hands through the opening, and reconciliation began.</li>
</ul>

---

<!-- _class: quote -->

<div class="eyebrow">The phrase it gave us</div>

<div class="statement wide">The historic door still stands at St. Patrick's Cathedral — a witness to reconciliation, and the origin of the phrase "to chance one's arm."</div>

<p class="wide dim">Peace required more than words; someone had to risk safety, pride, and control. Reconciliation begins when one person chooses courageous vulnerability.</p>

---

<div class="eyebrow">III &middot; Naming Our Moment</div>

## A World Trained to Divide

<div class="accent-line"></div>

<ul>
  <li>Polarized media environments give neighbors radically different pictures of reality.</li>
  <li>Difference is not the enemy; contempt for those who differ is the deeper danger.</li>
  <li>Echo chambers teach us to interpret neighbors as threats rather than people.</li>
  <li>Ideological purity is celebrated while listening and common ground are dismissed.</li>
</ul>

---

<!-- _class: light -->

# Peace Can Begin in the Church

<div class="accent-line"></div>

<ul class="small-list">
  <li>Christians are called to follow Jesus before following political tribes or cultural loyalties.</li>
  <li>The church should be known for sacrificial love, patient listening, and prayerful presence.</li>
  <li>Followers of Christ must resist protecting self-interest beneath the language of righteousness.</li>
  <li>God's people are invited to become agents of healing in divided communities.</li>
</ul>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">IV &middot; Matthew 5:44</div>
  <h2>Love Crosses Enemy Lines</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Jesus does not merely ask believers to tolerate enemies.</li>
    <li>He calls for active blessing, goodness, and prayer.</li>
    <li>Christian peacemaking begins by seeing an opponent as a neighbor whom God loves.</li>
  </ul>
</div>

<div class="panel soft">
  <p class="label">Scripture</p>
  <p class="wide">"Love your enemies, bless those who curse you, do good to those who hate you, and pray for those who spitefully use you and persecute you." &mdash; Matthew 5:44</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">V &middot; Galatians 3:26-29</div>
  <h2>In Christ, We Are One</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Through faith, believers become children of God and are clothed with Christ.</li>
    <li>Human distinctions no longer determine spiritual worth or belonging.</li>
    <li>In Christ, divided people become one family and heirs of the promise.</li>
  </ul>
</div>

<div class="panel soft">
  <p class="label">Scripture</p>
  <p class="wide">"There is no longer Jew or Greek... slave or free... male and female" &mdash; for you are all one in Christ Jesus. Galatians 3:26-29</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">VI &middot; Ephesians 2:14</div>
  <h2>Jesus Is Our Peace</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Sin separates humanity from God and turns people against one another.</li>
    <li>Jesus does not simply announce peace; He embodies and creates it.</li>
    <li>In His flesh, hostility is confronted and a new humanity is formed.</li>
  </ul>
</div>

<div class="panel soft">
  <p class="label">Scripture</p>
  <p class="wide">"For He is our peace... and has broken down the dividing wall, that is, the hostility between us." &mdash; Ephesians 2:14</p>
</div>

---

<div class="eyebrow">VII &middot; Ephesians 2:14-19</div>

## Reconciled Through the Cross

<div class="accent-line"></div>

<ul>
  <li>Through the cross, Jesus reconciles divided people to God in one body.</li>
  <li>Those once far away and those once near receive the same access to the Father.</li>
  <li>Strangers become fellow citizens, saints, and members of God's household.</li>
  <li>Communion with God creates the foundation for communion with one another.</li>
</ul>

---

<!-- _class: light -->

# Christ Chanced More Than an Arm

<div class="accent-line"></div>

<ul class="small-list">
  <li>Gerald Fitzgerald risked an arm to end a feud; Jesus gave His whole life to rescue His enemies.</li>
  <li>Humanity built walls of sin, alienation, and distrust.</li>
  <li>Jesus left the safety of heaven and crossed the barrier we could not cross.</li>
  <li>His sacrifice proves that God's offer of reconciliation is genuine.</li>
</ul>

---

<div class="eyebrow">VIII &middot; Calvary</div>

## The Cross Opens the Door

<div class="accent-line"></div>

<ul>
  <li>At Calvary, Jesus took the "axe" to the door of sin separating humanity from God.</li>
  <li>He bore our sin, was nailed to the cross, bled, and died.</li>
  <li>He rose again so that reconciliation would become living reality, not distant hope.</li>
  <li>Christ now extends His hand with an offer of rescue, life, and peace.</li>
</ul>

---

<!-- _class: quote -->

<div class="eyebrow">The Invitation</div>

<div class="statement wide">Take the Hand of Christ</div>

<p class="wide dim">Jesus' invitation can be accepted or rejected; love never removes the dignity of choice. His peace surpasses what political victory, personal control, or worldly security can offer. Receiving His hand means trusting His grace and entering the household of God. Reconciliation with others begins by first being reconciled to God.</p>

---

<!-- _class: light -->

<div class="eyebrow">IX &middot; The Charge</div>

# Become Partners of Peace

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <div class="num">1</div>
    <h4>Listen more than you preach.</h4>
  </div>
  <div class="card">
    <div class="num">2</div>
    <h4>Pray for neighbors more than you argue online.</h4>
  </div>
  <div class="card">
    <div class="num">3</div>
    <h4>Step beyond comfort to enter another person's experience with compassion.</h4>
  </div>
  <div class="card">
    <div class="num">4</div>
    <h4>Find creative, sacrificial ways to weaken the barriers dividing your community.</h4>
  </div>
</div>

---

<div class="eyebrow">X &middot; The Practice</div>

## Chance Your Arm

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h4>Risk Pride</h4>
    <p>By initiating the first honest conversation.</p>
  </div>
  <div class="card">
    <h4>Risk Certainty</h4>
    <p>By listening before preparing a rebuttal.</p>
  </div>
  <div class="card">
    <h4>Risk Comfort</h4>
    <p>By serving someone outside your familiar circle.</p>
  </div>
  <div class="card">
    <h4>Risk Being Misunderstood</h4>
    <p>By blessing an enemy in the spirit of Jesus.</p>
  </div>
</div>

---

<!-- _class: light -->

# Love Makes the First Move

<div class="accent-line"></div>

<ul class="small-list">
  <li>If Jesus loves me, I can learn to love my neighbor.</li>
  <li>If Jesus left heaven for me, I can step outside my comfort zone for another.</li>
  <li>If Jesus extended peace to me, I can extend peace even to an enemy.</li>
  <li>The courage to reconcile is a response to grace, not an achievement of willpower.</li>
</ul>

---

<div class="eyebrow">XI &middot; The Ordinance of Humility</div>

## Communion Without Barriers

<div class="accent-line"></div>

<ul>
  <li>The ordinance of humility gives reconciliation a physical expression.</li>
  <li>Washing another person's feet requires us to bend low and serve with our own hands.</li>
  <li>Communion remembers Christ's broken body and celebrates one reconciled household.</li>
  <li>At the Lord's table, former strangers receive one bread, one cup, and one peace.</li>
</ul>

---

<!-- _class: blessing -->

<div class="eyebrow">The Appeal</div>

<div class="closing-summary">The Hand Is Extended</div>

<p class="wide">Jesus is at the door today. Take His hand.</p>

<div class="panel soft" style="margin-top: 16px; text-align: left;">
  <p class="wide">Receive the peace of Christ. Extend that peace to your neighbor. Become a partner of reconciliation in a divided world.</p>
</div>

<p class="statement" style="margin-top: 14px;">Chance your arm. He already chanced His life.</p>
