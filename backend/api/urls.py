from django.urls import path
from . import views

urlpatterns = [
    path("todos/", views.TodoView.as_view(), name="todos"),
    path(
        "todos/<int:pk>",
        views.TodoRetriveUpdateDestroyView.as_view(),
        name="crud-todos",
    ),
    path(
        "todos/<int:pk>/compelete",
        views.TodoToggleCompeleteView.as_view(),
        name="compelete-todo",
    ),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
]
