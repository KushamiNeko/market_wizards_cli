import base64
import getpass
from typing import Callable, Any

import bcrypt
import helper
import config
from mongo import MongoInterface
from context import Context
from pages.watch_list import WatchList
from pages.calculator import Calculator
from pages.scan_organizer import ScanOrganizer

# from pages.charts_rename import ChartsRename
# from pages.ibd_stock_lists import IBDStockListsParser
# from pages.ibd_data_tables import IBDDataTablesParser

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


def _main_loop(context: Context) -> None:

    PAGES = [
        "scan organize",
        "calculator",
        "watch list",
        "trades",
        "new trade",
        "statistic",
        # "charts rename",
        # "ibd stock lists",
        # "ibd data tables",
        "exit",
    ]

    while True:
        page = helper.color_input(
            config.COLOR_PAGES,
            "Where Do you want to go?\n({}) ".format(" ".join(
                map(lambda x: "'{}'".format(x), PAGES))))

        if page not in PAGES:
            helper.color_print(config.COLOR_WARNINGS, "Unknown Page")
            continue

        if page == "exit":
            break

        if page == "scan organize":
            scan_split = ScanOrganizer(context)
            scan_split.main_loop()

        if page == "calculator":
            calculator = Calculator(context)
            calculator.main_loop()

        if page == "watch list":
            watchlist = WatchList(context)
            watchlist.main_loop()

        # if page == "charts rename":
        # rename = ChartsRename(context)
        # rename.main_loop()

        # if page == "ibd stock lists":
        # stock_lists_parser = IBDStockListsParser(context)
        # stock_lists_parser.main_loop()

        # if page == "ibd data tables":
        # data_tables_parser = IBDDataTablesParser(context)
        # data_tables_parser.main_loop()


##############################################################################

if __name__ == "__main__":

    MONGO = MongoInterface()
    UID = ""

    CONTEXT = Context(database=MONGO)

    ##########################################################################

    helper.color_print(config.COLOR_INFO,
                       "Welcom to Market Wizards command line interface")

    email = input("email: ")
    password = getpass.getpass("password: ").encode("utf-8")

    try:
        UID = login(MONGO, email, password)
        helper.color_print(config.COLOR_INFO, "Successful!!!")

        CONTEXT.set_uid(UID)

        _main_loop(CONTEXT)

        helper.color_print(config.COLOR_INFO,
                           "Thank you for using Market Wizards!!!")
    except Exception as err:
        helper.color_print(config.COLOR_WARNINGS, str(err))

##############################################################################
