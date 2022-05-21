import os
from re import A
from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from stapp.models import std
from django.contrib import messages

# Create your views here.


############              ############
def index(request):
    if request.method == 'POST':
        idd = request.POST.get('id')
        namee = request.POST.get('name')
        m11 = float(request.POST.get('m1'))
        m22 = float(request.POST.get('m2'))
        m33 = float(request.POST.get('m3'))
        tot = m11 + m22 + m33
        avg = tot / 3
        grd_avg =  tot / 3
        if grd_avg> 95:
            grd_avg="O"
        elif grd_avg > 90:
            grd_avg = "A"
        elif grd_avg > 80:
            grd_avg = "B"
        elif grd_avg > 70:
            grd_avg = "C"
        elif grd_avg > 60:
            grd_avg= "D"
        elif grd_avg > 50:
            grd_avg = "E"
        else:
            grd_avg = "F"
        print(grd_avg)

        std(id=idd, name=namee, m1=m11, m2=m22, m3=m33, total_mark=tot, avg_mark=avg,grade=grd_avg).save(force_insert='__all__')
        messages.success(request,"Data Saved")
        return render(request,'index.html')
    else:
        return render(request,'index.html')

############# Print all #############

def output(request):
    std_details = std.objects.all()
    return render(request,'output.html',{'std_details':std_details})

############ Search single student #########

def view(request):
    if request.method =='GET':
        mark = std.objects.filter(id=request.GET.get('id'))
    '''o1="O"
    Ap="A+"
    a1="A"
    b1="B"
    c1="C"
    d1="D"
    e1="E"
    f1="F"
    std(os=o1,ap=Ap,ag=a1,bg=b1,cg=c1,dg=d1,eg=e1,fail=f1).save(force_insert='__all__')'''
    
    return render(request,'search.html',{'mark':mark})

########## View student grade ###########
