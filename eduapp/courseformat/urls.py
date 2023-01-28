from django.urls import path
from .views import *

urlpatterns = [
    path('all-subjects', AllSubjectview.as_view()),
    path('create-subjects', CreateSubjectView.as_view()),
    path('create-course', CreateCourseview),
    path('teacher-course/<int:id>', listcourse),
    path('all-course/<int:id>', listallcourse),
    path('each-course/<str:id>', Eachcourse.as_view()),
    path('chapter-view/<str:id>', ChapterView.as_view()),
    path('add-new-chapter/<str:id>', Addchapter),
    path('new-chapter-material-add/', AddChapterMaterial),
    path('show-each-course/<str:id>', MainEachcourse.as_view()),
    path('complete-material', CompleteChapter),
    path('student-notification', courseMaterialNotification)
]