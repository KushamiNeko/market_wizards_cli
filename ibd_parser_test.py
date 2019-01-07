import unittest
import os

import ibd_parser

##############################################################################


class TestIBDResearchParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

##############################################################################

    def test_parse_succeed_01(self):

        filepath = os.path.join(
            "test_resources/ibd_research",
            "test_01.html",
        )

        parser = ibd_parser.IBDResearchParser()
        parser.parse(filepath)

        symbol = parser.symbol
        ratings = parser.ibd_research

        self.assertEqual(symbol, "FN")

        self.assertEqual(ratings.get("comp", 0), 81)
        self.assertEqual(ratings.get("eps", 0), 76)
        self.assertEqual(ratings.get("rs", 0), 98)
        self.assertEqual(ratings.get("grs", ""), "C")
        self.assertEqual(ratings.get("smr", ""), "C")
        self.assertEqual(ratings.get("acc", ""), "D")
        self.assertEqual(ratings.get("earnings", ""), "E20190204")

##############################################################################

    def test_parse_succeed_02(self):

        filepath = os.path.join(
            "test_resources/ibd_research",
            "test_02.html",
        )

        parser = ibd_parser.IBDResearchParser()
        parser.parse(filepath)

        symbol = parser.symbol
        ratings = parser.ibd_research

        self.assertEqual(symbol, "FIVN")

        self.assertEqual(ratings.get("comp", 0), 99)
        self.assertEqual(ratings.get("eps", 0), 76)
        self.assertEqual(ratings.get("rs", 0), 97)
        self.assertEqual(ratings.get("grs", ""), "A")
        self.assertEqual(ratings.get("smr", ""), "B")
        self.assertEqual(ratings.get("acc", ""), "D")
        self.assertEqual(ratings.get("earnings", ""), "E20190219")

##############################################################################

    def test_parse_invalid_path(self):

        filepath = "path does not exist"
        parser = ibd_parser.IBDResearchParser()
        with self.assertRaises(ValueError):
            parser.parse(filepath)


##############################################################################

if __name__ == '__main__':
    unittest.main(verbosity=2)

##############################################################################
