from rest_framework.urls import path

from .views import PaymentMethodView

urlpatterns = [
    path("payment_info/", PaymentMethodView.as_view()),
]
