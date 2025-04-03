from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from .models import Project, Contributor, Issue, Comment

class ProjectTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com',
            password='testpassword123',
            age=25
        )
        
        self.client.force_authenticate(user=self.user)
        
    def test_create_project(self):
        """
        Ensure we can create a new project.
        """
        url = reverse('project-list')
        data = {
            'title': 'Test Project',
            'description': 'Test Description',
            'type': 'back-end'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().title, 'Test Project')
        self.assertEqual(Project.objects.get().author, self.user)
