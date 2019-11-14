from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('user/<int:pk>', views.user_detail, name="user_detail") ,
    path('user/new', views.user_create, name='user_create'),
    path('user/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete', views.user_delete, name='user_delete'),
    path('videos/', views.videos_list, name='videos_list'),
    path('video/<int:pk>', views.video_detail, name='video_detail'),
    path('video/<int:pk>/edit', views.video_edit, name='video_edit'),
    path('video/new', views.video_create, name='video_create'),
    path('video/<int:pk>/delete', views.video_delete, name='video_delete'),
    path('about', views.about, name='about'),
]