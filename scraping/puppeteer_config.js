const puppeteer = require('puppeteer');

async function launchBrowser() {
    return await puppeteer.launch({
        headless: true, // Set to false for debugging
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
}

module.exports = { launchBrowser };
