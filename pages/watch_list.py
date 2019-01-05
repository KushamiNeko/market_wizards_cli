import helper
from terminal import TerminalColors
from pages.pages import Pages
from pages.helper import HelperPrintList
from pages.calculator import Calculator
from context import Context
from typing import Dict, List, Set
from data import watchlist
import config

##############################################################################


class WatchList(Pages, HelperPrintList):

    _actions = [
        "calc",
        "show",
        "find",
        "add",
        "edit",
        "delete",
        "clear all",
        "print csv",
        "print list",
    ]

    _width = 8
    _width_l = 12
    _width_xl = 36
    # _print_format = (
    # "  " + "{symbol: <6}" + "{price: >{width}}" + "{op: >{width}}" +
    # "{status: >{width_l}}" + "{earnings: >{width_l}}" + "{grs: >{width}}" +
    # "{rs: >{width}}" + "{acc: >{width}}" + "{eps: >{width}}" +
    # "{smr: >{width}}" + "{comp: >{width}}" + "{sctr: >{width}}" +
    # "{note: >{width_xl}}")

    _print_format = "".join([
        "  ",
        "{symbol: <6}",
        "{op: >{width}}",
        "{status: >{width_l}}",
        "{earnings: >{width_l}}",
        "{price: >{width_l}}",
        "{stop: >{width_l}}",
        "{loss: >{width_l}}",
        "{note: >{width_xl}}",
        "{grs: >{width}}",
        "{rs: >{width}}",
        "{acc: >{width}}",
        "{sctr: >{width}}",
        "{eps: >{width}}",
        "{smr: >{width}}",
        "{comp: >{width}}",
    ])

    _data_lables = [
        "SYMBOL",
        "OP",
        "STATUS",
        "EARNINGS",
        "PRICE",
        "STOP",
        "LOSS",
        "NOTE",
        "GRS",
        "RS",
        "ACC",
        "SCTR",
        "EPS",
        "SMR",
        "COMP",
        "FLAG",
    ]

    _database = "--watch-list--"

    _color_items_label = config.COLOR_INFO

    _color_items_sub_label = helper.hex_to_rgb(TerminalColors.paper_blue_300)

    _color_items_earnings = config.COLOR_WARNINGS

    _color_items_portfolio = helper.hex_to_rgb(TerminalColors.paper_purple_200)

    _color_items_portfolio_flag = helper.hex_to_rgb(
        TerminalColors.paper_purple_300)

    _color_items_flag = helper.hex_to_rgb(TerminalColors.paper_light_green_200)

    _color_items_general = helper.hex_to_rgb(TerminalColors.paper_grey_300)

    def __init__(self, context: Context) -> None:
        super(WatchList, self).__init__(context)

##############################################################################

    def _process_command(self, command: str) -> None:
        if command == "calc":
            calculator = Calculator(self.context)
            calculator.main_loop()

        if command == "show":
            self._command_show()

        if command == "find":
            self._command_find()

        # if command == "monitor":
        # self._command_monitor()

        if command == "add":
            self._command_add()

        if command == "edit":
            self._command_edit()

        if command == "delete":
            self._command_delete()

        if command == "clear all":
            self._command_clear_all()

        if command == "print csv":
            self._command_print_csv()

        if command == "print list":
            self._command_print_list()

##############################################################################

    def _command_show(self) -> None:
        entities = self.context.database.find(self._database, self.context.uid,
                                              {})

        if len(entities) == 0:
            helper.color_print(config.COLOR_WARNINGS,
                               "No Entities Match The Queries")
            return

        self._show_entities(entities)

