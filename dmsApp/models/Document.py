from django.db import models
from ..models.User import User

class Document(models.Model):
    file_name=models.CharField(max_length=255)
    original_name=models.CharField(max_length=200)
    path=models.CharField(max_length=255)
    extension=models.CharField(max_length=50)
    mime_type=models.CharField(max_length=255)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
