from django.urls import path
from . import views
app_name = 'ProjectApp'
urlpatterns = [
    path('create/', views.create_project, name='create_project'),
    path('edit/<slug:project_slug>/', views.edit_project, name='edit_project'),
    path('delete/<str:project_slug>/', views.delete_project, name='delete_project'),
    path('detail/<slug:project_slug>/', views.project_detail, name='project_detail'),
]
