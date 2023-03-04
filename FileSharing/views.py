from django.shortcuts import render,HttpResponse,redirect
from .forms import UploadFileForm
from .models import FileModel

name="raja"
password="raja,kavin,75397"

def Login(request):
    if request.method=="POST":
        n=request.POST.get('name')
        p=request.POST.get('password')
        if n==name and p==password:
            return redirect('home')
        else:
            return HttpResponse("User name password incorrect")
    else:
        return render(request,'login.html')

def Home(request):
    if request.method=="POST":
        f=request.FILES['file']
        object=FileModel.objects.create(file=f)
        object.save()
        return redirect('uplodedfiles')
    form=UploadFileForm()
    return render(request,'index.html',{'form':form})

def View(request):
    object=FileModel.objects.all()
    return render(request,'fileview.html',{'files':object})
def Del(request,i):
    object=FileModel.objects.get(id=i)
    object.delete()
    return redirect('uplodedfiles')









    