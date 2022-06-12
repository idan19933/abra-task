from rest_framework import serializers
from .models import Message,User

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','Sender','Receiver','Message','Receiver','date']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','first_name','last_name']








