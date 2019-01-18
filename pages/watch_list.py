import re
import os

import helper
from ibd_parser import IBDResearchParser
from ranker import MomentumRanker
from terminal import TerminalColors
from pages.pages import Pages
from list_printer import ListPrinter
from pages.calculator import Calculator
from context import Context
from typing import Dict, List, Set
from data.watch_list import WatchListItem
import config

##############################################################################


class WatchList():

    _actions = [
        "show",
        "find",
        "add",
        "edit",
        "delete",
        "ibd research",
        "clear all",
        "print csv",
        # "print list",
    ]

    _width = 8
    _width_l = 12
    _width_xl = 36

    _print_format = "".join([
        "  ",
        "{symbol: <6}",
        "{op: >{width}}",
        "{status: >{width_l}}",
        "{earnings: >{width_l}}",
        "{price: >{width_l}}",
        "{stop: >{width_l}}",
        # "{loss: >{width_l}}",
        "{grs: >{width}}",
        "{rs: >{width}}",
        "{acc: >{width}}",
        # "{sctr: >{width}}",
        "{eps: >{width}}",
        "{smr: >{width}}",
        "{comp: >{width}}",
        "{note: >{width_xl}}",
    ])

    _data_lables = [
        "SYMBOL",
        "OP",
        "STATUS",
        "EARNINGS",
        "PRICE",
        "STOP",
        # "LOSS",
        "GRS",
        "RS",
        "ACC",
        # "SCTR",
        "EPS",
        "SMR",
        "COMP",
        "FLAG",
        "NOTE",
    ]

    _database = "--watch-list--"

    def __init__(self, context: Context) -> None:
        self.context = context

        self._page = Pages(self._actions)

        self._handlers = {
            "show": self._command_show,
            "find": self._command_find,
            "add": self._command_add,
            "edit": self._command_edit,
            "delete": self._command_delete,
            "ibd research": self._command_ibd_research,
            "clear all": self._command_clear_all,
            "print csv": self._command_print_csv,
            # "print list": self._command_print_list,
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

    def _show_entities(self, entities: List) -> None:

        if len(entities) == 0:
            raise ValueError("No Entities Match The Queries")

        helper.color_print(
            config.COLOR_INFO,
            self._print_format.format(
                symbol="Symbol",
                op="Op",
                status="Status",
                earnings="Earnings",
                price="Price",
                stop="Stop",
                # loss="Loss",
                grs="GRS",
                rs="RS",
                acc="ACC",
                # sctr="SCTR",
                eps="EPS",
                smr="SMR",
                comp="COMP",
                note="Note",
                width=self._width,
                width_l=self._width_l,
                width_xl=self._width_xl))

        ranker = MomentumRanker()
        entities.sort(key=lambda entity: ranker.rank(entity))

        for entity in entities:
            item = WatchListItem(entity, colorize=True)

            helper.color_print(
                item.color,
                self._print_format.format(
                    symbol=entity.get("symbol", ""),
                    op=entity.get("op", ""),
                    status=entity.get("status", ""),
                    earnings=entity.get("earnings", ""),
                    price=entity.get("price", ""),
                    stop=entity.get("stop", ""),
                    # loss=entity.get("loss", ""),
                    grs=entity.get("grs", ""),
                    rs=entity.get("rs", ""),
                    acc=entity.get("acc", ""),
                    # sctr=entity.get("sctr", ""),
                    eps=entity.get("eps", ""),
                    smr=entity.get("smr", ""),
                    comp=entity.get("comp", ""),
                    note=entity.get("note", ""),
                    width=self._width,
                    width_l=self._width_l,
                    width_xl=self._width_xl))

##############################################################################

    def _command_show(self) -> None:
        entities = self._process_find({})

        try:
            self._show_entities(entities)

        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

##############################################################################

    def _command_find(self) -> None:
        try:
            q = helper.key_value_input(config.COLOR_INFO,
                                       "What do you want to search? ")

            entities = self._process_find(q)

            self._show_entities(entities)

        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

##############################################################################

    def _process_find(self,
                      query_entity: Dict[str, str]) -> List[Dict[str, str]]:

        query = WatchListItem(query_entity, clean=True, check_values=True)

        return self.context.database.find(self._database, self.context.uid,
                                          query.entity)

##############################################################################

    def _command_add(self) -> None:
        try:
            q = helper.key_value_input(
                config.COLOR_INFO, "Please enter your entity " + "({})".format(
                    " ".join(self._data_lables)))

            self._process_add(q)

        except ValueError as e:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(e))
            return

