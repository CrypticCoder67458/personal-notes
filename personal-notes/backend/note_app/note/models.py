from django.db import models
from userProfile.models import Profile


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    related_author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)   

    class Meta:
        ordering=['updated_at','-created_at']

    def __str__(self):
        return self.title