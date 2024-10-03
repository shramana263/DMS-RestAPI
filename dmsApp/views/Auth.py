from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.exceptions import AuthenticationFailed
from ..serializers.UserSerializer import UserSerializer
from django.contrib.auth import authenticate
from ..models.User import User
import jwt, datetime
from rest_framework import status

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer= UserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if user is None: 
            raise AuthenticationFailed('Invalid credentials')

        # Include user details in the response
        serializer = UserSerializer(user)  # Use your UserSerializer for detail control
        user_data = serializer.data

        payload = {
            'id': user.id,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now(datetime.timezone.utc)
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({
            "message": "success",
            "jwt": token,
            "user": user_data
        })