##############################################################################

    def _process_add(self, inputs_entity: Dict[str, str]) -> None:

        item = WatchListItem(
            inputs_entity, check_necessary=True, check_values=True, clean=True)

        entity = item.entity

        old_entity = self.context.database.find_one(
            self._database, self.context.uid, {"symbol": entity["symbol"]})

        if old_entity is not None:
            raise ValueError("Symbol already exists: {}".format(
                entity.get("symbol", "")))

        self.context.database.insert_one(self._database, self.context.uid,
                                         entity)

##############################################################################

    def _command_edit(self) -> None:
        try:
            q = helper.key_value_input(
                config.COLOR_INFO, "Which entity do you want to replace? ")

            new_properties = helper.key_value_input(
                config.COLOR_INFO, "Please enter your new properties " +
                "({})".format(" ".join(self._data_lables)))

            self._process_edit(q, new_properties)

        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

##############################################################################

    def _process_edit(self, query_entity: Dict[str, str],
                      properties_entity: Dict[str, str]) -> None:
        try:
            query = WatchListItem(query_entity, clean=True)
            properties = WatchListItem(
                properties_entity, check_values=True, clean=True)

        except ValueError as err:
            raise err

        entity = self.context.database.find_one(self._database,
                                                self.context.uid, query.entity)
        if not entity:
            raise ValueError("Query has no result: {}".format(query.entity))

        for k in properties.entity:
            entity[k] = properties.entity[k]

        self.context.database.replace_one(self._database, self.context.uid,
                                          query.entity, entity)

##############################################################################

    def _command_delete(self) -> None:
        try:
            q = helper.key_value_input(config.COLOR_INFO,
                                       "What do you want to delete? ")
            self._process_delete(q)

        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

##############################################################################

    def _process_delete(self, query_entity: Dict[str, str]) -> None:
        try:
            query = WatchListItem(query_entity, clean=True, check_values=True)
        except ValueError as err:
            raise err

        entity = self.context.database.find_one(self._database,
                                                self.context.uid, query.entity)
        if not entity:
            raise ValueError("Query has no result: {}".format(query.entity))

        self.context.database.delete(self._database, self.context.uid,
                                     query.entity)

##############################################################################

    def _command_ibd_research(self) -> None:
        path = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the folder containing ibd research html files: ")

        path = path.replace("'", "").strip()

        try:
            self._process_ibd_research(path)

        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))

##############################################################################

    def _process_ibd_research(self, path: str) -> None:

        if not os.path.exists(path):
            raise ValueError("path does not exist: {}".format(path))

        for f in os.listdir(path):
            filepath = os.path.join(path, f)

            parser = IBDResearchParser()
            parser.parse(filepath)

            q = {"symbol": parser.symbol}

            entity = self.context.database.find_one(self._database,
                                                    self.context.uid, q)

            if not entity:
                continue

            for k in parser.ibd_research:
                if k == "earnings":
                    if re.match(r"[CcOo]", entity.get("earnings", "")):
                        continue

                entity[k] = parser.ibd_research[k]

            self.context.database.replace_one(self._database, self.context.uid,
                                              q, entity)

##############################################################################

    def _command_clear_all(self) -> None:
        self.context.database.delete(self._database, self.context.uid, {})

##############################################################################

    def _command_print_csv(self) -> None:
        try:
            q = helper.key_value_input(config.COLOR_INFO,
                                       "What do you want to search? ")

            entities = self._process_find(q)
            symbols = self._get_symbols(entities)

            printer = ListPrinter()
            printer.print_csv(symbols)

        except ValueError as err:
            helper.color_print(config.COLOR_WARNINGS, "ERROR: {}".format(err))
            return

##############################################################################

    def _get_symbols(self, entities: List[Dict[str, str]]) -> List[str]:

        if len(entities) == 0:
            raise ValueError("No Entities Match The Queries")

        symbols = []

        for entity in entities:
            symbol = entity.get("symbol", "")
            if symbol != "":
                symbols.append(symbol)

        return symbols


##############################################################################
