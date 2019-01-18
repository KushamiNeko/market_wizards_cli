from typing import Dict
import helper
from pages.pages import Pages
from context import Context
from data.watch_list import WatchListItem
import re
import config

##############################################################################


class Calculator():

    _actions = [
        "stop",
        "depth",
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
            q = helper.key_value_input(config.COLOR_INFO,
                                       "What are the PRICE and OP ? ")
        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

        query = WatchListItem(q, clean=True, check_values=True)

        if "price" not in query.entity:
            helper.color_print(config.COLOR_WARNINGS, "No price value")
            return
        if "op" not in query.entity:
            helper.color_print(config.COLOR_WARNINGS, "No op value")
            return

        price = float(query.entity.get("price", 0))
        op = query.entity.get("op", "")

        try:

            stops = self._process_stop(price, op)

            for i in stops:
                color = config.COLOR_WHITE
                if i <= -7:
                    color = config.COLOR_WARNINGS

                helper.color_print(
                    color, "Stop {0: >3}%: {1: >4,.2f} $".format(i, stops[i]))

        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

##############################################################################

    def _process_stop(self, price: float, op: str) -> Dict[int, float]:

        if price <= 0:
            raise ValueError("Price should be greater than 0")

        stops = {}

        for i in range(-1, -11, -1):
            percent = float(i) / 100.0

            if op == "LONG":
                stops[i] = price * (1.0 + percent)
            elif op == "SHORT":
                stops[i] = price * (1.0 - percent)
            else:
                raise ValueError("Invalid OP")

        return stops

##############################################################################

    def _command_depth(self) -> None:
        try:
            q = helper.key_value_input(
                config.COLOR_INFO,
                "Please enter the start price and the end price...")
        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

        if "start" not in q and "s" not in q:
            helper.color_print(config.COLOR_WARNINGS, "No start price")
        elif "end" not in q and "e" not in q:
            helper.color_print(config.COLOR_WARNINGS, "No end price")

        start = q.get("start", q.get("s", ""))
        end = q.get("end", q.get("e", ""))

        if not re.match(r"[0-9.]+", start) or not re.match(r"[0-9.]+", end):
            helper.color_print(config.COLOR_WARNINGS, "invalid price")
            return

        start_price = float(start)
        end_price = float(end)

        try:
            depth = self._process_depth(start_price, end_price)

            helper.color_print(config.COLOR_WHITE,
                               "Depth : {0: >3,.2f} %".format(depth * 100.0))
        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

##############################################################################

    def _process_depth(self, start: float, end: float) -> float:
        if start <= 0:
            raise ValueError("Start Price should be greater than 0")

        if end <= 0:
            raise ValueError("End Price should be greater than 0")

        return (end - start) / start


##############################################################################
