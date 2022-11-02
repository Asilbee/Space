from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .forms import EmailForm
from .models import *

def index(r):
    icon = IconGallery.objects.all()
    services = UzServices.objects.all()
    team = TeamIcon.objects.all()
    module = Email()
    form = EmailForm(r.POST, instance=module)
    print(r.POST)
    if form.is_valid():
        form.save()
        return redirect("index")
    ctx = {
        'icon':icon,
        'services':services,
        'team':team,
        "form": form
    }
    return render(r,'main/index.html',ctx)
def ru(r):
    icon = IconGallery.objects.all()
    services = RuServices.objects.all()
    team = TeamIcon.objects.all()
    module = Email()
    form = EmailForm(r.POST, instance=module)
    print(r.POST)
    if form.is_valid():
        form.save()
        return redirect("index")
    ctx = {
        'icon': icon,
        'services': services,
        'team': team,
        "form": form
    }
    return render(r,'main/ru.html',ctx)
def uz(r):
    icon = IconGallery.objects.all()
    services = UzServices.objects.all()
    team = TeamIcon.objects.all()
    module = Email()
    form = EmailForm(r.POST, instance=module)
    print(r.POST)
    if form.is_valid():
        form.save()
        return redirect("index")
    ctx = {
        'icon': icon,
        'services': services,
        'team': team,
        "form": form
    }
    return render(r,'main/index.html',ctx)