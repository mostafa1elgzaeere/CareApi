from django.contrib import admin
from .models import Blogs, Categorie , Doctor  ,Appointment

# Register your models here.
def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]


class BlogAdmin(admin.ModelAdmin):
    list_display=["title"]

admin.site.register(Blogs, BlogAdmin)

class CategorieAdmin(admin.ModelAdmin):
    search_fields=["title",]
    list_filter = ('title',)


admin.site.register(Categorie, CategorieAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display=["name","phone","category"]
    search_fields=["name",]
    list_filter = ('category',)

    

admin.site.register(Doctor, DoctorAdmin)




class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name","phone","category","doctor",)
    search_fields=["name","date","phone"]
    list_filter = ('category',"date","doctor",)
   
    # def get_doctor(self, obj):
    #     return obj.doctors.name

admin.site.register(Appointment, AppointmentAdmin)
