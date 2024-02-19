from django.shortcuts import render


# Create your views here.
# function based / class based views

def admissions1(request):
    values = {'name':'lanith','age':23,'address':'vizag'}
    return render(request,'admissions/newadmissions.html',values)

def admissions2(request):
    return render(request,'admissions/oldadmission.html')




