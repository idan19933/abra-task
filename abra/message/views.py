from django.shortcuts import render
from .models import Message,User


from .serializers import LanguageSerializer
from rest_framework import viewsets,permissions


class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.AllowAny,)




















