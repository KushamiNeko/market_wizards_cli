from typing import Dict, List
import helper
from context import Context

##############################################################################


class Trading():
    def __init__(self, context: Context, live_trading: bool = False) -> None:
        self._context = context

        self._database = "--paper-trading--"
        if live_trading:
            self._database = "--live-trading--"

##############################################################################

    def add_transaction(self, entity: Dict[str, str]) -> None:

        old_entity = self._context.database.find_one(
            self._database, self._context.uid,
            {"symbol": entity.get("symbol", "")})

        if old_entity is not None:
            raise ValueError("SYMBOL ALREADY EXISTS: {}".format(
                entity.get("symbol", "")))

        self._context.database.insert_one(self._database, self._context.uid,
                                          entity)

##############################################################################

    def edit_transaction(self, query: Dict[str, str],
                         new_transaction: Dict[str, str]) -> None:

        entity = self._context.database.find_one(self._database,
                                                 self._context.uid, query)
        if not entity:
            raise ValueError("QUERY HAS NO RESULT: {}".format(query))

        for key in new_transaction:
            entity[key] = new_transaction[key]

        self._context.database.replace_one(self._database, self._context.uid,
                                           query, entity)

##############################################################################

    def find_transaction(self, query: Dict[str, str]) -> List[Dict[str, str]]:
        return self._context.database.find(self._database, self._context.uid,
                                           query)

##############################################################################

    def delete_transaction(self, query: Dict[str, str]) -> None:

        entity = self._context.database.find_one(self._database,
                                                 self._context.uid, query)
        if not entity:
            raise ValueError("QUERY HAS NO RESULT: {}".format(query))

        self._context.database.delete(self._database, self._context.uid, query)

##############################################################################

    def trades(self) -> List[Dict[str, str]]:
        pass

##############################################################################

    def statistic(self) -> Dict[str, str]:
        pass


##############################################################################
