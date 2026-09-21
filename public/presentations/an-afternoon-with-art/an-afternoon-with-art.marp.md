---
marp: true
theme: uncover
size: 16:9
paginate: false
html: true
title: "An Afternoon With Art — Encounters at the Art Institute of Chicago"
description: "A reflective journey through the Art Institute of Chicago by Dr. Chukwuma I. Onyeije — exploring 14 encounters with art, faith, fatherhood, medicine, technology, and family memory."
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,600&family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
  --wood: #241a12;
  --wood-deep: #150f0a;
  --wood-deeper: #0d0a06;
  --gold: #d9b06a;
  --amber: #c8863f;
  --ember: #e2a75a;
  --parchment: #f3e9d2;
  --dim: rgba(243,233,210,0.78);
  --line: rgba(243,233,210,0.18);
  --card-bg: rgba(13, 10, 6, 0.72);
}

section {
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  background:
    radial-gradient(circle at 88% 10%, rgba(226,167,90,0.22), transparent 34%),
    radial-gradient(circle at 6% 92%, rgba(200,134,63,0.15), transparent 36%),
    linear-gradient(155deg, var(--wood), var(--wood-deeper));
  color: var(--parchment);
  padding: 32px 52px;
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

h1, h2, h3, h4 {
  font-family: 'Playfair Display', serif;
  margin: 0 0 0.2em 0;
  color: var(--parchment);
  line-height: 1.15;
}

h1 { font-size: 2.35rem; max-width: 1080px; }
h2 { font-size: 1.7rem; max-width: 1040px; }
h3 { font-size: 1.15rem; }
h4 { font-size: 0.95rem; }

p {
  font-size: 0.92rem;
  line-height: 1.48;
  margin: 0.2em 0 0.5em 0;
  color: var(--parchment);
}

ul, ol {
  list-style: none;
  padding: 0;
  margin: 0.3em 0 0 0;
}

li {
  position: relative;
  padding: 0.15em 0 0.15em 1.2em;
  line-height: 1.42;
  font-size: 0.88rem;
}

li::before {
  content: '✦';
  position: absolute;
  left: 0;
  color: var(--ember);
  font-size: 0.75em;
  top: 0.2em;
}

strong { color: var(--ember); font-weight: 700; }
em { color: #eed5a8; font-style: italic; }

.eyebrow {
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--ember);
  margin-bottom: 0.5rem;
}

.accent-line {
  width: 48px;
  height: 3px;
  background: var(--ember);
  margin: 0.3rem 0 0.8rem 0;
}

.subtitle {
  max-width: 900px;
  font-family: 'Playfair Display', serif;
  font-size: 1.15rem;
  font-style: italic;
  line-height: 1.45;
  color: var(--dim);
}

.credit {
  font-size: 0.8rem;
  color: rgba(243,233,210,0.65);
  letter-spacing: 0.04em;
  margin-top: 0.8rem;
}

/* Slide Specific Layouts */
section.title {
  text-align: center;
  align-items: center;
  padding: 40px 60px;
}

section.title h1 {
  font-size: 2.85rem;
  margin-bottom: 0.3rem;
}

section.title .accent-line {
  margin-left: auto;
  margin-right: auto;
}

section.split {
  display: grid;
  grid-template-columns: 0.85fr 1.15fr;
  gap: 28px;
  align-items: center;
  padding: 24px 44px;
}

section.split.reverse {
  grid-template-columns: 1.15fr 0.85fr;
}

.art-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.art-img {
  max-height: 480px;
  max-width: 100%;
  object-fit: contain;
  border-radius: 8px;
  border: 1px solid var(--line);
  box-shadow: 0 12px 32px rgba(0,0,0,0.55);
}

.art-caption {
  font-size: 0.72rem;
  color: var(--dim);
  font-style: italic;
  margin-top: 8px;
  text-align: center;
  max-width: 90%;
}

.content-col {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.panel {
  background: var(--card-bg);
  border: 1px solid var(--line);
  border-left: 4px solid var(--ember);
  border-radius: 6px;
  padding: 12px 16px;
  margin-bottom: 10px;
  box-sizing: border-box;
}

.panel:last-child {
  margin-bottom: 0;
}

.panel-title {
  font-family: 'Inter', sans-serif;
  color: var(--ember);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.panel-text {
  font-size: 0.84rem;
  line-height: 1.42;
  color: var(--parchment);
  margin: 0;
}

.statement {
  font-family: 'Playfair Display', serif;
  font-size: 1.35rem;
  line-height: 1.3;
  color: var(--parchment);
  font-weight: 600;
}

.quote-box {
  background: rgba(217, 176, 106, 0.08);
  border-left: 3px solid var(--gold);
  padding: 10px 14px;
  border-radius: 4px;
  margin-top: 8px;
}

.quote-box p {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 0.95rem;
  color: #f7edd8;
  margin: 0;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  width: 100%;
  margin-top: 14px;
}

.card {
  background: var(--card-bg);
  border: 1px solid var(--line);
  border-top: 3px solid var(--ember);
  border-radius: 6px;
  padding: 14px;
  display: flex;
  flex-direction: column;
}

.card-num {
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--ember);
  letter-spacing: 0.1em;
  margin-bottom: 6px;
  text-transform: uppercase;
}

.card h4 {
  color: var(--parchment);
  margin-bottom: 6px;
  font-size: 0.95rem;
}

.card p {
  font-size: 0.78rem;
  color: var(--dim);
  line-height: 1.4;
  margin: 0;
}
</style>

<!-- Slide 1: Title -->
<!-- _class: title -->
<div class="eyebrow">ART INSTITUTE OF CHICAGO · SEPTEMBER 2026</div>
<h1>An Afternoon With Art</h1>
<div class="accent-line"></div>
<p class="subtitle">A family, a birthday, and an unexpected afternoon at the Art Institute of Chicago</p>
<div class="credit">Dr. Chukwuma I. Onyeije, MD, FACOG · Chukwuma Theology</div>

---

<!-- Slide 2: Before the Paintings -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/00-chicago-street.jpeg" alt="Chicago in the rain" class="art-img" />
  <div class="art-caption">Chicago · September 2026</div>
</div>
<div class="content-col">
  <div class="eyebrow">PROLOGUE</div>
  <h2>Before the Paintings</h2>
  <div class="accent-line"></div>
  <p><strong>The trip came first.</strong> We were in Chicago because my youngest son, Chidiebere, was turning twenty-four. Chi Chi and I had come with our three sons: <strong>Obi, Nnamdi, and Chidiebere</strong>.</p>
  <p>It was a chilly, rainy day — the kind that made several hours inside the Art Institute feel like a particularly good idea.</p>
  <div class="quote-box">
    <p>"I did not go into the museum intending to write a book. I was a father spending a weekend with his family. That matters, because the family context changed what I saw — especially before Abraham and Isaac."</p>
  </div>
  <p style="font-size: 0.8rem; color: var(--dim); margin-top: 8px;">There is something increasingly precious about getting all of us into the same place. Five adults moving through Chicago together.</p>
</div>

---

<!-- Slide 3: How I Want to Remember It -->
<div class="eyebrow">THE METHOD OF ENCOUNTER</div>
<h2>How I Want to Remember It</h2>
<div class="accent-line"></div>
<p style="margin-bottom: 8px;">Three distinct things were happening simultaneously with every canvas and sculpture:</p>

<div class="grid-3">
  <div class="card">
    <div class="card-num">Layer 01</div>
    <h4>What the Museum Told Me</h4>
    <p>Names, dates, materials, artistic movements, and formal histories. I needed that information, but I did not want it to become the only voice.</p>
  </div>
  <div class="card">
    <div class="card-num">Layer 02</div>
    <h4>What I Actually Saw</h4>
    <p>Faces, surfaces, scale, color, awkward details, brushwork, and reflections — things that made me walk closer or step back before I knew why they mattered.</p>
  </div>
  <div class="card">
    <div class="card-num">Layer 03</div>
    <h4>What It Caused Me to Think About</h4>
    <p>Fatherhood. Faith. Medicine. Nigeria. Technology. Labor. Aging. Mortality. Sometimes nothing grand — only honest wonder, surprise, or confusion.</p>
  </div>
</div>

<div class="quote-box" style="margin-top: 14px; width: 100%; box-sizing: border-box;">
  <p>"I do not want every work neatly decoded. Sometimes the most accurate sentence is simply: <em>I am still not sure what I think about this.</em>"</p>
</div>

---

<!-- Slide 4: 01 Abraham -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/01-restout-abraham.jpeg" alt="Jean II Restout - The Sacrifice of Abraham" class="art-img" />
  <div class="art-caption">Jean II Restout · The Sacrifice of Abraham (1746)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 01 · SACRED ART & FATHERHOOD</div>
  <h2>Abraham: The Hand That Held the Knife</h2>
  <div class="accent-line"></div>
  
  <div class="panel">
    <div class="panel-title">A Father Before Moriah</div>
    <p class="panel-text">It was the anguish in Abraham's face that stayed with me. Having read Genesis 22 for decades, standing with my three adult sons in the museum, I stopped seeing Abraham primarily as an ancient patriarch and saw him as a father.</p>
  </div>

  <div class="panel">
    <div class="panel-title">The Two Hands</div>
    <p class="panel-text">One hand holds the sacrificial knife high in mid-air. The other hand cradles Isaac's head tenderly upon the altar — shielding his boy even while the blade is poised.</p>
  </div>

  <div class="quote-box">
    <p>"The painting made me remain in the moment Scripture moves through quickly: the son, the father, the knife, and the interruption. Art made the story human again."</p>
  </div>
</div>

---

<!-- Slide 5: 02 Seurat -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/02-seurat-la-grande-jatte_1.jpeg" alt="Georges Seurat - A Sunday on La Grande Jatte" class="art-img" />
  <div class="art-caption">Georges Seurat · A Sunday on La Grande Jatte — 1884 (1884–86)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 02 · SCALE & CLINICAL GAZE</div>
  <h2>From Across the Room</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">What I Saw</div>
    <p class="panel-text">From a distance there was an entire cohesive world: people, water, umbrellas, sunlight. Up close, that coherent world dissolved into isolated dots of pure pigment.</p>
  </div>

  <div class="panel">
    <div class="panel-title">What the Museum Told Me</div>
    <p class="panel-text">Points of pure color designed to mix in the viewer's eye; Seurat seeking a modern, timeless Parisian harmony through rigorous pointillist technique.</p>
  </div>

  <div class="panel">
    <div class="panel-title">The Lesson for Medicine</div>
    <p class="panel-text">A measurement can be true. A lab value can be true. A diagnosis can be true. <strong>But so is the human being that appears only when you step back far enough.</strong></p>
  </div>
</div>

---

<!-- Slide 6: 03 Van Gogh -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/03-van-gogh-self-portrait.jpeg" alt="Vincent van Gogh - Self-Portrait" class="art-img" />
  <div class="art-caption">Vincent van Gogh · Self-Portrait (1887)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 03 · BIOGRAPHY & PRESENCE</div>
  <h2>A Face I Thought I Knew</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Meeting the Paint Before the Myth</div>
    <p class="panel-text">Van Gogh is so familiar that it is easy to meet the tragic biography before meeting the paint. In person, what struck me was the surface: short, urgent dabs of pigment vibrating around the face and coat.</p>
  </div>

  <div class="panel">
    <div class="panel-title">Responding to Paris</div>
    <p class="panel-text">Seen just after Seurat, the connection was alive: Van Gogh adapting pointillist experiments to his own restless, searching rhythm.</p>
  </div>

  <div class="quote-box">
    <p>"This was simply a man looking at himself — and, because he painted the encounter, allowing strangers more than a century later to look back."</p>
  </div>
</div>

---

<!-- Slide 7: 04 Marcus-Bello Bench -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/04-marcus-bello-friction-ridge-bench.jpeg" alt="Nifemi Marcus-Bello - Friction Ridge Bench" class="art-img" />
  <div class="art-caption">Nifemi Marcus-Bello · Friction Ridge Bench, Orikì (Act I)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 04 · CONTEMPORARY NIGERIAN DESIGN</div>
  <h2>A Fingerprint Large Enough to Sit On</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Monumental Human Trace</div>
    <p class="panel-text">I first saw an unusual bench. Then I saw the fingerprint. Something normally confined to the tip of a finger had become monumental.</p>
  </div>

  <div class="panel">
    <div class="panel-title">Contemporary Africa in the Museum</div>
    <p class="panel-text">As a Nigerian, I appreciated encountering contemporary Nigerian design here — not Nigeria preserved safely in the archaeological past, but Nigeria actively shaping modern dialogues on identity, materials, and making.</p>
  </div>

  <div class="panel">
    <div class="panel-title">Labor Made Visible</div>
    <p class="panel-text">A polished object can make labor disappear. The enlarged fingerprint did the opposite: <strong>it made the human trace enormous.</strong></p>
  </div>
</div>

---

<!-- Slide 8: 05 Marcus-Bello Headrest -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/05-marcus-bello-headrest.jpeg" alt="Nifemi Marcus-Bello - Headrest" class="art-img" />
  <div class="art-caption">Nifemi Marcus-Bello · Headrest, Orikì (Act III)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 05 · MATERIALITY & SUPPLY CHAINS</div>
  <h2>Objects Have Histories</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Intimacy and Provenance</div>
    <p class="panel-text">A headrest is intimate: a human body rests against it. But the material came from somewhere, passed through other hands, and carries a history that finished objects conceal.</p>
  </div>

  <div class="panel">
    <div class="panel-title">The Weight of Technology</div>
    <p class="panel-text">A phone, a computer, and even the "cloud" feel weightless when we use them. But they depend on minerals, factories, electricity, labor, transport, and physical infrastructure.</p>
  </div>

  <div class="quote-box">
    <p>"Nothing arrives from nowhere. The question I carried away was simple: <em>What had to happen in the world for this object to arrive in front of me?</em>"</p>
  </div>
</div>

---

<!-- Slide 9: Interlude -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/interlude-gallery.jpeg" alt="Gallery detail photographed before naming" class="art-img" />
  <div class="art-caption">Unidentified gallery object · Photographed before cataloging</div>
</div>
<div class="content-col">
  <div class="eyebrow">INTERLUDE · WONDER IN THE AGE OF AI</div>
  <h2>Curiosity Preserved</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Photographing Before Naming</div>
    <p class="panel-text">I photographed this before I knew what to call it. A museum visit does not have to be a sequence of successful, instantaneous classifications.</p>
  </div>

  <div class="panel">
    <div class="panel-title">The Trap of Pocket AI</div>
    <p class="panel-text">With artificial intelligence in our pockets, every encounter threatens to become a routine workflow: <em>photograph, identify, explain, move on</em>.</p>
  </div>

  <div class="quote-box">
    <p>"Identification is not the same thing as understanding. Sometimes curiosity should be allowed to remain curiosity for a while."</p>
  </div>
</div>

---

<!-- Slide 10: 06 Hopper Nighthawks -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/06-hopper-nighthawks_1.jpeg" alt="Edward Hopper - Nighthawks" class="art-img" />
  <div class="art-caption">Edward Hopper · Nighthawks (1942)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 06 · PROXIMITY & ISOLATION</div>
  <h2>Nighthawks: Light Without Warmth</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">What the Museum Told Me</div>
    <p class="panel-text">Hopper's diner is imagined rather than a literal portrait; the label highlights the isolation of the figures and the total absence of any visible entrance.</p>
  </div>

  <div class="panel">
    <div class="panel-title">What I Saw</div>
    <p class="panel-text">Bright fluorescent light without warmth. People physically close, yet profoundly separated. As a viewer, I could see inside the glass but could not enter.</p>
  </div>

  <div class="panel">
    <div class="panel-title">The Contrast of Family</div>
    <p class="panel-text">I was in Chicago with my family. The contrast mattered: <strong>Four people together in a painting were not necessarily less lonely than one person alone.</strong></p>
  </div>
</div>

---

<!-- Slide 11: 07 Peter Blume The Rock -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/07-blume-the-rock_1.jpeg" alt="Peter Blume - The Rock" class="art-img" />
  <div class="art-caption">Peter Blume · The Rock (1944–48)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 07 · RECONSTRUCTION & MEDICINE</div>
  <h2>The Rock: What Deserves to Be Rebuilt?</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Devastation and Renewal</div>
    <p class="panel-text">Blume connects crowded, difficult imagery to World War II devastation and reconstruction, while resisting neat, easy resolution.</p>
  </div>

  <div class="panel">
    <div class="panel-title">Wreckage vs. Hope</div>
    <p class="panel-text">I was not sure whether I found it hopeful. People were rebuilding, but the wreckage had not disappeared.</p>
  </div>

  <div class="panel">
    <div class="panel-title">The Medical Parallel</div>
    <p class="panel-text">Technology promises to rebuild healthcare. Yet we often digitize an old, broken workflow and call it modernization. <strong>The question is not how quickly we rebuild, but what deserves to be rebuilt.</strong></p>
  </div>
</div>

---

<!-- Slide 12: 08 Grant Wood American Gothic -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/08-grant-wood-american-gothic_1.jpeg" alt="Grant Wood - American Gothic" class="art-img" />
  <div class="art-caption">Grant Wood · American Gothic (1930)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 08 · DUTY & GENERATIONS</div>
  <h2>American Gothic: The Dignity & Cost of Duty</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Restraint and Discipline</div>
    <p class="panel-text">The pitchfork, austere clothing, guarded expressions, and gothic window all reflect intense discipline and self-restraint.</p>
  </div>

  <div class="panel">
    <div class="panel-title">Affection Expressed as Work</div>
    <p class="panel-text">Generations in which affection was expressed less by words than by work — providing, remaining, repairing, rising at dawn to do the necessary thing again.</p>
  </div>

  <div class="quote-box">
    <p>"There is dignity in that. There can also be a cost when duty becomes so visible that tenderness disappears."</p>
  </div>
</div>

---

<!-- Slide 13: 09 Rockwell The Dugout -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/09-rockwell-the-dugout_1.jpeg" alt="Norman Rockwell - The Dugout" class="art-img" />
  <div class="art-caption">Norman Rockwell · The Dugout (1948)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 09 · RESILIENCE & ADVERSITY</div>
  <h2>The Dugout: Painting the Slump</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">The Non-Triumphant Moment</div>
    <p class="panel-text">Rockwell did not paint the heroic home run; he painted dejected Chicago Cubs players sitting in the dugout beneath jeering Boston fans.</p>
  </div>

  <div class="panel">
    <div class="panel-title">Medicine, Leadership, Fatherhood</div>
    <p class="panel-text">All reward competence. But some days do not go well — sometimes through mistakes, sometimes despite flawless preparation, sometimes because life goes somewhere unexpected.</p>
  </div>

  <div class="quote-box">
    <p>"The crowd remembers the score. The person in the dugout has to decide whether to come back tomorrow."</p>
  </div>
</div>

---

<!-- Slide 14: 10 Wasson Twenty Mule Team -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/10-wasson-twenty-mule-team_1.jpeg" alt="Arthur Slim Wasson - Twenty Mule Team" class="art-img" />
  <div class="art-caption">Arthur "Slim" Wasson · Twenty Mule Team</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 10 · MINIATURES & MEMORY</div>
  <h2>A Small World Carrying a Large History</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Condensing Vast Systems</div>
    <p class="panel-text">Miniatures make large systems manageable. Industry becomes a wagon. Crushing labor becomes a carved figure. A vast landscape occupies a few feet.</p>
  </div>

  <div class="panel">
    <div class="panel-title">How Families Build Memory</div>
    <p class="panel-text">Families do something similar. Decades of living become stories: <em>Remember when...</em> Told often enough, a story becomes part of what a family believes itself to be.</p>
  </div>

  <div class="quote-box">
    <p>"This book is doing the same thing: I am taking one rainy afternoon in Chicago and constructing a memory of it."</p>
  </div>
</div>

---

<!-- Slide 15: 11 Juan Gris Picasso -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/11-juan-gris-picasso_1.jpeg" alt="Juan Gris - Portrait of Pablo Picasso" class="art-img" />
  <div class="art-caption">Juan Gris · Portrait of Pablo Picasso (1912)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 11 · PERCEPTION & IDENTITY</div>
  <h2>Picasso, Seen by Someone Else</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Surrendering the Photograph</div>
    <p class="panel-text">I knew I was looking at a man, but the man had been disassembled. I could recognize a portrait only after surrendering the expectation that it behave like a photograph.</p>
  </div>

  <div class="panel">
    <div class="panel-title">The Versions of Ourselves</div>
    <p class="panel-text">We create curated versions of ourselves — CVs, websites, social feeds. But my wife sees a version colleagues do not. My sons see another. Patients see another.</p>
  </div>

  <div class="quote-box">
    <p>"What does another person see in me that I cannot see from inside myself?"</p>
  </div>
</div>

---

<!-- Slide 16: 12 Ludwig Meidner -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/12-meidner-herrmann-neisse_1.jpeg" alt="Ludwig Meidner - Max Herrmann-Neisse" class="art-img" />
  <div class="art-caption">Ludwig Meidner · Max Herrmann-Neisse</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 12 · CLINICAL GAZE & HUMANITY</div>
  <h2>A Face Before a Biography</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Medicine Teaches You to Look</div>
    <p class="panel-text">Pain has a face. Anxiety has a face. Fatigue has a face. Grief has a face. Long before you consult the charts, you look at the patient's eyes.</p>
  </div>

  <div class="panel">
    <div class="panel-title">The Limits of the Chart</div>
    <p class="panel-text">An electronic medical record can contain extraordinary amounts of factual truth about a patient while completely failing to contain the human person.</p>
  </div>

  <div class="quote-box">
    <p>"I am glad I saw this face before I learned the biography. History came later. Humanity came first."</p>
  </div>
</div>

---

<!-- Slide 17: 13 Fernand Leger -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/13-leger-composition-in-blue_1.jpeg" alt="Fernand Léger - Composition in Blue" class="art-img" />
  <div class="art-caption">Fernand Léger · Composition in Blue</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 13 · ANTHROPOLOGY & AUTOMATION</div>
  <h2>Body, Machine, or Both?</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">Renegotiating the Boundary</div>
    <p class="panel-text">Body? Machine? Architecture? We are living through a moment when the line between human and machine is being radically renegotiated.</p>
  </div>

  <div class="panel">
    <div class="panel-title">AI in the Everyday</div>
    <p class="panel-text">I speak and software transcribes. Algorithms summarize. AI generates language. I find this exciting — but we must notice what it does to our self-understanding.</p>
  </div>

  <div class="quote-box">
    <p>"Where does the machine end, and where do I begin?"</p>
  </div>
</div>

---

<!-- Slide 18: 14 Francis Picabia -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/14-picabia-edtaonisl_1.jpeg" alt="Francis Picabia - Edtaonisl" class="art-img" />
  <div class="art-caption">Francis Picabia · Edtaonisl (Ecclesiastic)</div>
</div>
<div class="content-col">
  <div class="eyebrow">ENCOUNTER 14 · INTELLECTUAL HUMILITY</div>
  <h2>Not Everything Needs to Be Solved</h2>
  <div class="accent-line"></div>

  <div class="panel">
    <div class="panel-title">The Painting That Refused to Behave</div>
    <p class="panel-text">Even the title seemed determined not to help me. Information did not make the painting obvious — and I liked that.</p>
  </div>

  <div class="panel">
    <div class="panel-title">Information vs. Understanding</div>
    <p class="panel-text">Walking through a museum in 2026 with AI in our pockets allows instant identification. But identification can masquerade as understanding.</p>
  </div>

  <div class="quote-box">
    <p>"I am still not sure what I think about this painting. I want that sentence to remain in the book."</p>
  </div>
</div>

---

<!-- Slide 19: Epilogue 1 -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/15-rain-chicago-out_1.jpeg" alt="Out into the Chicago rain" class="art-img" />
  <div class="art-caption">Chicago streets · September 2026</div>
</div>
<div class="content-col">
  <div class="eyebrow">EPILOGUE · FROM ART TO LIFE</div>
  <h2>Out into the Rain</h2>
  <div class="accent-line"></div>
  
  <p class="statement" style="font-size: 1.15rem; margin-bottom: 16px;">"For several hours I had been looking at other people's attempts to preserve human experience.</p>
  
  <p class="statement" style="font-size: 1.15rem; color: var(--ember);">Then I walked outside and began taking photographs of the people whose lives actually belong to mine."</p>

  <p style="font-size: 0.85rem; color: var(--dim); margin-top: 12px;">Returning to the city with Chi Chi, Obi, Nnamdi, and Chidiebere — the living encounter that grounded everything.</p>
</div>

---

<!-- Slide 20: Closing Benediction -->
<!-- _class: split -->
<div class="art-container">
  <img src="./images/16-chicago-epilogue.jpeg" alt="Family in Chicago" class="art-img" />
  <div class="art-caption">Chi Chi, Obi, Nnamdi, Chidiebere & Chukwuma · Chicago 2026</div>
</div>
<div class="content-col">
  <div class="eyebrow">CHICAGO · SEPTEMBER 2026</div>
  <h2>The Unrepeatable Afternoon</h2>
  <div class="accent-line"></div>

  <div class="panel" style="background: rgba(13, 10, 6, 0.85); border-left-color: var(--gold);">
    <p class="panel-text" style="font-size: 0.95rem; font-style: italic; line-height: 1.55; color: #fdf5e6;">
      "The museum happened inside a birthday weekend. Chidiebere was twenty-four. Chi Chi, Obi, Nnamdi, Chidiebere, and I were together in Chicago.<br/><br/>
      <strong>I can return to a painting. I cannot return to exactly this afternoon.</strong><br/><br/>
      That does not make the afternoon sad. It makes it valuable."
    </p>
  </div>

  <div class="credit" style="margin-top: 12px;">
    <strong>Chukwuma Theology</strong> · Reflections on Art, Faith, and Life<br/>
    Dr. Chukwuma I. Onyeije, MD, FACOG
  </div>
</div>
