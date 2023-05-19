from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def home(request):
    return render(request, 'page/home.html')


def about(request):
    return render(request, 'page/about.html')


def contact(request):
    if request.method == 'POST':

        # 1:get the data from the form
        v_name = request.POST.get('name')
        v_email = request.POST.get('email')
        v_subject = request.POST.get('subject')
        v_message = request.POST.get('message')

        # 2: send this data to the DB(Models)
        v_contact = Contact(name=v_name, email=v_email, subject=v_subject, massage=v_message)
        v_contact.save()
        return render(request, "part/jv.js")

    else:
        return render(request, "page/contact.html")
