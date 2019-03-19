from django.db import models

# Create your models here.
class upload(models.Model):
    description = models.CharField(max_length=255, blank=True)
    upload = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
