from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import TeacherSerializer,GetTeacherSerializer
from .models import Teacher
from Authentications.models import Account


@api_view(['GET'])
def teacher_list_view(request):
    teacher = Teacher.objects.all()
    serializer = TeacherSerializer(teacher, many = True)
    return Response(serializer.data)

# @api_view(['GET'])
# def teacher_credentials(request, id):
#     teacher = TeacherCredentials.objects.get(teacher_id = id)
#     serializer = TeacherCredentialsSerializer(teacher)
#     return Response(serializer.data)


class teacherapply(CreateAPIView):
    serializer_class = TeacherSerializer
    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            user_id = request.data.get('user_id')
            user = Account.objects.get(id = user_id)
            user.data_uploaded = True
            user.save()
            response = {
                "message": "success"
            }

            serializer.save()
            return Response(data=response)
        print(serializer.errors)
        return Response(serializer.errors)

class CreateTeacherView(CreateAPIView):
    serializer_class = TeacherSerializer
    def post(self, request):

        user_id = request.data['user_id']
        profile_image = request.data['profile_image']
        certificate = request.data['certificate']
        subject = request.data['subject']
        home_address = request.data['home_address']
        test = [1,2]
        print(user_id, profile_image)
        user = Account.objects.get(id = user_id)
        newTeacher = Teacher.objects.create(
            user_id = user,
            profile_image = profile_image,
            certificate = certificate,
            home_address = home_address

        )
        x = subject.split(',')
        for i in x:
            newTeacher.subject.add(i)
        print(x)
        user.data_uploaded = True
        user.save()
        response = {
                "message": "success"
            }

            
        return Response(data=response)


# class teachercredentials(CreateAPIView):
#     serializer_class = TeacherCredentialsSerializer
#     def post(self, request):
#         serializer = TeacherCredentialsSerializer(data = request.data)
    
#         if serializer.is_valid():
#             # user_id = request.data.get('user_id')
#             # user = Account.objects.get(id = user_id)
#             # user.is_teacher = True
#             # user.save()
#             response = {
#                 # "user_role": user.is_teacher,
#                 "message": "success"
#             }

#             serializer.save()
#             return Response(data=response)
#             # return Response(serializer.data, status = status.HTTP_201_CREATED )
#         return Response(serializer.errors)
#         # return Response(data={"message": "Something went wrong!"})


class GetTeacherview(ListAPIView):
    permission_classes = [IsAuthenticated]
    # serializer_class = GetTeacherSerializer
    # queryset = Teacher.objects.get()
    def get(self, request):
        user = request.user
        teacher = Teacher.objects.get(user_id = user)
        serializer = GetTeacherSerializer(teacher)
        return Response(serializer.data)