from rest_framework.permissions import BasePermission
from rest_framework.views import Request

from user.models import User


class IsAdminUser(BasePermission):
    def has_permission(self, request: Request, _):
        restrict_methods = "GET"

        user: User = request.user

        if request.method in restrict_methods and not user.is_admin:
            return False

        return True
