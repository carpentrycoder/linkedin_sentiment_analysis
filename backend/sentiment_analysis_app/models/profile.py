from django.db import models

class LinkedInProfile(models.Model):
    profile_url = models.URLField(unique=True)
    name = models.CharField(max_length=255)
    headline = models.CharField(max_length=512, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    industry = models.CharField(max_length=255, null=True, blank=True)
    
    # Sentiment Scores
    sentiment_score = models.FloatField(null=True, blank=True)
    technical_knowledge_score = models.FloatField(null=True, blank=True)
    leadership_score = models.FloatField(null=True, blank=True)
    work_culture_fit_score = models.FloatField(null=True, blank=True)
    communication_style_score = models.FloatField(null=True, blank=True)
    engagement_sentiment_score = models.FloatField(null=True, blank=True)
    adaptability_score = models.FloatField(null=True, blank=True)
    networking_score = models.FloatField(null=True, blank=True)
    overall_suitability_score = models.FloatField(null=True, blank=True)
    
    # Key Insights
    key_insights = models.JSONField(null=True, blank=True)
    
    # Predictive Analysis
    emotional_trend = models.TextField(null=True, blank=True)
    industry_comparison = models.TextField(null=True, blank=True)
    ai_detected_red_flags = models.TextField(null=True, blank=True)
    final_verdict = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
