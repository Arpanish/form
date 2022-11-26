from django.shortcuts import render
from .forms import FormModel
from .models import User

def home(request):
    if request.method=='POST':
        fm=FormModel(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['username']
            em=fm.cleaned_data['email']
            pas=fm.cleaned_data['password']
            reg=User(username=nm,email=em,password=pas)
            reg.save()
            fm=FormModel()
    else:
        fm=FormModel()
    return render(request,'blog/home.html',{'form':fm})

# Create your views here.
