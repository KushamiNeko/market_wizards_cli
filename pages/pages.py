from context import Context
import helper
from terminal import TerminalColors

##############################################################################


class Pages():

    context = None
    database = None

    _actions = ["home", "exit"]

    def __init__(self, context: Context):
        self.context = context

##############################################################################

    def main_loop(self):
        while True:
            command = helper.color_input(
                TerminalColors.hex_to_rgb(TerminalColors.paper_teal_300),
                "Command ({}): ".format(" ".join(self._actions)))

            if command not in self._actions:
                self._unknown_command()
                continue

            if command == "home":
                self._command_home()
                break

            if command == "exit":
                self._command_exit()

            self._process_command(command)

##############################################################################

    def _process_command(self, command: str):
        print("Pages Process Command should be overwrited")
        assert False
        pass

##############################################################################

    def _unknown_command(self):
        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
            "Unknown Command")

##############################################################################

    def _command_home(self):
        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_amber_300),
            "Going back to the home page...")

##############################################################################

    def _command_exit(self):
        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_amber_300),
            "Thank you for using Market Wizards!!!")
        exit(0)


##############################################################################
