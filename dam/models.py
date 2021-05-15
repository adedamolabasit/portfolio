from django.db import models

# Create your models here.
class Profile(models.Model):
   first_name=models.CharField(max_length=32,blank=True,null=True)
   middle_name=models.CharField(max_length=32,blank=True,null=True)
   last_name=models.CharField(max_length=32,blank=True,null=True)
   age=models.IntegerField()
   phone_number=models.IntegerField()
   email=models.EmailField()
   status=models.TextField()
   image=models.ImageField(upload_to='profile image')
   date=models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f'{self.first_name}+{self.last_name}'
class Experience(models.Model):
    specialization1=models.TextField(blank=True,null=True)
    workplace1=models.TextField(blank=True,null=True)
    rank1=models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)

class Education(models.Model):
    university=models.TextField(null=True,blank=True)
    programme=models.CharField(max_length=20,null=True,blank=True)
    department=models.TextField(blank=True,null=True)
    remarks1=models.TextField(blank=True,null=True)
    high_school=models.TextField(blank=True,null=True)
    department2=models.CharField(max_length=20,blank=True,null=True)
    middle_shool=models.TextField(blank=True,null=True)
    remarks2=models.TextField(blank=True,null=True)
    primary_shool=models.TextField(blank=True,null=True)
    remarks3=models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)

class Skills(models.Model):
    heading=models.CharField(max_length=30)
    skills=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

class Interest(models.Model):
    interest=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

class Awards(models.Model):
    awards=models.TextField()
    date=models.DateTimeField(auto_now_add=True)



