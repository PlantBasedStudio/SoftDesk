from rest_framework import permissions
from .models import Project, Contributor

class IsAuthor(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.author == request.user

class IsProjectContributor(permissions.BasePermission):
    """
    Custom permission to only allow contributors of a project to access it.
    """
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        if not project_id:
            return True
            
        return request.user.is_authenticated and Contributor.objects.filter(
            project_id=project_id,
            user=request.user
        ).exists()
        
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'project'):
            project = obj.project
        elif hasattr(obj, 'issue'):
            project = obj.issue.project
        else:
            project = obj
            
        return Contributor.objects.filter(
            project=project,
            user=request.user
        ).exists()
