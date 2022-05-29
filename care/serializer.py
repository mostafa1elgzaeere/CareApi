
from .models import Appointment, Blogs, Categorie, Doctor
from rest_framework.serializers import *


 
class BlogSerializer(ModelSerializer):
    
    class Meta:
        model=Blogs
        fields="__all__"
           
    

class DoctorSerializer(ModelSerializer):
    category = StringRelatedField(many=False)
    

    class Meta:
        model=Doctor
        fields=["id","name","phone","category","image","email"]
        
 

class CategorieSerializer(ModelSerializer):

    class Meta:
        model=Categorie
        fields=["id","title"]
        
                
class AppointmentSerializer(ModelSerializer):
    # doctor=DoctorSerializer(read_only=False)
    # category=CategorieSerializer(read_only=False)
             

    # def create(self, validated_data):
    #     appoint = Appointment(
    #         name=validated_data['name'],
    #         phone=validated_data['phone'],
    #         national_id=validated_data['national_id'],
    #         date=validated_data['date'],
    #         category=self.category,
    #         doctor=self.doctor,
    #         message=validated_data['message'],
    #     )
    #     appoint.save()
    #     return appoint
        
    class Meta:
        model=Appointment
        fields=["name","phone","national_id","date","category","doctor","message"]
                    