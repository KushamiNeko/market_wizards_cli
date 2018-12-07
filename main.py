import bcrypt
import getpass
import base64

from mongo import MongoInterface
from pages.watch_list import WatchList
from pages.calculator import Calculator
from context import Context
import helper
import config

##############################################################################


def _main_loop(context: Context):

    PAGES = [
        "watch list", "calculator", "transactions", "new transactions",
        "statistic", "exit"
    ]

    while True:
        page = helper.color_input(
            config.COLOR_PAGES,
            "Where Do you want to go? ({}) ".format(" ".join(
                map(lambda x: "'{}'".format(x), PAGES))))

        if page not in PAGES:
            helper.color_print(config.COLOR_WARNINGS, "Unknown Page")
            continue

        if page == "exit":
            break

        if page == "watch list":
            watchlist = WatchList(context)
            watchlist.main_loop()

        if page == "calculator":
            calculator = Calculator(context)
            calculator.main_loop()


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

    user = MONGO.find_one(
        database="--admin--",
        collection="--user--",
        queries={
            "email": email,
        })

    if user is not None and bcrypt.checkpw(password,
                                           base64.b64decode(user["password"])):

        helper.color_print(config.COLOR_INFO, "Successful!!!")

        UID = user["uid"]

        CONTEXT.set_uid(UID)

        _main_loop(CONTEXT)

        helper.color_print(config.COLOR_INFO,
                           "Thank you for using Market Wizards!!!")

    else:
        helper.color_print(config.COLOR_WARNINGS, "Email or Password Error")

##############################################################################
