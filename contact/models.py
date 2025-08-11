from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from contact.fields import SnowflakeIDField

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    code = SnowflakeIDField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    code = SnowflakeIDField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%M/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                blank=True,
                                null=True)  
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                blank=True,
                                null=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
