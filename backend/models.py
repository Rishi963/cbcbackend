from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(blank=True)

class Studentreg(models.Model):
    firstname = models.CharField(max_length=500,blank=True)
    lastname = models.CharField(max_length=500,blank=True)
    email = models.EmailField(max_length=100,blank=True)
    gender = models.CharField(max_length=100,blank=True)
    father_name = models.CharField(max_length=500,blank=True)
    father_occupation = models.CharField(max_length=500,blank=True)
    mother_name = models.CharField(max_length=500,blank=True)
    mother_occupation = models.CharField(max_length=500,blank=True)
    nationality = models.CharField(max_length=100,blank=True)
    category = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    district = models.CharField(max_length=100,blank=True)

    school_name = models.CharField(max_length=500,blank=True)
    address = models.CharField(max_length=1000,blank=True)
    pincode = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    district = models.CharField(max_length=100,blank=True)
    board = models.CharField(max_length=100,blank=True)
    group = models.CharField(max_length=100,blank=True)
    mark_10 = models.CharField(max_length=100,blank=True)
    mark_11 = models.CharField(max_length=100,blank=True)
    mark_12 = models.CharField(max_length=100,blank=True)

    course = models.CharField(max_length=100,blank=True)
    batch = models.CharField(max_length=100,blank=True)
    duration = models.CharField(max_length=100,blank=True)
    total_fee = models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    join_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    branch = models.CharField(max_length=100,blank=True)
    scholorship = models.CharField(max_length=100,blank=True)
    scholorship_percentage = models.CharField(max_length=100,blank=True)
    source = models.CharField(max_length=100,blank=True)
    about_studibreeze = models.CharField(max_length=100,blank=True)
    student_id = models.CharField(max_length=500,blank=True, unique=True )
    school_state = models.CharField(max_length=200,blank=True)
    school_district= models.CharField(max_length=200,blank=True)
    studend_image = models.ImageField(blank=True)
    status = models.CharField(max_length=100,blank=True)



    

class Course(models.Model):
    course_name = models.CharField(max_length=800)
    

class Branch(models.Model):
    branch_name = models.CharField(max_length=800)
   
class Reference(models.Model):
    reference_name = models.CharField(max_length=800)
   

class Billingdata(models.Model):
    student_id = models.CharField(max_length=500,blank=True)
    bill_no = models.CharField(max_length=300,blank=True)
    date = models.DateField(blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    



    





    







    



    



