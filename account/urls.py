from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('<int:id>/', views.account, name='account')
]