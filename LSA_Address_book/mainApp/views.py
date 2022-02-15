from django.shortcuts import render, redirect
from .models import Contact, ContactList
from django.db import models
from .forms import CreateNewList
from .forms import CreateNewContact
from .forms import SearchResult
# Create your views here

#index will show login page and the link to registration
def home(request):
    return render(request, "mainApp/index.html", {})


def index(request, id):
    ls = ContactList.objects.get(id = id)
    items = ls.contact_set.all()
    if request.method == "POST":
        ls.delete()
        return redirect(view)

    return render(request, "mainApp/list.html", {"ls": ls, "items": items})

#view will show a user's default home page if they're logged in
def view(request):
    form = SearchResult(request.POST)

    if request.method == "POST":
        if form.is_valid():
            search = form.cleaned_data['searchresult']
            search = str(search)
        if search:
            query = Contact.objects.filter(firstName__contains = search) | Contact.objects.filter(lastName__contains = search) | Contact.objects.filter(homephoneNumber__contains = search) | Contact.objects.filter(email__contains = search) | Contact.objects.filter(address__contains = search) 
        else:
            query = Contact.objects.all()
        return render(request, "mainApp/view.html", {'query': query, "form": form})
    return render(request, "mainApp/view.html" , {"form": form})

def create(request):
    form = CreateNewList(request.POST)
    hphone = ""
    wphone = ""
    mphone = ""
    mail = ""
    ad = ""
    if request.method == "POST":
        if form.is_valid():
            f = form.cleaned_data["firstName"]
            l = form.cleaned_data["lastName"]
            hphone = form.cleaned_data["homephoneNumber"]
            wphone = form.cleaned_data["workphoneNumber"]
            mphone = form.cleaned_data["mobilephoneNumber"]
            mail = form.cleaned_data["email"]
            ad = form.cleaned_data["address"]
            fullName = f + " " + l
            new_contact = ContactList(name = fullName)
            new_contact.save()

        request.user.contactlist.add(new_contact)
        ls = ContactList.objects.get(id = new_contact.id)
        
        new_details = Contact(id=None,contactlist=new_contact, firstName= f, lastName= l, homephoneNumber=hphone, workphoneNumber = wphone, mobilephoneNumber=mphone, email=mail,address=ad)
        new_details.save()
        return redirect("/%i" %new_contact.id)    

    return render(request, "mainApp/create.html", {"form": form})


