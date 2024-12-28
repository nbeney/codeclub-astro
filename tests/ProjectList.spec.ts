import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/ProjectListTest');
});

// test('should have 2 cards', async ({ page }) => {
//   const cards = page.locator('.card');
//   await expect(cards).toHaveCount(2);
// });

// test('each card should be visible', async ({ page }) => {
//   const cards = page.locator('.card');
//   for (const card of await cards.all()) {
//     await expect(card).toBeVisible();
//   }
// });

// test('each card should have an image', async ({ page }) => {
//   const cards = page.locator('.card');
//   for (const card of await cards.all()) {
//     const img = card.locator('img');
//     await expect(img).toBeVisible();
//   }
// });

// test('each card should have a title', async ({ page }) => {
//   const cards = page.locator('.card');
//   for (const card of await cards.all()) {
//     const title = card.locator('.card-title');
//     await expect(title).toHaveText(/Page is (ready|not ready)/);
//   }
// });

// test('first card should have class python', async ({ page }) => {
//   const cards = page.locator('.card');
//   const card = cards.nth(0);
//   await expect(card).toHaveClass(/python/);
// });

// test('first card should have links to /dummy/page1/', async ({ page }) => {
//   const cards = page.locator('.card');
//   const card = cards.nth(0);
//   const links = card.locator('a');
//   for (const link of await links.all()) {
//     await expect(link).toHaveAttribute('href', '/codeclub-astro/dummy/page1/');
//   }
// });

// test('second card should have class not-ready', async ({ page }) => {
//   const cards = page.locator('.card');
//   const card = cards.nth(1);
//   await expect(card).toHaveClass(/not-ready/);
// });

// test('second card should have no links', async ({ page }) => {
//   const cards = page.locator('.card');
//   const card = cards.nth(1);
//   const links = card.locator('a');
//   await expect(links).toHaveCount(0);
// });

test('should have 3 cards', async ({ page }) => {
  const cards = page.locator('.card');
  await expect(cards).toHaveCount(3);
});

test('first card should have image', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(0);
  const img = card.locator('img');
  await expect(img).toBeVisible();
});

test('first card should have title ASCII Art Maker', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(0);
  const title = card.locator('.card-body');
  await expect(title).toHaveText('ASCII Art Maker EASY');
});

test('first card should have badge EASY', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(0);
  const badge = card.locator('.badge');
  await expect(badge).toHaveText('EASY');
});

test('second card should have image', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(1);
  const img = card.locator('img');
  await expect(img).toBeVisible();
});

test('second card should have title Binary Clock', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(1);
  const title = card.locator('.card-body');
  await expect(title).toHaveText('Binary Clock MEDIUM');
});

test('second card should have badge MEDIUM', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(1);
  const badge = card.locator('.badge');
  await expect(badge).toHaveText('MEDIUM');
});

test('third card should have image', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(2);
  const img = card.locator('img');
  await expect(img).toBeVisible();
});

test('third card should have title Connect Four', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(2);
  const title = card.locator('.card-body');
  await expect(title).toHaveText('Connect Four HARD');
});

test('third card should have badge HARD', async ({ page }) => {
  const cards = page.locator('.card');
  const card = cards.nth(2);
  const badge = card.locator('.badge');
  await expect(badge).toHaveText('HARD');
});

test('should see only one card with badge EASY when clicking on Easy filter', async ({ page }) => {
  await page.getByText('Easy', { exact: true }).click();
  const cards = page.locator('.card');
  await expect(cards).toHaveCount(3);

  for (const card of await cards.all()) {
    const badge = card.locator('.badge');
    if (await badge.textContent() === 'EASY') {
      await expect(card).toBeVisible();
    } else {
      await expect(card).not.toBeVisible();
    }
  }
});

test('should see only one card with badge MEDIUM when clicking on Medium filter', async ({ page }) => {
  await page.getByText('Medium', { exact: true }).click();
  const cards = page.locator('.card');
  await expect(cards).toHaveCount(3);

  for (const card of await cards.all()) {
    const badge = card.locator('.badge');
    if (await badge.textContent() === 'MEDIUM') {
      await expect(card).toBeVisible();
    } else {
      await expect(card).not.toBeVisible();
    }
  }
});

test('should see only one card with badge HARD when clicking on Hard filter', async ({ page }) => {
  await page.getByText('Hard', { exact: true }).click();
  const cards = page.locator('.card');
  await expect(cards).toHaveCount(3);

  for (const card of await cards.all()) {
    const badge = card.locator('.badge');
    if (await badge.textContent() === 'HARD') {
      await expect(card).toBeVisible();
    } else {
      await expect(card).not.toBeVisible();
    }
  }
});

test('should see all cards when clicking on All filter', async ({ page }) => {
  await page.getByText('Easy', { exact: true }).click();
  await page.getByText('Medium', { exact: true }).click();
  await page.getByText('Hard', { exact: true }).click();
  await page.getByText('All', { exact: true }).click();
  const cards = page.locator('.card');
  await expect(cards).toHaveCount(3);

  for (const card of await cards.all()) {
    await expect(card).toBeVisible();
  }
});
