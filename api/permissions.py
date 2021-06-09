from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only owner
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.creator == request.user:
                return True