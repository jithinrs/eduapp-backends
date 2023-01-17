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