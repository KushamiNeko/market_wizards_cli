import base64
import getpass

import bcrypt
import helper
import config
from mongo import MongoInterface
from context import Context
from pages.watch_list import WatchList
from pages.calculator import Calculator
from pages.scan_organizer import ScanOrganizer
from pages.pages import Pages

##############################################################################


class EntryPage():

    _actions = [
        "calculator",
        "paper trading",
        "live trading",
        # "scan organize",
        # "watch list",
    ]

    def __init__(self, context: Context) -> None:
        self.context = context

        self._page = Pages(self._actions, is_top_page=True)

        self._handlers = {
            "calculator": self._command_calculator,
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

    def _command_calculator(self) -> None:
        calculator = Calculator(self.context)
        calculator.main_loop()

##############################################################################

    def _command_scan_organize(self) -> None:
        scan_split = ScanOrganizer(self.context)
        scan_split.main_loop()

##############################################################################

    def _command_watch_list(self) -> None:
        watchlist = WatchList(self.context)
        watchlist.main_loop()


##############################################################################


def login(database: MongoInterface, email: str, password: bytes) -> str:

    user = database.find_one(
        database="--admin--",
        collection="--user--",
        queries={
            "email": email,
        })

    if user is not None and bcrypt.checkpw(password,
                                           base64.b64decode(user["password"])):
        UID = user["uid"]
        return UID
    else:
        raise ValueError("Invalid User or Password")


##############################################################################


def main() -> None:
    MONGO = MongoInterface()
    UID = ""

    CONTEXT = Context(database=MONGO)

    ##########################################################################

    helper.color_print(config.COLOR_INFO,
                       "Welcom to Market Wizards Wealthy Interface")

    email = input("email: ")
    password = getpass.getpass("password: ").encode("utf-8")

    try:
        UID = login(MONGO, email, password)
        helper.color_print(config.COLOR_INFO, "Successful!!!")

        CONTEXT.set_uid(UID)

        entry_page = EntryPage(CONTEXT)
        entry_page.main_loop()

        helper.color_print(config.COLOR_INFO,
                           "Thank you for using Market Wizards!!!")
    except Exception as err:
        helper.color_print(config.COLOR_WARNINGS, str(err))


##############################################################################

if __name__ == "__main__":
    main()

##############################################################################
