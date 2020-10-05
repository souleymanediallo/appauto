from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Car


# Create your views here.
# def car_list(request):
#     feature_cars = Car.objects.order_by('-created').filter(is_featured=True)
#     context = {'feature_cars': feature_cars}
#     return render(request, "car/car_list.html", context)


class CarListView(ListView):
    model = Car
    template_name = "car/car_list.html"
    context_object_name = "cars"


class CarDetailView(DetailView):
    model = Car
    template_name = "car/car_detail.html"
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
