import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/PageLayoutTest1');
});

test('should have correct title', async ({ page }) => {
  await expect(page).toHaveTitle('Test - PageLayout #1');
});

test('should have correct heading', async ({ page }) => {
  await expect(page.locator('h1')).toHaveText('PageLayout Test #1');
});

test('should have correct content', async ({ page }) => {
  const body = page.locator('body');
  await expect(body).toContainText('Some content here...');
  await expect(body).toContainText('Go to page #2');
});

test.describe('Header', () => {
  test('should have correct title', async ({ page }) => {
    await expect(page.locator('header')).toContainText('Code Club');
  });

  test('should have title linked to the first page', async ({ page }) => {
    const title = page.locator('header a.navbar-brand');
    await expect(title).toHaveAttribute('href', '/codeclub-astro/tests/PageLayoutTest1');
  });

  test('should have working navigation dropdown', async ({ page }) => {
    const dropdownButton = page.locator('#dropdownMenuButton');
    await expect(dropdownButton).toBeVisible();
    await expect(dropdownButton).toHaveText('Page1');

    await dropdownButton.click();

    const dropdownItems = [
      { text: 'Page1', href: '/codeclub-astro/tests/PageLayoutTest1' },
      { text: 'Page2', href: '/codeclub-astro/tests/PageLayoutTest2' },
    ];

    for (const item of dropdownItems) {
      const menuItem = page.locator('.dropdown-item', { hasText: item.text });
      await expect(menuItem).toBeVisible();
      await expect(menuItem).toHaveAttribute('href', item.href);
    }
  });
});

test.describe('Footer', () => {
  test('should have correct copyright', async ({ page }) => {
    const footer = page.locator('footer');
    const currentYear = new Date().getFullYear().toString();
    await expect(footer).toContainText(`© 2023-${currentYear} Nicolas Beney. All rights reserved.`);
  });
});
