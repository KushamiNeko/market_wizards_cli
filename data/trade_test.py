import unittest

from data.trade import FuturesTrade
from data.transaction import FuturesTransaction

##############################################################################


class TestFuturesTrade(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

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
        self.assertEqual(trade.average_cost, 2732.375)
        self.assertEqual(trade.average_revenue, 2776.625)
        self.assertEqual(trade.gl_point, 44.25)

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
        self.assertEqual(trade.average_cost, 2735.5833)
        self.assertEqual(trade.average_revenue, 2776.75)
        self.assertEqual(trade.gl_point, 41.1667)

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
        self.assertEqual(trade.average_cost, 2732.375)
        self.assertEqual(trade.average_revenue, 2723.75)
        self.assertEqual(trade.gl_point, -8.625)

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
        self.assertEqual(trade.average_cost, 2735.5833)
        self.assertEqual(trade.average_revenue, 2723.1667)
        self.assertEqual(trade.gl_point, -12.4166)

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
        self.assertEqual(trade.average_cost, 73.725)
        self.assertEqual(trade.average_revenue, 50.17)
        self.assertEqual(trade.gl_point, 23.555)

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
        self.assertEqual(trade.average_cost, 73.5)
        self.assertEqual(trade.average_revenue, 48.9567)
        self.assertEqual(trade.gl_point, 24.5433)

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
        self.assertEqual(trade.average_cost, 73.725)
        self.assertEqual(trade.average_revenue, 74.1)
        self.assertEqual(trade.gl_point, -0.375)

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
        self.assertEqual(trade.average_cost, 73.95)
        self.assertEqual(trade.average_revenue, 74.1)
        self.assertEqual(trade.gl_point, -0.15)

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
