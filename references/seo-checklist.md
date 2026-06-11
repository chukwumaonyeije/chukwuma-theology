# Editorial Workflow: 10-Item SEO Checklist

Follow this simple checklist for every new post or presentation to keep search engine optimization in peak health and avoid duplicate content issues.

---

### For MDX Blog Posts

1. **Frontmatter Validation**
   - Ensure the frontmatter matches the [post-template.mdx](file:///c:/Users/onyei/Projects/chukwuma-theology/src/content/posts/post-template.mdx).
   - Double-check that `draft: false` is set when you're ready to publish to production.

2. **Optimize Title and Description Lengths**
   - **Title**: Under 60 characters (displays fully in Google search results).
   - **Description**: Between 150 and 160 characters. This acts directly as your Google snippet/meta description.

3. **Establish Heading Hierarchy**
   - Verify there is exactly **one H1** tag (the main post title, generated automatically).
   - Use H2 tags (`##`) for main sections, and H3 tags (`###`) for subsections. Do not skip header levels (e.g., jumping from H2 directly to H4).

4. **Add Image Alt Text**
   - Ensure your featured image in frontmatter contains a descriptive, keyword-conscious `alt` string (e.g., `alt: "Samson breaking the pillars of the temple of Dagon"` instead of `alt: "samson image"`).

5. **Internal Contextual Linking**
   - Add at least 1-2 internal links to other reflections or presentations in the body text or in the "Related Reflections" section to guide readers and distribute crawl equity.

6. **Substack URL and Canonical Handling**
   - If the post is mirrored from or to Substack, supply the `substackUrl` in the frontmatter. The website will automatically style a beautiful discussion callout and output canonical meta tags pointing to **your site** as the primary version, protecting you from duplicate content penalties.

---

### For MARP HTML Presentations

7. **Inject MARP Metadata**
   - Define custom metadata in your MARP header:
     ```markdown
     ---
     marp: true
     title: Your Presentation Title
     description: A concise presentation description under 160 characters.
     ---
     ```
   - Update [presentations.json](file:///c:/Users/onyei/Projects/chukwuma-theology/src/data/presentations.json) to register the new presentation, providing the slug, description, type (`marp-html`), and a short summary transcript for crawlers.

---

### For PDF Presentations

8. **PDF Landing Page Creation**
   - When upload a PDF presentation, register it in [presentations.json](file:///c:/Users/onyei/Projects/chukwuma-theology/src/data/presentations.json) with `type: "pdf"`.
   - Provide a download URL pointing to the file (e.g. `/audio/` or custom folders).

9. **Write Search-Engine Crawlable Transcripts**
   - Write a structured markdown transcript or outline under the `transcript` key in `presentations.json`. Since search spiders cannot easily crawl embedded PDF readers, this text acts as the main content body Google indexes.

---

### Security & Tracking

10. **Link Security & Analytics Verification**
    - Double check that all external links opening in new tabs use `target="_blank" rel="noopener noreferrer"`.
    - Once built, test that pages contain the Google Analytics tracking scripts in the HTML header.
