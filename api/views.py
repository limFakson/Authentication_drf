from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


# Create your views here.
# class UserListView(generics.ListCreateApiView):
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_classes = UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, request):
        serializer = serializer_classes(self.queryset, many=True)
        return Response(serializer.data)