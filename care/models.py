
from django.db.models import *

# Create your models here.


class Categorie(Model):
    title=CharField(max_length=100,default="")

    def __str__(self):
        return self.title
    
    class Meta:    
        verbose_name_plural="Categories"


class Doctor(Model):
    name=CharField(max_length=100,default="")
    phone=IntegerField()
    category=ForeignKey(Categorie,related_name="Doctors",on_delete=CASCADE)
    email=CharField(max_length=200)
    image = ImageField(upload_to="uploads/", height_field=None, width_field=None, max_length=200)
    
    
    def __str__(self):
        return self.name
    


class Appointment(Model):
    name=CharField(max_length=100)
    phone=IntegerField()
    national_id=IntegerField()
    date=DateField()
    category=ForeignKey(Categorie,related_name="Appointments",on_delete=CASCADE,null=False,blank=False)
    doctor=ForeignKey(Doctor,on_delete=CASCADE,related_name="Appointment",null=False,blank=False)
    message=TextField(max_length=200)
    
    
    def __str__(self):
        return self.name
    
    

class Blogs(Model):
    image = ImageField(upload_to="uploads/", height_field=None, width_field=None, max_length=200)
    title=CharField(max_length=30)
    desciption=TextField(max_length=1000)

    def __str__(self):
        return self.title
        
    class Meta:    
        verbose_name_plural="Blogs"

    
    