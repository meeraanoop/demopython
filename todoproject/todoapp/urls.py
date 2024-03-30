from django.urls import path
from . import views

#urlpatterns = [
     #path('', views.create_task, name='create_task'),
      #path('task/<int:task_id>/', views.task_detail, name='task_detail'),

from django.urls import path
from . import views
from .views import TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', views.task_detail_and_create, name='task_detail_and_create'),
    path('task/<int:task_id>/done/', views.task_done, name='task_done'),
    path('task/<int:task_id>/update/', views.task_update, name='task_update'),
    path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
    path('cbvhome/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('cbvhome/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('cbvhome/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

]
