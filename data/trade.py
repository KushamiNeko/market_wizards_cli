from typing import List
from data.transaction import FuturesTransaction
import helper

##############################################################################


class FuturesTrade():
    def __init__(self, orders: List[FuturesTransaction]) -> None:

        self.orders = orders
        self.action = ""

        self.average_cost = 0.0
        self.average_revenue = 0.0
        self.gl_point = 0.0

        try:
            self._processing()
        except ValueError as err:
            raise err

##############################################################################

    def _processing(self) -> None:
        open_orders: List[FuturesTransaction] = []
        close_orders: List[FuturesTransaction] = []

        open_quatity = 0
        close_quantity = 0

        symbol = ""

        for order in self.orders:
            action = order.action.lower()

            if symbol == "":
                symbol = order.symbol
            else:
                if symbol != order.symbol:
                    raise ValueError(
                        "mismatch symbol in orders: {}, {}".format(
                            symbol, order.symbol))

            if action in ("long", "short"):
                self.action = order.action.upper()
                open_quatity += order.quantity
                open_orders.append(order)

            elif action == "increase":
                open_quatity += order.quantity
                open_orders.append(order)

            elif action in ("close", "decrease"):
                close_quantity += order.quantity
                close_orders.append(order)

        if open_quatity != close_quantity:
            raise ValueError(
                "Number of Open and Close Contract doesn't match: " +
                "open {} contracts, close {} contracts".format(
                    open_quatity, close_quantity))

        self.average_cost = round(self._average_point(open_orders), 4)
        self.average_revenue = round(self._average_point(close_orders), 4)

        if self.action == "LONG":
            self.gl_point = round(self.average_revenue - self.average_cost, 4)
        else:
            self.gl_point = round(self.average_cost - self.average_revenue, 4)

##############################################################################

    def _average_point(self, orders: List[FuturesTransaction]) -> float:
        quantity = 0
        total_point = 0.0
        for order in orders:
            total_point += order.point * order.quantity
            quantity += order.quantity

        return total_point / float(quantity)


##############################################################################

##############################################################################
