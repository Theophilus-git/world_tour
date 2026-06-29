from django.shortcuts import render
# from django.http import HttpResponse
from .models import tour

# Create your views here.
def index(request):
    tours = tour.objects.all()
    context = {'tours':tours}
    return render(request,'tours/index.html', context)
