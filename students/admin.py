from django.contrib import admin
from .models import UserDetNew
from .models import Stud
from .models import Teachers


@admin.register(UserDetNew)
class UserDetNewAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'usertype',
                    'username', 'email', 'password']


@admin.register(Stud)
class StudAdmin(admin.ModelAdmin):
    list_display = ['stu_name', 'stu_email', 'stu_profilepic', 'stu_address']


@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_dispaly = ['name', 'email', 'profilepic', 'address', 'qualification']
# Register your models here.
