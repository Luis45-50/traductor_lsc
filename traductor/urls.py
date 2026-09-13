from django.urls import path
from .views import escuchar_microfono

urlpatterns = [
    path('microfono/', escuchar_microfono, name='microfono'),
]
