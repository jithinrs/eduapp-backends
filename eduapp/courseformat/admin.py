from django.contrib import admin
from .models import Subjects,Course,Chapters,ChapterMaterials

admin.site.register(Subjects)
admin.site.register(Course)
admin.site.register(Chapters)
admin.site.register(ChapterMaterials)

