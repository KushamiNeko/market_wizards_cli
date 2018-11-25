# import pymongo
import bcrypt
import getpass
import base64
# from typing import Dict, List

from mongo import MongoInterface
from context import Context, ContextPages
from terminal import TerminalColors
import helper

##############################################################################

# client = pymongo.MongoClient("localhost", 27017)
# db = client["--admin--"]
# collection = db["--user--"]
# print(type(collection))

# print(collection.find_one({"email": "aa"}))

##############################################################################

# def color_print(rgb: typing.Tuple[int, int, int], message: str):
# print("\033[1;38;2;{};{};{}m{}\033[0m".format(rgb[0], rgb[1], rgb[2],
# message))

# ##############################################################################

# def color_input(rgb: typing.Tuple[int, int, int], message: str) -> str:
# return input("\033[1;38;2;{};{};{}m{}\033[0m".format(
# rgb[0], rgb[1], rgb[2], message))

##############################################################################

# class MongoInterface():

# client = pymongo.MongoClient("localhost", 27017)

# def __init__(self):
# pass

# def find_one(self, database: str, collection: str, queries: Dict) -> Dict:

# db = self.client[database]
# collection = db[collection]
# return collection.find_one(queries)

# def find(self, database: str, collection: str, queries: Dict) -> List:

# db = self.client[database]
# collection = db[collection]

# result = []
# for x in collection.find(queries):
# result.append(x)

# return result

##############################################################################

# class Pages():

# action = "action"
# watch_list = "watch_list"
# new = "new"
# statistic = "statistic"

##############################################################################

# class Context():

# uid: str = ""
# page: str = ""

# def __init__(self, database: MongoInterface):
# self.database = database

# def set_uid(self, uid: str):
# self.uid = uid

# def change_page(self, page: str):
# self.page = page
# helper.color_print(
# TerminalColors.hex_to_rgb(TerminalColors.paper_teal_300),
# "Page: {}\n".format(self.page))

# if self.page == Pages.action:
# handler_watch_list(self, self.database)
# if self.page == Pages.watch_list:
# handler_watch_list(self, self.database)

##############################################################################

# def handler_watch_list(context: Context, database: MongoInterface):

# action = ["show", "add", "delete", "goto", "exit"]

# while True:
# command = helper.color_input(
# TerminalColors.hex_to_rgb(TerminalColors.paper_teal_300),
# "Command ({}): ".format(" ,".join(action)))

# if command not in action:
# helper.color_print(
# TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
# "Unknown Command")
# continue

# if command == "exit":
# helper.color_print(
# TerminalColors.hex_to_rgb(TerminalColors.paper_amber_300),
# "\nThank you for using Market Wizards\n")
# exit(0)

# if command == "show":
# entities = database.find("--watch-list--", context.uid, {})

# if len(entities) == 0:
# helper.color_print(
# TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
# "No Entities Match The Queries\n")
# continue

# width = 20
# note_width = width * 2
# # labels = ("{m1: <6}" + "{m2: >{width}}" + "{m3: >{width}}" +
# # "{m4: >{width}}" + "{m5: >{width}}" + "{m6: >{width}}" +
# # "{m7: >{width}}" + "{m8: >{width}}")
# labels = ("{m1: <6}" + "{m2: >{width}}" + "{m3: >{width}}" +
# "{m4: >{width}}" + "{m5: >{width}}" + "{m6: >{width}}" +
# "{m7: >{note_width}}")
# helper.color_print(
# TerminalColors.hex_to_rgb(TerminalColors.paper_light_blue_300),
# labels.format(
# m1="Symbol",
# m2="Price",
# m3="Status",
# m4="Group RS",
# m5="RS",
# m6="Fundamentals",
# m7="Note",
# # m8="Flag",
# width=width,
# note_width=note_width))

# # symbol price grs rs fundamentals status note flag

# for entity in entities:
# helper.color_print(
# TerminalColors.hex_to_rgb(
# TerminalColors.paper_blue_grey_100),
# labels.format(
# m1=entity["symbol"],
# m2=entity["price"],
# m3=entity["status"],
# m4=entity["grs"],
# m5=entity["rs"],
# m6=entity["fundamentals"],
# m7=entity["note"],
# # m8=entity["flag"],
# width=width,
# note_width=note_width))

# break

##############################################################################

# class ContextPages():

# watch_list = "watch_list"

# ##############################################################################

# class Context():

# uid: str = ""
# page: str = ""
# database: MongoInterface = None

# def __init__(self, database: MongoInterface):
# self.database = database

# def set_uid(self, uid: str):
# self.uid = uid

# def change_page(self, page: str):
# self.page = page
# helper.color_print(
# TerminalColors.hex_to_rgb(TerminalColors.paper_teal_300),
# "Page: {}\n".format(self.page))

# # if self.page == Pages.action:
# # handler_watch_list(self, self.database)
# if self.page == ContextPages.watch_list:
# WatchList(self, self.database)

##############################################################################

if __name__ == "__main__":

    helper.color_print(
        TerminalColors.hex_to_rgb(TerminalColors.paper_amber_300),
        "\nWelcom to Market Wizards command line interface\n")

    email = input("email: ")
    password = getpass.getpass("password: ").encode("utf-8")

    mongo = MongoInterface()
    context = Context(mongo)

    user = mongo.find_one(
        database="--admin--", collection="--user--", queries={
            "email": email,
        })

    if user is not None and bcrypt.checkpw(password,
                                           base64.b64decode(user["password"])):

        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_amber_300),
            "\nSuccessful!!\n")
        uid = user["uid"]
        context.set_uid(uid)
        context.change_page(ContextPages.watch_list)
    else:
        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_red_500),
            "\nEmail or Password Error\n")

##############################################################################
