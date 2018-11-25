import pymongo
from typing import Dict, List

##############################################################################


class MongoInterface():

    client = pymongo.MongoClient("localhost", 27017)

    def __init__(self):
        pass

    def find_one(self, database: str, collection: str, queries: Dict) -> Dict:

        db = self.client[database]
        collection = db[collection]
        return collection.find_one(queries)

    def find(self, database: str, collection: str, queries: Dict) -> List:

        db = self.client[database]
        collection = db[collection]

        result = []
        for x in collection.find(queries):
            result.append(x)

        return result


##############################################################################
