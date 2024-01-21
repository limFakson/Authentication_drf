from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions  import IsAuthenticated

from .serializers import UserSerializer
from .models import User


# Create your views here.
class UserListView(generics.ListCreateApiView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_classes = UserSerializer