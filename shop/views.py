from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    return render(request, 'index.html',{'Pro':Product.objects.all()})