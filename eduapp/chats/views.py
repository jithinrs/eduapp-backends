from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializer import ChatUserSerializers
from courseformat.models import Course
from Students.models import CourseJoined
from Authentications.models import Account



class ChatUsersAll(generics.ListAPIView):
    serializer_class = ChatUserSerializers
    queryset = Account.objects.all()
    def get(self,request):
        user = request.user
        if user.roles == "T":
            print(user.id)
            courses = Course.objects.filter(user_id = user.id).values('id')
            coursejoined = CourseJoined.objects.filter(course_id__in = courses).values('student_id__user_id').distinct()
            frienusers = Account.objects.filter(id__in = coursejoined)
            serializer = ChatUserSerializers(frienusers, many = True)
            return Response(serializer.data)
        if user.roles == "S":
            print(user.id)
            coursejoined = CourseJoined.objects.filter(student_id__user_id = user.id).values('course_id')
            courses = Course.objects.filter(id__in = coursejoined).values('user_id').distinct()
            frienusers = Account.objects.filter(id__in = courses)
            serializer = ChatUserSerializers(frienusers, many = True)
            print(courses)
            print(coursejoined)

            return Response(serializer.data)


