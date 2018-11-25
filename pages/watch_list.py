import helper
from pages.pages import Pages
from terminal import TerminalColors

##############################################################################


class WatchList(Pages):

    actions = ["show", "add", "delete", "goto", "exit"]

    __width = 20
    __width_large = __width * 2
    __print_format = (
        "{m1: <6}" + "{m2: >{width}}" + "{m3: >{width}}" + "{m4: >{width}}" +
        "{m5: >{width}}" + "{m6: >{width}}" + "{m7: >{note_width}}")

    def __init__(self, context, database):
        super(WatchList, self).__init__(context, database)

    def _process_command(self, command: str):
        print("watch_list process")
        print(self.actions)
        if command == "show":
            print("show")
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
                width=self.__width,
                note_width=self.__width_large))

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
                    width=self.__width,
                    note_width=self.__width_large))


##############################################################################
