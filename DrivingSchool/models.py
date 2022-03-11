from datetime import date
from random import choices
from django.db import models

# Create your models here.

class instructor(models.Model):

    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = models.CharField(max_length=100, null = True)
    contact = models.CharField(max_length=200, null = True)
    address = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)
    username = models.CharField(max_length=200, null= True)
    gender = models.CharField(max_length=100, null = True, choices = GENDER)
    birthday = models.DateField(max_length=100, null = True)
    experience = models.CharField(max_length=100, null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null = True, choices = STATUS, default='Active')

    def __str__(self):
        return self.name

class student(models.Model):

    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = models.CharField(max_length=100, null = True)
    contact = models.CharField(max_length=200, null = True)
    address = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)
    username = models.CharField(max_length=200, null= True)
    gender = models.CharField(max_length=100, null = True, choices = GENDER)
    birthday = models.DateField(null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null = True, choices = STATUS)

    def __str__(self):
        return self.name

class schedule(models.Model):

    COURSE = (
        ('Driving Theory','Driving Theory'),
        ('Road Signs','Road Signs'),
        ('Driving practice','Driving practice'),
    )

    schedule_code = models.CharField(max_length=100, null = True)
    schedule_date = models.DateField(null = True)
    course = models.CharField(max_length=100, null = True, choices = COURSE)
    slots = models.IntegerField(null = True)
    price = models.FloatField(null = True)
    remarks = models.CharField(max_length=300, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True)

    instructor = models.ForeignKey(instructor, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.schedule_code

    def get_name(self):
        return self.instructor.name
class enrollment(models.Model):
    schedule_code = models.ForeignKey(schedule, null=True, on_delete=models.SET_NULL)
    instructor = models.ForeignKey(instructor, null = True, on_delete = models.SET_NULL)
    student = models.ForeignKey(student, null = True, on_delete=models.SET_NULL)
    remarks = models.CharField(max_length=300, null = True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.student.name } {self.schedule_code.schedule_code}"

class payment(models.Model):

    payment_code = models.CharField(max_length=100, null = True)
    payment_date = models.DateField(max_length=100, null = True)
    student = models.ForeignKey(student, null = True, on_delete=models.SET_NULL) 
    price_paid = models.FloatField(null = True)
    remarks = models.CharField(max_length=300, null = True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_code
