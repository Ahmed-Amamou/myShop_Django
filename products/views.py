from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    name = "zbanda9louch"
    age = "14"
    L = [1,2,3,4,5]
    return render(request,"products/home.html",{"name":name,
                                                "age":age})
    # return HttpResponse("Hello World")
    



    