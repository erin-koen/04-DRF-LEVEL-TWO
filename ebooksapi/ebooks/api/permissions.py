from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # not sure what super is doing here
        is_admin = super().has_permission(request, view)
        # is the user an admin or is the request http verb in safe methods?
        return request.method in permissions.SAFE_METHODS or is_admin


class IsReviewAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.review_author == request.user
