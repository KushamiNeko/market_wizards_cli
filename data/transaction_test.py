import unittest

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
            action="LONG",
            quantity=1,
            point=2722.75,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("LONG", order.action)
        self.assertEqual(1, order.quantity)
        self.assertEqual(2722.75, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

        order = FuturesTransaction(
            date=20190308,
            symbol="ES",
            action="SHORT",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("SHORT", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

        order = FuturesTransaction(
            date=20190308,
            symbol="ES",
            action="INCREASE",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("INCREASE", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

        order = FuturesTransaction(
            date=20190308,
            symbol="ES",
            action="DECREASE",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("DECREASE", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

        order = FuturesTransaction(
            date=20190308,
            symbol="ES",
            action="CLOSE",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("CLOSE", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

##############################################################################

    def test_new_transacton_lowercase_succeed(self):

        order = FuturesTransaction(
            date=20190308,
            symbol="es",
            action="long",
            quantity=1,
            point=2722.75,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("LONG", order.action)
        self.assertEqual(1, order.quantity)
        self.assertEqual(2722.75, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

        order = FuturesTransaction(
            date=20190308,
            symbol="es",
            action="short",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("SHORT", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

        order = FuturesTransaction(
            date=20190308,
            symbol="es",
            action="increase",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("INCREASE", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

        order = FuturesTransaction(
            date=20190308,
            symbol="es",
            action="decrease",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("DECREASE", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

        order = FuturesTransaction(
            date=20190308,
            symbol="es",
            action="close",
            quantity=10,
            point=2722,
            note="5SMA bounced off 20SMA",
        )

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("CLOSE", order.action)
        self.assertEqual(10, order.quantity)
        self.assertEqual(2722, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)

##############################################################################

    def test_new_transacton_invalid_date(self):
        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=0,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=-1,
                symbol="ES",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=2013,
                symbol="ES",
                action="LONG",
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
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="[]",
                action="LONG",
                quantity=1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="a123",
                action="LONG",
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
                action="SHORT",
                quantity=0,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="CLOSE",
                quantity=-1,
                point=2722.75,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="INCREASE",
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
                action="SHORT",
                quantity=1,
                point=0,
                note="5SMA bounced off 20SMA",
            )

        with self.assertRaises(ValueError):
            FuturesTransaction(
                date=20190308,
                symbol="CL",
                action="CLOSE",
                quantity=1,
                point=-2722.75,
                note="5SMA bounced off 20SMA",
            )

##############################################################################

    def test_entity_to_futures_transaction(self):
        order = entity_to_futures_transaction({
            "date": "20190308",
            "symbol": "ES",
            "action": "LONG",
            "quantity": "1",
            "point": "2722.75",
            "note": "5SMA bounced off 20SMA",
        })

        self.assertEqual(20190308, order.date)
        self.assertEqual("ES", order.symbol)
        self.assertEqual("LONG", order.action)
        self.assertEqual(1, order.quantity)
        self.assertEqual(2722.75, order.point)
        self.assertEqual("5SMA bounced off 20SMA", order.note)
        self.assertNotEqual("", order.index)


##############################################################################
