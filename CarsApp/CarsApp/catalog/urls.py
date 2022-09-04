from django.urls import path
from .views import catalogView, CarCreateView

urlpatterns = [
    path('', catalogView, name='index'),
    path('add/', CarCreateView.as_view(), name='add')
]
