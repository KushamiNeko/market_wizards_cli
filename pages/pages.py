# from context.context import Context
# from mongo.mongo import MongoInterface
import helper
from terminal import TerminalColors

##############################################################################


class Pages():

    context = None
    database = None

    actions = []

    def __init__(self, context, database):
        # def __init__(self, context: Context, database: MongoInterface):
        self.context = context
        self.database = database

        self._main_loop()

    def _main_loop(self):
        while True:
            command = helper.color_input(
                TerminalColors.hex_to_rgb(TerminalColors.paper_teal_300),
                "Command ({}): ".format(" ,".join(self.actions)))

            if command not in self.actions:
                self._unknown_command()
                continue

            if command == "filp":
                break

            if command == "exit":
                self._exit()

            self._process_command(command)

        # self.context.change_page(ContextPages.watch_list)

    def _process_command(self, command: str):
        print("Pages Process Command should be overwrited")
        assert (False)
        pass

    def _unknown_command(self):
        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
            "Unknown Command")

    def _exit(self):
        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_amber_300),
            "\nThank you for using Market Wizards\n")
        exit(0)


##############################################################################
