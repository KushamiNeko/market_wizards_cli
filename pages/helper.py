from typing import List

##############################################################################


class HelperPrintList():

    _actions: List[str] = []

    def __init__(self) -> None:
        print("helper")
        for action in ["print list", "print csv"]:
            if action not in self._actions:
                self._actions.append(action)

##############################################################################

    def _generate_list(self, separator: str) -> None:
        raise Exception("This method should be overwritten")

##############################################################################

    def _command_print_csv(self) -> None:
        self._generate_list(",")

##############################################################################

    def _command_print_list(self) -> None:
        self._generate_list("\n")


##############################################################################
