from django.contrib import admin
from .models import User

@admin.register(User)
class FormModel(admin.ModelAdmin):
    list_display=['id','username','email','password']

# Register your models here.
