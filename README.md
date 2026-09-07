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

1. Upload the video to YouTube and copy its ID — the part after `watch?v=` in the URL.
   For example, in `https://www.youtube.com/watch?v=ceekdJdtSJM` the ID is `ceekdJdtSJM`.
2. Open `index.html` and find the `const videos = [` block near the bottom.
3. Copy an existing entry and edit it:

```js
{
  id: "NEW_VIDEO_ID",
  title: "Video title here",
  description: "One-line description shown on the card."
},
```

Newest-first is a nice convention — put new entries at the top of the list.
The thumbnail, click-to-play embed, and YouTube link are generated automatically.

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
