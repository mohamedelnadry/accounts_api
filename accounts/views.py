from django.shortcuts import render

from rest_framework import generics
from .serializers import USerSerializer
from django.contrib.auth.models import User


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = USerSerializer


class DetailUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = USerSerializer


class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = USerSerializer

