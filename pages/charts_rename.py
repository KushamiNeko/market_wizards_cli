from typing import Dict, List
import re
import os
import helper
from terminal import TerminalColors
from pages.pages import Pages
from context import Context

##############################################################################


class ChartsRename(Pages):

    _actions = ["rename"]

    _date = ""

    def __init__(self, context: Context) -> None:
        super(ChartsRename, self).__init__(context)

##############################################################################

    def _process_command(self, command: str) -> None:
        if command == "rename":
            while True:
                try:
                    self._command_rename()
                    stop = helper.color_input(
                        helper.hex_to_rgb(TerminalColors.paper_amber_300),
                        "Finish your jobs? (y/n)")
                    if stop in ("y", "yes"):
                        break
                    elif stop in ("", "n", "no"):
                        continue
                except ValueError as err:
                    helper.color_print(
                        helper.hex_to_rgb(TerminalColors.paper_red_500),
                        str(err))

##############################################################################

    def _command_rename(self) -> None:
        new_date = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the date:")

        if new_date:
            match = re.match(r"\d{8}", new_date)
            if not match:
                raise ValueError("Invalid date")
            else:
                self._date = new_date
        else:
            if not self._date:
                raise ValueError("Invalid date")

        symbol = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the symbol:")

        match = re.match(r"[a-zA-Z]+", symbol)
        if not match:
            raise ValueError("Invalid symbol")

        symbol = symbol.upper()

        files = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the daily chart and the weekly chart files:")

        match = re.match(r"'([^']+)'\s*'([^']+)'", files)
        if len(match.groups()) < 2:
            raise ValueError("No files match")

        daily = match.group(1).strip()
        weekly = match.group(2).strip()

        if not os.path.exists(daily):
            raise ValueError("daily charts file does not exist")

        if not os.path.exists(weekly):
            raise ValueError("weekly charts file does not exist")

        print()

        helper.color_print(
            helper.hex_to_rgb(TerminalColors.paper_purple_300),
            "Date: {}\nSymbol: {}\n".format(self._date, symbol) +
            "Daily Chart File: {}\nWeekly Chart File: {}\n".format(
                daily, weekly))

        daily_new = os.path.join(
            os.path.dirname(daily), "{}_{}_D.png".format(self._date, symbol))

        weekly_new = os.path.join(
            os.path.dirname(weekly), "{}_{}_W.png".format(self._date, symbol))

        helper.color_print(
            helper.hex_to_rgb(TerminalColors.paper_light_blue_300),
            "rename: {} -> {}".format(daily, daily_new))

        os.renames(daily, daily_new)

        helper.color_print(
            helper.hex_to_rgb(TerminalColors.paper_light_blue_300),
            "rename: {} -> {}".format(weekly, weekly_new))

        os.renames(weekly, weekly_new)

        print()


##############################################################################
