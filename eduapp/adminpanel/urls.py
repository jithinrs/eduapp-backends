from django.urls import include, path
from .views import *

urlpatterns = [
    path('teachers-list', teacher_list_view, name='teachers_list'),
    path('teachers-pending/<int:id>', individual_teacher, name='teachers-pending'),
    path('students_list', student_list_view),
    path('teachervalidation', TeacherValidation),
    path('emailayakk', tryemail),
]
