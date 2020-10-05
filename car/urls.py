from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name="car-list"),
    path('/<int:pk>', views.CarDetailView.as_view(), name="car-detail"),

]