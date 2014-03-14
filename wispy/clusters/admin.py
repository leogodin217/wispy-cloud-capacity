from django.contrib import admin

from clusters.models import VirtualEnvironment
from clusters.models import Cluster


admin.site.register(VirtualEnvironment)
admin.site.register(Cluster)
