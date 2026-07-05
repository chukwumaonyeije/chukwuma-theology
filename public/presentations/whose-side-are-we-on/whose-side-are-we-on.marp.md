---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: Whose Side Are We On?
description: A Chukwuma Theology sermon presentation from Pastor Evan Knott's sermon at Atlanta North Seventh-day Adventist Church on Joshua 5:13-15, preached on July 4, 2026 — America's 250th Anniversary.
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

.stat {
  color: var(--gold);
  font-weight: 800;
}

</style>

<!-- _class: title -->

<div class="eyebrow">Atlanta North Seventh-day Adventist Church</div>

# Whose Side Are We On?

<div class="subtitle">Choosing allegiance to the Commander of the Lord's Army</div>

<div class="accent-line"></div>

<p class="reference">Key Scripture: Joshua 5:13-15</p>

<p class="credit">Sermon preached by Pastor Evan Knott at Atlanta North Seventh-day Adventist Church — July 4, 2026, America's 250th Anniversary</p>

---

<div class="eyebrow">America250</div>

## A Quarter Millennium of American Freedom

<div class="accent-line"></div>

<ul>
  <li>Parades, fireworks, and cookouts across America.</li>
  <li>250 years of independence — a remarkable experiment in liberty.</li>
  <li>Celebrating First Amendment freedoms: Sabbath, worship, and gospel proclamation.</li>
</ul>

<p class="dim"><em>These are freedoms we shouldn't take for granted.</em></p>

---

<!-- _class: light -->

<div class="eyebrow">The other side of the anniversary</div>

# But We Are Also Deeply Divided

<div class="accent-line"></div>

<ul>
  <li>Divided by race, gender, education, and geography.</li>
  <li>Political rhetoric: <strong>"If you're not for us, you're against us."</strong></li>
  <li>Friendships ended. Families torn apart.</li>
  <li>Even at the cookout, things get tense.</li>
</ul>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Not immune to the fracture</div>
  <h2>Christians Are Caught in the Crossfire</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Christians can be just as divided as everyone else.</li>
    <li>Social media: name-calling, propaganda, misinformation.</li>
    <li>Too often, our allegiance to a political party supersedes our allegiance to Christ.</li>
  </ul>
</div>

<div class="panel">
  <p class="wide"><em>"By this everyone will know that you are my disciples, if you have love for one another."</em></p>
  <p class="reference">— John 13:35</p>
</div>

---

<!-- _class: quote -->

<div class="eyebrow">Have we made Jesus a political ally?</div>

<ul class="small-list wide">
  <li>Turning political icons into idols.</li>
  <li>Treating political leaders as saviors.</li>
  <li>Assuming Jesus aligns with a specific political party.</li>
</ul>

<div class="statement">"Judging by the rhetoric, you might think Jesus' name is on the ballot."</div>

---

<div class="eyebrow">The text that changes everything</div>

## Joshua 5:13-15

<div class="accent-line"></div>

<div class="panel soft">
  <p class="wide">"Once when Joshua was by Jericho, he looked up and saw a man standing before him with a drawn sword in his hand. Joshua went to him and said, 'Are you one of us or one of our adversaries?' He replied, 'Neither; but as commander of the army of the LORD I have now come.' And Joshua fell on his face to the earth and worshiped... 'Remove the sandals from your feet, for the place where you stand is holy.'"</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Setting the scene</div>
  <h2>Joshua Faces the Walls of Jericho</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Israel has crossed the Jordan — but the hardest challenge is ahead.</li>
    <li>Jericho: massive, fortified, terrifying — walls they had never seen before.</li>
    <li>Joshua slips away at night to survey the city alone.</li>
    <li>Fear still lingers in the deeper regions of his heart.</li>
  </ul>
</div>

<div class="panel">
  <p class="dim">A general studying an enemy city in the dark, alone with his own uncertainty.</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">The encounter begins</div>
  <h2>A Man Armed for War</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>A figure appears in the darkness — sword already drawn.</li>
    <li>Joshua's military instinct: <em>"Are you for us or for our enemies?"</em></li>
    <li>The question assumes a binary: friend or foe, ally or adversary.</li>
    <li>This is the natural logic of a general assessing a stranger on a battlefield.</li>
  </ul>
</div>

<div class="panel soft">
  <p class="dim">The most reasonable military question in the world — and still the wrong one.</p>
</div>

---

<!-- _class: quote -->

<div class="eyebrow">The most surprising word in Scripture</div>

<div class="statement">"Neither. But as commander of the army of the Lord I have now come."</div>

<ul class="small-list wide">
  <li>He rejects the premise of the question entirely.</li>
  <li>He is not a combatant to be recruited — He is the Commander over Joshua.</li>
  <li>Joshua falls on his face and worships — recognizing divine authority.</li>
