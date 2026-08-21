# baroryan.github.io — rebuilt

Five pages, no framework, no build dependencies beyond Python. Each generated
`.html` file is self-contained (styles are inlined), so GitHub Pages serves it as-is.

## Drop-in

Copy these into the repo root:

```
index.html  research.html  join.html  teaching.html  projects.html
about_me.html  DIY.html  DIYFull.html      <- redirect stubs for old links
build.py  src/  figures/  README.md
```

The DIY page is `projects.html`, not `diy.html`, on purpose: the old-URL stub is
`DIY.html`, and on a case-insensitive filesystem (macOS, Windows) `DIY.html` and
`diy.html` are the same file — the stub overwrites the page and redirects to itself.
Don't rename it back.

Keep the folders the pages point at: `CV/`, `peru/`, `DIYPics/`, and `me.jpg`.
The ghost-forest page is retired but not deleted: `src/cascadia.body.html` and
`cascadia/copalis.jpg` are still in the bundle. To bring it back, add its two lines to
`PAGES` and `NAV` in `build.py` and rebuild.
You can delete the old `assets/`, `assetsNew/`, and `assetsFULL/` folders — nothing
references them any more. Fonts come from Google Fonts; icons are gone (the design
doesn't use any).

## Editing

Content lives in `src/*.body.html`, styling in `src/site.css`. After any change:

```bash
python3 build.py
```

That regenerates the five pages and the redirect stubs. Edit the `src/` files
rather than the generated ones, or your next build will overwrite you.

Shared header, footer, nav, and page titles are in `build.py` (`NAV`, `FOOTER`, `PAGES`).

## Things to fill in

- `src/teaching.body.html` — a commented-out course list is waiting near the top;
  uncomment and fill it once your Lehigh courses are set.
- `src/join.body.html` — the three recruiting cards say what you're taking this cycle.
  Worth revisiting every fall.
### animation/

Downloadable copies of the earthquake-cycle animation, offered through the small
Download menu under the figure on the home page. All four are the same full cycle
(18.3 s, looping), rendered from `index.html` itself so they always match what the site
shows, with "Bar Oryan, Lehigh University" bottom right and the phase word aligned to
the right edge of the displacement panel.

| file | what it is |
|---|---|
| `oryan-earthquake-cycle-purple.mp4` | 1920x596, 25 fps, H.264. Sharpest and smallest — use this in talks and on the web. |
| `oryan-earthquake-cycle-transparent.webm` | 1440 px, 25 fps, VP9 with a real alpha channel. Clean on any background; plays in browsers, not in PowerPoint or Keynote. |
| `oryan-earthquake-cycle-purple.gif` | 1000 px, 25 fps. Pastes into anything. |
| `oryan-earthquake-cycle-transparent.gif` | 1000 px, 12.5 fps. GIF transparency is on/off only, so the artwork is composited onto white and the surround is cut out — perfect on a light slide, slight white fringing on a dark one. Use the WebM for dark backgrounds. |

"site background" means the pale violet of the home page (`--band`, #efeaf7).

To regenerate after changing the figure, re-render from the built page rather than
editing these by hand: the frames are screenshots of `.cycle` in `index.html` with
`Math.random` and `requestAnimationFrame` stubbed so one deterministic cycle plays out
frame by frame. For the transparent pass, `#edgefade` has to be hidden — it paints the
page colour to dissolve the seaward edge, which becomes an opaque block once the
background is gone.

- `me.jpg` — 480x480, pre-cropped square framed on the head. The home page shows it
  as a circle beside the name (140 px on desktop, 120/78 px smaller up). Because the
  crop lives in the file, `.portrait img` is a plain `object-fit:cover` — replace the
  file with another square crop and nothing in the CSS needs touching.
- `lehigh_fall.jpg` — campus photo in the "Life at Lehigh" block on join.html.
- `ev_charger_availability.png` — dashboard screenshot on projects.html.
- `peru/pics/01,02,04,05.jpg` — the teaching-page gallery, resized to 1200x900.
- `DIYPics/pic1-3.jpg`, `DIYPics/phcam01-06.jpg` — the two projects-page galleries,
  resized to 1200x900.

Gallery images are pre-cropped to 4:3 at 1200x900 so the `figure img` crop is a no-op;
originals live in the `baroryan.github.io` repo. Re-crop from there rather than
upscaling these.

### figures/

Research-page figures. The two animations are `<video autoplay loop muted playsinline>`
rather than GIFs — an MP4 at this resolution is a fraction of the size a GIF would be,
and `site.css` already styles `.project-visual video` the same as `.project-visual img`.
A small script at the foot of `research.body.html` pauses whichever video is scrolled
off screen. Each carries a `poster` frame and a caption link that opens the file at
native resolution, since the multi-panel figures are denser than 600 px can show.

| file | size |
|---|---|
| `river-geodesy-animation.mp4` | 1800x1600, 7 fps, 1.3 MB |
| `tandem-animation.mp4` | 1600x1104, 30 fps, 0.9 MB (white margin cropped, 60 -> 30 fps) |
| `*-poster.jpg` | 1200 px still, shown before the video loads |

The PNGs are quantised to 256 colours, which is visually lossless on these figures and
cuts them hard: `indo-burma-map-transparent.png` 2160 -> 318 KB,
`optimal-transport-tohoku-cascadia.png` 1022 -> 367 KB, `coupling-cloud-logo.png`
962 -> 29 KB. Re-run that step if you replace one with a full-resolution export.

`chi-space-inversion.jpg` and `coupling-cloud-logo.jpg` are gone — the rewritten
research page no longer uses them.

### Navigation

The nav is generated from `NAV` in `build.py`, so adding or reordering an entry there
updates every page at once. External entries (currently the Coupling Cloud) get a small
arrow after the label from `.topbar nav a[href^="http"]::after`, so it is clear the link
leaves the site.

### CV

`CV/CV_BarOryan.pdf` is the file all twelve CV links across the site point at. To publish
a new version, overwrite that file and keep the name — do not add a version number or a
date to it, or every existing link, and anything anyone has bookmarked, breaks.

### Still needed

These paths are referenced by the pages but are not in this repo:

- `peru/2019_Storke_Peru_Field_Guide.pdf`, `peru/2019_Storke_Peru_Field_notes.pdf`,
  `peru/rough_itinerary.pdf`
- `ev-charger/index.html`

