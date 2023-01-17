from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class PendingRequestsSerializer(serializers.ModelSerializer):
    teacher_credentials = serializers.StringRelatedField(many=True)

    class Meta:
        model = Teacher
        fields = ['first_name','last_name','teacher_credentials']

class GetTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['profile_image', 'get_teacher_name', 'get_teacher_email', 'get_teacher_mobile', 'home_address','subject']