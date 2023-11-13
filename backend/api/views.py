from todo.models import Todo
from rest_framework import generics, permissions
from .serializers import TodoSerializer, TodoToggleCompeleteSerializer

from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate

# Create your views here.


class TodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by("-created")

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class TodoRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoToggleCompeleteView(generics.RetrieveUpdateAPIView):
    serializer_class = TodoToggleCompeleteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.compeleted = not (serializer.instance.compeleted)
        serializer.save()


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)  # data is a dictionary
            user = User.objects.create_user(
                username=data["username"], password=data["password"]
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({"token": str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {"error": "username taken. choose another username"}, status=400
            )


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        user = authenticate(
            request, username=data["username"], password=data["password"]
        )
        if user is None:
            return JsonResponse(
                {"error": "unable to login. check username and password"}, status=400
            )
        else:  # return user token
            try:
                token = Token.objects.get(user=user)
            except:  # if token not in db, create a new one
                token = Token.objects.create(user=user)
            return JsonResponse({"token": str(token)}, status=201)
