from django.db import models
from django.utils.timezone import now
import uuid
from users.models import User


class Project(models.Model):
    BACKEND = 'Back-end'
    FRONTEND = 'Front-end'
    IOS = 'IOS'
    ANDROID = 'Android'

    TYPE_CHOICES = [
        (BACKEND, 'Back-End'),
        (FRONTEND, 'Front-End'),
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    author = models.ForeignKey(User, related_name='authored_projects', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default="Contributor")

    class Meta:
        unique_together = [('user')]

    def __str__(self):
        return f"{self.user.username}"

class Issue(models.Model):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    BUG = 'BUG'
    FEATURE = 'FEATURE'
    TASK = 'TASK'

    TAG_CHOICES = [
        (BUG, 'Bug'),
        (FEATURE, 'Feature'),
        (TASK, 'Task'),
    ]

    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    FINISHED = 'Finished'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES, default=TASK)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    project = models.ForeignKey(Project, related_name='issues', on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name='assigned_issues', null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, related_name='authored_issues', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    issue = models.ForeignKey(Issue, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='authored_comments', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=now)

    def __str__(self):
        return f"Comment by {self.author.username} on Issue {self.issue.title}"
