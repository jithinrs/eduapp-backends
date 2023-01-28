from django.urls import path
from .views import Create_account,MyTokenObtainPairSerializer,MyTokenObtainPairView,LoginView,OtpLoginview,Otpverification,list_account, TokenRefresher, BlockUser


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', Create_account.as_view()),
    path('login', LoginView.as_view()),
    path('otplogin', OtpLoginview.as_view()),
    path('otpverify', Otpverification.as_view()),
    path('tokenrefresher', TokenRefresher),

    path('listall', list_account.as_view()),

    path('block-user/<int:id>',BlockUser ),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

