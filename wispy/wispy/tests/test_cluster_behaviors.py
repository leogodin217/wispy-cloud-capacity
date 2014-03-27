from django_webtest import WebTest

from clusters.tests.factories import VirtualEnvironmentFactory
from clusters.tests.factories import ClusterFactory

import sure


class TestHomePageBehavior(WebTest):

    """Tests behavior of the home page, mostly viewing data
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_home_page_shows_title(self):

        index = self.app.get('/')
        index.mustcontain('<title>Wispy Cloud Capacity</title>')

    def test_home_page_displays_virtual_environments_list(self):

        """As a Capacity Manager ISBAT view virtual environments
        """

        "Given three Virtual Environments exist."
        ve1 = VirtualEnvironmentFactory.create()
        ve2 = VirtualEnvironmentFactory.create()
        ve3 = VirtualEnvironmentFactory.create()

        "When I visit the home page"

        response = self.app.get('/')

        "Then I should see three virtual environments listed"

        response.mustcontain(ve1.name)
        response.mustcontain(ve2.name)
        response.mustcontain(ve3.name)

    def test_virtual_environments_show_related_clusters(self):

        """As a Capacity Manager ISBAT view clusters for a Virtual
        Environment"""

        """Given a virtual environment with three clusters exists"""
        ve1 = VirtualEnvironmentFactory.create()
        cluster1 = ClusterFactory.create(virtual_environment=ve1)
        cluster2 = ClusterFactory.create(virtual_environment=ve1)
        cluster3 = ClusterFactory.create(virtual_environment=ve1)

        """When I visit the home page
        """
        response = self.app.get('/')

        """Then I should see all of the clusters
        """
        response.mustcontain(cluster1.name)
        response.mustcontain(cluster1.status)
        response.mustcontain(cluster1.notes)
        response.mustcontain(cluster2.name)
        response.mustcontain(cluster2.status)
        response.mustcontain(cluster2.notes)
        response.mustcontain(cluster3.name)
        response.mustcontain(cluster3.status)
        response.mustcontain(cluster3.notes)


class TestClusterBehavior(WebTest):

    """Tests cluster behavior
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_view_cluster_data(self):

        """As a Capacity Manager ISBAT view all data for a Cluster
        """

        "Given a Cluster exists"
        ve1 = VirtualEnvironmentFactory.create()
        cluster = ClusterFactory.create(virtual_environment=ve1)

        "When I view the cluster"
        page = self.app.get('/clusters/%s/' % cluster.id)

        "I should see all data for the cluster"
        page.mustcontain(cluster.name)
        page.mustcontain(cluster.status)
        page.mustcontain(cluster.notes)
        page.mustcontain(cluster.virtual_environment.name)


class TestVirtualEnvironmentBehavior(WebTest):

    """Tests Virtual Environment behaviors
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_view_virtual_environment_data(self):

        """As a Capacity Manager ISBAT view all data for a Virtual Environment
        """

        "Given a Virtual Environment exists."
        ve1 = VirtualEnvironmentFactory.create()

        "When I view a Virtual Environment"
        virtual_environment_id = ve1.id
        response = self.app.get('/virtual_environments/%s/'
                                % virtual_environment_id)

        "I should see all data for the Virtual Environment"
        response.mustcontain(ve1.name)
        response.mustcontain(ve1.market)
        response.mustcontain(ve1.site)
        response.mustcontain(ve1.segment)
        response.mustcontain(ve1.application_layer)
        response.mustcontain(ve1.pipe)
        response.mustcontain(ve1.notes)
        response.mustcontain(ve1.status)
