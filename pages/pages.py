from context import Context
import helper
from typing import List
import config

##############################################################################


class Pages():

    context: Context = None

    _base_actions: List[str] = [
        "back",
        "exit",
    ]
    _actions: List[str] = []

    def __init__(self, context: Context) -> None:
        self.context = context
        for action in self._base_actions:
            if action not in self._actions:
                self._actions.append(action)

##############################################################################

    def main_loop(self) -> None:
        while True:
            command = helper.color_input(
                config.COLOR_COMMAND, "Command ({}): ".format(" ".join(
                    map(lambda x: "'{}'".format(x), self._actions))))

            command = command.strip()

            if command not in self._actions:
                self._unknown_command()
                continue

            if command == "back":
                self._command_back()
                break

            if command == "exit":
                self._command_exit()

            self._process_command(command)

##############################################################################

    def _process_command(self, command: str) -> None:
        print("Pages Process Command should be overwrited")
        assert False
        pass

##############################################################################

    def _unknown_command(self) -> None:
        helper.color_print(config.COLOR_WARNINGS, "Unknown Command")

##############################################################################

    def _command_back(self) -> None:
        helper.color_print(config.COLOR_INFO,
                           "Going back to the previous page...")

##############################################################################

    def _command_exit(self) -> None:
        helper.color_print(config.COLOR_INFO,
                           "Thank you for using Market Wizards!!!")
        exit(0)


##############################################################################
