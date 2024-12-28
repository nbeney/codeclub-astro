import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/CodeBlockTest');
});

test('should have 2 code blocks', async ({ page }) => {
  const codeBlocks = page.locator('pre');
  await expect(codeBlocks).toHaveCount(2);
});

test('first code block should contain text', async ({ page }) => {
  const codeBlocks = page.locator('pre');
  const codeBlock = codeBlocks.nth(0);
  await expect(codeBlock).toContainText('# This code was embedded in HTML.');
  await expect(codeBlock).toContainText('total = 1 + 2');
  await expect(codeBlock).toContainText('print(\'Hello World!\')');
});

test('second code block should contain text', async ({ page }) => {
  const codeBlocks = page.locator('pre');
  const codeBlock = codeBlocks.nth(1);
  await expect(codeBlock).toContainText('# This code was loaded from a file.');
  await expect(codeBlock).toContainText('total = 1 + 2');
  await expect(codeBlock).toContainText('print(\'Hello World!\')');
});

test('first code block contains hljs-comment CSS class', async ({ page }) => {
  const codeBlocks = page.locator('pre');
  const codeBlock = codeBlocks.nth(0);
  const span = codeBlock.locator('xpath=//span[starts-with(text(), "# This code")]').nth(0);
  await expect(span).toHaveClass(/hljs-comment/);
});

test('second code block contains hljs-comment CSS class', async ({ page }) => {
  const codeBlocks = page.locator('pre');
  const codeBlock = codeBlocks.nth(0);
  const span = codeBlock.locator('xpath=//span[starts-with(text(), "# This code")]').nth(0);
  await expect(span).toHaveClass(/hljs-comment/);
});

// TODO: Test that clipboard icons works.
