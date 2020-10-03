from django.shortcuts import render
from .models import Team


# Create your views here.
def home(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, "page/index.html", context)


def about(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, "page/about.html", context)


def service(request):
    return render(request, "page/service.html")


def contact(request):
    return render(request, "page/contact.html")