from django.shortcuts import render
from Logapp.models import user
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def reg(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        user(Username=Username, Password=Password).save(force_insert='__all__')
        messages.success(request, 'The New User' + " " + request.POST['Username'] + " " + 'is Saved')
        # messages.success(request,"The New User is Saved")
        return render(request, 'registration.html')
    else:
        return render(request, 'registration.html')


def log(request):
    if request.method == 'POST':
        try:
            userdtl = user.objects.get(Username=request.POST['Username'], Password=request.POST['Password'])
            print("Username=",userdtl)
            request.session['Username'] = userdtl.Username
            return render(request, 'index.html')
        except user.DoesNotExist as e:
            messages.success(request, 'Username/Password Invalid')

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['Username']
    except:
        return render(request,'index.html')
    return render(request,'index.html')