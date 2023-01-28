from rest_framework import generics
from .serializers import SubjectSerializer,CourseSerializer,AllcourseSerializer,ChapterSerializer,ChapterMaterialSerializer,StudentChapterSerialzer,chapterNotificationserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.db.models import Case, When, Value
from rest_framework.permissions import IsAuthenticated

from .models import Subjects,Chapters,ChapterMaterials
from .models import Course
from Authentications.models import Account
from Students.models import Student,CourseJoined


class AllSubjectview(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class CreateSubjectView(generics.CreateAPIView):
    serializer_class = SubjectSerializer
    def post(self, request):
        subj = request.data['title']
        print(subj)
        response = {
                "message": "success"
            }

            
        return Response(data=response)

@api_view(['POST'])
def CreateCourseview(request):
    if request.method == 'POST':
        print(request.data)
        user_id = request.data['user_id']
        subject_id = request.data['subject_id']
        grade = request.data['grade']
        price = request.data['price']
        image = request.data['image']
        course_description = request.data['course_description']
        subject = Subjects.objects.get(title = subject_id)
        user = Account.objects.get(id = user_id)
        newcourse = Course.objects.create(
            user_id = user,
            subject_id = subject,
            grade = grade,
            price = price,
            image = image,
            course_description = course_description
        )
        subject_slug = subject_id.replace(" ", "")

        course_slug = user_id+str(newcourse.id)+"-"+subject_slug
        newcourse.slug = course_slug

        newcourse.save()



        response = {
                "message": "success"
            }

            
        return Response(data=response)
@api_view(['GET'])
def listcourse(request,id):
    course = Course.objects.filter(user_id = id)
    serializer = CourseSerializer(course, many = True)
    return Response(serializer.data)



@api_view(['POST'])
def Addchapter(request,id):
    if request.method == 'POST':
        course = request.data['course_id']
        chapter_name = request.data['chapter_name']
        chapter_description =  request.data['chapter_description']
        course_id = Course.objects.get(slug=course)
        newChapter = Chapters.objects.create(
            course_id = course_id,
            chapter_name = chapter_name,
            chapter_description = chapter_description
        )
        chapter_namenew = chapter_name.replace(" ", '-')
        chapter_slug = str(newChapter.id) +  chapter_namenew
        newChapter.slug = chapter_slug
        newChapter.save()
        # for i in range(5000):
        #     print(i)
        response = {
                "message": "success"
            }

            
        return Response(data=response)

@api_view(['GET','POST'])
def listallcourse(request,id):
    if request.method == 'GET':
        user = Account.objects.get(id = id)
        student = Student.objects.get(user_id = user)
        grade = student.grade
        # course = Course.objects.order_by('grade')
        course = Course.objects.order_by(
            Case(
                When (grade = grade, then=Value(0)),
                default=Value(2)
            )
        )
        serializer  = AllcourseSerializer(course, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        user = Account.objects.get(id = id)
        student = Student.objects.get(user_id = user)
        grade = student.grade
        subject = request.data['subject']
        subject_id = Subjects.objects.get(title = subject)
        # course = Course.objects.order_by('grade')
        course = Course.objects.filter(subject_id = subject_id).order_by(
            Case(
                When (grade = grade, then=Value(0)),
                default=Value(2)
            )
        )
        serializer  = AllcourseSerializer(course, many = True)
        return Response(serializer.data)


class Eachcourse(generics.ListAPIView):
    queryset = Chapters.objects.all
    def get(self,request,id):
        # for i in range(3000):
        #     print(i)
        course = Course.objects.get(slug = id)
        chapters = Chapters.objects.filter(course_id = course)
        serializer = ChapterSerializer(chapters, many = True)
        return Response(serializer.data)

class ChapterView(generics.ListAPIView):
    queryset = ChapterMaterials.objects.all()
    def get(self, request, id):
        course = Chapters.objects.get(slug=id)
        chapter_material = ChapterMaterials.objects.filter(chapter_id = course)
        serializer = ChapterMaterialSerializer(chapter_material, many = True)
        return Response(serializer.data)


@api_view(['POST'])
def AddChapterMaterial(request):
    if request.method == 'POST':
        chapter_slug = request.data['chapter_slug']
        chapter_id = Chapters.objects.get(slug = chapter_slug)
        file_name = request.data['file_name']
        file_description = request.data['file_description']
        files = request.data['files']
        file_extension = files.name.split(".")
        if file_extension[1] == "jpg":
            file_type = "image"
        elif file_extension[1] == "mp4":
            file_type = "video"
        else:
            file_type = "doc"
        
        newMaterial = ChapterMaterials.objects.create(
            chapter_id = chapter_id,
            file_name = file_name,
            files = files,
            file_description = file_description,
            file_type = file_type
        )
        test = newMaterial.files.name.split(".")
        response = {
                "message": "success"
            }

            
        return Response(data=response)


class MainEachcourse(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Chapters.objects.all
    def get(self,request,id):
        print(request.user)
        user = request.user
        course = Course.objects.get(slug = id)
        try:
            test = CourseJoined.objects.get(student_id__user_id = user, course_id = course)
            chapters = Chapters.objects.filter(course_id = course)
            serializer = StudentChapterSerialzer(chapters, many = True)
            print("hi")
            return Response(serializer.data)

        except Exception as e:
            print(e)
        chapters = Chapters.objects.filter(course_id = course)
        serializer = ChapterSerializer(chapters, many = True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CompleteChapter(request):
    if request.method == 'POST':
        chapter_id = request.data['chapter']
        material_id = request.data['material_id']
        user = request.user
        chapter = Chapters.objects.get(slug = chapter_id)
        material = ChapterMaterials.objects.get(chapter_id = chapter, id = material_id)
        material.user_id.add(user)
        print(material)
        response = {
                "message": "success"
            }
        return Response(data = response)


        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def courseMaterialNotification(request):
    if request.method == "GET":
        user = request.user
        coursejoined = CourseJoined.objects.filter(student_id__user_id = user).values('course_id')
        chapters = Chapters.objects.filter(course_id__in = coursejoined).order_by('-created_at')[0:4]
        print(chapters)
        serializer = chapterNotificationserializer(chapters, many = True)

        return Response(data = serializer.data)

