from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *

# Create your views here.

from django.views import View

class IndexFormsView(CreateView):
    template_name = "index.html"
    model = Fornecedor
    fields = '__all__'


