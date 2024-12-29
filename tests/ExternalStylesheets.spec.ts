import { test, expect } from '@playwright/test';
import fs from 'fs';
import path from 'path';

const pages = [
    ['home', '/codeclub-astro/'],
    ['guizero', '/codeclub-astro/activities/guizero-based/'],
    ['pygame-zero', '/codeclub-astro/activities/pygame-zero-based/'],
    ['adventurelib', '/codeclub-astro/activities/adventurelib-based/'],
    ['p5', '/codeclub-astro/activities/p5-based/'],
    ['python-libraries', '/codeclub-astro/activities/python-libraries/'],
];
  
const expectedStylesheets = [
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/styles/vs2015.min.css',
  'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css',
  'https://fonts.googleapis.com/css2?family=Luckiest Guy:wght@400&amp;display=swap',
];

// Create debug directory if it doesn't exist
const debugDir = path.join(process.cwd(), 'test-debug');
if (!fs.existsSync(debugDir)) {
  fs.mkdirSync(debugDir);
}

test.describe('External stylesheet tests', () => {
  for (const [pageName, pagePath] of pages) {
    test(`page ${pagePath} should have all required stylesheets`, async ({ page }) => {
      // Navigate to the page and get the content
      await page.goto(pagePath);
      const content = await page.content();
      
      // Save page source to debug file
      const filename = pageName + '.html';
      const debugFilePath = path.join(debugDir, filename);
      fs.writeFileSync(debugFilePath, content);
      
      // Check each expected stylesheet
      for (const stylesheet of expectedStylesheets) {
        await expect(
          content.includes(stylesheet),
          `Stylesheet ${stylesheet} not found in source of page ${pagePath}. Debug file saved to ${debugFilePath}`
        ).toBeTruthy();
      }
      
      // Log success message with debug file location
      console.log(`✓ Saved source for ${pagePath} to ${debugFilePath}`);
    });
  }
});
