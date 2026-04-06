from rest_framework.permissions import BasePermission,  SAFE_METHODS


class ProductPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.groups.filter(name='Manager').exists():
            return True

        if user.groups.filter(name='Employee').exists():
            return request.method in SAFE_METHODS

        if user.groups.filter(name='Customer').exists():
            return request.method in SAFE_METHODS

        return False