from rest_framework.urls import path

from payable.views import PayablesView

urlpatterns = [path("payables/", PayablesView.as_view())]
