---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: Into Eternity
description: A Sabbath School presentation on the eschatological journey from the struggles of a fallen world to the glorious hope of the New Jerusalem. Atlanta North Seventh-day Adventist Church, June 22, 2026.
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --forest: #14221a;
  --forest-deep: #0d1712;
  --clay: #cf7654;
  --gold: #dfb143;
  --linen: #f5efe4;
  --muted: rgba(245,239,228,0.72);
  --line: rgba(245,239,228,0.18);
}

section {
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
  background:
    radial-gradient(circle at 78% 20%, rgba(223,177,67,0.22), transparent 32%),
    radial-gradient(circle at 20% 80%, rgba(207,118,84,0.18), transparent 34%),
    linear-gradient(135deg, var(--forest), var(--forest-deep));
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
  background: linear-gradient(90deg, var(--gold), var(--clay), var(--gold));
}

h1,
h2,
h3 {
  font-family: 'Playfair Display', serif;
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
em { color: var(--clay); }

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
  font-family: 'Playfair Display', serif;
  font-size: 24px;
  font-style: italic;
  color: var(--muted);
  max-width: 860px;
}

.credit,
.reference {
  color: rgba(245,239,228,0.58);
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
    linear-gradient(140deg, #e7d3b0, #81583a 48%, var(--forest-deep));
  color: var(--forest-deep);
}

section.light h1,
section.light h2,
section.light h3,
section.light p,
section.light li {
  color: var(--forest-deep);
}

section.light strong {
  color: #8c5e3c;
}

section.split {
  display: grid;
  grid-template-columns: 0.95fr 1.05fr;
  gap: 22px;
  align-items: center;
}

.panel {
  background: rgba(13,23,18,0.62);
  border: 1px solid var(--line);
  border-left: 5px solid var(--gold);
  padding: 14px 18px;
  width: 100%;
  box-sizing: border-box;
}

.panel.soft {
  background: rgba(245,239,228,0.08);
  border-left-color: var(--clay);
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
  background: rgba(245,239,228,0.08);
  border: 1px solid var(--line);
  border-top: 4px solid var(--gold);
  border-radius: 8px;
  padding: 13px 16px;
  box-sizing: border-box;
}

.card.alt {
  border-top-color: var(--clay);
  background: rgba(207,118,84,0.13);
}

.card.dark {
  background: rgba(13,23,18,0.72);
  border-top-color: var(--clay);
}

.card h3,
.label {
  font-family: 'Inter', sans-serif;
  color: var(--gold);
  font-size: 14px;
  font-weight: 800;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  margin: 0 0 8px 0;
}

.statement {
  font-family: 'Playfair Display', serif;
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
  font-family: 'Playfair Display', serif;
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
  background: rgba(223,177,67,0.22);
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
  background: rgba(223,177,67,0.14);
  border: 1px solid rgba(223,177,67,0.38);
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
  background: rgba(245,239,228,0.07);
  border: 1px solid var(--line);
  border-top: 4px solid var(--gold);
  border-radius: 8px;
  padding: 14px 14px;
  text-align: center;
}

.step.highlight {
  border-top-color: #f5d47a;
  background: rgba(223,177,67,0.18);
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

<div class="eyebrow">Atlanta North Seventh-day Adventist Church · Sabbath School · June 22, 2026</div>

# Into Eternity

<div class="subtitle">Growing in a Relationship With God</div>

<div class="accent-line"></div>

<p class="reference">The eschatological journey from the struggles of a fallen world to the glorious hope of the New Jerusalem.</p>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">The Core Tension</div>
  <h2>Living Between Two Realms</h2>
  <div class="accent-line"></div>
  <p><strong>The Present Reality:</strong></p>
  <ul>
    <li>The world is heaving and groaning with wars, famines, earthquakes, and intensifying persecution (Matt. 24:6-11).</li>
    <li>Life is brief — a vapor that appears for a little time and then vanishes (James 4:13-14).</li>
  </ul>
</div>

<div class="panel">
  <p><strong>The Eternal Hope:</strong></p>
  <br/>
  <ul>
    <li><em>"Beloved, now we are children of God"</em> (1 John 3:2).</li>
    <li>God has placed eternity in our hearts (Eccl. 3:11).</li>
    <li>Jesus is faithful; His promises of salvation and presence are true, regardless of our earthly timeline.</li>
  </ul>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Spiritual Renewal</div>
  <h2>The Mechanics of Revival</h2>
  <div class="accent-line"></div>
  <p><strong>Revival</strong> is a renewal of spiritual life, initiated by the Holy Spirit and sustained by grace.</p>
  <br/>
  <div class="takeaway">The catalyst is driven by prayer and a deep hunger for the Word, crying out: <em>"Cause Your face to shine, and we shall be saved!"</em> (Psalm 80:3).</div>
</div>

<div class="panel soft">
  <p><strong>The Mechanics:</strong></p>
  <ul>
    <li><strong>The Process:</strong> The renewal of God’s grace created by the Holy Spirit.</li>
    <li><strong>The Goal:</strong> Preparing believers to live comfortably in the new current of the New Jerusalem.</li>
  </ul>
</div>

---

<div class="eyebrow">End-Times Checklist</div>

## Living in the End Times

<div class="accent-line"></div>

<div class="grid three">
  <div class="card">
    <h3>1. Be Prepared</h3>
    <p>Cast off darkness and put on the armor of light. Live knowing Christ's return is imminent.</p>
  </div>
  <div class="card alt">
    <h3>2. Be Persevering</h3>
    <p>Endure trials and persecution faithfully to receive the crown of life.</p>
  </div>
  <div class="card">
    <h3>3. Be Focused</h3>
    <p>Put on Christ and ignore fleshly distractions; watch the signs of the times.</p>
  </div>
</div>

<div class="grid two" style="margin-top: 15px;">
  <div class="card alt">
    <h3>4. Be Revived</h3>
    <p>Seek personal and congregational renewal daily through the Holy Spirit.</p>
  </div>
  <div class="card">
    <h3>5. Be Prayerful</h3>
    <p>Maintain constant, Enoch-like communion with God in every circumstance.</p>
  </div>
</div>

---

<div class="eyebrow">The Blessed Hope</div>

## The Anatomy of the Return

<div class="accent-line"></div>

<p>The return of Christ is not a quiet event; it is the physical culmination of history.</p>

<div class="step-row">
  <div class="step">
    <div class="step-num">Step 1</div>
    <h3>The Cloud</h3>
    <p>A small black cloud in the eastern sky, growing brighter.</p>
  </div>
  <div class="step">
    <div class="step-num">Step 2</div>
    <h3>The King</h3>
    <p>The Son of man appears with a sharp sickle (Rev. 14:14).</p>
  </div>
  <div class="step">
    <div class="step-num">Step 3</div>
    <h3>The Call</h3>
    <p>A shout and the trumpet of God echo across the earth.</p>
  </div>
  <div class="step">
    <div class="step-num">Step 4</div>
    <h3>Resurrection</h3>
    <p>Tombs of those asleep in Christ open first (1 Thess. 4:16).</p>
  </div>
  <div class="step highlight">
    <div class="step-num">Step 5</div>
    <h3>Change</h3>
    <p>The living are transformed, gaining immortality.</p>
  </div>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Eternal Fellowship</div>
  <h2>Finally, Face-to-Face</h2>
  <div class="accent-line"></div>
  <p><strong>The End of the Wait:</strong></p>
  <p>Every persevering prayer, trial, and prioritized moment culminates in seeing His face.</p>
  <p><em>"We shall see Him as He is."</em> (1 John 3:2)</p>
</div>

<div class="panel">
  <p><strong>The Defining Mark:</strong></p>
  <p>His name shall be on their foreheads (Rev. 22:4) — meaning we will always be thinking of Him and reflecting His character.</p>
  <br/>
  <p><strong>The Great Confession:</strong></p>
  <p>We will hear His voice and confess that He is Lord to the glory of God (Phil. 2:10-11).</p>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">The Metaphor</div>
  <h2>The Bride of Christ</h2>
  <div class="accent-line"></div>
  <p>Why do God's people and the New Jerusalem share the title of the <strong>"Bride"</strong>?</p>
  <br/>
  <p>This beautiful description signifies the intimate, inseparable connection between God's people and the city they inhabit. Jesus unites His people to Himself within this glorious gift.</p>
</div>

<div class="panel soft">
  <ul>
    <li><strong>God's People (The Saints):</strong> Prepared, revived, and adorned for her husband (Rev. 19:7).</li>
    <li><strong>The Capital City:</strong> The New Jerusalem, coming down out of heaven (Rev. 21:2).</li>
  </ul>
</div>

---

<div class="eyebrow">The New Jerusalem</div>

## The Architecture of Restoration

<div class="accent-line"></div>

<p class="wide">The New Jerusalem is not a human achievement, but a glorious, incomprehensible gift from God.</p>

<div class="grid three">
  <div class="card">
    <h3>The 12 Gates</h3>
    <p>Representing God's desire to invite all people — regardless of past failures — into His presence.</p>
  </div>
  <div class="card alt">
    <h3>Absence of Sorrow</h3>
    <p>There shall be no more death, nor sorrow, nor crying, for the former things have passed away (Rev. 21:4).</p>
  </div>
  <div class="card">
    <h3>Living Fountains</h3>
    <p>The provision of eternal sustenance and the pure, heavenly current of grace flowing from the throne.</p>
  </div>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">Discipleship</div>
  <h2>Following the Lamb</h2>
  <div class="accent-line"></div>
  <p class="subtitle">"If we want to follow Him in heaven, we must first follow Him here on earth."</p>
</div>

<div class="grid two">
  <div class="card dark">
    <h3>The Present Walk</h3>
    <p>Following Jesus as the Lamb of God through the trials, suffering, and heaving of a fallen world.</p>
    <div class="takeaway" style="font-size: 15px; margin-top: 5px;"><strong>Action:</strong> Learning to know His voice through His Word today so we recognize it when He calls.</div>
  </div>
  <div class="card alt">
    <h3>The Eternal Walk</h3>
    <p>The Lamb in the midst of the throne will shepherd them and lead them to living fountains (Rev. 7:17).</p>
    <div class="takeaway" style="font-size: 15px; margin-top: 5px; background: rgba(207,118,84,0.14); border-left-color: var(--clay);"><strong>Action:</strong> A joyous, unending exploration of heaven, guided forever by the One who saved us.</div>
  </div>
</div>

---

<!-- _class: split -->

<div>
  <div class="eyebrow">A Modern Story</div>
  <h2>Amelia's Mission: Living the Hope</h2>
  <div class="accent-line"></div>
  <p><strong>Stage 1: Despair</strong></p>
  <p>Struggling with mental health and deep pain, Amelia could not envision a future.</p>
  <p><strong>Stage 2: Surrender</strong></p>
  <p>Claiming Psalm 37:5, she prayed: <em>"I will work for you, Lord, if You help me out of this problem."</em></p>
</div>

<div class="panel">
  <p><strong>Stage 3: Mission</strong></p>
  <p>She became a Global Mission pioneer, teaching and leading worship in a remote mountain village.</p>
  <br/>
  <p><strong>Stage 4: Perseverance</strong></p>
  <p>Faced with severe opposition and witchcraft from a village leader, she knelt at the altar for strength, remained faithful, and witnessed the power of God.</p>
</div>

---

<!-- _class: quote -->

<div class="eyebrow">The Call</div>

<div class="statement">"And the Spirit and the bride say, Come!"</div>

<p class="reference">"And let him who hears say, Come! And let him who thirsts come. Whoever desires, let him take the water of life freely." (Rev. 22:17)</p>

<div class="grid three" style="margin-top: 20px; text-align: left;">
  <div class="card">
    <h3>The Spirit</h3>
    <p>Draws us; Jesus promises, <em>"Who comes to Me I will by no means cast out."</em></p>
  </div>
  <div class="card alt">
    <h3>The Church</h3>
    <p>As the Bride, the church extends the call to the world.</p>
  </div>
  <div class="card">
    <h3>The Individual</h3>
    <p>Tasked with inviting others into a saving relationship.</p>
  </div>
</div>

<div class="takeaway" style="margin-top: 15px;"><strong>The Cost:</strong> The invitation is entirely free — a gift of pure grace.</div>

---

<div class="eyebrow">Master Synthesis</div>

## The Arc of Eternity

<div class="accent-line"></div>

| **Stage** | **The State of Fellowship** | **The Divine Action** |
|---|---|---|
| **Eden Lost** | We were made for closeness (Gen. 2:7), but sin shattered our face-to-face communion. | **Initiation:** God seeks the lost, promising redemption. |
| **Great Controversy** | Living between realms; heaving world; trials and refinement. | **Refinement:** Culminates in the cross; Holy Spirit revival. |
| **New Jerusalem** | Fellowship fully restored; no more pain or death; access to the Tree of Life. | **Restoration:** Guided to living fountains of water. |

<div class="takeaway"><em>"Being confident of this very thing, that He who has begun a good work in you will complete it."</em> (Philippians 1:6)</div>

---

<!-- _class: blessing -->

<div class="eyebrow">The Hope</div>

<div class="closing-summary">"Surely I am coming quickly."</div>

<div class="accent-line"></div>

<div class="statement">Amen. Even so, come, Lord Jesus.</div>

<p class="reference">Revelation 22:20</p>

<p class="dim" style="margin-top: 20px;">Keep this desire alive, ever before you, in faith and in trust in the love and goodness of God.</p>
