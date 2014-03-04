import factory

from clusters.models import VirtualEnvironment

class VirtualEnvironmentFactory(factory.Factory):

    FACTORY_FOR = VirtualEnvironment
    name = factory.sequence(lambda n: 'virtual environment {0}'.format(n))