from django.shortcuts import render

# Create your views here.
def jam(request):
    return render(request,'jam.html')
