from django_webtest import WebTest
from django.contrib.auth.models import User

from clusters.models import VirtualEnvironment

import sure


class TestAdministrationFunctionality(WebTest):

    """Tests administration functionality. Mostly just ensures administration
       is enabled for neccessary models.
    """

    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@myhost.com',
            password='adminpass')
        self.admin_user.is_staff = True
        self.admin_user.save()

    def tearDown(self):
        pass

    def admin_login(self):
        """Logs in and returns a WebTest TestResponse object
        """
        response = self.app.get('/admin/')
        response.mustcontain('Username')
        form = response.forms['login-form']
        form['username'] = "admin"
        form['password'] = "adminpass"
        return form.submit('Log in').follow()

    def test_can_create_virtual_environment(self):
        """As a Capacity Manager ISBAT create Virtual Environments
        """

        "Given no Virtual Environments exist"

        VirtualEnvironment.objects.all().count().should.equal(0)

        "When I login to the admin site"
        response = self.admin_login()
        "And add a new virtual environment"
        page = response.click(description='Virtual environments')
        page = page.click(description="Add virtual environment")
        form = page.forms['virtualenvironment_form']
        form["market"] = "Market1"
        form["site"] = "site1"
        form["segment"] = "segment1"
        form["application_layer"] = "application_layer1"
        form["pipe"] = "Pipe1"
        form["status"] = "status1"
        form["notes"] = "A bunch of notes"
        page = form.submit().follow()

        "Then I should get a response code of 200"
        page.status.should.equal("200 OK")

        "And I should have one virtual environment create"
        VirtualEnvironment.objects.all().count().should.equal(1)

        "And the Virtual Environment's name should be a concatenation"
        "of the market, site, segment, application layer and pipe fields"
        name = VirtualEnvironment.objects.all()[0].name
        name.should.equal(
            "Market1 site1 segment1 application_layer1 Pipe1")
