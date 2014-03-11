import factory

from clusters.models import VirtualEnvironment


class VirtualEnvironmentFactory(factory.Factory):

    FACTORY_FOR = VirtualEnvironment
    market = factory.sequence(lambda n: 'market {0}'.format(n))
    site = factory.sequence(lambda n: 'site {0}'.format(n))
    segment = factory.sequence(lambda n: 'segment {0}'.format(n))
    application_layer = factory.sequence(
        lambda n: 'application_layer {0}'.format(n))
    pipe = factory.sequence(lambda n: 'pipe {0}'.format(n))
    notes = factory.sequence(lambda n: 'notes {0}'.format(n))
    status = factory.sequence(lambda n: 'status {0}'.format(n))
