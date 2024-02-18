from django.urls import path
from . import views

app_name = 'UserApp'
urlpatterns = [
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
]
