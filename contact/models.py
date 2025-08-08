from django.db import models
from django.utils import timezone

from contact.fields import SnowflakeIDField

class Contact(models.Model):
    code = SnowflakeIDField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
