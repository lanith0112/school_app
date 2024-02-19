from django.shortcuts import render

# Create your views here.

def finance1(request):
    return render(request,'finance/checkdue.html')

def finance2(request):
    return render(request,'finance/payfees.html')
