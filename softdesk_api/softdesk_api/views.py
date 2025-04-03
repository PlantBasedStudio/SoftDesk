from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project, Issue, Comment, Contributor
from .serializers import (
    ProjectSerializer, IssueSerializer, CommentSerializer, 
    ContributorSerializer, UserSerializer
)
from .permissions import IsAuthor, IsProjectContributor
from django.shortcuts import get_object_or_404

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]
    
    def get_queryset(self):
        return Project.objects.filter(
            contributors__user=self.request.user
        ).distinct()
    
    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project)

class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectContributor]
    
    def get_queryset(self):
        return Contributor.objects.filter(
            project_id=self.kwargs.get('project_pk')
        )
    
    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        serializer.save(project=project)

class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectContributor, IsAuthor]
    
    def get_queryset(self):
        return Issue.objects.filter(
            project_id=self.kwargs.get('project_pk')
        )
    
    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        serializer.save(author=self.request.user, project=project)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectContributor, IsAuthor]
    
    def get_queryset(self):
        return Comment.objects.filter(
            issue_id=self.kwargs.get('issue_pk'),
            issue__project_id=self.kwargs.get('project_pk')
        )
    
    def perform_create(self, serializer):
        issue = get_object_or_404(Issue, 
                                pk=self.kwargs.get('issue_pk'),
                                project_id=self.kwargs.get('project_pk'))
        serializer.save(author=self.request.user, issue=issue)