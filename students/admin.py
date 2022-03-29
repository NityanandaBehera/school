from django.contrib import admin
from .models import UserDetNew


@admin.register(UserDetNew)
class UserDetNewAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'usertype',
                    'username', 'email', 'password']

# Register your models here.
