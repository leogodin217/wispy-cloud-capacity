from django_webtest import WebTest
from django.contrib.auth.models import User

from clusters.models import VirtualEnvironment
from clusters.models import Cluster

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

    def test_can_create_cluster(self):
        """As a Capacity Manager ISBAT create Clusters
        """

        "Given no Clusters exist"
        Cluster.objects.all().count().should.equal(0)

        "And one Virtual Environment Exists"
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

        "When I login to the admin site"
        page = self.admin_login()

        "And add a new Cluster"
        page = page.click('Clusters', index=1, verbose=True)
        page = page.click('Add cluster')
        form = page.forms['cluster_form']
        form["name"] = "cluster1"
        form["status"] = "Closed"
        form["notes"] = "These are some notes"
        form["virtual_environment"].select(text=ve1.name)
        page = form.submit().follow()

        "The form should submit propperly"
        page.status.should.equal("200 OK")

        "And the cluster should be created"
        Cluster.objects.all().count().should.equal(1)
        Cluster.objects.all()[0].name.should.equal("cluster1")
