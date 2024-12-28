// SAMPLE HTML TO TEST:
// ===================
// <!DOCTYPE html><html lang="en"> <head><meta charset="utf-8"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="generator" content="Astro v5.1.1"><title>Test - ActivityCard</title><style data-vite-dev-id="C:/Users/nbene/repos/codeclub-astro/node_modules/astro/components/image.css">[data-astro-image] {
// 	width: 100%;
// 	height: auto;
// 	object-fit: var(--fit);
// 	object-position: var(--pos);
// 	aspect-ratio: var(--w) / var(--h);
// }
// /* Styles for responsive layout */
// [data-astro-image='responsive'] {
// 	max-width: calc(var(--w) * 1px);
// 	max-height: calc(var(--h) * 1px);
// }
// /* Styles for fixed layout */
// [data-astro-image='fixed'] {
// 	width: calc(var(--w) * 1px);
// 	height: calc(var(--h) * 1px);
// }
// </style>
// <style data-vite-dev-id="C:/Users/nbene/repos/codeclub-astro/src/components/ConditionalLink.astro?astro&#38;type=style&#38;index=0&#38;lang.css">a[data-astro-cid-liyrbuud]{text-decoration:none;color:inherit}</style>
// <style data-vite-dev-id="C:/Users/nbene/repos/codeclub-astro/src/components/ActivityCard.astro?astro&#38;type=style&#38;index=0&#38;lang.css">.card[data-astro-cid-uriw3r4u]{display:inline-block;width:15rem;margin:3px}.card-title[data-astro-cid-uriw3r4u]{height:4.5rem;overflow:hidden}.not-ready[data-astro-cid-uriw3r4u] [data-astro-cid-uriw3r4u]{color:lightgrey}.card[data-astro-cid-uriw3r4u].python{position:relative}.card[data-astro-cid-uriw3r4u].python::after{content:"";position:absolute;bottom:10px;right:10px;width:35px;height:35px;background-image:url(https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg);background-size:contain;background-repeat:no-repeat;z-index:10;pointer-events:none}.card[data-astro-cid-uriw3r4u].not-ready img[data-astro-cid-uriw3r4u]{filter:opacity(40%)}.card[data-astro-cid-uriw3r4u].not-ready a[data-astro-cid-uriw3r4u]{color:lightgrey}.card[data-astro-cid-uriw3r4u] a[data-astro-cid-uriw3r4u]{text-decoration:none;color:black}.card[data-astro-cid-uriw3r4u]:hover{box-shadow:0 0 20px 0 rgba(0,0,0,0.5)}.card[data-astro-cid-uriw3r4u].not-ready:hover{box-shadow:none}</style>
// <style data-vite-dev-id="C:/Users/nbene/repos/codeclub-astro/src/components/Footer.astro?astro&#38;type=style&#38;index=0&#38;lang.css">footer[data-astro-cid-sz7xmlte] p[data-astro-cid-sz7xmlte]{margin-top:1em;font-style:italic;color:grey}</style>
// <style data-vite-dev-id="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro?astro&#38;type=style&#38;index=0&#38;lang.css">.dropdown-item[data-astro-cid-3ef6ksr2].active{background-color:var(--bs-primary);color:white}.dropdown-toggle[data-astro-cid-3ef6ksr2]::after{margin-left:0.5em}</style>
// <style data-vite-dev-id="C:/Users/nbene/repos/codeclub-astro/src/styles/global.css">@import url("https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css");
// @import url("https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/styles/vs2015.min.css");
// @import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css");
// @import url('https://fonts.googleapis.com/css2?family=Luckiest Guy:wght@400&display=swap');
// /*  */
// h1,
// h2 {
//     font-family: 'Luckiest Guy', cursive;
// }
// h1 {
//     margin-top: 1em;
// }
// h2 {
//     margin-top: 1em;
// }
// </style><script type="module" src="/@vite/client"></script>
// <script type="module" src="/@fs/C:/Users/nbene/repos/codeclub-astro/node_modules/astro/dist/runtime/client/dev-toolbar/entrypoint.js?v=aa34de41"></script>
// <script>window.__astro_dev_toolbar__ = {"root":"C:\\Users\\nbene\\repos\\codeclub-astro\\","version":"5.1.1","debugInfo":"Astro                    v5.1.1\nNode                     v22.12.0\nSystem                   Windows (x64)\nPackage Manager          npm\nOutput                   static\nAdapter                  none\nIntegrations             none"}</script>
// <script type="module" src="/node_modules/astro/components/image.css"></script>
// <script type="module" src="/src/components/ConditionalLink.astro?astro&type=style&index=0&lang.css"></script>
// <script type="module" src="/src/components/ActivityCard.astro?astro&type=style&index=0&lang.css"></script>
// <script type="module" src="/src/components/Footer.astro?astro&type=style&index=0&lang.css"></script>
// <script type="module" src="/src/components/Header.astro?astro&type=style&index=0&lang.css"></script>
// <script type="module" src="/src/styles/global.css"></script></head> <body class="container" data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/layouts/PageLayout.astro" data-astro-source-loc="19:29"> <header data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="11:9"> <nav class="navbar navbar-expand-lg navbar-dark bg-primary" data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="12:65"> <div class="container-fluid" data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="13:38"> <a class="navbar-brand" href="/codeclub-astro/tests/ActivityCardTest" data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="14:86">Code Club</a> <div class="dropdown" data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="15:35"> <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false" data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="22:18"> Home </button> <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton" data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="25:98"> <li data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="27:29"> <a class="dropdown-item active" href="/codeclub-astro/tests/ActivityCardTest" data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="34:30"> Home </a> </li><li data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="27:29"> <a class="dropdown-item" href="/codeclub-astro/dummy/page1/" data-astro-cid-3ef6ksr2 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Header.astro" data-astro-source-loc="34:30"> Page1 </a> </li> </ul> </div> </div> </nav> </header>  <h1 data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/layouts/PageLayout.astro" data-astro-source-loc="21:7">ActivityCard Test</h1> <a href="/codeclub-astro/dummy/page1/" data-astro-cid-liyrbuud data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/ConditionalLink.astro" data-astro-source-loc="5:30"> <div class="card python" data-astro-cid-uriw3r4u data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/ActivityCard.astro" data-astro-source-loc="16:66"> <a href="/codeclub-astro/dummy/page1/" data-astro-cid-liyrbuud data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/ConditionalLink.astro" data-astro-source-loc="5:30"> <img src="/codeclub-astro/_image?href=%2F%40fs%2FC%3A%2FUsers%2Fnbene%2Frepos%2Fcodeclub-astro%2Fsrc%2Fassets%2Fimages%2Fdummy%2Fpage1%2Flogo.jpg%3ForigWidth%3D1024%26origHeight%3D1024%26origFormat%3Djpg&#38;w=238&#38;h=238&#38;f=webp" data-image-component="true" alt="/dummy/page1/" data-astro-cid-uriw3r4u="true" width="238" height="238" loading="lazy" decoding="async" class="card-img-top" data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/node_modules/astro/components/Image.astro" data-astro-source-loc="61:2"> <div class="card-body" data-astro-cid-uriw3r4u data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/ActivityCard.astro" data-astro-source-loc="19:36"> <h5 class="card-title" data-astro-cid-uriw3r4u data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/ActivityCard.astro" data-astro-source-loc="20:40"> Page is <em>ready</em> </h5> </div> </a> </div> </a>  <div class="card not-ready" data-astro-cid-uriw3r4u data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/ActivityCard.astro" data-astro-source-loc="16:66">  <img src="/codeclub-astro/_image?href=%2F%40fs%2FC%3A%2FUsers%2Fnbene%2Frepos%2Fcodeclub-astro%2Fsrc%2Fassets%2Fimages%2Fdummy%2Fpage2%2Flogo.jpg%3ForigWidth%3D1024%26origHeight%3D1024%26origFormat%3Djpg&#38;w=238&#38;h=238&#38;f=webp" data-image-component="true" alt="/dummy/page2/" data-astro-cid-uriw3r4u="true" width="238" height="238" loading="lazy" decoding="async" class="card-img-top" data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/node_modules/astro/components/Image.astro" data-astro-source-loc="61:2"> <div class="card-body" data-astro-cid-uriw3r4u data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/ActivityCard.astro" data-astro-source-loc="19:36"> <h5 class="card-title" data-astro-cid-uriw3r4u data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/ActivityCard.astro" data-astro-source-loc="20:40"> Page is <em>not ready</em> </h5> </div>  </div>   <footer data-astro-cid-sz7xmlte data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Footer.astro" data-astro-source-loc="4:9"> <p data-astro-cid-sz7xmlte data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Footer.astro" data-astro-source-loc="5:8">&copy; 2023-<span id="currentYear" data-astro-cid-sz7xmlte data-astro-source-file="C:/Users/nbene/repos/codeclub-astro/src/components/Footer.astro" data-astro-source-loc="5:43">2025</span> Nicolas Beney. All rights reserved.</p> </footer> <script>
//     document.getElementById('currentYear').textContent = new Date().getFullYear();
// </script>  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script> </body></html>

