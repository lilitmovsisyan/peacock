from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, {}),
    path('index/', views.index, name='index'),
    path('project<int:project_id>/<str:project_title>/', views.project, name='project')
]