##############################################################################

    def _generate_list(self, separator: str) -> None:
        entities = self.context.database.find(self._database, self.context.uid,
                                              {})

        if len(entities) == 0:
            helper.color_print(config.COLOR_WARNINGS,
                               "No Entities Match The Queries")
            return

        symbols_l: Set = set()
        symbols_s: Set = set()

        for entity in entities:
            symbol = entity.get("symbol", "")
            op = entity.get("op", "").lower()
            if symbol and op:
                if op == "long":
                    symbols_l.add(symbol)
                elif op == "short":
                    symbols_s.add(symbol)

        if (len(symbols_l) + len(symbols_s)) != len(entities):
            helper.color_print(
                config.COLOR_WARNINGS,
                "CSV list missing symbols due to empty symbol or op" + "\n" +
                "symbols: {}, entities: {}".format(
                    len(symbols_l) + len(symbols_s), len(entities)))

        helper.color_print(
            self._color_items_label, "Watch List CSV LONG: {} stocks".format(
                len(symbols_l)))

        helper.color_print(self._color_items_general,
                           separator.join(symbols_l))

        helper.color_print(
            self._color_items_label, "Watch List CSV SHORT: {} stocks".format(
                len(symbols_s)))

        helper.color_print(self._color_items_general,
                           separator.join(symbols_s))

##############################################################################

    def _show_entities(self, entities: List) -> None:

        if len(entities) == 0:
            helper.color_print(config.COLOR_WARNINGS,
                               "No Entities Match The Queries")
            return

        helper.color_print(
            self._color_items_label,
            self._print_format.format(
                symbol="Symbol",
                op="Op",
                status="Status",
                earnings="Earnings",
                price="Price",
                stop="Stop",
                loss="Loss",
                note="Note",
                grs="GRS",
                rs="RS",
                acc="ACC",
                sctr="SCTR",
                eps="EPS",
                smr="SMR",
                comp="COMP",
                width=self._width,
                width_l=self._width_l,
                width_xl=self._width_xl))

        entities.sort(key=lambda entity: self._sort_entity(entity))

        for entity in entities:

            color = self._color_items_general

            if entity.get("flag", False):
                color = self._color_items_flag

            if entity.get("status", "").lower() == "portfolio":
                if entity.get("flag", False):
                    color = self._color_items_portfolio_flag
                else:
                    color = self._color_items_portfolio

            if entity.get("earnings", "") != "":
                if helper.days_to_date(entity.get("earnings", "")) < 7:
                    color = self._color_items_earnings

            helper.color_print(
                color,
                self._print_format.format(
                    symbol=entity.get("symbol", ""),
                    op=entity.get("op", ""),
                    status=entity.get("status", ""),
                    earnings=entity.get("earnings", ""),
                    price=entity.get("price", ""),
                    stop=entity.get("stop", ""),
                    loss=entity.get("loss", ""),
                    note=entity.get("note", ""),
                    grs=entity.get("grs", ""),
                    rs=entity.get("rs", ""),
                    acc=entity.get("acc", ""),
                    sctr=entity.get("sctr", ""),
                    eps=entity.get("eps", ""),
                    smr=entity.get("smr", ""),
                    comp=entity.get("comp", ""),
                    width=self._width,
                    width_l=self._width_l,
                    width_xl=self._width_xl))

        helper.color_print(
            self._color_items_sub_label, "  (NOTE: {}\n         {})".format(
                ", ".join([
                    "NUM%=DEPTH",
                    "W=WEEKS",
                    "LF=LOOKING FOR",
                    "B=BREAKING UP/DOWN",
                    "S=SUPPORT",
                    "R=RESISTANCE",
                    "MA=MOVING AVERAGE",
                ]), ", ".join([
                    "VC=VOLUME CONTRACTION",
                    "PC=PRICE CONTRACTION",
                    "VCP=VOLATILITY CONTRACTION PATTERN",
                    "OP=OPEN POINT",
                    "SP=STOP POINT",
                ])))

##############################################################################

    def _sort_entity(self, entity: Dict) -> int:

        multiplier = 100

        points = 0

        points += self._sort_entity_op(entity, (5**7) * multiplier)
        points += self._sort_entity_status(entity, (5**6) * multiplier)
        points += self._sort_entity_flag(entity, (5**5) * multiplier)
        points += self._sort_entity_rank(entity, "grs", (5**4) * multiplier)
        points += self._sort_entity_rank(entity, "rs", (5**3) * multiplier)
        points += self._sort_entity_rank(entity, "acc", (5**2) * multiplier)

        return points

