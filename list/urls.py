from django.urls import path 
from .views import List , TaskDetail
urlpatterns =[
    path('', List.as_view(), name='list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task '),


]