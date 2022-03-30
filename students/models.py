from email.policy import default
from xml.parsers.expat import model
from django.db import models

# Create your models here.


class UserDetNew(models.Model):
    c = (
        ('Stu', 'Student'),
        ('Teacher', 'Teacher')
    )
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    profile_pic = models.ImageField(upload_to="images")
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    usertype = models.CharField(max_length=20, choices=c)

    def __str__(self):
        return self.usertype
# Create your models here.


class Stud(models.Model):
    user = models.ForeignKey(UserDetNew, on_delete=models.CASCADE)
    stu_name = models.CharField(max_length=100)
    stu_email = models.CharField(max_length=100)
    stu_profilepic = models.ImageField(upload_to="images")
    stu_address = models.CharField(max_length=200)


class Teachers(models.Model):
    user = models.ForeignKey(UserDetNew, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="images")
    address = models.CharField(max_length=120)
    qualification = models.CharField(max_length=23)

    def __str__(self):
        return self.name
