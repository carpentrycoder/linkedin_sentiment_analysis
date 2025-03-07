import json
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from sentiment_analysis_app.ai_model.ai_pipeline import analyze_sentiment  # Import AI function

@method_decorator(csrf_exempt, name='dispatch')
class AnalyzeProfile(View):
    def post(self, request):
        try:
            # ✅ Debugging: Print incoming request
            print("📥 Incoming Request Body:", request.body.decode("utf-8"))

            # ✅ Fix JSON decoding
            data = json.loads(request.body)
            print(f"📥 Parsed Data: {data}")

            profile_url = data.get("profile_url")  # ✅ Fix key name

            if not profile_url:
                return JsonResponse({"error": "Profile URL is required"}, status=400)

            print(f"🔍 Profile URL received: {profile_url}")

            # ✅ Run the scraping script
            process = subprocess.run(
                ["node", "../scraping/scraper.js", profile_url],
                capture_output=True,
                text=True
            )

            print(f"📝 Scraper Output: {process.stdout}")
            print(f"⚠️ Scraper Errors: {process.stderr}")

            if process.returncode != 0:
                return JsonResponse({"error": "Scraper failed", "details": process.stderr}, status=500)

            # ✅ Parse scraped data correctly
            try:
                scraped_data = json.loads(process.stdout)
            except json.JSONDecodeError as e:
                return JsonResponse({"error": "Failed to parse scraper output", "details": str(e)}, status=500)

            print(f"✅ Scraped Data: {scraped_data}")

            # ✅ Perform sentiment analysis
            analysis_result = analyze_sentiment(scraped_data)
            print(f"📊 Sentiment Analysis Result: {analysis_result}")

            return JsonResponse({"result": analysis_result})

        except Exception as e:
            print(f"❌ Internal Server Error: {e}")
            return JsonResponse({"error": "Internal server error", "details": str(e)}, status=500)

    def get(self, request):
        return JsonResponse({"error": "Invalid request"}, status=400)
