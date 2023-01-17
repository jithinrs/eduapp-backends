from django.urls import include, path
from .views import *


urlpatterns = [
    path('', teacher_list_view),
    path('teacher-apply', teacherapply.as_view()),
    path('teacher-create', CreateTeacherView.as_view()),
    path('get-each-teacher', GetTeacherview.as_view())
]
