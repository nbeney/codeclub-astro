import { test, expect } from '@playwright/test';

const badges = [
  { index: 0, text: 'EASY', class: 'bg-success' },
  { index: 1, text: 'MEDIUM', class: 'bg-warning' },
  { index: 2, text: 'HARD', class: 'bg-danger' },
];

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/BadgeTest');
});

// Basic badge count test
test('should have correct number of badges', async ({ page }) => {
  const badgeElements = page.locator('span.badge');
  await expect(badgeElements).toHaveCount(badges.length);
});

// Parameterized tests for badge properties
test.describe('Badge properties', () => {
  for (const badge of badges) {
    test(`badge ${badge.index} should have correct class and text`, async ({ page }) => {
      const badgeElement = page.locator('span.badge').nth(badge.index);

      // Test class
      await expect(badgeElement).toHaveClass(new RegExp(badge.class));

      // Test text
      await expect(badgeElement).toHaveText(badge.text);
    });
  }
});