from django_webtest import WebTest

import sure

from clusters.tests.factories import VirtualEnvironmentFactory

class TestHomePageBehavior(WebTest):

    """Tests behavior of the home page, mostly viewing data
    """

    def test_home_page_shows_title(self):

        index = self.app.get('/')
        index.mustcontain('<title>Wispy Cloud Capacity</title>')

    def test_home_page_displays_virtual_environments(self):

        """As a Capacity Manager ISBAT view virtual environments
        """

        "Given three Virtual Environments exist"
        ve1 = VirtualEnvironmentFactory.create()
        ve2 = VirtualEnvironmentFactory.create()
        ve3 = VirtualEnvironmentFactory.create()

        "When I visit the home page"

        response = self.app.get('/')

        "Then I should see three virtual environments listed"
        response.mustcontain(ve1.name)
        response.mustcontain(ve2.name)
        response.mustcontain(ve3.name)
