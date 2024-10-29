from rest_framework.permissions import BasePermission


class IsUserModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
