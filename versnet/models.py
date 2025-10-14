from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='versnet_authored')
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='versnet_images/')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
