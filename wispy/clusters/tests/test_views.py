from django_webtest import WebTest
import sure
from sure import expect

class TestHomePage(WebTest):

    """Tests for home page functionality including some basic system Tests
    """

    def test_home_page_shows_clusters(self):
        """Tests if clusters are displayed on the home page. Requires clusters
        and virtual environments
        """
