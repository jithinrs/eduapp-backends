from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['user_id','first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'phone_number','grade','school_name', 'school_address', 'home_address', 'guardian', 'guardian_number']
        fields = '__all__'