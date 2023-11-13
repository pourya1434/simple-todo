from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "memo", "compeleted", "created"]
        read_only_field = ["created", "compeleted"]


class TodoToggleCompeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id"]
        read_only_field = ["title", "memo", "compeleted", "created"]
