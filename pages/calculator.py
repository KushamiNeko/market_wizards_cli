import helper
from pages.pages import Pages
from context import Context
from terminal import TerminalColors
import re

##############################################################################


class Calculator(Pages):

    _actions = ["stop", "profit"]

    def __init__(self, context: Context):
        super(Calculator, self).__init__(context)

##############################################################################

    def _process_command(self, command: str):
        if command == "stop":
            self._command_stop()
        if command == "profit":
            self._command_profit()

##############################################################################

    def _command_stop(self):
        try:
            q = helper.key_value_input(
                helper.hex_to_rgb(TerminalColors.paper_orange_200),
                "What is your price ? ")
        except ValueError as e:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500),
                "error: {}".format(e))
            return

        if "price" not in q:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500),
                "No price value")
        else:
            value = q["price"]
            if re.match(r"[0-9.]+", value):
                price = float(value)

                for i in range(-1, -9, -1):
                    percent = float(i) / 100.0

                    color = helper.hex_to_rgb(TerminalColors.paper_grey_300)
                    helper.color_print(
                        color, "Stop {0: >2}%: {1: >4,.4f} $".format(
                            i, price * (1.0 + percent)))

            else:
                helper.color_print(
                    helper.hex_to_rgb(TerminalColors.paper_red_500),
                    "invalid price")
                return

##############################################################################

    def _command_profit(self):
        try:
            q = helper.key_value_input(
                helper.hex_to_rgb(TerminalColors.paper_orange_200),
                "What is your price? ")
        except ValueError as e:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500),
                "error: {}".format(e))
            return

        if "price" not in q:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500),
                "No price value")
        else:
            value = q["price"]
            if re.match(r"[0-9.]+", value):
                price = float(value)

                for i in range(1, 36):
                    percent = float(i) / 100.0

                    color = helper.hex_to_rgb(TerminalColors.paper_grey_300)
                    helper.color_print(
                        color, "Profit {0: >3}%: {1: >4,.4f} $".format(
                            i, price * (1.0 + percent)))

            else:
                helper.color_print(
                    helper.hex_to_rgb(TerminalColors.paper_red_500),
                    "invalid price")
                return


##############################################################################
