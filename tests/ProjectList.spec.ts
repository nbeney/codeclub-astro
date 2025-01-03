import { test, expect } from '@playwright/test';

const projects = [
  { index: 0, title: 'ASCII Art Maker', difficulty: 'EASY' },
  { index: 1, title: 'Binary Clock', difficulty: 'MEDIUM' },
  { index: 2, title: 'Connect Four', difficulty: 'HARD' }
];

const difficulties = ['EASY', 'MEDIUM', 'HARD'];

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/ProjectListTest');
});

// Basic card tests
test('should have correct number of cards', async ({ page }) => {
  const cards = page.locator('.card');
  await expect(cards).toHaveCount(3);
});

// Parameterized tests for each card
test.describe('Card content tests', () => {
  for (const project of projects) {
    test(`card ${project.index} should have correct content`, async ({ page }) => {
      const card = page.locator('.card').nth(project.index);

      // Test image
      const img = card.locator('img');
      await expect(img).toBeVisible();

      // Test title and difficulty
      const body = card.locator('.card-body');
      await expect(body).toHaveText(`${project.title} ${project.difficulty}`);

      // Test badge
      const badge = card.locator('.badge');
      await expect(badge).toHaveText(project.difficulty);
    });
  }
});

// Parameterized tests for difficulty filters
test.describe('Difficulty filter tests', () => {
  for (const difficulty of difficulties) {
    test(`should show only ${difficulty} cards when clicking ${difficulty} filter`, async ({ page }) => {
      // Click the filter
      await page.getByText(difficulty.charAt(0) + difficulty.slice(1).toLowerCase(), { exact: true }).click();

      const cards = page.locator('.card');
      await expect(cards).toHaveCount(3); // Total cards should remain the same

      // Check visibility of each card based on difficulty
      for (const card of await cards.all()) {
        const badge = card.locator('.badge');
        if (await badge.textContent() === difficulty) {
          await expect(card).toBeVisible();
        } else {
          await expect(card).not.toBeVisible();
        }
      }
    });
  }
});

// Test for "All" filter
test('should show all cards when clicking All filter after applying filters', async ({ page }) => {
  // Apply all filters first
  for (const difficulty of difficulties) {
    await page.getByText(difficulty.charAt(0) + difficulty.slice(1).toLowerCase(), { exact: true }).click();
  }

  // Click All filter
  await page.getByText('All', { exact: true }).click();

  // Verify all cards are visible
  const cards = page.locator('.card');
  await expect(cards).toHaveCount(3);

  for (const card of await cards.all()) {
    await expect(card).toBeVisible();
  }
});

// Test that the first card changes appearance when hovered
test('cards should show hover effect', async ({ page }) => {
  // Get all cards
  const cards = await page.locator('.card').all();

  // Test each card
  for (const card of cards) {
      // Get initial styles
      const initialBox = await card.evaluate((el) => {
          const style = window.getComputedStyle(el);
          return {
              shadow: style.boxShadow,
              transform: style.transform,
              transition: style.transition
          };
      });

      // Hover over the card
      await card.hover();

      // Wait for any transitions to complete (typical transition duration)
      await page.waitForTimeout(300);

      // Get styles after hover
      const hoverBox = await card.evaluate((el) => {
          const style = window.getComputedStyle(el);
          return {
              shadow: style.boxShadow,
              transform: style.transform,
              transition: style.transition
          };
      });

      // Verify that styles changed on hover
      expect(hoverBox).not.toEqual(initialBox);

      // Optional: Add specific style checks if you know the exact hover effects
      // For example, if you expect a specific transform or shadow:
      // expect(hoverBox.transform).not.toBe('none');
      // expect(hoverBox.shadow).not.toBe('none');
  }

  // for (const project of projects) {
  //   test(`card ${project.index} should have correct content`, async ({ page }) => {
  //     const card = page.locator('.card').nth(project.index);

  //   });
  // }
});
