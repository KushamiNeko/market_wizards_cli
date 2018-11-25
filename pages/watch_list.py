import helper
from pages.pages import Pages
from terminal import TerminalColors
from typing import Dict

##############################################################################


class WatchList(Pages):

    actions = ["show", "search", "add", "edit", "delete", "goto", "exit"]

    __width = 20
    __width_large = __width * 3
    __print_format = ("    " + "{m1: <6}" + "{m2: >{width}}" + "{m3: >{width}}"
                      + "{m4: >{width}}" + "{m5: >{width}}" + "{m6: >{width}}" +
                      "{m7: >{note_width}}")

    def __init__(self, context, database):
        super(WatchList, self).__init__(context, database)

    def _process_command(self, command: str):
        if command == "show":
            self.__command_show()

    def __command_show(self):
        entities = self.database.find("--watch-list--", self.context.uid, {})

        if len(entities) == 0:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
                "No Entities Match The Queries\n")
            return

        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_light_blue_300),
            self.__print_format.format(
                m1="Symbol",
                m2="Price",
                m3="Status",
                m4="Group RS",
                m5="RS",
                m6="Fundamentals",
                m7="Note",
                # m8="Flag",
                width=self.__width,
                note_width=self.__width_large))

        entities.sort(key=lambda entity: self._sort_entity(entity, {}))

        for entity in entities:
            helper.color_print(
                TerminalColors.hex_to_rgb(TerminalColors.paper_blue_grey_100),
                self.__print_format.format(
                    m1=entity["symbol"],
                    m2=entity["price"],
                    m3=entity["status"],
                    m4=entity["grs"],
                    m5=entity["rs"],
                    m6=entity["fundamentals"],
                    m7=entity["note"],
                    # m8=entity["flag"],
                    width=self.__width,
                    note_width=self.__width_large))

    def _sort_entity(self, entity: Dict, weights: Dict):

        points = 0

        points += self._sort_entity_status(entity, 100)
        points += self._sort_entity_flag(entity, 50)
        points += self._sort_entity_rank(entity, "grs", 20)
        points += self._sort_entity_rank(entity, "rs", 10)
        points += self._sort_entity_rank(entity, "fundamentals", 5)

        return points

    def _sort_entity_status(self, entity: Dict, multiplier: int):
        if entity["status"].lower() == "earnings":
            return 1 * multiplier
        if entity["status"].lower() == "portfolio":
            return 2 * multiplier
        if entity["status"].lower() == "charging":
            return 3 * multiplier
        if entity["status"].lower() == "launched":
            return 4 * multiplier

    def _sort_entity_flag(self, entity: Dict, multiplier: int):
        if entity["flag"]:
            return 1 * multiplier
        else:
            return 2 * multiplier

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
