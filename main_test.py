import unittest
import main
from mongo import MongoInterface
from context import Context

##############################################################################


class TestMain(unittest.TestCase):

    MONGO = None
    CONTEXT = None

    @classmethod
    def setUpClass(cls):
        cls.MONGO = MongoInterface()
        cls.CONTEXT = Context(database=cls.MONGO)

    def test_login_success(self):
        email = "aa"
        password = "aa".encode("utf-8")
        uid = main.login(self.MONGO, email, password)

        self.assertEqual(
            uid,
            "Y6Rmv1+R7Cn2LsVyxU9bv7hWB5Zgqehys1Yi8CUd8RRfSHxig0iF5taLBCjoBSNKiYxfUNEwc5uyiJ5Zb4UjDg=="
        )

    def test_login_empty(self):
        email = ""
        password = "".encode("utf-8")
        uid = main.login(self.MONGO, email, password)

        self.assertEqual(uid, "")

    def test_login_wrong_email(self):
        email = "wrong"
        password = "aa".encode("utf-8")
        uid = main.login(self.MONGO, email, password)

        self.assertEqual(uid, "")

    def test_login_wrong_password(self):
        email = "aa"
        password = "wrong".encode("utf-8")
        uid = main.login(self.MONGO, email, password)

        self.assertEqual(uid, "")

    def test_login_wrong_both(self):
        email = "wrong"
        password = "wrong".encode("utf-8")
        uid = main.login(self.MONGO, email, password)

        self.assertEqual(uid, "")


##############################################################################

if __name__ == '__main__':
    unittest.main(verbosity=2)

##############################################################################
