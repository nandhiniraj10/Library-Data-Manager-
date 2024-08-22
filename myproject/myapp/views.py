from django.shortcuts import render
from . models import Data
from . forms import Mydata




# Create your views here.
def home(request):
    a=Mydata()
    return render(request,"indec.html",{'form':a})
    
    #return render(request,'index.html')

def product(request):
    
        Mobile=request.POST['mobile']
        Keyboard=request.POST['keyboard']
        Monitor=request.POST['monitor']
        myvar=Data(mobile=Mobile,keyboard=Keyboard,monitor=Monitor)
        myvar.save()

        return render(request,'result.html',{"mobile":Mobile,
                                            "keyboard":Keyboard,
                                            "monitor" :Monitor,
                                            })






