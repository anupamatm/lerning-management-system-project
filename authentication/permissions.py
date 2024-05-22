# authentication/permissions.py

from rest_framework.permissions import BasePermission

class IsAdminOrTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type in ['admin', 'teacher']
