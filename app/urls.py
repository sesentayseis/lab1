from django.urls import path
#from django.urls import include, path
#from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.mensaje, name='mensaje'),
]


urlpatterns = [
    
    # ex: localhost:8080/polls/5/
    path('sumar/<int:n1>/<int:n2>', views.sumar, name='sumar'),
    # ex: localhost:8080/polls/5/results/
    path('restar/<int:n1>/<int:n2>', views.restar, name='restar'),
    path('multiplicar/<int:n1>/<int:n2>', views.multiplicar, name='multiplicar'),

]
