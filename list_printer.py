from typing import List

import config
import helper
from terminal import TerminalColors

##############################################################################


class ListPrinter():
    def __init__(self):
        pass

##############################################################################

    @classmethod
    def _generate_list(cls, stocks_list: List[str], separator: str) -> None:

        loop = (len(stocks_list) // 500) + 1

        for i in range(loop):
            start = i * 500
            end = (i + 1) * 500
            if i != (loop - 1):
                symbols = stocks_list[start:end]
            else:
                symbols = stocks_list[start:]

            message = "\n{} STOCKS\n"

            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_amber_300),
                message.format(len(symbols)))

            helper.color_print(config.COLOR_WHITE, separator.join(symbols))

##############################################################################

    @classmethod
    def print_csv(cls, stocks_list: List[str]):
        cls._generate_list(stocks_list, ",")

##############################################################################

    @classmethod
    def print_list(cls, stocks_list: List[str]):
        cls._generate_list(stocks_list, "\n")


##############################################################################
