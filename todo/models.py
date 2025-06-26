from django.db import models

from django.contrib.auth.models import User

class StatusChoise(models.TextChoices):
    NEW = 'New', 'New'
    IN_PROGRESS = 'In progress', 'In progress'
    COMPLATED = 'Complated', 'Complated'


class Task(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=StatusChoise.choices, default='New')
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
