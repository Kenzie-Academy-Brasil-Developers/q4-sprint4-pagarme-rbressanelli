from rest_framework.urls import path

from transaction.views import TransactionsView

urlpatterns = [
    path("transactions/", TransactionsView.as_view(), name="createTransaction"),
]
