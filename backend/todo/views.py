from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializers import TodoSerializer




class TodoView(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()