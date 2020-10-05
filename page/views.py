from django.shortcuts import render
from .models import Team
from car.models import Car


# Create your views here.
def home(request):
    teams = Team.objects.all()
    feature_cars = Car.objects.order_by('-created').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created')
    context = {'teams': teams, 'feature_cars': feature_cars, 'all_cars': all_cars}
    return render(request, "page/index.html", context)


def about(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, "page/about.html", context)


def service(request):
    return render(request, "page/service.html")


def contact(request):
    return render(request, "page/contact.html")