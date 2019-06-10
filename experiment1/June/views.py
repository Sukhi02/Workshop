from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return  HttpResponse("<H2>HEY! Mr.Napinder Singh!  </H2>")