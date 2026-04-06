from rest_framework.permissions import BasePermission,  SAFE_METHODS


class OrderPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if user.groups.filter(name='Manager').exists():
            return True

        if user.groups.filter(name='Employee').exists():
            return request.method in SAFE_METHODS

        if user.groups.filter(name='Customer').exists():
            if request.method in SAFE_METHODS:
                return True
            return request.method == 'POST'

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.groups.filter(name='Manager').exists():
            return True

        if user.groups.filter(name='Employee').exists():
            return request.method in SAFE_METHODS

        if user.groups.filter(name='Customer').exists():
            return obj.customer.user == user

        return False