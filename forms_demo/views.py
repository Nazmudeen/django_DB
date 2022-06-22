from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.http import HttpResponse
# Create your views here.

def index1(request):
    Cust=CustomerForm()
    return render(request,"index1.html",{"form":Cust})

def addcustomer(request):
   # try:
        if request.method=="POST":
            Cust=CustomerForm(request.POST)
            if Cust.is_valid():
                Cust.save()
        return render(request,"index1.html",{'form':Cust,'msg':'saved'})
    #except Exception as e:
  #      print(e)
   #     return HttpResponse("error")             