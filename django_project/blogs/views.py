from django.shortcuts import render
from django.http import HttpResponse







def index(request):
    return render(request,'blogs/index.html')

def page1(request):
    return render(request,'blogs/page1.html')

def page2(request):
    return render(request,'blogs/page2.html')


 
