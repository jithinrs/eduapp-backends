from django.urls import path

from .views import *

urlpatterns = [
    path('student_enroll', student_list.as_view()),
    path('student-create', CreateStudentview.as_view()),
    path('course-join', Addcoursetostudent),

    path('student-courses/<int:id>', studentlistcourse)
    
]
