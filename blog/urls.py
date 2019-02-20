from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, {}, name='bloghome'),
    path('index/', views.index, name='index'),
    path('bio/', views.bio, name='bio'),
    path('project<int:project_id>/<str:project_title>/', views.project, name='project'),
    path('tags/', views.taglist, name='tags'),
    path('tags/<str:tag_name>/', views.tagpage, name='tagpage')
]