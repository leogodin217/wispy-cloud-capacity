from django_webtest import WebTest

from clusters.models import VirtualEnvironment

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
        ve1 = VirtualEnvironment.objects.create(name="ve1")
        ve2 = VirtualEnvironment.objects.create(name="ve2")
        ve3 = VirtualEnvironment.objects.create(name="ve3")

        "When I visit the home page"

        response = self.app.get('/')

        "Then I should see three virtual environments listed"

        response.mustcontain(ve1.name)
        response.mustcontain(ve2.name)
        response.mustcontain(ve3.name)


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
        ve1 = VirtualEnvironment.objects.create(
            name="ve1",
            market="market1",
            site="site1",
            segment="segment1",
            application_layer="application layer 1",
            pipe="pipe1",
            notes="notes1",
            status="status1"
        )
        cluster = ve1.cluster_set.create(
            name="cluster1",
            status="closed",
            notes="These are some notes for the cluster"
        )

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
        ve1 = VirtualEnvironment.objects.create(
            name="ve1",
            market="market1",
            site="site1",
            segment="segment1",
            application_layer="application layer 1",
            pipe="pipe1",
            notes="notes1",
            status="status1"
        )

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
