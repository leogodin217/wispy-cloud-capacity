import factory

#from clusters.models import VirtualEnvironment
from clusters import models


class VirtualEnvironmentFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.VirtualEnvironment

    #id = factory.Sequence(lambda n: n, int)
    market = factory.sequence(lambda n: 'market {0}'.format(n))
    site = factory.sequence(lambda n: 'site {0}'.format(n))
    segment = factory.sequence(lambda n: 'segment {0}'.format(n))
    application_layer = factory.sequence(
        lambda n: 'application_layer {0}'.format(n))
    pipe = factory.sequence(lambda n: 'pipe {0}'.format(n))
    notes = factory.sequence(lambda n: 'notes {0}'.format(n))
    status = factory.sequence(lambda n: 'status {0}'.format(n))
