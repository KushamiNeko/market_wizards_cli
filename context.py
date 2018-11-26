from mongo import MongoInterface

##############################################################################


class Context():

    uid: str = ""
    database: MongoInterface = None

    def __init__(self, uid: str = "", database: MongoInterface = None):

        if uid:
            self.uid = uid

        if database:
            self.database = database

    def set_uid(self, uid: str):
        self.uid = uid

    def set_database(self, database: MongoInterface):
        self.database = database


##############################################################################
