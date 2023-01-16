from django.shortcuts import render,redirect
from .forms import MyForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def home(request):
    form=MyForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('success')                        
    return render(request,"home.html",{"form":form})


def success(request):
    a='AK'
    return render(request,'success.html',{'context':a})