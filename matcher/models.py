from django.db import models


class MatchResult(models.Model):
    resume_text = models.TextField()
    jd_text = models.TextField()
    score = models.IntegerField()
    must_have_matched = models.JSONField(default=list)
    must_have_missing = models.JSONField(default=list)
    nice_to_have_matched = models.JSONField(default=list)
    nice_to_have_missing = models.JSONField(default=list)
    summary = models.TextField()
    suggestions = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Match ({self.score}%) - {self.created_at.strftime('%Y-%m-%d %H:%M')}"