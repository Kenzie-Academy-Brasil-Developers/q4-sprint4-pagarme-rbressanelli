from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from user.models import User


class IsAdminUser(BasePermission):
    def has_permission(self, request: Request, view):
        restrict_methods = ["GET", "POST"]

        user: User = request.user

        if request.method in restrict_methods and not user.is_admin:
            return False

        return True
