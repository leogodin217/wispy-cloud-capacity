from django.test import TestCase

import sure

from factories import VirtualEnvironmentFactory


class TestCluster(TestCase):
    """Tests cluster functionality
    """

    def test_name_derived_from_cluster_fields(self):
        ve = VirtualEnvironmentFactory.create()
        ve.name.should.equal(ve.market + ' ' +
                             ve.site + ' ' +
                             ve.segment + ' ' +
                             ve.application_layer + ' ' +
                             ve.pipe)
