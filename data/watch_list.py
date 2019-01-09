from typing import Dict, Any
import re

from terminal import TerminalColors
import helper
import config

##############################################################################


class WatchListItem:

    _necessary_keys = [
        "symbol",
        "op",
        "status",
    ]

    _regex_symbol = r"^[A-Za-z]+$"
    _regex_op = r"^(?:long|short|l|s)$"
    _regex_status = r"^(?:portfolio|repairing|charging|launched|p|r|c|l)$"

    _regex_int = r"^[0-9]+$"
    _regex_float = r"^[0-9.]+$"
    _regex_bool = r"^(?:true|false|t|f)$"

    _regex_ranks = r"^[A-Ea-e]$"

    _regex_float_range = r"^[0-9.]+(?:[~-][0-9.]+)?$"

    _regex_date = r"^[Ee]?(\d{8})[OoCc]?$"

    _regex_book = {
        "symbol": _regex_symbol,
        "op": _regex_op,
        "status": _regex_status,
        "earnings": _regex_date,
        "price": _regex_float_range,
        "stop": _regex_float_range,
        "note": r"\S+",
        "grs": _regex_ranks,
        "rs": _regex_int,
        "acc": _regex_ranks,
        "comp": _regex_int,
        "eps": _regex_int,
        "smr": _regex_ranks,
        "flag": _regex_bool,
        "action": _regex_bool,
    }

    _short_keys = {
        "sy": "symbol",
        "st": "status",
        "o": "op",
        "e": "earnings",
        "p": "price",
        "s": "stop",
        "n": "note",
        "f": "flag",
        "a": "action",
    }

    _color_earnings = config.COLOR_WARNINGS

    _color_flag = helper.hex_to_rgb(TerminalColors.paper_blue_200)
    _color_action = helper.hex_to_rgb(TerminalColors.paper_green_300)

    _color_portfolio_flag = helper.hex_to_rgb(
        TerminalColors.paper_deep_purple_300)
    _color_portfolio = helper.hex_to_rgb(TerminalColors.paper_purple_300)

    _color_general = helper.hex_to_rgb(TerminalColors.paper_grey_300)

    _date_to_earnings_threshold = 14

    def __init__(self,
                 entity: Dict[str, str],
                 check_necessary: bool = False,
                 check_values: bool = False,
                 clean: bool = False,
                 colorize: bool = False):

        self.entity: Dict[str, str] = entity
        self.color = self._color_general

        if clean:
            self._clean_keys()
            self._clean_values()

        if check_necessary:
            self._check_necessary_keys()

        if check_values:
            self._check_values()

        if colorize:
            self._colorize()

##############################################################################

    def _check_necessary_keys(self) -> None:
        for key in self._necessary_keys:
            if key not in self.entity:
                raise ValueError("{} can not be empty".format(key))

##############################################################################

    def _check_values(self) -> None:

        for key in self.entity:
            value = str(self.entity[key]).strip().lower()

            if value == "":
                continue

            regex = self._regex_book.get(key, None)
            if not regex:
                continue

            match = re.match(regex, value, re.DOTALL)
            if not match:
                raise ValueError("invalid key value pair: {}={}".format(
                    key, value))

##############################################################################

    def _clean_keys(self) -> None:

        new_entity: Dict[str, str] = {}

        for key in self.entity:
            if key in self._short_keys:
                k = self._short_keys[key]
            else:
                k = key

            new_entity[k] = self.entity[key]

        self.entity = new_entity

##############################################################################

    def _clean_values(self) -> None:

        for key in self.entity:
            value = str(self.entity[key]).strip()

            if key == "op":
                if value == "l":
                    value = "long"
                elif value == "s":
                    value = "short"

            if key == "status":
                if value == "p":
                    value = "portfolio"
                if value == "r":
                    value = "repairing"
                if value == "c":
                    value = "charging"
                if value == "l":
                    value = "launched"

            if key == "price":
                if value == "0" or value == "0.0":
                    value = ""

            if key == "stop":
                if value == "0" or value == "0.0":
                    value = ""

            if key == "note":
                value = value.replace("_", " ", -1)

            if key == "flag":
                if value == "t":
                    value = "true"
                if value == "f":
                    value = "false"

            if key == "action":
                if value == "t":
                    value = "true"
                if value == "f":
                    value = "false"

            self.entity[key] = value.upper()

##############################################################################

    def _colorize(self) -> None:

        if str(self.entity.get("flag", "")).upper() == "TRUE":
            self.color = self._color_flag

        if self.entity.get("status", "") == "PORTFOLIO":
            if str(self.entity.get("flag", "")).upper() == "TRUE":
                self.color = self._color_portfolio_flag
            else:
                self.color = self._color_portfolio

        if str(self.entity.get("action", "")).upper() == "TRUE":
            self.color = self._color_action

        if str(self.entity.get("earnings", "")) != "":
            match = re.match(self._regex_date,
                             str(self.entity.get("earnings", "")))

            if match:
                date = int(match.group(1))

                if helper.days_to_date(
                        date) < self._date_to_earnings_threshold:
                    self.color = self._color_earnings


##############################################################################