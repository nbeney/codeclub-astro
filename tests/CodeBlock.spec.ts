import { test, expect } from '@playwright/test';

const codeBlocks = [
  {
    index: 0,
    expectedTexts: [
      '# This code was embedded in HTML.',
      'total = 1 + 2',
      'print(\'Hello World!\')'
    ],
    commentText: '# This code was embedded in HTML.'
  },
  {
    index: 1,
    expectedTexts: [
      '# This code was loaded from a file.',
      'total = 1 + 2',
      'print(\'Hello World!\')'
    ],
    commentText: '# This code was loaded from a file.'
  }
];

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/CodeBlockTest');
});

// Basic code block count test
test('should have correct number of code blocks', async ({ page }) => {
  const codeBlockElements = page.locator('pre');
  await expect(codeBlockElements).toHaveCount(codeBlocks.length);
});

// Parameterized tests for code block content
test.describe('Code block content', () => {
  for (const block of codeBlocks) {
    test(`code block ${block.index} should have correct content and styling`, async ({ page }) => {
      const codeBlock = page.locator('pre').nth(block.index);
      
      // Test all expected text content
      for (const text of block.expectedTexts) {
        await expect(codeBlock).toContainText(text);
      }
      
      // Test syntax highlighting for comments
      const commentSpan = codeBlock.locator(`xpath=//span[starts-with(text(), "${block.commentText}")]`).nth(0);
      await expect(commentSpan).toHaveClass(/hljs-comment/);
    });
  }
});

// TODO: Add tests for clipboard functionality
// test.describe('Clipboard functionality', () => {
//   // Add tests for clipboard icons when ready
// });