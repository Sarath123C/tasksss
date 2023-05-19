from django import forms
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.name
GENDER_CHOICES=(('M','Male'),('F','Female'))

class Person(models.Model):
    name = models.CharField(max_length=124)
    DOB = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=128,null=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(max_length=200,null=True)
    address = models.TextField(max_length=300,null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name