import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/ActivityCardTest');
});

test('should have 2 cards', async ({ page }) => {
  const cards = page.locator('.card');
  await expect(cards).toHaveCount(2);
});

test('each card should be visible', async ({ page }) => {
  const cards = page.locator('.card');
  for (const card of await cards.all()) {
    await expect(card).toBeVisible();
  }
});

test('each card should have an image', async ({ page }) => {
  const cards = page.locator('.card');
  for (const card of await cards.all()) {
    const img = card.locator('img');
    await expect(img).toBeVisible();
  }
});

test('each card should have a title', async ({ page }) => {
  const cards = page.locator('.card');
  for (const card of await cards.all()) {
    const title = card.locator('.card-title');
    await expect(title).toHaveText(/Page is (ready|not ready)/);
  }
});

test('first card should have class python', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(0);
  await expect(card).toHaveClass(/python/);
});

test('first card should have links to /dummy/page1/', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(0);
  const links = card.locator('a');
  for (const link of await links.all()) {
    await expect(link).toHaveAttribute('href', '/codeclub-astro/dummy/page1/');
  }
});

test('second card should have class not-ready', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(1);
  await expect(card).toHaveClass(/not-ready/);
});

test('second card should have no links', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(1);
  const links = card.locator('a');
  await expect(links).toHaveCount(0);
});
