from django.http import JsonResponse
from rest_framework.generics import *

from rest_framework.views import *
from care.models import Appointment, Categorie, Doctor,Blogs
from care.serializer import AppointmentSerializer, CategorieSerializer, DoctorSerializer,BlogSerializer



class AppointmentApi(ListCreateAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer
   
 
    def post(self, request, *args, **kwargs):
        data=AppointmentSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse ({"data":data.data})


    
class DoctorApi(ListAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer    
    
    
    
class BlogApi(ListAPIView):
    queryset=Blogs.objects.all()
    serializer_class=BlogSerializer    
    
    
        
    
    

class CategorieApi(ListAPIView):
    queryset=Categorie.objects.all()
    serializer_class=CategorieSerializer        
    
    
    
class CategoryDoctorsApi(APIView):
    def get(self,request,cat):
        categ=Categorie.objects.get(id=cat)
        doctors=Doctor.objects.filter(category=categ)
        serializer=DoctorSerializer(doctors,many=True)
        return Response({"data":serializer.data})   
