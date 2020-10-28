from django.urls import path

#from .views import calculoabv
from . import views

urlpatterns = [
    path('', views.calculoabv), #pagina principal

]