import { test, expect } from '@playwright/test';

const baseUrl = process.env.BASE_URL || 'http://localhost:5000';

test('postcode lookup returns Buckinghamshire Council', async ({ page }) => {

  await page.goto(baseUrl);

  await page.fill(
    'input[name="postcode"]',
    'MK18 1RY'
  );

  await page.click('button');

  await expect(page.locator('body'))
    .toContainText('Buckinghamshire Council');

});


