from typing import Dict
import helper
from pages.pages import Pages
from context import Context
from data.watch_list import WatchListItem
from data.cleaner import Cleaner
import re
import config

##############################################################################


class Calculator():

    _actions = [
        "stop",
        "depth",
        "retracement",
        "pivot",
    ]

    def __init__(self, context: Context) -> None:
        self.context = context

        self._page = Pages(self._actions)

        self._handlers = {
            "stop": self._command_stop,
            "depth": self._command_depth,
        }

##############################################################################

    def main_loop(self) -> None:
        self._page.main_loop(self._process_command)

##############################################################################

    def _process_command(self, command: str) -> None:
        handler = self._handlers.get(command, None)
        if handler:
            handler()

##############################################################################

    def _command_stop(self) -> None:
        try:
            raw_inputs = helper.key_value_input(config.COLOR_INFO,
                                                "What is the PRICE and OP ? ")

            cleaner = Cleaner(
                key_abbreviation={
                    "p": "price",
                    "o": "op",
                },
                value_abbreviation={
                    "op": {
                        "l": "LONG",
                        "s": "SHORT",
                    },
                },
                necessary_keys=[
                    "price",
                    "op",
                ],
                regex_book={
                    "price": r"^[0-9.]+$",
                    "op": r"^(?:long|short|l|s)$",
                })

            clean_inputs = cleaner.clean(raw_inputs)

            price = float(clean_inputs.get("price", 0))
            op = clean_inputs.get("op", "").upper()

            stops = self._process_stop(price, op)

            for i in stops:
                color = config.COLOR_WHITE
                if i <= -7:
                    color = config.COLOR_WARNINGS

                helper.color_print(
                    color, "Stop {0: >3}%: {1: >4,.2f} $".format(i, stops[i]))

        except ValueError as err:
            raise err

##############################################################################

    def _process_stop(self, price: float, op: str) -> Dict[int, float]:

        if price <= 0:
            raise ValueError("PRICE SHOULD BE GREATER THAN 0")

        stops = {}

        for i in range(-1, -11, -1):
            percent = float(i) / 100.0

            if op == "LONG":
                stops[i] = price * (1.0 + percent)
            elif op == "SHORT":
                stops[i] = price * (1.0 - percent)
            else:
                raise ValueError("INVALID OP")

        return stops

##############################################################################

    def _command_depth(self) -> None:
        try:
            raw_inputs = helper.key_value_input(
                config.COLOR_INFO,
                "Please enter the START PRICE and the END PRICE...")

            cleaner = Cleaner(
                key_abbreviation={
                    "s": "start",
                    "e": "end",
                },
                necessary_keys=[
                    "start",
                    "end",
                ],
                regex_book={
                    "start": r"^[0-9.]+$",
                    "end": r"^[0-9.]+$",
                })

            clean_inputs = cleaner.clean(raw_inputs)

            start = float(clean_inputs.get("start", ""))
            end = float(clean_inputs.get("end", ""))

            depth = self._process_depth(start, end)

            helper.color_print(config.COLOR_WHITE,
                               "Depth : {0: >3,.2f} %".format(depth * 100.0))

        except ValueError as err:
            raise err

##############################################################################

    def _process_depth(self, start: float, end: float) -> float:
        if start <= 0:
            raise ValueError("START PRICE SHOULD BE GREATER THAN 0")

        if end <= 0:
            raise ValueError("END PRICE SHOULD BE GREATER THAN 0")

        return (end - start) / start


##############################################################################
