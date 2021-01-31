from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<int:id>/', views.post, name='post'),
    path('tag/<slug:tag>/', views.posts_by_tag, name='posts_by_tag'),
    path('add/', views.add_post, name='add_post'),
]
