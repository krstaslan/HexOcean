from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Image,User,Tier

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name']

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