</ul>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Who is this Commander?</div>
  <h2>The Commander Is Christ</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>This is not just an angel — Joshua's worship is accepted (contrast Rev. 19:10).</li>
    <li>John 1:1 — "In the beginning was the Word... and the Word was God."</li>
    <li>The story of Jesus did not begin in a manger — He is the eternal Creator.</li>
    <li>Daniel 8:11 uses the same title for the pre-incarnate Christ.</li>
  </ul>
</div>

<div class="panel">
  <p class="label">SDA Theology</p>
  <p>Ellen White identifies this Commander as Christ Himself — "no common angel... the Son of God" (<em>Patriarchs and Prophets</em>, 491-492).</p>
</div>

---

<!-- _class: light -->

<div class="eyebrow">The correction</div>

# Jesus Is Not on Your Side

<div class="accent-line"></div>

<ul>
  <li>Jesus is not on your side. He is also not on your enemy's side.</li>
  <li>The sovereign God of the universe is far above any notion of sides we create.</li>
  <li>We reduce Jesus to a trump card, or a weapon for our quarrels.</li>
</ul>

<p class="dim">The real question was never "Is God on my side?" but <strong>"Am I on God's side?"</strong></p>

---

<div class="eyebrow">An enormous chasm of difference</div>

## Two Very Different Postures

<div class="accent-line"></div>

<div class="grid two">
  <div class="card">
    <h3>Believing God is on your side</h3>
    <p>You are in control. God is your ally.</p>
  </div>
  <div class="card alt">
    <h3>Choosing to be on God's side</h3>
    <p>God is in command. You are the servant.</p>
  </div>
</div>

<p class="dim">Joshua thought he was the commander of the Lord's army. Jesus corrected him: <em>"There is only one Commander — and it isn't you."</em></p>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">The command</div>
  <h2>The Call to Surrender</h2>
  <div class="accent-line"></div>
  <ul class="small-list">
    <li>Bare feet on rough terrain: no escape, no fallback plan.</li>
    <li>This is total surrender — no options kept open.</li>
    <li>Parallel to Moses at the burning bush (Exodus 3:5).</li>
    <li>SDA sanctuary theology: God's presence sanctifies space and demands reverence.</li>
  </ul>
</div>

<div class="panel">
  <p class="wide"><em>"Remove the sandals from your feet, for the place where you stand is holy."</em></p>
</div>

---

<div class="eyebrow">What does it actually mean?</div>

## What Does It Mean to Be on God's Side?

<div class="accent-line"></div>

<ul>
  <li><span class="stat">673 million</span> people are starving globally.</li>
  <li><span class="stat">36 million</span> Americans live in poverty.</li>
  <li>Racism, broken homes, abuse of power — these are real evils.</li>
  <li>Christians are called to holy anger and real action — not partisan bickering, but surrender-driven service.</li>
</ul>

<p class="dim"><em>"Whoever wants to become great among you must be your servant."</em> — Matthew 20:26</p>

---

<!-- _class: light -->

<div class="eyebrow">The hope ahead</div>

# He Is Coming Back

<div class="accent-line"></div>

<ul>
  <li>Jesus cares about every tear, every injustice, every human life.</li>
  <li>"His eye is on the sparrow — and His eye is on every human life."</li>
  <li>Jesus already has a sword in His hand.</li>
  <li>On a day coming very soon, He will break through the clouds of heaven and lead the angel armies to end sin, evil, and suffering once and forevermore.</li>
</ul>

---

<!-- _class: quote -->

<div class="eyebrow">The strongest position in the universe</div>

<div class="statement">The most powerful place you can be in this universe is at the feet of Jesus.</div>

<p class="wide">The strongest thing we can do in this life is surrender at the foot of the cross. While our nation fights for the soul of America — surrender your soul to Jesus Christ. Pledge your life to following the Commander of the Lord's Army.</p>

---

<div class="eyebrow">How the world will know</div>

## How the World Will Know

<div class="accent-line"></div>

<ul>
  <li>This church will not be known by how sure we are that we're right.</li>
  <li>We will be known by how we treat our neighbors whom we're convinced are wrong.</li>
  <li>Choose to be different in a divided world.</li>
</ul>

<p class="dim"><em>"By this everyone will know that you are my disciples, if you have love for one another."</em> — John 13:35</p>

---

<!-- _class: blessing -->

<div class="eyebrow">Closing prayer</div>

<div class="closing-summary">Lord, We Choose Your Side</div>

<p class="wide">Lord Jesus, You are the Commander of the Lord's Army. Today we recognize that You are not on our side — but we choose to be on Yours. Give us the courage to follow You in difficult circumstances. Give us the strength to surrender to You right now, so that we can show Your love to our neighbors. In Your precious and holy name, Amen.</p>

<p class="statement">Will you choose today to be on His side?</p>
