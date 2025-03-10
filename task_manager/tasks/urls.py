from django.urls import path, include # type: ignore
from . import views  # Import views properly

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:id>/edit/', views.task_update, name='task_update'),
    path('<int:id>/delete/', views.task_delete, name='task_delete'),
    path('', views.task_list, name='task_list'),
]

