---
name: invocation-offering
description: "Write Sabbath invocation prayers and calls for offering (tithes/offering appeals) for Chukwuma's role as an elder at Atlanta North Seventh-day Adventist Church. Use this skill any time he gives a topic, scripture, theme, illustration, or just says 'I'm on invocation this week' or 'I have offering this Sabbath' — even a bare date or a one-line thought is enough to trigger drafting. Also use when he asks to write a pastoral prayer, a communion prayer, a tithe appeal, or any piece of spoken liturgical content for a Sabbath service at ANC. Produces pieces meant to be read aloud from the pulpit, matching the voice and structure of his own past invocations and offering calls."
---

# Invocation & Call-for-Offering Writer (Atlanta North SDA Church)

Chukwuma serves as an elder at Atlanta North Seventh-day Adventist Church (ANC) and periodically delivers the **invocation prayer** and/or the **call for offering** during Sabbath service. This skill drafts both, in his established voice, from nothing more than a thought, theme, scripture, or date.

Read [references/examples.md](references/examples.md) before drafting — it contains real invocations and offering calls he has delivered from 2023–2025. These are the ground truth for voice, pacing, and structure. Skim it fresh each time rather than relying on memory of a past session; his archive is the source of truth, not this file's summary of it.

## Quick Start

1. Ask (or infer from what he gives you) three things if not already clear: **the date of the Sabbath**, **which piece(s)** he needs (invocation, offering, or both — sometimes also communion prayers), and **the thought/theme/scripture** he wants woven in. If he gives only a theme with no date, use the upcoming Saturday.
2. Read [references/examples.md](references/examples.md) for voice grounding if you haven't already this session.
3. Draft the piece(s) following the structures below.
4. Save the output to `INVOCATION-OFFERING/` in the project root (see Output & Filing below).
5. Show the drafted text in the chat as well, so he can review or ask for a revision before it's filed away.

## Voice

This is spoken prayer and pulpit address, not an essay. Read it aloud in your head as you draft:

- Warm, reverent, unhurried. Long, flowing sentences built on "and," participial clauses, and repeated invocation of God's attributes — this is liturgical cadence, not clipped prose.
- Address God directly and consistently ("Heavenly Father," "Lord," "Gracious God") — vary the address across a piece rather than repeating one name mechanically.
- Adventist-specific theological color throughout: the Sabbath as gift and rest, the soon return of Christ, the sanctuary/investigative-judgment frame when relevant, the church as a "family" and "flock," stewardship as worship rather than obligation.
- First person plural ("we," "us," "our") — this is prayed *with* and *on behalf of* the congregation, never lecturing at it.
- Scripture, when used, is quoted in full and placed where it lands hardest — not sprinkled as citations.
- It is fine, and often better, to reach for a concrete illustration (a mission story, a congregation member, a personal memory) before turning theological, especially for offering calls. See the pattern notes at the bottom of references/examples.md.

## Invocation Prayer — Structure

A typical invocation runs 5–9 short paragraphs and moves through these beats (not rigidly — vary the order and don't force every beat into every prayer):

1. **Address and gathering** — naming God, acknowledging the congregation has gathered on the Sabbath.
2. **Adoration** — praising an attribute of God (Creator, Redeemer, sustainer), sometimes anchored in a specific scripture quoted in full.
3. **Petition for the service** — asking for the Spirit's presence over the worship, the Word, the music, the fellowship to come.
4. **Intercession** — a lift-up for church leaders, and/or for the sick, lonely, grieving, or those outside the fellowship.
5. **Sabbath/end-time note** — gratitude for Sabbath rest, or a turn toward Christ's soon return, when it fits the week's theme.
6. **Closing formula** — always ends with a "we pray" line naming Jesus, then "Amen." Vary the exact wording (see examples for the range: "In the name of Jesus Christ, our Savior and Redeemer, we pray. Amen." / "In Your holy name, we pray. Amen." / "In the precious name of Jesus, our Worthy Lamb. Amen.").

If Chukwuma names the opening hymn, add a line after the Amen: `OUR OPENING HYMN THIS MORNING IS: Hymn # ___ — [Title]`. Otherwise omit it — don't invent a hymn number.

## Call for Offering — Structure

A typical call for offering is longer and more oratorical — it's a short homily that lands on an appeal, followed by a distinct closing prayer:

1. **Hook** — a question, a vivid image, or the opening line of an illustration/story. Personal testimony from Chukwuma's own life is a strong and authentic option (his medical career, marriage, family) — invent something plausible and specific in that register if he hasn't supplied a real story, but flag clearly that it's a suggested illustration he should confirm or swap for a real memory.
2. **Illustration developed** — 1–3 paragraphs telling the story through to its point.
3. **Scripture pivot** — one passage, quoted in full, that reframes the illustration as being about giving/stewardship/sacrifice.
4. **Theological bridge** — connect to Christ's own self-giving (incarnation, cross) as the model for the congregation's giving. This is the recurring theological center of gravity across his past offering calls — giving as participation in Christ's sacrifice, not a budget line.
5. **The three ways to give** — reproduce this block near verbatim, since it's fixed ANC logistics:

   ```
   There are several ways for you to give today:
   1. Adventist Giving — through the ANC website, by scanning the QR code, or by texting "GIVE" to 770-818-4323
   2. The SDA Giving App (Android & iPhone)
   3. The Offering Box in the foyer
   ```

6. **Closing prayer, set off clearly** with its own heading (`PRAYER FOR TITHES AND OFFERINGS`), 3–5 sentences, ending "In Jesus' name, we pray. Amen."
7. Optionally close with a one-line warm send-off after the Amen: "Thank you for your generous hearts. God bless you all."

Use bracketed stage directions sparingly — `[Pause for effect]`, `[Slow down and emphasize]`, `[Pause and smile]` — only when the piece is written for a more performative, story-driven delivery (see Example 2 in references/examples.md). Skip them for shorter or more restrained pieces; don't add them by default.

## Special Occasions

- **Communion Sabbath**: if he mentions communion, also offer two short paired prayers — one for the bread, one for the (unfermented) wine/juice — each 4–6 sentences, addressed separately to Christ's body and blood, closing "In Jesus' name, Amen." See references/examples.md for the exact past pattern.
- **If he gives a specific scripture or sermon theme for the week**, build the whole piece around it rather than defaulting to a generic template — the strongest past examples (e.g., the Revelation 5:12 invocations) are the ones anchored tightly to one passage.

## Output & Filing

Save every finished piece as a Markdown file in `INVOCATION-OFFERING/` at the project root, named by type and date, matching the convention in his own archive:

- `Invocation MM.DD.YY.md`
- `Offering MM.DD.YY.md`
- `Invocation and Offering MM.DD.YY.md` if both are delivered together in one file (this was his most common past format)

If he asks for a Word document (to match his existing `.docx` archive, or to email to the bulletin editor), use the `docx` skill to also produce a matching `.docx` in the same folder.

## Avoid

- Generic, denomination-neutral prayer language — this should read as unmistakably Adventist and unmistakably his.
- Turning the offering call into a guilt-driven fundraising pitch — the register throughout his past pieces is gratitude and stewardship, never pressure.
- Overloading a single piece with more than one or two scripture references — one well-placed passage beats several skimmed ones.
- Inventing ANC-specific facts (giving methods, hymn numbers, event names) beyond what's given or already fixed in this file — ask if unsure rather than guessing.
