from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, {}, name='home'),
    path('index/', views.index, name='index'),
    path('bio/', views.bio, name='bio'),
    path('project<int:project_id>/<str:project_title>/', views.project, name='project')
]