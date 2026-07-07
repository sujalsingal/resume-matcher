from django.urls import path
from .views import IndexView
from .api_views import MatchView

app_name = "matcher"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("api/match/", MatchView.as_view(), name="match-api"),
]