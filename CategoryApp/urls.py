# CategoryApp/urls.py
from django.urls import path
from . import views
app_name = 'CategoryApp'
urlpatterns = [
    path('', views.all_categories, name='all_categories'),
]
