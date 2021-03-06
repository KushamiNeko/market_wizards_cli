from typing import Dict, List
import pymongo

##############################################################################


class MongoInterface():

    client = pymongo.MongoClient("localhost", 27017)

    def __init__(self):
        pass

##############################################################################

    def insert_one(self, database: str, collection: str,
                   entity: Dict[str, str]) -> None:
        db = self.client[database]
        collection = db[collection]

        collection.insert_one(entity)

##############################################################################

    def insert(self, database: str, collection: str,
               entities: List[Dict[str, str]]) -> None:
        db = self.client[database]
        collection = db[collection]

        collection.insert_one(entities)

##############################################################################

    def replace_one(self, database: str, collection: str,
                    queries: Dict[str, str],
                    new_entity: Dict[str, str]) -> None:
        db = self.client[database]
        collection = db[collection]

        collection.replace_one(queries, new_entity)

##############################################################################

    def replace(self, database: str, collection: str, queries: Dict[str, str],
                new_entity: Dict[str, str]) -> None:
        db = self.client[database]
        collection = db[collection]

        collection.replace_many(queries, new_entity)

##############################################################################

    def find_one(self, database: str, collection: str,
                 queries: Dict[str, str]) -> Dict[str, str]:

        db = self.client[database]
        collection = db[collection]

        return collection.find_one(queries)

##############################################################################

    def find(self, database: str, collection: str,
             queries: Dict[str, str]) -> List[Dict[str, str]]:

        db = self.client[database]
        collection = db[collection]

        result = []
        for x in collection.find(queries):
            result.append(x)

        return result

##############################################################################

    def delete_one(self, database: str, collection: str,
                   queries: Dict[str, str]) -> None:

        db = self.client[database]
        collection = db[collection]

        collection.delete_one(queries)

##############################################################################

    def delete(self, database: str, collection: str,
               queries: Dict[str, str]) -> None:

        db = self.client[database]
        collection = db[collection]

        collection.delete_many(queries)


##############################################################################
