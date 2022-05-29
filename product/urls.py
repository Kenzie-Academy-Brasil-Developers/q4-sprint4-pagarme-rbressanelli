from rest_framework.urls import path

from product.views import GetProductBySellerId, ProductView, ProductViewById

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<pk>/", ProductViewById.as_view()),
    path("products/seller/<seller_id>/", GetProductBySellerId.as_view()),
]
