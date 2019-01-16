import unittest
import datetime

from data.watch_list import WatchListItem

##############################################################################


class TestWatchListItem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

##############################################################################

    def test_check_necessary_keys_succeed(self):
        entity = {
            "symbol": "A",
            "op": "LONG",
            "status": "CHARGING",
        }

        item = WatchListItem(entity, check_necessary=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))
        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))
        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

##############################################################################

    def test_check_necessary_keys_miss(self):
        entity = {
            "op": "LONG",
            "status": "CHARGING",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_necessary=True)

        entity = {
            "symbol": "A",
            "status": "CHARGING",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_necessary=True)

        entity = {
            "symbol": "A",
            "op": "LONG",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_necessary=True)

##############################################################################

    def test_check_values_succeed_symbol(self):
        entity = {
            "symbol": "A",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))

        entity = {
            "symbol": "a",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))

        entity = {
            "symbol": " A ",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))

##############################################################################

    def test_check_values_invalid_symbol(self):
        entity = {
            "symbol": "",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "symbol": "123",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "symbol": ",[]",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "symbol": "123ABC[]",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_op(self):
        entity = {
            "op": "LONG",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

        entity = {
            "op": " LONG ",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

        entity = {
            "op": "SHORT",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

        entity = {
            "op": "long",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

        entity = {
            "op": "short",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

        entity = {
            "op": "L",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

        entity = {
            "op": "S",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

        entity = {
            "op": "l",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

        entity = {
            "op": "s",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))

##############################################################################

    def test_check_values_invalid_op(self):
        entity = {
            "op": "",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "op": "ABC",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "op": "abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "op": "123",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "op": "[],",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "op": "123[],ABC",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_status(self):
        entity = {
            "status": "CHARGING",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": " CHARGING ",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "REPAIRING",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "LAUNCHED",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "PORTFOLIO",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "charging",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "repairing",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "launched",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "portfolio",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "C",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "R",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "L",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "P",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "c",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "r",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "l",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

        entity = {
            "status": "p",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))

##############################################################################

    def test_check_values_invalid_status(self):
        entity = {
            "status": "",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "status": "ABC",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "status": "abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "status": "123",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "status": "[]",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "status": "123Abc[]",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_earnings(self):
        entity = {
            "earnings": "",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "20190110",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))

        entity = {
            "earnings": " 20190110 ",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))

        entity = {
            "earnings": "E20190110",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))

        entity = {
            "earnings": "20190110O",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))

        entity = {
            "earnings": "20190110C",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))

        entity = {
            "earnings": "e20190110",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))

        entity = {
            "earnings": "20190110o",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))

        entity = {
            "earnings": "20190110c",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))

##############################################################################

    def test_check_values_invalid_earnings(self):
        entity = {
            "earnings": "ABC",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "2019",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "20190110 O",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "E 20190110",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "20190110A",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "20190110a",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "B20190110",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "b20190110",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "[],",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "earnings": "aBc[],",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_price(self):
        entity = {
            "price": "",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "price": "100",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))

        entity = {
            "price": "100.0",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))

        entity = {
            "price": "100.0-105.0",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))

        entity = {
            "price": "100.0~105.0",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))

##############################################################################

    def test_check_values_invalid_price(self):
        entity = {
            "price": "-10.0",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "price": "ABC",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "price": "abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "price": "[]",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "price": "ABC[]123",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_stop(self):
        entity = {
            "stop": "",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "stop": "100",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))

        entity = {
            "stop": "100.0",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))

        entity = {
            "stop": "100.0-105.0",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))

        entity = {
            "stop": "100.0~105.0",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))

##############################################################################

    def test_check_values_invalid_stop(self):
        entity = {
            "stop": "-10.0",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "stop": "ABC",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "stop": "abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "stop": "[]",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "stop": "ABC[]123",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_note(self):
        entity = {
            "note": "HELLO",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))

        entity = {
            "note": "HELLO_WORLD",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))

        entity = {
            "note": "HELLO,WORLD",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))

        entity = {
            "note": " HELLO,WORLD ",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))

