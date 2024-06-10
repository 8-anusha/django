from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(req):
    #pull data from db
    # transform
    #send emails
    #return HttpResponse('hello world')
#map view to url -req at that url this function called
    return render(req, 'hello.html',{'name':'Anusha'})


