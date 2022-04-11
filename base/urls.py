import imp
from django.urls import path 
from .views import TaskCreate, TaskDetail, Taskdelete, Tasklist , Taskupdate 
from django.contrib.auth import views as auth_views
from . import views as core_views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path( 'login/',auth_views.LoginView.as_view(template_name="base/login.html"), name="login"),
    path('',Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(), name='create-task'),
    path('task-update/<int:pk>/',Taskupdate.as_view(), name='update-task'),
    path('task-delete/<int:pk>/',Taskdelete.as_view(), name='delete-task'),
    path('signup/', core_views.signup, name='signup'),
    path('/logout', LogoutView.as_view(next_page='login'),name='logout')
]