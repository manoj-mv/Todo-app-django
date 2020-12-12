from django.urls import path


from . import views

app_name='tasks'

urlpatterns = [
    # path('',views.IndexView.as_view(),name='index'),
    path('',views.CreateTask_and_list.as_view(),name="create_and_list"),
    path('todo/<int:pk>/update',views.updateTask.as_view(),name='task_update'),
    path('todo/<int:pk>/delete',views.deleteTask.as_view(),name='task_delete'),
    path('task_complete/<int:pk>',views.TaskComplete.as_view(),name='task_complete'),
    path('task_incomplete/<int:pk>',views.TaskIncomplete.as_view(),name='task_incomplete'),
]
