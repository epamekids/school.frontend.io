from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def rand(request):
    return HttpResponse(random.randint(0, 10000000))
