from django_webtest import WebTest
from django.contrib.auth.models import User

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

    def test_can_create_virtual_environment(self):
        """As a Capacity Manager ISBAT create Virtual Environments
        """

        "Given an admin User exists"
        admin_user = User.objects.create_superuser(username='admin',
                                   email='admin@myhost.com',
                                   password='adminpass')
        admin_user.is_staff = True
        admin_user.save()

        "And no Virtual Environments exist"
        for ve in VirtualEnvironment.objects.all():
            ve.delete()

        VirtualEnvironment.objects.all().count().should.equal(0)

        "When I login to the admin site"
        response = self.app.get('/admin/')
        response.mustcontain('Username')
        form = response.forms['login-form']
        form['username'] = "admin"
        form['password'] = "adminpass"
        res = form.submit('Log in')
        response = res.follow()

        "And add a new virtual environment"
        response = response.click(description='Virtual environments')
        "And click add virtual environment"
        response = response.click(description="Add virtual environment")
        form = response.forms['virtualenvironment_form']
        form["market"] = "Market1"
        form["site"] = "site1"
        form["segment"] = "segment1"
        form["application_layer"] = "application_layer1"
        form["pipe"] = "Pipe1"
        form["status"] = "status1"
        form["notes"] = "A bunch of notes"

        "And click submit"
        result = form.submit().follow()

        "Then I should get a response code of 200"
        result.status.should.equal("200 OK")

        "And I should have one virtual environment create"
        VirtualEnvironment.objects.all().count().should.equal(1)

        "And the Virtual Environment's name should be a concatenation"
        "of the market, site, segment, application layer and pipe fields"
        name = VirtualEnvironment.objects.all()[0].name
        name.should.equal(
            "Market1 site1 segment1 application_layer1 Pipe1")
