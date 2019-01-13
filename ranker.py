import re
from typing import Dict

##############################################################################


class MomentumRanker():
    def __init__(self) -> None:
        self._base = 5
        self._multiplier = 100

##############################################################################

    def rank(self, entity: Dict) -> int:

        points = 0

        points += self._sort_entity_op(entity,
                                       (self._base**7) * self._multiplier)

        points += self._sort_entity_status(entity,
                                           (self._base**6) * self._multiplier)

        points += self._sort_entity_action(entity,
                                           (self._base**5) * self._multiplier)

        # points += self._sort_entity_flag(entity,
        # (self._base**5) * self._multiplier)

        points += self._sort_entity_rank(entity, "grs",
                                         (self._base**4) * self._multiplier)

        points += self._sort_entity_int(entity, "rs",
                                        (self._base**3) * self._multiplier)

        # points += self._sort_entity_rank(entity, "acc",
        # (self._base**2) * self._multiplier)

        return points

##############################################################################

    def _sort_entity_status(self, entity: Dict, multiplier: int) -> int:

        points = 0
        value = entity.get("status", None)

        if value:
            value = value.lower()

            if value == "portfolio":
                points = 1 * multiplier
            if value == "charging":
                points = 2 * multiplier
            if value == "launched":
                points = 3 * multiplier
            if value == "repairing":
                points = 4 * multiplier

        else:
            points = 5 * multiplier

        return points

##############################################################################

    def _sort_entity_op(self, entity: Dict, multiplier: int) -> int:

        points = 0
        value = entity.get("op", None)

        if value:
            value = value.lower()
            if value == "long":
                points = 1 * multiplier
            if value == "short":
                points = 2 * multiplier
        else:
            points = 3 * multiplier

        return points

##############################################################################

    def _sort_entity_flag(self, entity: Dict, multiplier: int) -> int:
        if entity.get("flag", False):
            return 1 * multiplier
        else:
            return 2 * multiplier

##############################################################################

    def _sort_entity_action(self, entity: Dict, multiplier: int) -> int:
        if entity.get("action", False):
            return 1 * multiplier
        else:
            return 2 * multiplier

##############################################################################

    def _sort_entity_int(self,
                         entity: Dict,
                         label: str,
                         multiplier: int,
                         maximum: int = 100) -> int:

        value = entity.get(label, 0)

        if not re.match(r"\d+", str(value)):
            value = 0

        return ((maximum - value) / 100.0) * multiplier

##############################################################################

    def _sort_entity_rank(self, entity: Dict, rank: str,
                          multiplier: int) -> int:
        points = 0
        value = entity.get(rank, None)

        if value:
            if value == "A":
                points = 1 * multiplier
            if value == "B":
                points = 2 * multiplier
            if value == "C":
                points = 3 * multiplier
            if value == "D":
                points = 4 * multiplier
            if value == "E":
                points = 5 * multiplier

        else:
            points = 6 * multiplier

        return points


##############################################################################
