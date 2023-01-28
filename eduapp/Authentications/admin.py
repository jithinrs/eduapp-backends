from django.contrib import admin
from .models import Account, teste


# Register your models here.
class Accounttable(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile', 'roles')

admin.site.register(Account, Accounttable)    
admin.site.register(teste)
