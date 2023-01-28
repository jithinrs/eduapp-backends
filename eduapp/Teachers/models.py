from django.db import models
from Authentications.models import Account
from courseformat.models import Subjects



class Teacher(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    profile_image = models.ImageField()
    home_address = models.CharField(max_length=511)
    certificate = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ManyToManyField(Subjects, blank=True)
    is_active = models.BooleanField(default=True)
    

    class Meta():
        verbose_name_plural = "Teacher"
    
    def __str__(self):
        return self.user_id.first_name + " " + self.user_id.last_name
    
    def get_teacher_name(self):
        return self.user_id.first_name + " " + self.user_id.last_name

    def get_teacher_email(self):
        return self.user_id.email
    
    def get_teacher_mobile(self):
        return self.user_id.mobile



class testhello(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=63)