##############################################################################

    def _sort_entity_status(self, entity: Dict, multiplier: int) -> int:
        value = entity.get("status", "")
        if value != "":
            value = value.lower()
        else:
            return 5 * multiplier

        if value == "portfolio":
            return 1 * multiplier
        if value == "charging":
            return 2 * multiplier
        if value == "launched":
            return 3 * multiplier
        if value == "repairing":
            return 4 * multiplier

        raise ValueError("_sort_entity_status should not reach this part")

##############################################################################

    def _sort_entity_op(self, entity: Dict, multiplier: int) -> int:
        value = entity.get("op", "")
        if value != "":
            value = value.lower()
        else:
            return 3 * multiplier

        if value == "long":
            return 1 * multiplier
        if value == "short":
            return 2 * multiplier

        print(entity)

        raise ValueError("_sort_entity_op should not reach this part")

##############################################################################

    def _sort_entity_flag(self, entity: Dict, multiplier: int) -> int:
        if entity.get("flag", False):
            return 1 * multiplier
        else:
            return 2 * multiplier

##############################################################################

    def _sort_entity_int(self,
                         entity: Dict,
                         label: str,
                         multiplier: int,
                         maximum: int = 100) -> int:

        value = entity.get(label, 0)
        return (maximum - value) * multiplier

##############################################################################

    def _sort_entity_rank(self, entity: Dict, rank: str,
                          multiplier: int) -> int:
        value = entity.get(rank, "")
        if value == "":
            return 6 * multiplier

        if value == "A":
            return 1 * multiplier
        if value == "B":
            return 2 * multiplier
        if value == "C":
            return 3 * multiplier
        if value == "D":
            return 4 * multiplier
        if value == "E":
            return 5 * multiplier

        raise ValueError("_sort_entity_rank should not reach this part")

##############################################################################

    def _command_find(self) -> None:
        try:
            q = helper.key_value_input(config.COLOR_INFO,
                                       "What do you want to search? ")
        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "error: {}".format(e))
            return

        q = watchlist.clean_entity(q)

        entities = self.context.database.find(self._database, self.context.uid,
                                              q)

        self._show_entities(entities)

##############################################################################

    def _command_add(self) -> None:
        try:
            q = helper.key_value_input(
                config.COLOR_INFO, "Please enter your entity " + "({})".format(
                    " ".join(self._data_lables)))

            watchlist.check_necessary_keys(q)
            entity = watchlist.check_values(q)

        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "error: {}".format(e))
            return

        old_entity = self.context.database.find_one(
            self._database, self.context.uid, {"symbol": entity["symbol"]})

        if old_entity is not None:
            helper.color_print(
                config.COLOR_WARNINGS,
                "symbol already exists: {}".format(entity["symbol"]))
            return

        self.context.database.insert_one(self._database, self.context.uid,
                                         entity)

##############################################################################

    def _command_edit(self) -> None:
        try:
            q = helper.key_value_input(
                config.COLOR_INFO, "Which entity do you want to replace? ")
        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "error: {}".format(e))
            return

        try:
            new_values = helper.key_value_input(
                config.COLOR_INFO, "Please enter your entity " + "({})".format(
                    " ".join(self._data_lables)))

            new_values = watchlist.check_values(new_values)
        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "error: {}".format(e))
            return

        q = watchlist.clean_entity(q)

        entity = self.context.database.find_one(self._database,
                                                self.context.uid, q)

        for k in new_values:
            entity[k] = new_values[k]

        self.context.database.replace_one(self._database, self.context.uid, q,
                                          entity)

##############################################################################

    def _command_delete(self) -> None:
        try:
            q = helper.key_value_input(config.COLOR_INFO,
                                       "What do you want to delete? ")
        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "error: {}".format(e))
            return

        q = watchlist.clean_entity(q)

        self.context.database.delete(self._database, self.context.uid, q)

##############################################################################

    def _command_clear_all(self) -> None:
        self.context.database.delete(self._database, self.context.uid, {})


##############################################################################
