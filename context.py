from mongo import MongoInterface
from terminal import TerminalColors
import helper

from pages.watch_list import WatchList

##############################################################################


class ContextPages():

    watch_list = "watch_list"


##############################################################################


class Context():

    uid: str = ""
    database: MongoInterface = None

    page: str = ""

    def __init__(self, database: MongoInterface):
        self.database = database

    def set_uid(self, uid: str):
        self.uid = uid

    def change_page(self, page: str):
        self.page = page
        helper.color_print(
            TerminalColors.hex_to_rgb(TerminalColors.paper_teal_300),
            "Page: {}\n".format(self.page))

        # if self.page == Pages.action:
        # handler_watch_list(self, self.database)
        if self.page == ContextPages.watch_list:
            WatchList(self, self.database)


##############################################################################
