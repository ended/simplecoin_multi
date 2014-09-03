import simplecoin
import unittest

from simplecoin import db


class UnitTest(unittest.TestCase):
    """ Represents a set of tests that only need the database iniailized, but
    no fixture data """
    def setUp(self):
        app = simplecoin.create_app('webserver', config='test.yml')
        with app.app_context():
            self.db = simplecoin.db
            self.setup_db()

        self.app = app
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        # dump the test elasticsearch index
        db.session.remove()
        db.drop_all()

    def setup_db(self):
        self.db.drop_all()
        self.db.create_all()
        db.session.commit()
