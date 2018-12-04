from typing import Dict, Any
import re

##############################################################################


def check_item(entity: Dict[str, str]) -> Dict[str, Any]:

    struct: Dict[str, Any] = {}

    necessary = ["symbol", "price", "status", "grs", "rs", "value", "flag"]
    # unnecessary = ["earnings", "note"]

    re_symbol = r"[A-Za-z]+"
    re_status = r"(?:portfolio|charging|launched|p|c|l)"
    re_price = r"[0-9.]"
    re_ranks = r"[A-Ea-e]"
    re_earnings = r"\d{8}"
    re_flag = r"(?:true|false|t|f)"

    for key in necessary:
        if key not in entity:
            raise ValueError("{} can not be empty".format(key))

    for key in entity:
        value = entity[key].strip()

        if key == "symbol":
            if re.match(re_symbol, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "price":
            if re.match(re_price, value):
                struct[key] = float(value)
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "status":
            if re.match(re_status, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "earnings":
            if re.match(re_earnings, value):
                struct[key] = int(value)
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "grs":
            if re.match(re_ranks, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "rs":
            if re.match(re_ranks, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "value":
            if re.match(re_ranks, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "note":
            struct[key] = value

        if key == "flag":
            if re.match(re_flag, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        struct = clean_entity(struct)

    return struct


##############################################################################


def clean_entity(entity: Dict[str, Any]) -> Dict[str, Any]:

    for key in entity:
        value = entity[key]

        if key == "symbol":
            entity[key] = value.upper()

        if key == "price":
            pass

        if key == "status":
            if value == "p":
                value = "portfolio"
            if value == "c":
                value = "charging"
            if value == "l":
                value = "launched"

            entity[key] = value.upper()

        if key == "earnings":
            pass

        if key == "grs":
            entity[key] = value.upper()

        if key == "rs":
            entity[key] = value.upper()

        if key == "value":
            entity[key] = value.upper()

        if key == "note":
            entity[key] = value.upper()

        if key == "flag":
            if value == "true" or value == "t":
                entity[key] = True
            elif value == "false" or value == "f":
                entity[key] = False

    return entity


##############################################################################
