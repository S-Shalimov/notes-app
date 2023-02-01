from home.models import Contact
from django.shortcuts import render
from datetime import datetime
from django.contrib import messages


def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, contact=contact, desc=desc, date=datetime.today())
        contact.save()
        #messages.success(request, 'Your Form has been Submitted')
    return render(request,"contact.html")