##############################################################################

    def test_check_values_invalid_note(self):
        entity = {
            "note": "HELLO WORLD",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_flag(self):
        entity = {
            "flag": " TRUE ",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "flag": "TRUE",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "flag": "true",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))

        entity = {
            "flag": "T",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))

        entity = {
            "flag": "t",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))

        entity = {
            "flag": "FALSE",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "flag": "false",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))

        entity = {
            "flag": "F",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))

        entity = {
            "flag": "f",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))

##############################################################################

    def test_check_values_invalid_flag(self):
        entity = {
            "flag": "ABC",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "flag": "abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "flag": "123",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "flag": "[],",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "flag": "123[],Abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_action(self):
        entity = {
            "action": " TRUE ",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "action": "TRUE",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "action": "true",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

        entity = {
            "action": "T",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

        entity = {
            "action": "t",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

        entity = {
            "action": "FALSE",
        }

        item = WatchListItem(entity, check_values=True)

        entity = {
            "action": "false",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

        entity = {
            "action": "F",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

        entity = {
            "action": "f",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

##############################################################################

    def test_check_values_invalid_action(self):
        entity = {
            "action": "ABC",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "action": "abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "action": "123",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "action": "[],",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

        entity = {
            "action": "123[],Abc",
        }

        with self.assertRaises(ValueError):
            WatchListItem(entity, check_values=True)

##############################################################################

    def test_check_values_succeed_01(self):
        entity = {
            "symbol": "A",
            "op": "LONG",
            "status": "CHARGING",
            "earnings": "20190110",
            "price": "100",
            "stop": "100",
            "note": "HELLO",
            "flag": "TRUE",
            "action": "FALSE",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))
        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))
        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))
        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))
        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))
        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))
        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))
        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))
        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

##############################################################################

    def test_check_values_succeed_02(self):
        entity = {
            "symbol": "A",
            "op": "SHORT",
            "status": "PORTFOLIO",
            "earnings": "E20190110",
            "price": "100-105",
            "stop": "95-97",
            "note": " HELLO",
            "flag": "T",
            "action": "f",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))
        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))
        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))
        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))
        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))
        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))
        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))
        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))
        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

##############################################################################

    def test_check_values_succeed_03(self):
        entity = {
            "symbol": "A",
            "op": " LONG",
            "status": "LAUNCHED",
            "earnings": "20190110C",
            "price": "100~105",
            "stop": "95~97",
            "note": "HELLO ",
            "flag": "true",
            "action": "false",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))
        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))
        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))
        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))
        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))
        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))
        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))
        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))
        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

##############################################################################

    def test_check_values_succeed_04(self):
        entity = {
            "symbol": "A",
            "op": "SHORT ",
            "status": "REPAIRING",
            "earnings": "20190110O",
            "price": "0",
            "stop": "0",
            "note": " HELLO  ",
            "flag": "TRUE ",
            "action": " FALSE",
        }

        item = WatchListItem(entity, check_values=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))
        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))
        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))
        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))
        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))
        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))
        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))
        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))
        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

