from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
import random

from .models import OTPModel
from .serializers import UserSerializer

class RequestOTP(APIView):
    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)

        otp = str(random.randint(100000, 999999))
        OTPModel.objects.create(email=email, otp=otp)

        send_mail(
            'Your OTP Code',
            f'Your OTP is: {otp}',
            'atulthakur5103@gmail.com',
            [email],
            fail_silently=False
        )

        return Response({'message': 'OTP sent to your email.'}, status=200)

class VerifyOTP(APIView):
    def post(self, request):
        otp = request.data.get('otp')
        email = request.data.get('email')

        if not otp or not email:
            return Response({'error': 'OTP and email are required.'}, status=400)

        try:
            otp_record = OTPModel.objects.get(email=email, otp=otp)

            if otp_record.created_at < now() - timedelta(minutes=5):
                otp_record.delete()
                return Response({'error': 'OTP has expired.'}, status=400)

            # Optional: Delete OTP after successful validation
            otp_record.delete()

            try:
                user = User.objects.get(email=email)
                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": {
                        "username": user.username,
                        "email": user.email
                    }
                }, status=200)
            except User.DoesNotExist:
                return Response({'error': 'No user associated with this email.'}, status=404)

        except OTPModel.DoesNotExist:
            return Response({'error': 'Invalid OTP or email.'}, status=400)

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserSignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
