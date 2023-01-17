from django.db import models
from Authentications.models import Account
from courseformat.models import Course


class Student(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    profile_image = models.ImageField()
    
    grade_choice = [
        ('8th grade','8th grade'),
        ('9th grade','9th grade'),
        ('10th grade','10th grade'),
        ('11th grade','11th grade'),
        ('12th grade','12th grade')
    ]
    grade = models.CharField(max_length=15, choices=grade_choice)
    school_name = models.CharField(max_length=255)
    school_address = models.CharField(max_length=511)
    home_address = models.CharField(max_length=511)
    guardian = models.CharField(max_length=127)
    guardian_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    
    class Meta():
        verbose_name_plural = "Student"

    def __str__(self):
        return self.user_id.first_name + " " + self.user_id.last_name
    
    

    


# class CourseJoined(models.Model):
#     user_id = models.ForeignKey(Account,on_delete=models.CASCADE)
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
