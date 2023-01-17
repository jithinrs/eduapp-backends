# from Teachers.models import Teacher
from django.db import models
from Authentications.models import Account
import uuid

class Subjects(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.title
    
class Course(models.Model):
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    # teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255,null=True, blank=True)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    grade_choice = [
        ('8th grade','8th grade'),
        ('9th grade','9th grade'),
        ('10th grade','10th grade'),
        ('11th grade','11th grade'),
        ('12th grade','12th grade')
    ]
    grade = models.CharField(max_length=15, choices=grade_choice)
    image = models.ImageField()
    course_description = models.TextField()

    class Meta():
        verbose_name_plural = "Course"

    def __str__(self):
        return self.subject_id.title + " " + self.grade

class Chapters(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255,null=True, blank=True)
    chapter_name = models.CharField(max_length=255)
    chapter_description = models.TextField()

    class Meta():
        verbose_name_plural = "Chapters"

    def __str__(self):
        return self.chapter_name

class ChapterMaterials(models.Model):
    chapter_id = models.ForeignKey(Chapters, related_name='chapter_materials', on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_description = models.TextField(null=True)
    files =  models.FileField()
    file_type = models.CharField(max_length=7, null=True)

    class Meta():
        verbose_name_plural = "Chapter material"

    def __str__(self):
        return self.chapter_id.chapter_name + "'s files"
