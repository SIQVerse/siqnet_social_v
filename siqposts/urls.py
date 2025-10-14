from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('search/', views.search_posts, name='search_posts'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('avatar/<str:username>/', views.avatar_view, name='avatar_view'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:username>/', views.send_message, name='send_message'),
    path('tag/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
]
