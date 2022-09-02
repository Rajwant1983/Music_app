from unicodedata import name
from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from flask import url_for

#  this is testing 3
from app import application,d
from schema import Colleges


class TestBase(LiveServerTestCase):
    TEST_PORT = 5050  # test port, doesn't need to be open

    def create_app(self):
        application.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            LIVESERVER_PORT=self.TEST_PORT,
            DEBUG=True,
            TESTING=True
        )
        return application

    def setUp(self):
        from schema import Students
        d.create_all()  # create schema before we try to get the page
        #
        test_college = Colleges(name="Test")
        d.session.add(test_college)
        d.session.commit()

    def tearDown(self):
        d.session.remove()
        d.drop_all()


class TestAdd(TestBase):

    def test_index_route(self):
        response = application.test_client().get('/')

        assert response.status_code == 200