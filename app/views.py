from django.shortcuts import render
from django.http import HttpResponse

def mensaje(request):
    return HttpResponse("ESTA ES UNA CALCULADORA!")

def sumar(request, n1,n2):
    return HttpResponse("La suma de "+str(n1)+" + "+str(n2)+" = "+ str(n1+n2))

def restar(request, n1,n2):
    return HttpResponse("La resta de "+str(n1)+" - "+str(n2)+" = "+ str(n1-n2))

def multiplicar(request, n1,n2):
    return HttpResponse("La resta de "+str(n1)+" x "+str(n2)+" = "+ str(n1*n2))

