from django.urls import path

from .views import UserView, login_view

urlpatterns = [
    path("accounts/", UserView.as_view()),
    path("login/", login_view),
]
