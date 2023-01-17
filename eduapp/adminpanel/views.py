from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView


from .serializers import AdminTeacherSerializer
from Teachers.models import Teacher

#From students app.
from Students.serializers import StudentSerializer
from Students.models import Student

from Authentications.models import Account

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse


@api_view(['GET'])
def teacher_list_view(request):
    teacher = Teacher.objects.all()
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
            user.verified_role = True
            user.save()
        
        if data == 'decline':
            user = Teacher.objects.get(user_id = user_id)
            user.delete()

        response = {
                "message": "success"
            }

            
        return Response(data=response)
    


def tryemail(request):
    subject = "jithinrs"
    message = "poda patti"
    email_from = settings.EMAIL_HOST_USER
    recipent = ['jithinrs2.0@gmail.com',]
    send_mail(subject, message, email_from, recipent)
    return HttpResponse('<h1> poda </h1>')