from django_webtest import WebTest
import sure

class TestHomePageBehavior(WebTest):

    """Tests behavior of the home page, mostly viewing data
    """

    def test_home_page_shows_title(self):

        index = self.app.get('/')
        index.mustcontain('<title>Wispy Cloud Capacity</title>')