from rest_framework import permissions
from rest_framework.permissions import BasePermission



class IsObjectOwner(permissions.BasePermission):
    edit_methods=("PATCH","PUT")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj == request.user:
            return True
        
        if request.user.is_staff and request.method not in self.edit_methods:
            return True
        
        return False        
