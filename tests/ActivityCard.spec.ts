import { test, expect } from '@playwright/test';

const cards = [
  {
    index: 0,
    class: 'python',
    link: '/codeclub-astro/dummy/page1/',
    hasLinks: true
  },
  {
    index: 1,
    class: 'not-ready',
    hasLinks: false
  }
];

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/ActivityCardTest');
});

// Basic card count test
test('should have correct number of cards', async ({ page }) => {
  const cardElements = page.locator('.card');
  await expect(cardElements).toHaveCount(cards.length);
});

// Parameterized tests for common card properties
test.describe('Common card properties', () => {
  for (const [index] of cards.entries()) {
    test(`card ${index} should have basic required elements`, async ({ page }) => {
      const card = page.locator('.card').nth(index);
      
      // Test visibility
      await expect(card).toBeVisible();
      
      // Test image presence
      const img = card.locator('img');
      await expect(img).toBeVisible();
      
      // Test title presence and format
      const title = card.locator('.card-title');
      await expect(title).toHaveText(/Page is (ready|not ready)/);
    });
  }
});

// Parameterized tests for specific card properties
test.describe('Specific card properties', () => {
  for (const card of cards) {
    test(`card ${card.index} should have correct class and links`, async ({ page }) => {
      const cardElement = page.locator('.card').nth(card.index);
      
      // Test class
      await expect(cardElement).toHaveClass(new RegExp(card.class));
      
      // Test links
      const links = cardElement.locator('a');
      if (card.hasLinks) {
        for (const link of await links.all()) {
          await expect(link).toHaveAttribute('href', card.link);
        }
      } else {
        await expect(links).toHaveCount(0);
      }
    });
  }
});