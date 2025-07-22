from django.urls import path
from . views import TodoView,TodoDetail


urlpatterns = [
    path('todos/', TodoView.as_view()),
    path('todo/<str:id>/', TodoDetail.as_view())
]
    