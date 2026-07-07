from django.contrib import admin
from .models import MatchResult


@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    list_display = ("id", "score", "created_at")
    list_filter = ("score",)
    readonly_fields = ("created_at",)