import unittest

from pages.calculator import Calculator

##############################################################################


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

##############################################################################

    def test_stop_long_succeed(self):
        calculator = Calculator(None)

        price = 100.0
        op = "LONG"

        stops = calculator._process_stop(price, op)

        for stop in stops:
            value = (float(100 + stop) / 100.0) * price
            self.assertEqual(stops[stop], value)

##############################################################################

    def test_stop_short_succeed(self):
        calculator = Calculator(None)

        price = 100.0
        op = "SHORT"

        stops = calculator._process_stop(price, op)

        for stop in stops:
            value = (float(100 - stop) / 100.0) * price
            self.assertEqual(stops[stop], value)

##############################################################################

    def test_stop_negative_price(self):
        calculator = Calculator(None)

        price = -100.0
        op = "SHORT"

        with self.assertRaises(ValueError):
            calculator._process_stop(price, op)

##############################################################################

    def test_stop_zero_price(self):
        calculator = Calculator(None)

        price = 0
        op = "SHORT"

        with self.assertRaises(ValueError):
            calculator._process_stop(price, op)

##############################################################################

    def test_stop_invalid_op(self):
        calculator = Calculator(None)

        price = 100.0
        op = "HELLO"

        with self.assertRaises(ValueError):
            calculator._process_stop(price, op)

##############################################################################

    def test_depth_succeed(self):
        calculator = Calculator(None)

        start = 100.0
        end = 50.0

        depth = calculator._process_depth(start, end)

        self.assertEqual(depth, (end - start) / start)

##############################################################################

    def test_depth_zero_start(self):
        calculator = Calculator(None)

        start = 0
        end = 50.0

        with self.assertRaises(ValueError):
            calculator._process_depth(start, end)

##############################################################################

    def test_depth_negative_start(self):
        calculator = Calculator(None)

        start = -100.0
        end = 50.0

        with self.assertRaises(ValueError):
            calculator._process_depth(start, end)

##############################################################################

    def test_depth_zero_end(self):
        calculator = Calculator(None)

        start = 100.0
        end = 0

        with self.assertRaises(ValueError):
            calculator._process_depth(start, end)

##############################################################################

    def test_depth_negative_end(self):
        calculator = Calculator(None)

        start = 100.0
        end = -50.0

        with self.assertRaises(ValueError):
            calculator._process_depth(start, end)


##############################################################################

if __name__ == '__main__':
    unittest.main(verbosity=2)

##############################################################################
