from django.urls import path

#from .views import calculoabv
from . import views

urlpatterns = [
    path(r'',views.teste, name='home'),
    path(r'/receitas',views.receitas, name='receitas'),
    path(r'/calculoabv', views.calculoabv, name='calculoabv')
    #path('', views.calculoabv), #pagina principal

]