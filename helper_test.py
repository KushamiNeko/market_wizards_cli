import unittest
import helper
import datetime

##############################################################################


class TestHelper(unittest.TestCase):
    def test_days_to_date_future(self):
        now = int(datetime.datetime.now().strftime("%Y%m%d")) + 1
        days = helper.days_to_date(now)
        self.assertEqual(days, 1)

##############################################################################

    def test_days_to_date_today(self):
        now = int(datetime.datetime.now().strftime("%Y%m%d"))
        days = helper.days_to_date(now)
        self.assertEqual(days, 0)

##############################################################################

    def test_days_to_date_past(self):
        now = int(datetime.datetime.now().strftime("%Y%m%d")) - 1
        days = helper.days_to_date(now)
        # self.assertEqual(days, 0)
        self.assertEqual(days, -1)

##############################################################################

    def test_hex_to_rgb_white(self):
        rgb = helper.hex_to_rgb("ffffff")
        self.assertTupleEqual(rgb, (255, 255, 255))

##############################################################################

    def test_hex_to_rgb_red(self):
        rgb = helper.hex_to_rgb("ff0000")
        self.assertTupleEqual(rgb, (255, 0, 0))

##############################################################################

    def test_hex_to_rgb_green(self):
        rgb = helper.hex_to_rgb("00ff00")
        self.assertTupleEqual(rgb, (0, 255, 0))

##############################################################################

    def test_hex_to_rgb_blue(self):
        rgb = helper.hex_to_rgb("0000ff")
        self.assertTupleEqual(rgb, (0, 0, 255))

##############################################################################

    def test_hex_to_rgb_black(self):
        rgb = helper.hex_to_rgb("000000")
        self.assertTupleEqual(rgb, (0, 0, 0))

##############################################################################

    def test_random_string(self):
        for _ in range(100):
            rand_string_01 = helper.random_string()
            rand_string_02 = helper.random_string()

            self.assertNotEqual(rand_string_01, rand_string_02)

##############################################################################

    def test_key_value_pair_succeed(self):
        inputs = "price=100;op=l"
        pair = helper.key_value_pair(inputs)

        self.assertEqual(pair.get("price", ""), "100")
        self.assertEqual(pair.get("op", ""), "l")

        inputs = "price=100 ; op=l"
        pair = helper.key_value_pair(inputs)

        self.assertEqual(pair.get("price", ""), "100")
        self.assertEqual(pair.get("op", ""), "l")

        inputs = "price=100.5 ; note={}".format(
            "there was a VCP, and 5SMA bounced off 20SMA nicely.")
        pair = helper.key_value_pair(inputs)

        self.assertEqual(pair.get("price", ""), "100.5")
        self.assertEqual(
            pair.get("note", ""),
            "there was a VCP, and 5SMA bounced off 20SMA nicely.")

        inputs = "action=+ ; op=-"
        pair = helper.key_value_pair(inputs)

        self.assertEqual(pair.get("action", ""), "+")
        self.assertEqual(pair.get("op", ""), "-")

##############################################################################

    def test_key_value_pair_empty(self):
        inputs = ""
        with self.assertRaises(ValueError):
            helper.key_value_pair(inputs)

        inputs = "price=;o=l"
        with self.assertRaises(ValueError):
            helper.key_value_pair(inputs)

        inputs = "=100.5;o=l"
        with self.assertRaises(ValueError):
            helper.key_value_pair(inputs)


##############################################################################

if __name__ == '__main__':
    unittest.main(verbosity=2)

##############################################################################
