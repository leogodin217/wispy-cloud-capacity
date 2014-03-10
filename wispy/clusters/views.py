from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import VirtualEnvironment


def home(request):

    context = {"virtual_environments": VirtualEnvironment.objects.all()}
    return render(request, 'clusters/home.html', context)


def virtual_environment_detail(request, virtual_environment_id):
    virtual_environment = get_object_or_404(
        VirtualEnvironment, pk=virtual_environment_id
    )
    context = {'virtual_environment': virtual_environment}
    return render(request, 'clusters/virtual_environment_detail.html', context)
