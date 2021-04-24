from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me', 'Please email me at pulkit12dhingra@gmail.com ', 'My phone number is :-790559650', 'Address:- A-27 Brahmapuri Indira Nagar Lucknow']})
    