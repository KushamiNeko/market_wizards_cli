import unittest

from pages.pages import Pages

##############################################################################


class TestPage(unittest.TestCase):

    _actions = [
        "add",
        "search",
        "stop",
    ]

    @classmethod
    def setUpClass(cls):
        pass

##############################################################################

    def test_clean_command_succeed_01(self):
        page = Pages(self._actions)
        command = page._clean_command("st")
        self.assertEqual(command, "stop")

##############################################################################

    def test_clean_command_succeed_02(self):
        page = Pages(self._actions)
        command = page._clean_command("search")
        self.assertEqual(command, "search")

##############################################################################

    def test_clean_command_succeed_03(self):
        page = Pages(self._actions)
        command = page._clean_command("a")
        self.assertEqual(command, "add")

##############################################################################

    def test_clean_command_multiple(self):
        page = Pages(self._actions)

        with self.assertRaises(ValueError):
            page._clean_command("s")

##############################################################################

    def test_clean_command_unknown(self):
        page = Pages(self._actions)

        with self.assertRaises(ValueError):
            page._clean_command("f")


##############################################################################

if __name__ == '__main__':
    unittest.main(verbosity=2)

##############################################################################
