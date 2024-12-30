import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/AccordionTest');
});

test('first accordion should expand and collapse correctly', async ({ page }) => {
  // Check initial state
  await expect(page.locator('#panelsStayOpen-collapse17')).toHaveClass(/collapse/);
  await expect(page.locator('#panelsStayOpen-collapse18')).toHaveClass(/collapse/);

  // Click first item and verify it expands
  await page.click('button:has-text("Item #1")');
  await expect(page.locator('#panelsStayOpen-collapse17')).toHaveClass(/collapse show/);
  await expect(page.locator('#panelsStayOpen-collapse18')).toHaveClass(/collapse/);

  // Verify content is visible
  await expect(page.locator('#panelsStayOpen-collapse17')).toContainText('First content');

  // Click first item again and verify it collapses
  await page.click('button:has-text("Item #1")');
  await expect(page.locator('#panelsStayOpen-collapse17')).toHaveClass(/collapse/);
});

test('second accordion should expand and collapse correctly', async ({ page }) => {
  // Check initial state
  await expect(page.locator('#panelsStayOpen-collapse19')).toHaveClass(/collapse/);
  await expect(page.locator('#panelsStayOpen-collapse20')).toHaveClass(/collapse/);

  // Click third item and verify it expands
  await page.click('button:has-text("Item #3")');
  await expect(page.locator('#panelsStayOpen-collapse19')).toHaveClass(/collapse show/);
  await expect(page.locator('#panelsStayOpen-collapse20')).toHaveClass(/collapse/);

  // Verify content is visible
  await expect(page.locator('#panelsStayOpen-collapse19')).toContainText('Third content');

  // Click third item again and verify it collapses
  await page.click('button:has-text("Item #3")');
  await expect(page.locator('#panelsStayOpen-collapse19')).toHaveClass(/collapse/);
});

test('multiple accordion items can be open simultaneously', async ({ page }) => {
  // Click multiple items
  await page.click('button:has-text("Item #1")');
  await page.click('button:has-text("Item #3")');

  // Verify both items are expanded
  await expect(page.locator('#panelsStayOpen-collapse17')).toHaveClass(/collapse show/);
  await expect(page.locator('#panelsStayOpen-collapse19')).toHaveClass(/collapse show/);

  // Verify content is visible
  await expect(page.locator('#panelsStayOpen-collapse17')).toContainText('First content');
  await expect(page.locator('#panelsStayOpen-collapse19')).toContainText('Third content');
});

test('accordion buttons should have correct text and styling', async ({ page }) => {
  // Verify button text contains both item number and description
  await expect(page.locator('button:has-text("Item #1")')).toContainText('First item');
  await expect(page.locator('button:has-text("Item #2")')).toContainText('Second item');
  await expect(page.locator('button:has-text("Item #3")')).toContainText('Third item');
  await expect(page.locator('button:has-text("Item #4")')).toContainText('Fourth item');

  // Verify item numbers have primary color
  await expect(page.locator('button strong.text-primary')).toHaveCount(4);
});