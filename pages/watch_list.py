import helper
from pages.pages import Pages
from context import Context
from terminal import TerminalColors
from typing import Dict, List

##############################################################################


class WatchList(Pages):

    _actions = [
        "show", "search", "add", "edit", "delete", "clear all", "home", "exit"
    ]

    _width = 20
    _width_large = _width * 3
    _print_format = ("    " + "{m1: <6}" + "{m2: >{width}}" + "{m3: >{width}}" +
                     "{m4: >{width}}" + "{m5: >{width}}" + "{m6: >{width}}" +
                     "{m7: >{note_width}}")

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
                m1="Symbol",
                m2="Price",
                m3="Status",
                m4="GroupRS",
                m5="RS",
                m6="Fundamentals",
                m7="Note",
                # m8="Flag",
                width=self._width,
                note_width=self._width_large))

        entities.sort(key=lambda entity: self._sort_entity(entity, {}))

        for entity in entities:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_blue_grey_100),
                self._print_format.format(
                    m1=entity["symbol"],
                    m2=entity["price"],
                    m3=entity["status"],
                    m4=entity["grs"],
                    m5=entity["rs"],
                    m6=entity["fundamentals"],
                    m7=entity["note"],
                    # m8=entity["flag"],
                    width=self._width,
                    note_width=self._width_large))

##############################################################################

    def _sort_entity(self, entity: Dict, weights: Dict):

        points = 0

        points += self._sort_entity_status(entity, 100)
        points += self._sort_entity_flag(entity, 50)
        points += self._sort_entity_rank(entity, "grs", 20)
        points += self._sort_entity_rank(entity, "rs", 10)
        points += self._sort_entity_rank(entity, "fundamentals", 5)

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
        q = helper.key_value_input(
            TerminalColors.hex_to_rgb(TerminalColors.paper_orange_200),
            "What do you want to search? ")

        entities = self.context.database.find(self._database, self.context.uid,
                                              q)

        self._show_entities(entities)

##############################################################################

    def _command_add(self):
        pass

##############################################################################

    def _command_edit(self):
        pass

##############################################################################

    def _command_delete(self):
        q = helper.key_value_input(
            TerminalColors.hex_to_rgb(TerminalColors.paper_orange_200),
            "What do you want to delete? ")

        if len(q) == 0:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
                "No Queries Dound")
            return

        self.context.database.delete(self._database, self.context.uid, q)

##############################################################################

    def _command_clear_all(self):
        self.context.database.delete(self._database, self.context.uid, {})


##############################################################################
