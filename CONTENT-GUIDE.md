# Updating this site — no HTML editing required

The site is a [Jekyll](https://jekyllrb.com) site. GitHub Pages builds and
deploys it automatically on every push to `main` — there is no build step
for you to run and no GitHub Action required for deployment. Just edit a
file below, commit, and push; the live site updates in 1-2 minutes.

## Change your job / add to the timeline
Edit `_data/timeline.yml`. Copy the top block and fill in the new role,
newest first.

## Add a publication, talk, or conference abstract
Edit `_data/publications.yml`. Each category (`peer_reviewed`, `submitted`,
`conference_abstracts`, `invited_talks`, `scientific_sessions`, `teaching`)
is its own list — copy an entry within the right list and fill it in.

## Update your bio, headline stats, or programming skills
Edit `_data/profile.yml`.

## Change social links
Edit `_data/social.yml`.

## Write a new blog post (bi-weekly content)
Add a new file to `_posts/`, named `YYYY-MM-DD-a-short-slug.md`, e.g.:

```
_posts/2026-08-22-storm-loss-modelling-with-generative-ai.md
```

With this at the top:

```markdown
---
title: "Storm Loss Modelling with Generative AI"
date: 2026-08-22
categories: [Climate Risk, Machine Learning]
image: "/img/blog2.jpg"   # optional; can be a URL too
---
Your post content here, in Markdown. Use ## for subheadings, ```python for
code blocks, etc.
```

That's it — it automatically appears at the top of the homepage "Blog"
preview, on `/blog/`, and gets its own shareable URL like
`/blog/2026/08/22/storm-loss-modelling-with-generative-ai/` for posting to
LinkedIn/Twitter.

Aim for roughly one post every two weeks to keep the cadence promised on the
site.

## Industry / physical climate risk news feed (`/news/`)
This section spotlights recent news and research across themes relevant to a
(re)insurance / parametric audience. `/news/` shows a filter sidebar with one
tab per distinct `category` value in `_data/news.yml`, automatically —
themes currently in use:

- **Tropical Cyclone**, **Severe Convective Storm**, **Flood**, **Wildfire** — hazard-specific news
- **Climate Modelling** — TC/ETC/SCS and NatCat modelling research (journals + targeted searches)
- **Physical Risk Service Providers** — press mentions of vendors like Climate X, MSCI, Jupiter Intelligence, Swiss Re, Munich Re RMP, Moody's RMS, Verisk
- **Parametric Insurance**, **Reinsurance** — (re)insurance/ILS trade press
- **Adaptation & Sustainability** — climate adaptation & resilience news
- **General** — anything that doesn't fit the above

Adding any new `category` value in `_data/news.yml` (by hand or via the
script) automatically creates a new filter tab — no template changes needed.

**Manual curation:** edit `_data/news.yml` directly — add an entry at the top
with `title`, `url`, `source`, `date`, `category`, `summary`.

**Automated collection:** `scripts/fetch_news.py` polls a list of public
RSS/Atom feeds — scientific journals (Copernicus), agency/trade press
(Artemis, Reinsurance News), an official EU platform (Climate-ADAPT), and
Google News' public RSS search endpoint for vendors that don't publish their
own feed (Climate X, MSCI, Jupiter Intelligence, Swiss Re, Munich Re, Moody's
RMS, Verisk) — and appends new, deduplicated items to `_data/news.yml`. It's
wired up as a scheduled GitHub Action (`.github/workflows/fetch-news.yml`,
runs **every two days**, or trigger manually from the Actions tab) that opens
a **pull request** with the new entries — nothing publishes automatically
until you review and merge.

> **Note on LinkedIn:** LinkedIn's Terms of Service prohibit automated
> scraping of the platform, so this pipeline does not and should not pull
> from LinkedIn directly. If you want LinkedIn-sourced items, add them to
> `_data/news.yml` by hand, or manually share posts and reference the public
> URL.

To add a new feed source or vendor to track, edit the `FEEDS` list in
`scripts/fetch_news.py` — either a direct RSS URL, or `google_news("your search query")`
for a source (like the vendors above) that doesn't publish its own feed.
Run it locally any time with:

```bash
pip install feedparser pyyaml
python scripts/fetch_news.py
```

## Newsletter / subscriptions
The subscribe forms (`_includes/newsletter-form.html`) currently post to a
placeholder [Formspree](https://formspree.io) endpoint — replace
`YOUR_FORM_ID` with your own free Formspree form ID to start collecting
emails today (GitHub Pages has no backend, so a hosted form service is the
simplest option).

When you're ready to run a real industry newsletter, swap the form action
(and optionally the whole `newsletter-form.html` embed) for
[Buttondown](https://buttondown.email), [Mailchimp](https://mailchimp.com),
or [ConvertKit](https://convertkit.com) — all offer a simple HTML embed
that can paste in as a drop-in replacement, and `_data/news.yml` can double
as the source content you send out.

## Contact form
`_includes/contact.html` also posts to Formspree (`YOUR_FORM_ID`) — same
setup as the newsletter form.

## Mobile
Responsive styles live in `styles/_media.scss` (compiled base template
breakpoints) and `styles/components.css` (blog/news/publications/contact,
including phone-width fixes at 900px/600px/400px). If a new section looks
off on phones, add a rule under the matching `@media` block in
`styles/components.css`.
