from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    profile = models.FileField(upload_to='images/profile/', null=True)
    verification_code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())
      
    class Meta:
        db_table = 'app_users'