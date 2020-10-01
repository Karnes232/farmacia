from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    title = models.CharField(max_length=64)
    post_body = models.TextField()
    link = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Sales(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    daily_sales = models.IntegerField(blank=False, null=False)
    cost = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.timestamp} - Sales - {self.daily_sales}"

class Inventroy(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    cost = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return f"Cost - {self.timestamp} - {self.cost}"
 
