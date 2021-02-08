from django.shortcuts import render
from .models import Order


# Create your views here.

def first_page(request):
    return render(request, './index.html')
