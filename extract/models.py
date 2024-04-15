from django.db import models

# Create your models here.

class CV(models.Model):
    file = models.FileField(upload_to='uploads/')
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    text = models.TextField(null=True, blank=True)