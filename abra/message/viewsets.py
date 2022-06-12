from rest_framework import viewsets

from .models import Message
from .serializers import LanguageSerializer



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'pk'
