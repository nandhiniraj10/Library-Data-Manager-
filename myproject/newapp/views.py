from django.shortcuts import render
from .models import Data

# Create your views here.
def home(request):
    
    return render(request,'find.html')


def full(request):
    
        Name=request.POST['name']
        Contact=request.POST['contact']
        Address=request.POST['address']
        Books=request.POST['contact']
        Amount=request.POST['amount']
        myvar=Data(name=Name,contact=Contact,books=Books,amount=Amount)
        myvar.save()

        return render(request,'object.html',{"name":Name,
                                            "conatct":Contact,
                                            "address":Address,
                                            "books":Books,
                                            "amount" :Amount,
                                            })