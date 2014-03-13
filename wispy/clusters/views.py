from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import VirtualEnvironment
from .models import Cluster


def home(request):

    context = {"virtual_environments": VirtualEnvironment.objects.all()}
    return render(request, 'clusters/home.html', context)


def virtual_environment_detail(request, virtual_environment_id):
    virtual_environment = get_object_or_404(
        VirtualEnvironment, pk=virtual_environment_id
    )
    context = {'virtual_environment': virtual_environment}
    return render(request, 'clusters/virtual_environment_detail.html', context)


def cluster_detail(request, cluster_id):
    cluster = get_object_or_404(Cluster, pk=cluster_id)
    context = {'cluster': cluster}
    return render(request, 'clusters/cluster_detail.html', context)
