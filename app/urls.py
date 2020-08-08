from django.urls import path
from app.views import UserActivity

urlpatterns = [
    path("user_activity", UserActivity.as_view()),
]
