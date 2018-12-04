import bcrypt
import getpass
import base64

from mongo import MongoInterface
from pages.watch_list import WatchList
from context import Context
from terminal import TerminalColors
import helper

##############################################################################


def _main_loop(context: Context):

    PAGES = [
        "watch list", "transactions", "new transactions", "statistic", "exit"
    ]

    while True:
        page = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_purple_300),
            "Where Do you want to go? ({}) ".format(" ".join(
                map(lambda x: "'{}'".format(x), PAGES))))

        if page not in PAGES:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500), "Unknown Page")
            continue

        if page == "exit":
            break

        if page == "watch list":
            p = WatchList(context)
            p.main_loop()


##############################################################################

if __name__ == "__main__":

    MONGO = MongoInterface()
    UID = ""

    CONTEXT = Context(database=MONGO)

    ##########################################################################

    helper.color_print(
        helper.hex_to_rgb(TerminalColors.paper_amber_300),
        "Welcom to Market Wizards command line interface")

    email = input("email: ")
    password = getpass.getpass("password: ").encode("utf-8")

    user = MONGO.find_one(
        database="--admin--", collection="--user--", queries={
            "email": email,
        })

    if user is not None and bcrypt.checkpw(password,
                                           base64.b64decode(user["password"])):

        helper.color_print(
            helper.hex_to_rgb(TerminalColors.paper_amber_300), "Successful!!!")

        UID = user["uid"]

        CONTEXT.set_uid(UID)

        _main_loop(CONTEXT)

        helper.color_print(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Thank you for using Market Wizards!!!")

    else:
        helper.color_print(
            helper.hex_to_rgb(TerminalColors.paper_red_500),
            "Email or Password Error")

##############################################################################
