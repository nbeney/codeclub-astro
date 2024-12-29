import { test, expect } from '@playwright/test';

const pages = [
  ['home', '/codeclub-astro/'],
  ['guizero', '/codeclub-astro/activities/guizero-based/'],
  ['pygame-zero', '/codeclub-astro/activities/pygame-zero-based/'],
  ['adventurelib', '/codeclub-astro/activities/adventurelib-based/'],
  ['p5', '/codeclub-astro/activities/p5-based/'],
  ['python-libraries', '/codeclub-astro/activities/python-libraries/'],
];

test.describe('Navigation styling tests', () => {
  for (const [pageName, pagePath] of pages) {
    test(`page ${pagePath} should have properly styled navigation`, async ({ page }) => {
      // Navigate to the page
      await page.goto(pagePath);

      // Wait for any animations/transitions to complete
      await page.waitForTimeout(2000);

      // Get the navigation element
      const nav = page.locator('nav');

      // Take a screenshot of just the navigation area
      await nav.screenshot({
        path: `test-results/nav-${pageName}.png`
      });

      // Get the computed background color of the nav
      const backgroundColor = await nav.evaluate((element) => {
        return window.getComputedStyle(element).backgroundColor;
      });

      // Check if it's some shade of blue (rgb or rgba)
      const isBlue = backgroundColor.match(/rgba?\(\d+,\s*\d+,\s*(\d+)/);
      const blueValue = isBlue ? parseInt(isBlue[1]) : 0;

      // The blue component should be higher than red and green for a blue color
      expect(isBlue,
        `Navigation on ${pagePath} is not blue. Got color: ${backgroundColor}`
      ).toBeTruthy();
      expect(blueValue > 100,
        `Navigation on ${pagePath} doesn't have enough blue (${blueValue}). Color: ${backgroundColor}`
      ).toBeTruthy();

      // Check that the nav has some minimum height (not collapsed)
      const boundingBox = await nav.boundingBox();
      expect(boundingBox.height > 40,
        `Navigation on ${pagePath} is too short (${boundingBox.height}px). Might not be properly styled.`
      ).toBeTruthy();

      // Verify dropdown functionality
      const dropdown = page.locator('.dropdown-toggle');
      await expect(dropdown).toBeVisible();

      // Click the dropdown and verify menu appears
      await dropdown.click();
      const dropdownMenu = page.locator('.dropdown-menu');
      await expect(dropdownMenu).toBeVisible();

      // Take another screenshot with dropdown open
      await nav.screenshot({
        path: `test-results/nav-dropdown-${pageName}.png`
      });
    });
  }
});

// // Helper function to run tests in both dev and prod modes
// test.describe('Cross-environment tests', () => {
//   test('visual comparison between dev and prod', async ({ page }) => {
//     // Note: You'll need to set up environment variables or command line args
//     // to switch between dev and prod URLs
//     const isProd = process.env.TEST_ENV === 'prod';
//     console.log(`Running in ${isProd ? 'production' : 'development'} mode`);

//     // Log environment-specific information
//     if (isProd) {
//       console.log('💡 If tests fail in prod but pass in dev, check:');
//       console.log('1. Asset paths and base URLs');
//       console.log('2. CSS bundling and minification');
//       console.log('3. Build output directory structure');
//     }
//   });
// });
