from typing import Dict, Any
import re
import helper
import time

##############################################################################


class FuturesTransaction():

    _regex_date = r"^(\d{8})$"
    _regex_symbol = r"^[A-Za-z]+$"
    _regex_action = r"^[+-]$"
    _regex_int = r"^[0-9]+$"
    _regex_float = r"^[0-9.]+$"

    def __init__(self,
                 date: int,
                 symbol: str,
                 action: str,
                 quantity: int,
                 point: float,
                 note: str,
                 index: str = "",
                 time_stamp: float = 0) -> None:

        if index == "":
            self.index = helper.random_string()
        else:
            self.index = index

        if time_stamp <= 0:
            self.time_stamp = time.time()
        else:
            self.time_stamp = time_stamp

        if not re.match(self._regex_date, str(date)):
            raise ValueError("INVALID TRANSACTION DATE")
        self.date = date

        if not re.match(self._regex_symbol, symbol.lower()):
            raise ValueError("INVALID TRANSACTION SYMBOL")
        self.symbol = symbol.strip().upper()

        if not re.match(self._regex_action, action.lower()):
            raise ValueError("INVALID TRANSACTION ACTION")
        self.action = action.strip().upper()

        if not re.match(self._regex_int, str(quantity)) or quantity <= 0:
            raise ValueError("INVALID TRANSACTION QUANTITY")
        self.quantity = quantity

        if not re.match(self._regex_float, str(point)) or point <= 0.0:
            raise ValueError("INVALID TRANSACTION POINT")
        self.point = point

        self.note = note.strip()

##############################################################################

    @property
    def entity(self) -> Dict[str, str]:
        entity = {
            "index": str(self.index),
            "time_stamp": str(self.time_stamp),
            "date": str(self.date),
            "symbol": str(self.symbol),
            "action": str(self.action),
            "quantity": str(self.quantity),
            "point": str(self.point),
            "note": str(self.note),
        }

        return entity


##############################################################################


def entity_to_futures_transaction(
        entity: Dict[str, str]) -> FuturesTransaction:

    return FuturesTransaction(
        int(entity.get("date", 0)),
        entity.get("symbol", ""),
        entity.get("action", ""),
        int(entity.get("quantity", 0)),
        float(entity.get("point", 0)),
        entity.get("note", ""),
        index=entity.get("index", ""),
        time_stamp=float(entity.get("time_stamp", 0)),
    )


##############################################################################
