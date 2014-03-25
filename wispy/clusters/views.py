from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import Context

from .models import VirtualEnvironment
from .models import Cluster


def home(request):

    virtual_environments_grouped = {}

    markets = VirtualEnvironment.objects.values('market').distinct()
    markets = [market['market'] for market in markets]
    for market in markets:
        virtual_environments_grouped[market] = {}
        segments = VirtualEnvironment.objects.filter(
            market=market).values('segment').distinct()
        segments = [segment['segment'] for segment in segments]
        for segment in segments:
            virtual_environments = VirtualEnvironment.objects.filter(
                market=market, segment=segment).order_by('site')
            virtual_environments_grouped[market][segment] = virtual_environments

    context = Context(
        {"virtual_environments": virtual_environments_grouped,
         "markets": markets}
    )
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
