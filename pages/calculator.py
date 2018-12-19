import helper
from pages.pages import Pages
from context import Context
import re
import config

##############################################################################


class Calculator(Pages):

    _actions = ["stop", "depth"]

    def __init__(self, context: Context) -> None:
        super(Calculator, self).__init__(context)

##############################################################################

    def _process_command(self, command: str) -> None:
        if command == "stop":
            self._command_stop()
        if command == "depth":
            self._command_depth()
        # if command == "profit":
        # self._command_profit()

##############################################################################

    def _command_stop(self) -> None:
        try:
            q = helper.key_value_input(config.COLOR_INFO,
                                       "What is the price ? ")
        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "error: {}".format(e))
            return

        if "price" not in q:
            helper.color_print(config.COLOR_WARNINGS, "No price value")
        else:
            value = q["price"]
            if re.match(r"[0-9.]+", value):
                price = float(value)

                for i in range(-1, -11, -1):
                    percent = float(i) / 100.0

                    color = config.COLOR_WHITE

                    if i <= -7:
                        color = config.COLOR_WARNINGS

                    helper.color_print(
                        color, "Stop {0: >2}%: {1: >4,.2f} $".format(
                            i, price * (1.0 + percent)))

            else:
                helper.color_print(config.COLOR_WARNINGS, "invalid price")
                return

##############################################################################

    def _command_profit(self) -> None:
        pass
        try:
            q = helper.key_value_input(config.COLOR_INFO,
                                       "What is the price? ")
        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "error: {}".format(e))
            return

        if "price" not in q:
            helper.color_print(config.COLOR_WARNINGS, "No price value")
        else:
            value = q["price"]
            if re.match(r"[0-9.]+", value):
                price = float(value)

                for i in range(1, 36):
                    percent = float(i) / 100.0

                    helper.color_print(
                        config.COLOR_WHITE,
                        "Profit {0: >3}%: {1: >4,.2f} $".format(
                            i, price * (1.0 + percent)))

            else:
                helper.color_print(config.COLOR_WARNINGS, "invalid price")
                return

##############################################################################

    def _command_depth(self) -> None:
        try:
            q = helper.key_value_input(
                config.COLOR_INFO,
                "Please enter the start price and the end price...")
        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "error: {}".format(e))
            return

        if "start" not in q and "s" not in q:
            helper.color_print(config.COLOR_WARNINGS, "No start price")
        elif "end" not in q and "e" not in q:
            helper.color_print(config.COLOR_WARNINGS, "No end price")
        else:
            start = q.get("start", q.get("s", ""))
            end = q.get("end", q.get("e", ""))

            if re.match(r"[0-9.]+", start) and re.match(r"[0-9.]+", end):
                start_price = float(start)
                end_price = float(end)

                depth = (end_price - start_price) / start_price

                helper.color_print(
                    config.COLOR_WHITE,
                    "Depth : {0: >3,.2f} %".format(depth * 100.0))

            else:
                helper.color_print(config.COLOR_WARNINGS, "invalid price")
                return


##############################################################################
