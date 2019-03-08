from typing import List, Dict
from data.transaction import FuturesTransaction
import helper
import config

##############################################################################


class FuturesTrade():
    def __init__(self, orders: List[FuturesTransaction]) -> None:

        if not orders:
            raise ValueError("EMPTY TRANSACTION ORDERS")

        self.orders = sorted(orders, key=lambda o: o.time_stamp)

        self.action = self.orders[0].action
        self.symbol = self.orders[0].symbol
        self.open_date = self.orders[0].date
        self.close_date = self.orders[-1].date

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
            action = order.action

            if symbol == "":
                symbol = order.symbol
            else:
                if symbol != order.symbol:
                    raise ValueError(
                        "MISMATCH SYMBOL IN ORDERS: {}, {}".format(
                            symbol, order.symbol))

            if action == self.action:
                open_quatity += order.quantity
                open_orders.append(order)
            else:
                close_quantity += order.quantity
                close_orders.append(order)

        if open_quatity != close_quantity:
            raise ValueError(
                "NUMBER OF OPEN AND CLOSE CONTRACT DOESN'T MATCH: " +
                "OPEN {} CONTRACTS, CLOSE {} CONTRACTS".format(
                    open_quatity, close_quantity))

        self.average_cost = round(
            self._average_point(open_orders), config.DOLLAR_DECIMALS)
        self.average_revenue = round(
            self._average_point(close_orders), config.DOLLAR_DECIMALS)

        if self.action == "+":
            self.gl_point = round(self.average_revenue - self.average_cost,
                                  config.DOLLAR_DECIMALS)
        else:
            self.gl_point = round(self.average_cost - self.average_revenue,
                                  config.DOLLAR_DECIMALS)

##############################################################################

    def _average_point(self, orders: List[FuturesTransaction]) -> float:
        quantity = 0
        total_point = 0.0
        for order in orders:
            total_point += order.point * order.quantity
            quantity += order.quantity

        return total_point / float(quantity)

##############################################################################

    @property
    def entity(self) -> Dict[str, str]:
        entity = {
            "action": str(self.action),
            "symbol": str(self.symbol),
            "open_date": str(self.open_date),
            "close_date": str(self.close_date),
            "average_cost": str(self.average_cost),
            "average_revenue": str(self.average_revenue),
            "gl_point": str(self.gl_point),
        }

        return entity


##############################################################################
