from context import Context
import helper
from typing import List
import config

##############################################################################


class Pages():

    _base_actions: List[str] = [
        "back",
        "exit",
    ]

    def __init__(self, actions: List[str]) -> None:
        self._actions: List[str] = actions + self._base_actions

        self.change = False

##############################################################################

    def action_command(self) -> str:
        command = helper.color_input(
            config.COLOR_COMMAND, "Command ({}): ".format(" ".join(
                map(lambda x: "'{}'".format(x), self._actions))))

        command = command.strip()

        if command not in self._actions:
            self.command_unknow()
            raise ValueError("Unknow Command")

        return command

##############################################################################

    def process_command(self, command: str) -> None:
        responses = {
            "back": self.command_back,
            "exit": self.command_exit,
        }

        response = responses.get(command, None)
        if response:
            response()

##############################################################################

    def command_back(self) -> None:
        self.change = True
        helper.color_print(config.COLOR_INFO,
                           "Going back to the previous page...")

##############################################################################

    @staticmethod
    def command_unknow() -> None:
        helper.color_print(config.COLOR_WARNINGS, "Unknown Command")

##############################################################################

    @staticmethod
    def command_exit() -> None:
        helper.color_print(config.COLOR_INFO,
                           "Thank you for using Market Wizards!!!")
        exit(0)


##############################################################################
