import unittest
import time

from data.transaction import FuturesTransaction, entity_to_futures_transaction

##############################################################################


class TestFuturesTransaction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

##############################################################################

    def test_new_transacton_succeed(self):
        order = FuturesTransaction(
            date=20190308,
            symbol="ES",
            action="+",
            quantity=1,
            point=2722.75,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("+", order.action)
        self.assertEqual(1, order.quantity)
        self.assertEqual(2722.75, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)
        self.assertNotEqual(0, order.time_stamp)

        order = FuturesTransaction(
            date=20190308,
            symbol="ES",
            action="-",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("-", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)
        self.assertNotEqual(0, order.time_stamp)

##############################################################################

    def test_new_transacton_lowercase_succeed(self):

        order = FuturesTransaction(
            date=20190308,
            symbol="es",
            action="+",
            quantity=1,
            point=2722.75,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("+", order.action)
        self.assertEqual(1, order.quantity)
        self.assertEqual(2722.75, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)
        self.assertNotEqual(0, order.time_stamp)

        order = FuturesTransaction(
            date=20190308,
            symbol="es",
            action="-",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("-", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)
        self.assertNotEqual(0, order.time_stamp)

##############################################################################

    def test_new_transacton_invalid_date(self):
        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=0,
                symbol="ES",
                action="+",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=-1,
                symbol="ES",
                action="+",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=2013,
                symbol="ES",
                action="-",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

##############################################################################

    def test_new_transacton_invalid_symbol(self):
        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="",
                action="+",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="[]",
                action="+",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="a123",
                action="+",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

##############################################################################

    def test_new_transacton_invalid_action(self):
        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="HI",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="123",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

##############################################################################

    def test_new_transacton_invalid_quantity(self):
        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="-",
                quantity=0,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="-",
                quantity=-1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="+",
                quantity=11.25,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

##############################################################################

    def test_new_transacton_invalid_point(self):
        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="-",
                quantity=1,
                point=0,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="-",
                quantity=1,
                point=-2722.75,
                note="5SMA bounced off 20SMA",
            )

##############################################################################

    def test_entity_to_futures_transaction_succeed(self):
        order = entity_to_futures_transaction({
            "date": "20190308",
            "symbol": "ES",
            "action": "+",
            "quantity": "1",
            "point": "2722.75",
            "note": "5SMA bounced off 20SMA",
        })

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("+", order.action)
        self.assertEqual(1, order.quantity)
        self.assertEqual(2722.75, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)
        self.assertNotEqual(0, order.time_stamp)

##############################################################################

    def test_entity_to_futures_transaction_time_stamp_succeed(self):
        time_stamp = time.time()

        order = entity_to_futures_transaction({
            "date":
            "20190308",
            "symbol":
            "ES",
            "action":
            "+",
            "quantity":
            "1",
            "point":
            "2722.75",
            "note":
            "5SMA bounced off 20SMA",
            "time_stamp":
            time_stamp,
        })

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("+", order.action)
        self.assertEqual(1, order.quantity)
        self.assertEqual(2722.75, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertEqual(time_stamp, order.time_stamp)
        self.assertNotEqual("", order.index)

##############################################################################

    def test_entity_to_futures_transaction_time_stamp_sort_succeed(self):

        order_f = entity_to_futures_transaction({
            "date":
            "20190308",
            "symbol":
            "ES",
            "action":
            "+",
            "quantity":
            "1",
            "point":
            "2722.75",
            "note":
            "5SMA bounced off 20SMA",
            "time_stamp":
            time.time(),
        })

        order_s = entity_to_futures_transaction({
            "date":
            "20190308",
            "symbol":
            "ES",
            "action":
            "+",
            "quantity":
            "1",
            "point":
            "2722.75",
            "note":
            "5SMA bounced off 20SMA",
            "time_stamp":
            time.time(),
        })

        self.assertNotEqual(0, order_f.time_stamp)
        self.assertNotEqual(0, order_s.time_stamp)
        self.assertNotEqual(order_f.time_stamp, order_s.time_stamp)
        self.assertLess(order_f.time_stamp, order_s.time_stamp)

##############################################################################

    def test_futures_transaction_to_entity_succeed(self):
        order = FuturesTransaction(
            date=20190308,
            symbol="ES",
            action="+",
            quantity=1,
            point=2722.75,
            note="5SMA bounced off 20SMA",
        )

        new_transaction = entity_to_futures_transaction(order.entity)

        self.assertEqual(new_transaction.date, order.date)
        self.assertEqual(new_transaction.symbol, order.symbol)
        self.assertEqual(new_transaction.action, order.action)
        self.assertEqual(new_transaction.quantity, order.quantity)
        self.assertEqual(new_transaction.point, order.point)
        self.assertEqual(new_transaction.note, order.note)
        self.assertEqual(new_transaction.index, order.index)
        self.assertEqual(new_transaction.time_stamp, order.time_stamp)


##############################################################################
