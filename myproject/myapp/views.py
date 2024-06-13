# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .serializers import RegisterSerializer, LoginSerializer
from django.http import JsonResponse

class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('home')
        return render(request, 'register.html', {'errors': serializer.errors})

class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        return render(request, 'login.html', {'errors': serializer.errors})

def home_view(request):
    data = {
        "message": "Welcome to the Home Page"
    }
    return render(request, 'home.html', data)
