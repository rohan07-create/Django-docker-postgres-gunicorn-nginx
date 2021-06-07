from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable": "hello this a variable",
    }
    
    return render(request, "index.html")
    # return render(request, 'index.html', context)
    # return HttpResponse("Hello from Index")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("Hello from about")


def contact(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        addr = request.POST.get("addr")
        desc = request.POST.get("desc")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        contact = Contact(
            fname=fname,
            lname=lname,
            email=email,
            phone=phone,
            addr=addr,
            desc=desc,
            city=city,
            state=state,
            zip=zip,
            date=datetime.today()
        )
        contact.save()
        messages.success(request, "Thank You For Contacting Us...!!!")

    return render(request, "contact.html")
    # return HttpResponse("Hello from contact")



