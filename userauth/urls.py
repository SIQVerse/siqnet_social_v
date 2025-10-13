from django.urls import path
from .views import edit_profile, public_profile

urlpatterns = [
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', public_profile, name='public_profile'),
]
