from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.index, name='index'),
    path('photos/', views.photo_gallery, name='photo_gallery'),
    path('photos/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('videos/', views.video_gallery, name='video_gallery'),
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
]
