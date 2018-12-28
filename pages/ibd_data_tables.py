from typing import Set, List
import re
import os
import config
import helper
from terminal import TerminalColors
from pages.pages import Pages
from context import Context

##############################################################################


class IBDDataTablesParser(Pages):

    _actions = ["list", "csv"]

    _path = ""

    def __init__(self, context: Context) -> None:
        super(IBDDataTablesParser, self).__init__(context)

##############################################################################

    def _process_command(self, command: str) -> None:

        if command == "list":
            self._command_list()

        if command == "csv":
            self._command_csv()

##############################################################################

    def _command_list(self) -> None:
        self._generate_list("\n")

##############################################################################

    def _command_csv(self) -> None:
        self._generate_list(",")

##############################################################################

    def _generate_list(self, separator: str) -> None:
        symbols = self._parse_html()

        helper.color_print(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "\nIBD Stocks Lists: {} stocks\n".format(len(symbols)))

        helper.color_print(config.COLOR_WHITE, separator.join(symbols))

##############################################################################

    def _parse_html(self) -> Set[str]:
        path = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the folder containing ibd data tabels html files: ")

        path = path.replace("'", "").strip()
        if not os.path.exists(path):
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500),
                "Path does not exist: {}".format(path))
            return set()

        symbols = set()

        for f in os.listdir(path):

            if f == "":
                continue

            with open(os.path.join(path, f), "r") as text:
                content = text.read()
                match = re.finditer(r"<(?:td|TD)>\s*([A-Z]+)\s*</(?:td|TD)>",
                                    content, re.DOTALL)

                for m in match:
                    if not m:
                        continue
                    symbols.add(m.group(1))

        return symbols


##############################################################################
