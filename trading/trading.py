from typing import Dict, List
import helper
from context import Context

from data.transaction import FuturesTransaction, entity_to_futures_transaction
from data.trade import FuturesTrade

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
        entities = self.find_transaction({})
        transactions = [
            entity_to_futures_transaction(entity) for entity in entities
        ]

        trades_entities = [
            trade.entity for trade in self._process_trades(transactions)
        ]
        return trades_entities

##############################################################################

    def _process_trades(self, transactions: List[FuturesTransaction]
                        ) -> List[FuturesTrade]:

        sorted_transaction = sorted(transactions, key=lambda x: x.time_stamp)

        trades = []
        round_transactions = []
        position = 0

        for transaction in sorted_transaction:
            action = int("{}{}".format(transaction.action,
                                       transaction.quantity))

            position += action
            round_transactions.append(transaction)

            if position == 0:
                trade = FuturesTrade(round_transactions)
                trades.append(trade)

                round_transactions = []
                continue

        return trades

##############################################################################

    def statistic(self) -> Dict[str, str]:
        entities = self.find_transaction({})
        transactions = [
            entity_to_futures_transaction(entity) for entity in entities
        ]

        trades = self._process_trades(transactions)
        return {}


##############################################################################
