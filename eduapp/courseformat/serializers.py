from rest_framework import serializers
from .models import Subjects, Course, Chapters,ChapterMaterials


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AllcourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # fields = ['subject_id', 'title', 'grade', 'image', 'course_description']
        fields = '__all__'


class ChapterMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterMaterials
        fields = '__all__'



class ChapterSerializer(serializers.ModelSerializer):
    chapter_materials = ChapterMaterialSerializer(many = True)
    class Meta:
        model = Chapters
        fields = '__all__'

class StudentChapterSerialzer(serializers.ModelSerializer):
    chapter_materials = ChapterMaterialSerializer(many = True)
    class Meta:
        model = Chapters
        fields = ['id', 'course_id', 'slug', 'chapter_name', 'chapter_description', 'chapter_materials', 'course_joined']


class chapterNotificationserializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = ['chapter_name', 'teacher_name', 'course_name','course_slug', 'slug']