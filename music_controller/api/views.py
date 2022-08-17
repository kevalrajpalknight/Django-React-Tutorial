from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Room
from .serializers import RoomSerializer


class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer