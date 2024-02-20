from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()
    
    def __str__(self):
       return self.email

    
    
class Enrollment(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField(max_length=25)
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=25) 
    SelectMembershipplan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    paymentStatus=models.CharField(max_length=55, blank=True, null=True)
    price=models.IntegerField(max_length=55, blank=True, null=True)
    DueDate=models.DateField(blank=True, null=True)
    timeStamp=models.DateTimeField(default=timezone.now, blank=True)



    def __str__(self):
       return self.FullName

class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField(max_length=25)
    timeStamp=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
       return self.name
    
class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)
    
    def __str__(self):
       return self.plan
   
class Gellery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
       return self.title
   
class Attendance(models.Model):
    Selectdate=models.DateTimeField(default=timezone.now)
    phonenumber=models.CharField(max_length=15)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    
    def __int__(self):
        return self.id
    
#otp verifivation    
    
class Otp(models.Model):
    otp = models.IntegerField(max_length=4)
    
class LoginOtp(models.Model):
    otp = models.IntegerField()
    