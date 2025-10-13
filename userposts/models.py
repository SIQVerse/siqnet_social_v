from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    badge = models.ImageField(upload_to='badges/')
    date_joined = models.DateField(auto_now_add=True)
    impact_score = models.IntegerField(default=0)

    CATEGORY_CHOICES = [
        ('impact', 'Impact'),
        ('silence', 'Silence'),
        ('legacy', 'Legacy'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='impact')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    siq_score = models.IntegerField(default=0)
    campaigns = models.ManyToManyField(Campaign, blank=True)

    def __str__(self):
        return self.user.username
