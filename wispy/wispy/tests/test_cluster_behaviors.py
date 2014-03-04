from django_webtest import WebTest
from clusters.models import VirtualEnvironment

import sure

class TestHomePageBehavior(WebTest):

    """Tests behavior of the home page, mostly viewing data
    """

    def setUp(self):
        self.ve1 = VirtualEnvironment.objects.create(name="ve1")
        self.ve2 = VirtualEnvironment.objects.create(name="ve2")
        self.ve3 = VirtualEnvironment.objects.create(name="ve3")

    def tearDown(self):
        pass



    def test_home_page_shows_title(self):


        index = self.app.get('/')
        index.mustcontain('<title>Wispy Cloud Capacity</title>')

    def test_home_page_displays_virtual_environments(self):

        """As a Capacity Manager ISBAT view virtual environments
        """

        "three Virtual Environments exist"
        # ve1 = VirtualEnvironment.objects.create(name="ve1")
        # ve2 = VirtualEnvironment.objects.create(name="ve2")
        # ve3 = VirtualEnvironment.objects.create(name="ve3")

        "When I visit the home page"

        response = self.app.get('/')

        "Then I should see three virtual environments listed"
        response.mustcontain(self.ve1.name)
        response.mustcontain(self.ve2.name)
        response.mustcontain(self.ve3.name)
