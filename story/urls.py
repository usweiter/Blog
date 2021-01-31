from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [
    path('add/', views.add_story, name='add_story')
]
