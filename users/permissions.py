from rest_framework.permissions import BasePermission


class IsUserModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()
