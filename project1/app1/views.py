from django.shortcuts import render
from .forms import MyForm
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
