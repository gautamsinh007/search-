from django.http.response import HttpResponse
from .models import blog
from django.shortcuts import render

# Create your views here.


def home(request):
   
    return render(request,'app/home.html')


def blogg(request):
    u = blog.objects.all()
    return render(request,'app/blog.html',{'u':u})



def search(request):

    q = request.GET['q']
    if len(q)>70:
        u  = blog.objects.none()
    else:   
      oo =  blog.objects.filter(tital__icontains = q) 
      uu =  blog.objects.filter(con__icontains = q) 
      u =   oo.union(uu)

    
    # u =  blog.objects.filter(con__icontains = q) 
    

    return render(request,'app/search.html',{'u':u})

    