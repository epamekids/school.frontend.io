from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def randome(request):
    return HttpResponse(random.randint(0, 10000000))