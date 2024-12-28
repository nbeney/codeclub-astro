import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('/codeclub-astro/tests/BadgeTest');
});

test('should have 3 badges', async ({ page }) => {
  const badges = page.locator('span.badge');
  await expect(badges).toHaveCount(3);
});

test('first badge should have class bg-success', async ({ page }) => {
  const badges = page.locator('span.badge');
  const badge = badges.nth(0);
  await expect(badge).toHaveClass(/bg-success/);
});

test('first badge should say EASY', async ({ page }) => {
  const badges = page.locator('span.badge');
  const badge = badges.nth(0);
  await expect(badge).toHaveText('EASY');
});

test('second badge should have class bg-warning', async ({ page }) => {
  const badges = page.locator('span.badge');
  const badge = badges.nth(1);
  await expect(badge).toHaveClass(/bg-warning/);
});

test('second badge should say MEDIUM', async ({ page }) => {
  const badges = page.locator('span.badge');
  const badge = badges.nth(1);
  await expect(badge).toHaveText('MEDIUM');
});

test('third badge should have class bg-danger', async ({ page }) => {
  const badges = page.locator('span.badge');
  const badge = badges.nth(2);
  await expect(badge).toHaveClass(/bg-danger/);
});

test('third badge should say HARD', async ({ page }) => {
  const badges = page.locator('span.badge');
  const badge = badges.nth(2);
  await expect(badge).toHaveText('HARD');
});
