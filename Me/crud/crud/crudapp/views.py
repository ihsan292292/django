from django.contrib.admin.templatetags.admin_list import results
from django.shortcuts import render
from crudapp.models import stud
from django.contrib import messages
from .forms import stform


# Create your views here.

def stinsert(request):
    if request.method == "POST":
        savest = stud()
        savest.sid = request.POST.get('sid')
        savest.sname = request.POST.get('sname')
        savest.sadds = request.POST.get('sadds')
        savest.scity = request.POST.get('scity')
        savest.semail = request.POST.get('semail')
        savest.sphon = request.POST.get('sphon')
        savest.save(force_insert='__al__')
        messages.success(request,"The Data"+" "+ savest.sname + " " + "is saved successfully...")
        return render(request, 'create.html')
    else:
        return render(request,'create.html')

############## EDIT ##############

def stedit(request,sid):
    getstudata = stud.objects.get(sid=sid)
    return render(request,'edit.html',{"stud":getstudata})

############ UPDATE ###############

def stupdate(request,sid):
    stupdate = stud.objects.get(sid=sid)
    form = stform(request.POST, instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The student record is updated successfully...")
        return render(request,'edit.html',{"stud":stupdate})
    else:
        return render(request, 'edit.html')

############# DELETE ##############

def stdel(request, sid):
    delstu =stud.objects.get(sid=sid)
    delstu.delete()
    results = stud.objects.all()
    return render(request,"index.html",{"stud": results})

def stdisplay(request):
    result = stud.objects.all()
    return render(request,'index.html',{"stud":result})
