from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "page/index.html")


def about(request):
    return render(request, "page/about.html")


def service(request):
    return render(request, "page/service.html")


def contact(request):
    return render(request, "page/contact.html")