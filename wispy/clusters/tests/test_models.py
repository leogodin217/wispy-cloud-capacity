from django.test import TestCase

from django_webtest import WebTest
import sure

from factories import VirtualEnvironmentFactory


class TestVirtualEnvironment(TestCase):
    """Tests cluster functionality
    """

    def setUp(self):
        self.ve1 = VirtualEnvironmentFactory.create()

    def test_name_derived_from_cluster_fields(self):
        self.ve1.name.should.equal(self.ve1.market + ' ' +
                                   self.ve1.site + ' ' +
                                   self.ve1.segment + ' ' +
                                   self.ve1.application_layer + ' ' +
                                   self.ve1.pipe)


class TestVirtualEnvironmentURLs(WebTest):
    """Tests URLs associated with Virtual Environments
    """

    def setUp(self):
        self.ve1 = VirtualEnvironmentFactory.create()
        self.ve2 = VirtualEnvironmentFactory.create()

    def test_virtual_environment_detail_url(self):
        response = self.app.get(self.ve1.get_absolute_url())

        response.status.should.equal("200 OK")
        response.mustcontain(self.ve1.name)
        response.html.get_text().should_not.contain(self.ve2.name)
