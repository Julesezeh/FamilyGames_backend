from django.urls import path
from .views import GameViews


urlpatterns = [
    path("",GameViews.as_view())
]