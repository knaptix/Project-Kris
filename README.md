# Striking Literary Football Growth Proposal

A static, responsive web presentation for the Striking Literary football app growth proposal.

## Files

- `index.html` — proposal content and page structure.
- `styles.css` — premium dark-green football-inspired visual system and responsive layout.
- `netlify.toml` — Netlify static-site deployment configuration.
- `vercel.json` — Vercel static-site deployment configuration.
- `.github/workflows/deploy-pages.yml` — GitHub Pages deployment workflow.

## Run locally

```bash
npm start
```

Then open `http://localhost:8000` in a browser.

If you do not want to use npm, run the same static server directly:

```bash
python3 -m http.server 8000
```

## Validate

```bash
npm test
```

The validation script parses the HTML and checks for the core proposal content and CSS markers.

## Deploy and get a public link

### GitHub Pages

1. Push this repository to GitHub.
2. In GitHub, open **Settings → Pages** and set the source to **GitHub Actions**.
3. Push to `main` or `master`, or run the **Deploy static proposal to GitHub Pages** workflow manually.
4. The public URL will be shown in the workflow summary as `page_url`.

### Netlify

```bash
npm install -g netlify-cli
netlify deploy --prod --dir .
```

Netlify will print the live production URL when the deploy finishes.

### Vercel

```bash
npm install -g vercel
vercel --prod
```

Vercel will print the live production URL when the deploy finishes.
