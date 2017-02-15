from django.shortcuts import render
from djangos.http import HttpResponse

# Create your views here.

def posts_home(request):
    return render("<h1>Hello</h1>")
