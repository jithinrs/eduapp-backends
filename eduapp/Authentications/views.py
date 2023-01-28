from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from rest_framework.permissions import  AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView 

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Account
from .serializers import AuthenticationSerializer
from .tokens import create_jwt_pair_tokens
from django.contrib.auth.models import User
from .verify import verify_otp, send_otp


class Create_account(CreateAPIView):
    serializer_class = AuthenticationSerializer
    def post(self, request):
        serializer = AuthenticationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class list_account(ListAPIView):
    # permission_classes =  [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AuthenticationSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token['first_name'] = user.first_name
        # token['email'] = user.email
        # ...
        name = user.first_name + " " + user.last_name
        token['Fullname'] = name
        token['Roles'] = user.roles
        token['email'] = user.email
        token['verified'] = user.verified_role
        token['datafilled'] = user.data_uploaded

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class LoginView(APIView):
    permission_classes =  [AllowAny]

    def post(self , request:Request):
        email = request.data.get('email')
        password = request.data.get('password') 
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_verified == True:
                tokens = create_jwt_pair_tokens(user)    
                response = {
                    "message": "Login successfull",
                    "token": tokens,
                    "user" : {
                        "user_id":user.id,
                        "email":user.email,
                        "firstname":user.first_name,
                        "isAdmin" : user.is_admin,
                        
                    }
                } 
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                response = {
                    "message": "User is not Verified",
                } 
                return Response(data=response)

        else:
            return Response(data={"message": "Invalid email or password!"})


@api_view(['POST'])
def TokenRefresher(request):
    if request.method == 'POST':

        user_id = request.data['user_id']
        user = Account.objects.get(id = user_id)
        tokens = create_jwt_pair_tokens(user)
        response = {
                "message": "success",
                "token" : tokens,
                "user" : {
                        "user_id":user.id,
                        "email":user.email,
                        "firstname":user.first_name,
                        "isAdmin" : user.is_admin,
                }
            }

            
        return Response(data=response)


class OtpLoginview(APIView):
    permission_classes =  [AllowAny]

    def post(self , request:Request):
        mobile = request.data.get('mobile')
        print("poda")
        print(mobile)
        try:
            user = Account.objects.get(mobile = mobile)
            send_otp(mobile)
            return Response(data={"message": " email or password!"})
        except:
            return Response(data={"message": "mobile is not registered"})

class Otpverification(APIView):
    permission_classes = [AllowAny]

    def post(self , request:Request):
        otp = request.data.get('otp')
        mobile = request.data.get('mobile')
        check = verify_otp(mobile,otp)
        print(check)
        if check:
            user = Account.objects.get(mobile=mobile)
            tokens = create_jwt_pair_tokens(user) 
            login(request,user)   
            response = {
                "message": "Login successfull",
                "token": tokens,
                "user" : {
                    "user_id":user.id,
                    "email":user.email,
                    "firstname":user.first_name
                    
                }
            } 
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "invalid otp"})
@api_view(['POST'])
def BlockUser(request):
    if request.method == 'POST':



        response = {
                "message": "success"
            }

            
        return Response(data=response)