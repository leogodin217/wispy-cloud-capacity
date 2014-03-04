from django_webtest import WebTest
import sure

class TestHomePage(WebTest):

  """Tests for home page functionality including some basic system Tests
  """

  def test_home_page_renders_correct_template(self):
    response = self.app.get('/')
    response.status.should.equal("200 OK")
