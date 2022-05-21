from django.contrib.admin.templatetags.admin_list import results
from django.shortcuts import render
from CRUDApp.models import Stud
from django.contrib import messages
from .forms import stform


# Create your views here.
############ Display view #########
def stdisplay(request):
    results = Stud.objects.all()
    return render(request, 'index.html', {"Stud": results})


#################     Insertion  ##################
def stinsert(request):
    if request.method == 'POST':
        savest = Stud()
        savest.sid = request.POST.get('sid')
        savest.sname = request.POST.get('sname')
        savest.sadds = request.POST.get('sadds')
        savest.scity = request.POST.get('scity')
        savest.semail = request.POST.get('semail')
        savest.sphon = request.POST.get('sphon')
        savest.save(force_insert='__al__')
        messages.success(request, "The Data" + " " + savest.sname + " " + "is saved succesfully...")
        return render(request, 'create.html')
    else:
        return render(request, 'create.html')


########## Edit ##############
def stedit(request, sid):
    edit = Stud()
    getstudata = Stud.objects.get(sid=sid)
    # getstudata = Stud.objects.get(sid=sid)
    return render(request, 'edit.html', {"Stud": getstudata})


##############################
def stupdate(request, sid):
    stupdate = Stud.objects.get(sid=sid)
    form = stform(request.POST, instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The Student Record is updated succesfully....")
        return render(request, 'edit.html', {"Stud": stupdate})
    else:
        return render(request, 'edit.html')

############## DELETE############

def stdel(request, sid):
    delstu = stupdat = Stud.objects.get(sid=sid)
    delstu.delete()
    results = Stud.objects.all()
    return render(request, "index.html", {"Stud": results})
