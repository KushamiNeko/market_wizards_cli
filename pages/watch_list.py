import helper
from pages.pages import Pages
from context import Context
from terminal import TerminalColors
from typing import Dict, List
from data import watchlist

##############################################################################


class WatchList(Pages):

    _actions = [
        "show", "search", "calculate", "add", "edit", "delete", "clear all",
        "home", "exit"
    ]

    _width = 20
    _width_large = _width * 2
    _print_format = (
        "    " + "{symbol: <6}" + "{price: >{width}}" + "{status: >{width}}" +
        "{grs: >{width}}" + "{rs: >{width}}" + "{value: >{width}}" +
        "{earnings: >{width}}" + "{note: >{note_width}}")

    _database = "--watch-list--"

    def __init__(self, context: Context):
        super(WatchList, self).__init__(context)

##############################################################################

    def _process_command(self, command: str):
        if command == "show":
            self._command_show()

        if command == "search":
            self._command_search()

        if command == "add":
            self._command_add()

        if command == "edit":
            self._command_edit()

        if command == "delete":
            self._command_delete()

        if command == "clear all":
            self._command_clear_all()

##############################################################################

    def _command_show(self):
        entities = self.context.database.find(self._database, self.context.uid,
                                              {})

        if len(entities) == 0:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
                "No Entities Match The Queries")
            return

        self._show_entities(entities)

##############################################################################

    def _show_entities(self, entities: List):

        if len(entities) == 0:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
                "No Entities Match The Queries")
            return

        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_light_blue_300),
            self._print_format.format(
                symbol="Symbol",
                price="Price",
                status="Status",
                grs="GroupRS",
                rs="RS",
                value="Value",
                earnings="EarningsDate",
                note="Note",
                width=self._width,
                note_width=self._width_large))

        entities.sort(key=lambda entity: self._sort_entity(entity))

        for entity in entities:

            color = TerminalColors.hex_to_rgb(TerminalColors.paper_grey_400)

            if entity["flag"]:
                color = TerminalColors.hex_to_rgb(
                    TerminalColors.paper_green_200)

            if entity["status"].lower() == "portfolio":
                if entity["flag"]:
                    color = TerminalColors.hex_to_rgb(
                        TerminalColors.paper_indigo_200)
                else:
                    color = TerminalColors.hex_to_rgb(
                        TerminalColors.paper_indigo_300)

            if entity["status"].lower() == "earnings":
                if entity["flag"]:
                    color = TerminalColors.hex_to_rgb(
                        TerminalColors.paper_amber_200)
                else:
                    color = TerminalColors.hex_to_rgb(
                        TerminalColors.paper_amber_300)

            if entity.get("earnings", "") != "":
                if helper.days_to_date(entity["earnings"]) < 7:
                    color = TerminalColors.hex_to_rgb(
                        TerminalColors.paper_pink_200)

            helper.color_print(
                color,
                self._print_format.format(
                    symbol=entity.get("symbol", ""),
                    price=entity.get("price", ""),
                    status=entity.get("status", ""),
                    grs=entity.get("grs", ""),
                    rs=entity.get("rs", ""),
                    value=entity.get("value", ""),
                    earnings=entity.get("earnings", ""),
                    note=entity.get("note", ""),
                    width=self._width,
                    note_width=self._width_large))

##############################################################################

    def _sort_entity(self, entity: Dict):

        multiplier = 100

        points = 0

        points += self._sort_entity_status(entity, 1024 * multiplier)
        points += self._sort_entity_flag(entity, 256 * multiplier)
        points += self._sort_entity_rank(entity, "grs", 64 * multiplier)
        points += self._sort_entity_rank(entity, "rs", 16 * multiplier)
        points += self._sort_entity_rank(entity, "value", 4 * multiplier)

        return points

##############################################################################

    def _sort_entity_status(self, entity: Dict, multiplier: int):
        if entity["status"].lower() == "earnings":
            return 1 * multiplier
        if entity["status"].lower() == "portfolio":
            return 2 * multiplier
        if entity["status"].lower() == "charging":
            return 3 * multiplier
        if entity["status"].lower() == "launched":
            return 4 * multiplier

##############################################################################

    def _sort_entity_flag(self, entity: Dict, multiplier: int):
        if entity["flag"]:
            return 1 * multiplier
        else:
            return 2 * multiplier

##############################################################################

    def _sort_entity_rank(self, entity: Dict, rank: str, multiplier: int):
        if entity[rank] == "A":
            return 1 * multiplier
        if entity[rank] == "B":
            return 2 * multiplier
        if entity[rank] == "C":
            return 3 * multiplier
        if entity[rank] == "D":
            return 4 * multiplier

##############################################################################

    def _command_search(self):
        try:
            q = helper.key_value_input(
                TerminalColors.hex_to_rgb(TerminalColors.paper_orange_200),
                "What do you want to search? ")
        except ValueError as e:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
                "error: {}".format(e))
            return

        entities = self.context.database.find(self._database, self.context.uid,
                                              q)

        self._show_entities(entities)

##############################################################################

    def _command_add(self):
        try:
            q = helper.key_value_input(
                TerminalColors.hex_to_rgb(TerminalColors.paper_orange_200),
                "Please enter your entity " +
                "(symbol price status earnings grs rs value flag note) ")

            entity = watchlist.check_item(q)
        except ValueError as e:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
                "error: {}".format(e))
            return

        self.context.database.insert_one(self._database, self.context.uid,
                                         entity)

##############################################################################

    def _command_edit(self):
        pass

##############################################################################

    def _command_delete(self):
        try:
            q = helper.key_value_input(
                TerminalColors.hex_to_rgb(TerminalColors.paper_orange_200),
                "What do you want to delete? ")
        except ValueError as e:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
                "error: {}".format(e))
            return

        self.context.database.delete(self._database, self.context.uid, q)

##############################################################################

    def _command_clear_all(self):
        self.context.database.delete(self._database, self.context.uid, {})


##############################################################################
