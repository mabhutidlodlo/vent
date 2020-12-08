from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import Articles , Likes , DisLikes , Comments


class CreateArticleSerializer (serializers.Serializer):
    class Meta:
        model = Articles
        fields = ['article']

class GetArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['id', 'user', 'article']

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment']

class GetCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', 'article','comment']
