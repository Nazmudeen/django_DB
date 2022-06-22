from django.shortcuts import render
from .models import employee



def index(request):
    return render(request,"index.html")

def addemployee(request):
    response={}
    try:
       Name=request.POST["username"]
       Address=request.POST["useraddress"]
       emplist=employee(name=Name,address=Address)
        #or emplist=employee.object.create(name=Name,address=Address)
       emplist.save()
       response["msg"]="Employee added"
       return render(request,"index.html",response)
    except Exception as e:
        print(e)
        response["msg"]="Employee cannote be added"
        return render(request,"index.html",response)    

def display(request):
    empdtls=employee.objects.all()
    return render(request,"index.html",{'emp':empdtls })

# Create your views here.

#all(),get(id=1),filter(name=Name)
#variable=employee.objects.get(id=1)
#Name=request.POST['name']
#variable=employee.objects.filter(name=Name)
    
def delete(request):
    Name=request.POST["username"]
    empdtls=employee.objects.filter(name=Name)
    empdtls.delete()
    return render(request,"index.html",{'msg':'deleted'})

def updates(request):
    Oldname=request.POST["oldname"]
    Newname=request.POST["newname"]
    emp=employee.objects.get(name=Oldname)
    emp.name=Newname
    emp.save()
    return render(request,"index.html",{'msg1':'updated'})    
"""
    try:
         Oldname=request.POST["oldname"]
         Newname=request.POST["newname"]
         emp=employee.objects.filter(name=Oldname)
         if emp.exists():
             emp.update(name=Newname)
             return render(request,"index.html",{"msg2":"updated"})
         else:
            return render(request,"index.html",{"msg2":"record not found"})
    except Exception as e:
        print(e)
        return render(request,"index.html",{"msg2":"not updated"})        
        """