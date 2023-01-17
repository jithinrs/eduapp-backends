from rest_framework import serializers
from Teachers.models import Teacher
from Authentications.models import Account

class AdminTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['user_id','get_teacher_name', 'get_teacher_email', 'get_teacher_mobile', 'profile_image', 'certificate','home_address', 'subject']
    
