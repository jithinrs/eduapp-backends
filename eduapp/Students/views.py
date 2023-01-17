from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import StudentSerializer
from Authentications.models import Account
from .models import Student

# Create your views here.


class student_list(CreateAPIView):
    serializer_class = StudentSerializer
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
    
        if serializer.is_valid():
            user_id = request.data.get('user_id')
            user = Account.objects.get(id = user_id)
            user.is_student = True
            user.save()
            response = {
                "user_role": user.is_student,
                "message": "success"
            }

            serializer.save()
            return Response(data=response)
            # return Response(serializer.data, status = status.HTTP_201_CREATED )
        return Response(serializer.errors)
        # return Response(data={"message": "Something went wrong!"})


class CreateStudentview(CreateAPIView):
    serializer_class = StudentSerializer
    def post(self,request):
        user_id = request.data['user_id']
        profile_image = request.data['profile_image']
        grade = request.data['grade']
        print(grade)
        school_name = request.data['school_name']
        school_address = request.data['school_address']
        home_address = request.data['home_address']
        guardian = request.data['guardian']
        guardian_number = request.data['guardian_number']
        user = Account.objects.get(id = user_id)
        newstudent = Student.objects.create(
            user_id = user,
            profile_image = profile_image,
            grade = grade,
            school_name = school_name,
            school_address = school_address,
            home_address = home_address,
            guardian = guardian,
            guardian_number = guardian_number
        )
        user.data_uploaded = True
        user.save()
        response = {
                "message": "success"
            }

            
        return Response(data=response)