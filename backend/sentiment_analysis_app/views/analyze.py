import json
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ai_model.ai_pipeline import analyze_sentiment  # Import AI function

@csrf_exempt
def analyze_profile(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"📥 Received Data: {data}")
            profile_link = data.get("profile_link")

            if not profile_link:
                return JsonResponse({"error": "Profile link is required"}, status=400)

            print(f"🔍 Received profile link: {profile_link}")

            # Run the scraping script
            process = subprocess.run(
                ["node", "../scraping/scraper.js", profile_link],
                capture_output=True,
                text=True
            )

            print(f"📝 Scraper Output: {process.stdout}")
            print(f"⚠️ Scraper Errors: {process.stderr}")

            if process.returncode != 0:
                return JsonResponse({"error": "Scraper failed", "details": process.stderr}, status=500)

            # Parse scraped data
            try:
                scraped_data = json.loads(process.stdout)
            except json.JSONDecodeError as e:
                return JsonResponse({"error": "Failed to parse scraper output", "details": str(e)}, status=500)

            print(f"✅ Scraped Data: {scraped_data}")

            # Perform sentiment analysis
            analysis_result = analyze_sentiment(scraped_data)
            print(f"📊 Sentiment Analysis Result: {analysis_result}")

            return JsonResponse({"result": analysis_result})

        except Exception as e:
            return JsonResponse({"error": "Internal server error", "details": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
