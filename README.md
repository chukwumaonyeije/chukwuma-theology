# Chukwuma Theology

A personal theology blog exploring the intersection of Seventh-day Adventist theology, biblical truth, medical ethics, and Christian reflection — written by Dr. Chukwuma I. Onyeije, MD, FACOG.

**Live site:** [chukwumaonyeije.github.io/chukwuma-theology](https://chukwumaonyeije.github.io/chukwuma-theology)

---

## About

This blog is where medicine and theology converge. As a practicing OB/GYN physician, Dr. Onyeije brings a clinician's clarity and rigor to biblical exposition — examining Adventist eschatology, contemporary cultural events through a scriptural lens, and the deeper questions that arise at the intersection of faith and science.

Posts are published in both written and audio formats, and mirrored to Substack for wider distribution.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | [Astro](https://astro.build) v4 |
| Content | MDX (Markdown + JSX components) |
| Styling | Custom CSS with design tokens |
| RSS | `@astrojs/rss` (site-wide + per-post feeds) |
| Audio | OpenAI TTS or ElevenLabs (Python script) |
| Deployment | GitHub Pages |

---

## Project Structure

```
chukwuma-theology/
├── src/
│   ├── pages/
│   │   ├── index.astro              # Homepage: hero, posts grid, about section
│   │   ├── posts/
│   │   │   ├── [...slug].astro      # Dynamic post template
│   │   │   └── rss/
│   │   │       └── [slug].xml.js   # Per-post RSS feed (Substack syndication)
│   │   └── rss.xml.js              # Site-wide RSS feed
│   ├── layouts/
│   │   └── PostLayout.astro        # Post wrapper: header, meta, audio, footer
│   ├── components/
│   │   └── AudioPlayer.astro       # Custom HTML5 audio player with progress bar
│   ├── content/
│   │   ├── config.ts               # Content collection schema (Zod)
│   │   └── posts/                  # MDX blog posts
│   └── styles/
│       ├── global.css              # Design tokens, nav, header, footer
│       └── post.css                # Prose typography, scripture callouts
├── public/
│   ├── audio/                      # Pre-generated MP3 files (one per post)
│   └── images/posts/               # Featured post images
├── scripts/
│   └── generate_audio.py           # TTS audio generation (OpenAI or ElevenLabs)
├── references/
│   └── voice-analysis.md           # Brand voice analysis and writing guidelines
├── .env.example                    # Environment variable template
└── astro.config.mjs                # Astro config (site URL, GitHub Pages base path)
```

---

## Getting Started

### Prerequisites

- Node.js 18+
- npm

### Install & Run

```bash
# Clone the repo
git clone https://github.com/chukwumaonyeije/chukwuma-theology.git
cd chukwuma-theology

# Install dependencies
npm install

# Start the dev server (http://localhost:4321)
npm run dev
```

> Draft posts are visible in development mode and hidden in production builds.

### Build & Preview

```bash
# Build for production
npm run build

# Preview the production build locally
npm run preview
```

---

## Writing Posts

Posts live in `src/content/posts/` as `.mdx` files. Create a new file with the following frontmatter:

```mdx
---
title: "Your Post Title"
description: "A one-sentence summary of the post."
date: 2026-01-15
author: "Dr. Chukwuma I. Onyeije"
tags: ["Eschatology", "Adventist", "Culture"]
image:
  url: "/chukwuma-theology/images/posts/your-image.jpg"
  alt: "Alt text for the featured image"
draft: false
audioUrl: "/chukwuma-theology/audio/your-post-slug.mp3"
---

Your post content here, using **Markdown** or MDX components.
```

| Field | Required | Description |
|---|---|---|
| `title` | Yes | Post title |
| `description` | Yes | Short summary (used in cards and RSS) |
| `date` | Yes | Publication date |
| `author` | No | Defaults to blank if omitted |
| `tags` | No | Array of topic tags |
| `image` | No | Object with `url` and `alt` |
| `draft` | No | Set `true` to hide from production |
| `audioUrl` | No | Path to MP3 — enables audio player |

### Scripture Callouts

Use a `div` with class `scripture-callout` for pull-quote styling:

```html
<div class="scripture-callout">
  "But now you must also rid yourselves of all such things." — Colossians 3:8
</div>
```

---

## Audio Generation

Each post can have a companion audio file generated via text-to-speech.

### Setup

```bash
# Install Python dependencies
pip install openai elevenlabs python-frontmatter python-dotenv

# Copy the env template and fill in your API keys
cp .env.example .env
```

### `.env` Configuration

```
AUDIO_PROVIDER=openai          # or: elevenlabs
OPENAI_API_KEY=sk-...
ELEVENLABS_API_KEY=...
ELEVENLABS_VOICE_ID=...        # Optional: custom/cloned voice ID
```

### Run

```bash
# Generate audio for all posts missing an MP3
python scripts/generate_audio.py

# Test with a single post (dry-run / quick check)
python scripts/generate_audio.py --test
```

The script:
1. Reads each MDX file in `src/content/posts/`
2. Strips markdown syntax to plain text
3. Sends text to OpenAI (tts-1, onyx voice) or ElevenLabs in chunks
4. Saves the resulting MP3 to `public/audio/{slug}.mp3`
5. Updates the post's frontmatter with the `audioUrl` field

**OpenAI** (`tts-1` model) is recommended for speed. **ElevenLabs** supports custom voice cloning for a more personalized reading experience.

---

## RSS Feeds

Two levels of RSS are provided:

| Feed | URL | Purpose |
|---|---|---|
| Site-wide | `/rss.xml` | General subscriber RSS |
| Per-post | `/rss/{slug}.xml` | Individual post feed for Substack import |

Both feeds include sanitized full HTML content and support featured images.

### Substack Syndication

The per-post RSS feeds are designed for Substack's RSS import feature, allowing posts to be automatically mirrored to the Substack newsletter audience.

---

## Design System

Colors are defined as CSS variables in `src/styles/global.css`:

| Token | Value | Usage |
|---|---|---|
| `--primary` | `#2d4739` | Deep forest green — nav, buttons, headings |
| `--secondary` | `#c26d4b` | Terracotta — accents, tags |
| `--accent` | `#d4af37` | Gold — audio player progress, highlights |
| `--bg-light` | `#faf9f6` | Parchment — page background |
| `--text-dark` | `#2c2c2c` | Body text |
| `--text-muted` | `#666` | Captions, meta, dates |

Typography uses **Playfair Display** (serif, headings) and **Inter** (sans-serif, body) from Google Fonts.

---

## Deployment

The site is configured for **GitHub Pages** deployment:

- **Site URL:** `https://chukwumaonyeije.github.io`
- **Base path:** `/chukwuma-theology`

These are set in `astro.config.mjs`. All internal links and asset paths use this base path automatically.

To deploy, push to the `main` branch. Configure GitHub Pages to deploy from the `dist/` output of `npm run build`, or use GitHub Actions with the Astro deploy workflow.

---

## Author

**Dr. Chukwuma I. Onyeije, MD, FACOG**
Practicing obstetrician-gynecologist, theologian, and writer.

- Blog: [chukwumaonyeije.github.io/chukwuma-theology](https://chukwumaonyeije.github.io/chukwuma-theology)
- Substack: linked in site navigation

---

## License

Content (blog posts, writing) is copyright Dr. Chukwuma I. Onyeije. Code is available for reference and personal adaptation.
