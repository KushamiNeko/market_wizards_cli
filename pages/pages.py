from context import Context
import helper
from typing import List, Callable
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

        self._handlers = {
            "back": self.command_back,
            "exit": self.command_exit,
        }

##############################################################################

    def main_loop(self, handler: Callable[[str], None]) -> None:
        while True:
            try:
                command = self.get_command()
            except ValueError as err:
                helper.color_print(config.COLOR_WARNINGS, str(err))
                continue

            self.process_command(command)
            handler(command)

            if self.change:
                break

##############################################################################

    def get_command(self) -> str:
        command = helper.color_input(
            config.COLOR_COMMAND, "Command ({}): ".format(" ".join(
                map(lambda x: "'{}'".format(x), self._actions))))

        try:
            command = self._clean_command(command.strip())
            return command

        except ValueError as err:
            raise err

##############################################################################

    def _clean_command(self, command: str) -> str:
        clean = ""

        for action in self._actions:
            if action.startswith(command):
                if clean == "":
                    clean = action
                else:
                    raise ValueError(
                        "Unclear Command with Multiple Actions: {}".format(
                            [action, clean]))

        if clean != "":
            return clean

        raise ValueError("Unknow Command")

##############################################################################

    def process_command(self, command: str) -> None:
        handler = self._handlers.get(command, None)
        if handler:
            handler()

##############################################################################

    def command_back(self) -> None:
        self.change = True
        helper.color_print(config.COLOR_INFO,
                           "Going back to the previous page...")

##############################################################################

    def command_exit(self) -> None:
        helper.color_print(config.COLOR_INFO,
                           "Thank you for using Market Wizards!!!")
        exit(0)


##############################################################################
