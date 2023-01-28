from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from datetime import date

from .serializers import StudentSerializer
from Authentications.models import Account
from .models import Student,CourseJoined
from courseformat.models import Course
from courseformat.serializers import CourseSerializer

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
        todays_date = date.today()
        year = todays_date.year
        newgrade = grade.replace(" ", "")
        uniqueid = str(year) + str(user_id) + str(newgrade)
        newstudent.sstudentuniqueid = uniqueid
        newstudent.save()
        response = {
                "message": "success"
            }

            
        return Response(data=response)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Addcoursetostudent(request):
    if request.method == 'POST':
        print("test")
        user = request.user
        student_id = Student.objects.get(user_id = user)
        print(request.data)
        course = request.data['course_id']
        course_id = Course.objects.get(slug = course)
        newjoin = CourseJoined.objects.create(
            student_id = student_id,
            course_id = course_id
        )
        response = {
                "message": "success"
            }

            
        return Response(data=response)




@api_view(['GET'])
@permission_classes([AllowAny])
def studentlistcourse(request,id):
    # user_id = request.user
    user_id = Account.objects.get(id = id)
    student_id = Student.objects.get(user_id = user_id)
    students = CourseJoined.objects.filter(student_id = student_id).values('course_id')
    course = Course.objects.filter(id__in = students)
    serializer = CourseSerializer(course, many = True)
    return Response(serializer.data)