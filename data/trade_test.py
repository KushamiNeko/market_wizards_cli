import unittest

from data.trade import FuturesTrade
from data.transaction import FuturesTransaction
import config

##############################################################################


class TestFuturesTrade(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

##############################################################################

    def test_empty_orders(self):
        orders = []
        with self.assertRaises(ValueError):
            FuturesTrade(orders)

##############################################################################

    def test_long_gain_succeed(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="ES",
                action="increase",
                quantity=1,
                point=2742.00,
                note="break out",
            ),
            FuturesTransaction(
                date=20190315,
                symbol="ES",
                action="DECREASE",
                quantity=1,
                point=2776.25,
                note="losing strength",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="ES",
                action="CLOSE",
                quantity=1,
                point=2777.00,
                note="break down",
            ),
        ]

        trade = FuturesTrade(orders)

        self.assertEqual(trade.action, "LONG")
        self.assertEqual(trade.average_cost,
                         round(2732.375, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.average_revenue,
                         round(2776.625, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.gl_point, round(44.25, config.DOLLAR_DECIMALS))

##############################################################################

    def test_long_gain_complex_succeed(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="ES",
                action="increase",
                quantity=2,
                point=2742.00,
                note="break out",
            ),
            FuturesTransaction(
                date=20190315,
                symbol="ES",
                action="DECREASE",
                quantity=1,
                point=2776.25,
                note="losing strength",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="ES",
                action="CLOSE",
                quantity=2,
                point=2777.00,
                note="break down",
            ),
        ]

        trade = FuturesTrade(orders)

        self.assertEqual(trade.action, "LONG")
        self.assertEqual(trade.average_cost,
                         round(2735.5833, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.average_revenue,
                         round(2776.75, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.gl_point, round(41.1667,
                                               config.DOLLAR_DECIMALS))

##############################################################################

    def test_long_stop_loss_succeed(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="ES",
                action="increase",
                quantity=1,
                point=2742.00,
                note="break out",
            ),
            FuturesTransaction(
                date=20190315,
                symbol="ES",
                action="DECREASE",
                quantity=1,
                point=2725.5,
                note="losing strength",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="ES",
                action="CLOSE",
                quantity=1,
                point=2722.00,
                note="break down",
            ),
        ]

        trade = FuturesTrade(orders)

        self.assertEqual(trade.action, "LONG")
        self.assertEqual(trade.average_cost,
                         round(2732.375, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.average_revenue,
                         round(2723.75, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.gl_point, round(-8.625, config.DOLLAR_DECIMALS))

##############################################################################

    def test_long_stop_loss_complex_succeed(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="ES",
                action="increase",
                quantity=2,
                point=2742.00,
                note="break out",
            ),
            FuturesTransaction(
                date=20190315,
                symbol="ES",
                action="DECREASE",
                quantity=1,
                point=2725.5,
                note="losing strength",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="ES",
                action="CLOSE",
                quantity=2,
                point=2722.00,
                note="break down",
            ),
        ]

        trade = FuturesTrade(orders)

        self.assertEqual(trade.action, "LONG")
        self.assertEqual(trade.average_cost,
                         round(2735.5833, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.average_revenue,
                         round(2723.1667, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.gl_point, round(-12.4166,
                                               config.DOLLAR_DECIMALS))

##############################################################################

    def test_short_gain_succeed(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="SHORT",
                quantity=1,
                point=74.4,
                note="bounced off 5SMA on the short side",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="CL",
                action="increase",
                quantity=1,
                point=73.05,
                note="break down",
            ),
            FuturesTransaction(
                date=20190315,
                symbol="CL",
                action="DECREASE",
                quantity=1,
                point=53.81,
                note="gap up",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="CL",
                action="CLOSE",
                quantity=1,
                point=46.53,
                note="bounced sharply",
            ),
        ]

        trade = FuturesTrade(orders)

        self.assertEqual(trade.action, "SHORT")
        self.assertEqual(trade.average_cost,
                         round(73.725, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.average_revenue,
                         round(50.17, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.gl_point, round(23.555, config.DOLLAR_DECIMALS))

##############################################################################

    def test_short_gain_complex_succeed(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="SHORT",
                quantity=1,
                point=74.4,
                note="bounced off 5SMA on the short side",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="CL",
                action="increase",
                quantity=2,
                point=73.05,
                note="break down",
            ),
            FuturesTransaction(
                date=20190315,
                symbol="CL",
                action="DECREASE",
                quantity=1,
                point=53.81,
                note="gap up",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="CL",
                action="CLOSE",
                quantity=2,
                point=46.53,
                note="bounced sharply",
            ),
        ]

        trade = FuturesTrade(orders)

        self.assertEqual(trade.action, "SHORT")
        self.assertEqual(trade.average_cost, round(73.5,
                                                   config.DOLLAR_DECIMALS))
        self.assertEqual(trade.average_revenue,
                         round(48.9567, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.gl_point, round(24.5433,
                                               config.DOLLAR_DECIMALS))

##############################################################################

    def test_short_stop_loss_succeed(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="SHORT",
                quantity=1,
                point=74.4,
                note="bounced off 5SMA on the short side",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="CL",
                action="increase",
                quantity=1,
                point=73.05,
                note="break down",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="CL",
                action="CLOSE",
                quantity=2,
                point=74.1,
                note="bounced sharply",
            ),
        ]

        trade = FuturesTrade(orders)

        self.assertEqual(trade.action, "SHORT")
        self.assertEqual(trade.average_cost,
                         round(73.725, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.average_revenue,
                         round(74.1, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.gl_point, round(-0.375, config.DOLLAR_DECIMALS))

##############################################################################

    def test_short_stop_loss_complex_succeed(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="SHORT",
                quantity=2,
                point=74.4,
                note="bounced off 5SMA on the short side",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="CL",
                action="increase",
                quantity=1,
                point=73.05,
                note="break down",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="CL",
                action="CLOSE",
                quantity=3,
                point=74.1,
                note="bounced sharply",
            ),
        ]

        trade = FuturesTrade(orders)

        self.assertEqual(trade.action, "SHORT")
        self.assertEqual(trade.average_cost,
                         round(73.95, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.average_revenue,
                         round(74.1, config.DOLLAR_DECIMALS))
        self.assertEqual(trade.gl_point, round(-0.15, config.DOLLAR_DECIMALS))

##############################################################################

    def test_quantity_mismatch_open(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            ),
            FuturesTransaction(
                date=20190315,
                symbol="ES",
                action="DECREASE",
                quantity=1,
                point=2776.25,
                note="losing strength",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="ES",
                action="CLOSE",
                quantity=1,
                point=2777.00,
                note="break down",
            ),
        ]

        with self.assertRaises(ValueError):
            FuturesTrade(orders)

##############################################################################

    def test_quantity_mismatch_close(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="ES",
                action="increase",
                quantity=1,
                point=2742.00,
                note="break out",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="ES",
                action="CLOSE",
                quantity=1,
                point=2777.00,
                note="break down",
            ),
        ]

        with self.assertRaises(ValueError):
            FuturesTrade(orders)

##############################################################################

    def test_symbol_mismatch_open(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="GC",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            ),
            FuturesTransaction(
                date=20190315,
                symbol="ES",
                action="DECREASE",
                quantity=1,
                point=2776.25,
                note="losing strength",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="ES",
                action="CLOSE",
                quantity=1,
                point=2777.00,
                note="break down",
            ),
        ]

        with self.assertRaises(ValueError):
            FuturesTrade(orders)

##############################################################################

    def test_symbol_mismatch_close(self):

        orders = [
            FuturesTransaction(
                date=20190308,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            ),
            FuturesTransaction(
                date=20190309,
                symbol="ES",
                action="increase",
                quantity=1,
                point=2742.00,
                note="break out",
            ),
            FuturesTransaction(
                date=20190318,
                symbol="SI",
                action="CLOSE",
                quantity=1,
                point=2777.00,
                note="break down",
            ),
        ]

        with self.assertRaises(ValueError):
            FuturesTrade(orders)


##############################################################################
if __name__ == '__main__':
    unittest.main(verbosity=2)

##############################################################################
