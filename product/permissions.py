from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework.views import Request

from user.models import User


class IsSellerUser(BasePermission):
    def has_permission(self, request: Request, _):
        restrict_methods = ["POST"]

        user: User = request.user

        if request.method in restrict_methods and not user.is_seller:
            return False

        return True
