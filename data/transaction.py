from typing import Dict, Any
import re
import helper

##############################################################################


class FuturesTransaction():

    _regex_date = r"^(\d{8})$"
    _regex_symbol = r"^[A-Za-z]+$"
    _regex_action = r"^(?:long|short|increase|decrease|close)$"
    _regex_int = r"^[0-9]+$"
    _regex_float = r"^[0-9.]+$"

    def __init__(self, date: int, symbol: str, action: str, quantity: int,
                 point: float, note: str) -> None:

        self.index = helper.random_string()

        if not re.match(self._regex_date, str(date)):
            raise ValueError("invalid transaction date")
        self.date = date

        if not re.match(self._regex_symbol, symbol.lower()):
            raise ValueError("invalid transaction symbol")
        self.symbol = symbol.strip().upper()

        if not re.match(self._regex_action, action.lower()):
            raise ValueError("invalid transaction action")
        self.action = action.strip().upper()

        if not re.match(self._regex_int, str(quantity)) or quantity <= 0:
            raise ValueError("invalid transaction quantity")
        self.quantity = quantity

        if not re.match(self._regex_float, str(point)) or point <= 0.0:
            raise ValueError("invalid transaction point")
        self.point = point

        self.note = note.strip()

##############################################################################

    @property
    def entity(self) -> Dict[str, str]:
        entity = {
            "index": str(self.index),
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
    )


##############################################################################
