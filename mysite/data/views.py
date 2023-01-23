from django.shortcuts import render
from .models import Profile
# Create your views here.

def accept(request):
    if request.method=="POST":
        name = request.POST.get("name","")
        age = request.POST.get("age","")
        city = request.POST.get("city","")
        phone = request.POST.get("phone","")
        email = request.POST.get("email","")
        qualification = request.POST.get("qualification","")

        profile=Profile(name=name,age=age,city=city,phone=phone,email=email,qualification=qualification)
        profile.save()

    return render (request,'data/accept.html')

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    return render(request,'data/resume.html',{'user_profile':user_profile})