##############################################################################

    def test_clean_keys_normal(self):
        entity = {
            "symbol": "A",
            "op": "LONG",
            "status": "CHARGING",
            "earnings": "20190110",
            "price": "100",
            "stop": "100",
            "note": "HELLO",
            "flag": "TRUE",
            "action": "TRUE",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(
            entity.get("symbol", ""), item.entity.get("symbol", ""))
        self.assertEqual(entity.get("op", ""), item.entity.get("op", ""))
        self.assertEqual(
            entity.get("status", ""), item.entity.get("status", ""))
        self.assertEqual(
            entity.get("earnings", ""), item.entity.get("earnings", ""))
        self.assertEqual(entity.get("price", ""), item.entity.get("price", ""))
        self.assertEqual(entity.get("stop", ""), item.entity.get("stop", ""))
        self.assertEqual(entity.get("note", ""), item.entity.get("note", ""))
        self.assertEqual(entity.get("flag", ""), item.entity.get("flag", ""))
        self.assertEqual(
            entity.get("action", ""), item.entity.get("action", ""))

##############################################################################

    def test_clean_keys_short(self):
        entity = {
            "sy": "A",
            "o": "LONG",
            "st": "CHARGING",
            "e": "20190110",
            "p": "100",
            "s": "100",
            "n": "HELLO",
            "f": "TRUE",
            "a": "TRUE",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(entity.get("sy", ""), item.entity.get("symbol", ""))
        self.assertEqual(entity.get("o", ""), item.entity.get("op", ""))
        self.assertEqual(entity.get("st", ""), item.entity.get("status", ""))
        self.assertEqual(entity.get("e", ""), item.entity.get("earnings", ""))
        self.assertEqual(entity.get("p", ""), item.entity.get("price", ""))
        self.assertEqual(entity.get("s", ""), item.entity.get("stop", ""))
        self.assertEqual(entity.get("n", ""), item.entity.get("note", ""))
        self.assertEqual(entity.get("f", ""), item.entity.get("flag", ""))
        self.assertEqual(entity.get("a", ""), item.entity.get("action", ""))

##############################################################################

    def test_clean_values_succeed_symbol(self):
        entity = {
            "symbol": "A",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("symbol", ""), "A")

        entity = {
            "symbol": "a",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("symbol", ""), "A")

        entity = {
            "symbol": " a ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("symbol", ""), "A")

##############################################################################

    def test_clean_values_succeed_op(self):
        entity = {
            "op": "LONG",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "LONG")

        entity = {
            "op": "long",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "LONG")

        entity = {
            "op": "L",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "LONG")

        entity = {
            "op": "l",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "LONG")

        entity = {
            "op": "SHORT",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "SHORT")

        entity = {
            "op": "short",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "SHORT")

        entity = {
            "op": "S",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "SHORT")

        entity = {
            "op": "s",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "SHORT")

        entity = {
            "op": " s ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("op", ""), "SHORT")

##############################################################################

    def test_clean_values_succeed_status(self):
        entity = {
            "status": "CHARGING",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "CHARGING")

        entity = {
            "status": "charging",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "CHARGING")

        entity = {
            "status": "C",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "CHARGING")

        entity = {
            "status": "c",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "CHARGING")

        entity = {
            "status": "LAUNCHED",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "LAUNCHED")

        entity = {
            "status": "launched",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "LAUNCHED")

        entity = {
            "status": "L",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "LAUNCHED")

        entity = {
            "status": "l",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "LAUNCHED")

        entity = {
            "status": "REPAIRING",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "REPAIRING")

        entity = {
            "status": "repairing",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "REPAIRING")

        entity = {
            "status": "R",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "REPAIRING")

        entity = {
            "status": "r",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "REPAIRING")

        entity = {
            "status": "PORTFOLIO",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "PORTFOLIO")

        entity = {
            "status": "portfolio",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "PORTFOLIO")

        entity = {
            "status": "P",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "PORTFOLIO")

        entity = {
            "status": "p",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "PORTFOLIO")

        entity = {
            "status": " p ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("status", ""), "PORTFOLIO")

##############################################################################

    def test_clean_values_succeed_earnings(self):
        entity = {
            "earnings": "20190112",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("earnings", ""), "20190112")

        entity = {
            "earnings": "E20190112",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("earnings", ""), "E20190112")

        entity = {
            "earnings": "e20190112",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("earnings", ""), "E20190112")

        entity = {
            "earnings": "20190112O",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("earnings", ""), "20190112O")

        entity = {
            "earnings": "20190112o",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("earnings", ""), "20190112O")

        entity = {
            "earnings": "20190112C",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("earnings", ""), "20190112C")

        entity = {
            "earnings": "20190112c",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("earnings", ""), "20190112C")

        entity = {
            "earnings": " 20190112 ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("earnings", ""), "20190112")

##############################################################################

    def test_clean_values_succeed_price(self):
        entity = {
            "price": "100",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "100")

        entity = {
            "price": "100.0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "100.0")

        entity = {
            "price": "100-105",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "100-105")

        entity = {
            "price": "100.0-105.0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "100.0-105.0")

        entity = {
            "price": "100~105",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "100~105")

        entity = {
            "price": "100.0~105.0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "100.0~105.0")

        entity = {
            "price": " 100.0~105.0 ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "100.0~105.0")

        entity = {
            "price": "0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "")

        entity = {
            "price": "0.0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("price", ""), "")

##############################################################################

    def test_clean_values_succeed_stop(self):
        entity = {
            "stop": "100",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "100")

        entity = {
            "stop": "100.0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "100.0")

        entity = {
            "stop": "100-105",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "100-105")

        entity = {
            "stop": "100.0-105.0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "100.0-105.0")

        entity = {
            "stop": "100~105",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "100~105")

        entity = {
            "stop": "100.0~105.0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "100.0~105.0")

        entity = {
            "stop": " 100.0~105.0 ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "100.0~105.0")

        entity = {
            "stop": "0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "")

        entity = {
            "stop": "0.0",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("stop", ""), "")

##############################################################################

    def test_clean_values_succeed_note(self):
        entity = {
            "note": "LFVCP",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("note", ""), "LFVCP")

        entity = {
            "note": "lfvcp",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("note", ""), "LFVCP")

        entity = {
            "note": " lfvcp ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("note", ""), "LFVCP")

        entity = {
            "note": "LOW_PRICE",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("note", ""), "LOW PRICE")

        entity = {
            "note": "low_price",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("note", ""), "LOW PRICE")

##############################################################################

    def test_clean_values_succeed_flag(self):
        entity = {
            "flag": "TRUE",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "TRUE")

        entity = {
            "flag": "true",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "TRUE")

        entity = {
            "flag": "T",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "TRUE")

        entity = {
            "flag": "t",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "TRUE")

        entity = {
            "flag": "FALSE",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "FALSE")

        entity = {
            "flag": "false",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "FALSE")

        entity = {
            "flag": "F",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "FALSE")

        entity = {
            "flag": "f",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "FALSE")

        entity = {
            "flag": " f ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("flag", ""), "FALSE")

##############################################################################

    def test_clean_values_succeed_action(self):
        entity = {
            "action": "TRUE",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "TRUE")

        entity = {
            "action": "true",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "TRUE")

        entity = {
            "action": "T",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "TRUE")

        entity = {
            "action": "t",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "TRUE")

        entity = {
            "action": "FALSE",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "FALSE")

        entity = {
            "action": "false",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "FALSE")

        entity = {
            "action": "F",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "FALSE")

        entity = {
            "action": "f",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "FALSE")

        entity = {
            "action": " f ",
        }

        item = WatchListItem(entity, clean=True)

        self.assertEqual(item.entity.get("action", ""), "FALSE")

##############################################################################

    def teset_colorize(self):

        earnings_date_threshold = 7

        entity = {
            "symbol": "A",
            "op": "LONG ",
            "status": "REPAIRING",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": " FALSE",
            "action": " FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_general)

        entity = {
            "symbol": "A",
            "op": "SHORT",
            "status": "CHARGING",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": " FALSE",
            "action": " FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_general)

        entity = {
            "symbol": "A",
            "op": "LONG",
            "status": "LAUNCHED",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": " FALSE",
            "action": " FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_general)

        entity = {
            "symbol": "A",
            "op": "LONG",
            "status": "PORTFOLIO",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": " FALSE",
            "action": " FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_portfolio)

        entity = {
            "symbol": "A",
            "op": "LONG ",
            "status": "REPAIRING",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": " TRUE",
            "action": " FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_flag)

        entity = {
            "symbol": "A",
            "op": "LONG ",
            "status": "REPAIRING",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": " FALSE",
            "action": " TRUE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_action)

        entity = {
            "symbol": "A",
            "op": "LONG ",
            "status": "REPAIRING",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": " TRUE",
            "action": " TRUE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_action)

        entity = {
            "symbol": "A",
            "op": "LONG ",
            "status": "PORTFOLIO",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": "TRUE",
            "action": " FLASE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_flag)

        entity = {
            "symbol": "A",
            "op": "LONG ",
            "status": "PORTFOLIO",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": "FALSE",
            "action": " TRUE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_action)

        entity = {
            "symbol": "A",
            "op": "LONG ",
            "status": "PORTFOLIO",
            "earnings": "21190110",
            "price": "0",
            "stop": "0",
            "note": "HELLO",
            "flag": "TRUE",
            "action": " TRUE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_action)

        entity = {
            "symbol":
            "A",
            "op":
            "LONG ",
            "status":
            "REPAIRING",
            "earnings":
            "{}".format(
                int(datetime.datetime.now().strftime("%Y%m%d")) +
                earnings_date_threshold),
            "price":
            "0",
            "stop":
            "0",
            "note":
            "HELLO",
            "flag":
            "FALSE",
            "action":
            "FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_earnings)

        entity = {
            "symbol":
            "A",
            "op":
            "LONG ",
            "status":
            "CHARGING",
            "earnings":
            "{}".format(
                int(datetime.datetime.now().strftime("%Y%m%d")) +
                earnings_date_threshold),
            "price":
            "0",
            "stop":
            "0",
            "note":
            "HELLO",
            "flag":
            "FALSE",
            "action":
            "FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_earnings)

        entity = {
            "symbol":
            "A",
            "op":
            "LONG ",
            "status":
            "LAUNCHED",
            "earnings":
            "{}".format(
                int(datetime.datetime.now().strftime("%Y%m%d")) +
                earnings_date_threshold),
            "price":
            "0",
            "stop":
            "0",
            "note":
            "HELLO",
            "flag":
            "FALSE",
            "action":
            "FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_earnings)

        entity = {
            "symbol":
            "A",
            "op":
            "LONG ",
            "status":
            "PORTFOLIO",
            "earnings":
            "{}".format(
                int(datetime.datetime.now().strftime("%Y%m%d")) +
                earnings_date_threshold),
            "price":
            "0",
            "stop":
            "0",
            "note":
            "HELLO",
            "flag":
            "FALSE",
            "action":
            "FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_earnings)

        entity = {
            "symbol":
            "A",
            "op":
            "LONG ",
            "status":
            "PORTFOLIO",
            "earnings":
            "{}".format(
                int(datetime.datetime.now().strftime("%Y%m%d")) +
                earnings_date_threshold),
            "price":
            "0",
            "stop":
            "0",
            "note":
            "HELLO",
            "flag":
            "TRUE",
            "action":
            "FALSE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_earnings)

        entity = {
            "symbol":
            "A",
            "op":
            "LONG ",
            "status":
            "PORTFOLIO",
            "earnings":
            "{}".format(
                int(datetime.datetime.now().strftime("%Y%m%d")) +
                earnings_date_threshold),
            "price":
            "0",
            "stop":
            "0",
            "note":
            "HELLO",
            "flag":
            "FLASE",
            "action":
            "TRUE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_earnings)

        entity = {
            "symbol":
            "A",
            "op":
            "LONG ",
            "status":
            "PORTFOLIO",
            "earnings":
            "{}".format(
                int(datetime.datetime.now().strftime("%Y%m%d")) +
                earnings_date_threshold),
            "price":
            "0",
            "stop":
            "0",
            "note":
            "HELLO",
            "flag":
            "TRUE",
            "action":
            "TRUE",
        }

        item = WatchListItem(entity, clean=True, colorize=True)

        self.assertTupleEqual(item.color, item._color_earnings)


##############################################################################

if __name__ == '__main__':
    unittest.main(verbosity=2)

##############################################################################
