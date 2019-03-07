import helper

##############################################################################


class FuturesTransaction():
    def __init__(self, date: int, symbol: str, action: str, quantity: int,
                 point: float, note: str) -> None:

        self.index = helper.random_string()

        self.date = date
        self.symbol = symbol
        self.action = action
        self.quantity = quantity
        self.point = point
        self.note = note


##############################################################################
