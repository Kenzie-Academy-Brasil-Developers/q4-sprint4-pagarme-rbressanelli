from rest_framework.urls import path

from .views import FeeView, FeeViewById


urlpatterns = [
    path('fee/', FeeView.as_view()),
    path('fee/<pk>/', FeeViewById.as_view())
]
