
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm


class CarCreateView(CreateView):
    template = 'addCar.html'
    form_class = CarForm
    success_url = reverse_lazy('index')


def catalogView(request):
    allcars = Car.objects.all()
    return render(request, 'catalog/index.html', {'allcars': allcars})

