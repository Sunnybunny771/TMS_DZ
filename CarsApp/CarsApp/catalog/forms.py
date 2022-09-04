from django.forms import ModelForm

from .models import CarBrand, CarType, Engine, Car


class CarBrandForm(ModelForm):
    class Meta:
        model = CarBrand
        fields = ('brand', )


class EngineForm(ModelForm):
    class Meta:
        model = Engine
        fields = ('type', 'volume', 'horsepower', 'fuel')


class CarTypeForm(ModelForm):
    class Meta:
        model = CarType
        fields = ('wheel_drive', 'transmission', 'type')


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 'type', 'engine', 'published')