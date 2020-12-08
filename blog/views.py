from django.shortcuts import render
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import CreateArticleSerializer ,GetArticlesSerializer, CreateCommentSerializer , GetCommentSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Articles , Comments , Likes, DisLikes
# Create your views here.

class  MyArticle(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class  = CreateArticleSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP200.ok)
        return Response(serializer.errors, status = status.HTTP400)


    def put(self, request , pk):
        try:
            article = Articles.objects.get(pk = pk)

        except Articles.DoesNotExist:
            return Response({"error": "the article doesn't exist "})

        serializer = CreateArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP200.ok)
        return Response(serializer.errors, status = status.HTTP400)

    def get(self, request):

        try :
            article = Articles.objects.filter(user = request.user)
        except Article.DoesNotExist:
            return Response({"error":"the are no articles available"})

        serializer = GetArticlesSerializer(article, many = True)
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP200.ok)
        return Response(serializer.errors, status = status.HTTP400)

class getAllArticles(APIView):
    serializer_class = GetArticlesSerializer

    def get(self, request):
        serializer = GetArticlesSerializer(Articles.objects.all(), many  = True)
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP200.ok)
        return Response(serializer.errors, status = status.HTTP400)

class MyComment(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCommentSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateCommentSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status =400)

    def put(self, request, pk):
        try:
            comment = Comments.objects.get(pk = pk)
        except Comments.DoesNotExist:
            return Response({"error" : "the comment does not exist"})

        serializer =CreateCommentSerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AllComments(APIView):
    serializer_class = GetCommentSerializer

    def get(self,request, article):
        try:
            comments = Comments.objects.filter(article = article)
        except Comments.DoesNotExist:
            return Response({"error" : "there are no comments"})

        serializer = GetCommentSerializer(comments, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
