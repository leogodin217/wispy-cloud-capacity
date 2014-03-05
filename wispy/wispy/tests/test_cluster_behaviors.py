from django_webtest import WebTest
from clusters.models import VirtualEnvironment

import sure

class TestHomePageBehavior(WebTest):

  """Tests behavior of the home page, mostly viewing data
  """

  def setUp(self):
      self.ve1 = VirtualEnvironment.objects.create(
        name="ve1",
        market="market1",
        site="site1",
        segment="segment1",
        application_layer="application layer 1",
        pipe="pipe1",
        notes="notes1",
        status="status1"
      )
      self.ve2 = VirtualEnvironment.objects.create(name="ve2")
      self.ve3 = VirtualEnvironment.objects.create(name="ve3")

  def tearDown(self):
    pass



  def test_home_page_shows_title(self):

    index = self.app.get('/')
    index.mustcontain('<title>Wispy Cloud Capacity</title>')

  def test_home_page_displays_virtual_environments_list(self):

    """As a Capacity Manager ISBAT view virtual environments
    """

    "Given three Virtual Environments exist. Handled in setUp"

    "When I visit the home page"

    response = self.app.get('/')

    "Then I should see three virtual environments listed"
    fields = ["name", "id"]

    response.mustcontain(self.ve1.name)
    response.mustcontain(self.ve2.name)
    response.mustcontain(self.ve3.name)


class TestVirtualEnvironmentBehavior(WebTest):

  """Tests Virtual Environment behaviors
  """

  def setUp(self):
      self.ve1 = VirtualEnvironment.objects.create(name="ve1")

  def tearDown(self):
    pass

  def test_can_view_virtual_environment_data(self):

    """As a Capacity Manager ISBAT view all data for a Virtual Environment
    """

    "Given a Virtual Environment exists. (Handled in setUp)"

    "When I view a Virtual Environment"
    response = self.app.get('/virtual_environments/1/')

    "I should see all data for the Virtual Environment"
    response.mustcontain(self.ve1.name)
    response.mustcontain(self.ve1.market)
    response.mustcontain(self.ve1.site)
    response.mustcontain(self.ve1.segment)
    response.mustcontain(self.ve1.application_layer)
    response.mustcontain(self.ve1.pipe)
    response.mustcontain(self.ve1.notes)
    response.mustcontain(self.ve1.status)


