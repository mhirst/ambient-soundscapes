# Ambient Soundscapes — Website

Static website for the [Ambient Soundscapes YouTube channel](https://www.youtube.com/@ambntsnd).

One file, no build step, no dependencies. Everything lives in `index.html`.

## Preview locally

```bash
python -m http.server 8000
```

Then open http://localhost:8000

(Or just double-click `index.html` — it works fine opened directly too.)

## Adding a new video

Nothing to do — just upload to YouTube. A GitHub Action
(`.github/workflows/update-videos.yml`) runs daily, pulls the channel's RSS
feed, and rebuilds `videos.json`. When it finds a new upload it commits the
change and GitHub Pages redeploys automatically.

Don't want to wait for the daily run? Trigger it manually from the repo's
**Actions** tab → "Update videos from YouTube" → **Run workflow**, or run
locally:

```bash
python scripts/update_videos.py
git add videos.json && git commit -m "Update videos" && git push
```

Card descriptions use the first line of each video's YouTube description, so
lead with a good sentence there. Titles, thumbnails, and embeds all come from
the video itself.

## Hosting

### GitHub Pages (this repo)

Already set up — push to `main` and the site updates automatically:

```bash
git add -A
git commit -m "Add new video"
git push
```

### Netlify Drop (alternative)

Drag this folder onto https://app.netlify.com/drop and you get a URL instantly.

## Notes

- Videos embed via `youtube-nocookie.com` and only load the player when clicked,
  so the page is fast and sets no cookies until someone hits play.
- The design palette matches the channel art: deep night blues with a warm moon accent.
  Colors are defined as CSS variables at the top of `index.html` if you want to tweak them.
