from django.shortcuts import render
from .models import FoodType, Food, Comment
from .serializer import FoodTypeSerializer, FoodSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


# Create your views here.

class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    authentication_classes = [TokenAuthentication]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    authentication_classes = [TokenAuthentication]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]

