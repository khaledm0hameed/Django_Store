from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
