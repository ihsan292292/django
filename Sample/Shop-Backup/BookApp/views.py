from django.shortcuts import render
from django.http import HttpResponse
from BookApp.models import Book
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
           b = Book()
           b.Accno = request.POST.get('Accno')
           b.Title = request.POST.get('Title')
           b.Author = request.POST.get('Author')
           b.save(force_insert='__all__')
           messages.success(request," Data Saved")
           return render(request, 'index.html')

    else:
        return render(request, 'index.html')

def search(request):
 if request.method == 'GET':
     s = Book()
     s = Book.objects.filter(Title=request.GET.get('tit'))
     return render(request,'search.html',{'ss':s})


