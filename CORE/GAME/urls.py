from django.urls import path
from .views import GameViews, CategoryViews


urlpatterns = [
    path("",GameViews.as_view()),
    path("<int:pk>", GameViews.as_view()),
    path("categories",CategoryViews.as_view()),
    path("categories/<int:pk>",CategoryViews.as_view())
]