from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, LoginSerializer, UpdateProfileSerializer, ProfileSerializer , UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile
# Create your views here.


class RegisterApi(APIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data =request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        if user:
            token = Token.objects.create(user=user)
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    serializer_class = LoginSerializer
    def post(self, request, *args , **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.get(user=user)
            response = {}
            response['user'] = serializer.data
            response['token'] = token.key

            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

class My_profile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    def get(self, request):
        try:
            profile =  Profile.objects.get(user = request.user)
        except Profile.DoesNotExist:
            return Response({"error":"The profile doesn't exist"})

        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_200_OK)

class Update_profile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateProfileSerializer
    def put(self, request, pk):
            profile = Profile.objects.get(pk=pk)
            serializer = UpdateProfileSerializer(profile, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class Individual_profile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    def get(self, request,pk):
        try:
            profile =  Profile.objects.get(pk = pk)
        except Profile.DoesNotExist:
            return Response({"error":"The profile doesn't exist"})

        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_200_OK)



class Profile_pictures(APIView):

    serializer_class = ProfileSerializer
    def get(self ,request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
