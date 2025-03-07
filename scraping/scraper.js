// scraper.js
const puppeteer = require('puppeteer');
const axios = require('axios');

const DJANGO_API_URL = 'http://127.0.0.1:8000/api/analyze/'; // Django API endpoint

async function scrapeProfile(profileUrl) {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    try {
        await page.goto(profileUrl, { waitUntil: 'networkidle2' });

        const scrapedData = await page.evaluate(() => {
            const name = document.querySelector('h1')?.innerText.trim() || "";
            const title = document.querySelector('p.text-gray-400')?.innerText.trim() || "";
            const location = document.querySelector('p.text-gray-500')?.innerText.trim() || "";
            
            const experience = Array.from(document.querySelectorAll('div.border-t.border-gray-600.p-6 ul li'))
                .map(el => el.innerText.trim());

            const posts = Array.from(document.querySelectorAll('div.cursor-pointer'))
                .map(el => ({
                    title: el.querySelector('h3')?.innerText.trim() || "",
                    content: el.nextElementSibling?.innerText.trim() || ""
                }));

            return { name, title, location, experience, posts };
        });

        // Send data to Django backend
        const response = await axios.post(DJANGO_API_URL, scrapedData, {
            headers: { 'Content-Type': 'application/json' }
        });

        console.log("✅ Data sent successfully:", response.data);
    } catch (error) {
        console.error("❌ Error:", error);
    } finally {
        await browser.close();
    }
}

// Get profile URL from command-line arguments
const profileUrl = process.argv[2];
if (!profileUrl) {
    console.error("❌ Error: No profile URL provided.");
    process.exit(1);
}

scrapeProfile(profileUrl);
