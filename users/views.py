from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.auth import SignUpSerializer

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully'})