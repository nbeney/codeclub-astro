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
