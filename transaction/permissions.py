from rest_framework.permissions import BasePermission
from rest_framework.views import Request

from user.models import User


class IsBuyerUser(BasePermission):
    def has_permission(self, request: Request, _):
        restrict_methods = ["GET", "POST"]

        user: User = request.user

        if user.is_anonymous:
            return False

        if request.method in restrict_methods and user.is_admin and user.is_seller:
            return False

        return True
