from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import AdminTeacherSerializer
from Teachers.models import Teacher

#From students app.
from Students.serializers import StudentSerializer
from Students.models import Student

from Authentications.models import Account

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

from courseformat.models import Subjects
from courseformat.serializers import SubjectSerializer



@api_view(['GET'])
def teacher_list_view(request):
    teacher = Teacher.objects.filter(user_id__verified_role = True)
    serializer = AdminTeacherSerializer(teacher, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def pending_teacher_request(request):
    teacher = Teacher.objects.filter(user_id__verified_role = False, user_id__data_uploaded = True)
    serializer = AdminTeacherSerializer(teacher, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def individual_teacher(request,id):
    teacher = Teacher.objects.get(user_id = id)
    serializer = AdminTeacherSerializer(teacher)
    return Response(serializer.data)





@api_view(['GET','POST'])
def student_list_view(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)


@api_view(['POST'])
def TeacherValidation(request):
    if request.method == 'POST':
        data = request.data['verify']
        user_id = request.data['user_id']

        if data == "accept":
            user = Account.objects.get(id = user_id)
            email = user.email
            user.verified_role = True
            user.save()
        
        if data == 'decline':
            user = Teacher.objects.get(user_id = user_id)
            userdetails = Account.objects.get(id = user_id)
            email = userdetails.email
            user.delete()

        response = {
                "message": "success"
            }
        subject = "Validation"
        message = "Your credentials are validated and you can now join our website as a teacher."
        email_from = settings.EMAIL_HOST_USER
        recipent = [email, ]
        send_mail(subject, message, email_from, recipent)
            
        return Response(data=response)
    

class ListSubjects(ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser]

@api_view(['POST'])
def blockunblockuser(request, id):
    account = Account.objects.get(id = id)
    validity = account.is_verified
    account.is_verified = not validity
    print("hello")
    account.save()

    response = {
                "message": "success"
            }
    return Response(data = response)



def tryemail(request):
    subject = "Calidation"
    message = "Your credentials are validated and you can now join our website as a teacher."
    email_from = settings.EMAIL_HOST_USER
    recipent = ['jithinrs2.0@gmail.com',]
    send_mail(subject, message, email_from, recipent)
    return HttpResponse('<h1> Testing </h1>')