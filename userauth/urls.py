from .views import edit_profile, public_profile, profile

urlpatterns = [
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', public_profile, name='public_profile'),
]
