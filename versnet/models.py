from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='versnet_posts')
    headline = models.CharField(max_length=255)
    summary = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.headline} by {self.author.username}"
