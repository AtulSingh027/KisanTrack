from django.urls import path
from .views import RequestOTP, VerifyOTP, UserLogin, UserSignUp, UserDetail

urlpatterns = [
    path('request-otp/', RequestOTP.as_view(), name='request_otp'),
    path('verify-otp/', VerifyOTP.as_view(), name='verify_otp'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('signup/', UserSignUp.as_view(), name='user_signup'),
    path('user-detail/', UserDetail.as_view(), name='user_detail'),
]
