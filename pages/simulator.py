from typing import Dict
import helper
from pages.pages import Pages
from context import Context
import config

##############################################################################


class Simulator():

    _actions = [
        "add",
        "edit",
        "delete",
        "find",
        "trade",
        "statistic",
    ]

    def __init__(self, context: Context) -> None:
        self.context = context

        self._page = Pages(self._actions)

        self._handlers = {
            # "stop": self._command_stop,
            # "depth": self._command_depth,
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
