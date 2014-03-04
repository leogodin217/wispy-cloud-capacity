from django.shortcuts import render

from .models import VirtualEnvironment

# Create your views here.
def home(request):

    context = {"virtual_environments": VirtualEnvironment.objects.all()}
    return render(request, 'clusters/home.html', context)