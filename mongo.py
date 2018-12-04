from typing import Dict, List, Any
import pymongo

##############################################################################


class MongoInterface():

    client = pymongo.MongoClient("localhost", 27017)

    def __init__(self):
        pass

##############################################################################

    def insert_one(self, database: str, collection: str,
                   entity: Dict[str, Any]):
        db = self.client[database]
        collection = db[collection]
        collection.insert_one(entity)

##############################################################################

    def insert(self, database: str, collection: str,
               entities: List[Dict[str, Any]]):
        db = self.client[database]
        collection = db[collection]
        collection.insert_one(entities)

##############################################################################

    def find_one(self, database: str, collection: str,
                 queries: Dict[str, Any]) -> Dict[str, Any]:

        db = self.client[database]
        collection = db[collection]
        return collection.find_one(queries)

##############################################################################

    def find(self, database: str, collection: str,
             queries: Dict[str, Any]) -> List[Dict[str, Any]]:

        db = self.client[database]
        collection = db[collection]

        result = []
        for x in collection.find(queries):
            result.append(x)

        return result

##############################################################################

    def delete_one(self, database: str, collection: str,
                   queries: Dict[str, Any]):

        db = self.client[database]
        collection = db[collection]

        collection.delete_one(queries)

##############################################################################

    def delete(self, database: str, collection: str, queries: Dict[str, Any]):

        db = self.client[database]
        collection = db[collection]

        collection.delete_many(queries)


##############################################################################
