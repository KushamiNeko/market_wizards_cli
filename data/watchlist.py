from typing import Dict, Any
import re

##############################################################################


def check_necessary_keys(entity: Dict[str, Any]) -> None:
    # necessary = [
    # "symbol", "op", "status", "sctr", "grs", "rs", "acc", "eps", "smr",
    # "comp"
    # ]
    necessary = ["symbol", "op", "status"]
    # unnecessary = ["price", "earnings", "note", "flag"]

    for key in necessary:
        if key not in entity:
            raise ValueError("{} can not be empty".format(key))


##############################################################################


def check_values(entity: Dict[str, str]) -> Dict[str, Any]:

    # necessary = ["symbol", "price", "status", "grs", "rs", "value", "flag"]
    # unnecessary = ["earnings", "note"]

    # for key in necessary:
    # if key not in entity:
    # raise ValueError("{} can not be empty".format(key))

    struct: Dict[str, Any] = {}

    re_symbol = r"^[A-Za-z]+$"
    re_op = r"^(?:long|short|l|s)$"
    re_status = r"^(?:portfolio|repairing|charging|launched|p|r|c|l)$"

    re_int = r"^[0-9]+$"
    re_float = r"^[0-9.]+$"
    re_float_range = r"^[0-9.]+~[0-9.]+$"
    re_bool = r"^(?:true|false|t|f)$"

    re_date = r"^\d{8}$"
    re_ranks = r"^[A-Ea-e]$"

    for key in entity:
        value = entity[key].strip()

        if key == "symbol":
            if re.match(re_symbol, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "op":
            if re.match(re_op, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "status":
            if re.match(re_status, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "earnings":
            if re.match(re_date, value):
                struct[key] = int(value)
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "price":
            if re.match(re_float_range, value):
                struct[key] = float(value)
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "stop":
            if re.match(re_float_range, value):
                struct[key] = float(value)
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "note":
            struct[key] = value

        if key == "grs":
            if re.match(re_ranks, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "rs":
            if re.match(re_int, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "acc":
            if re.match(re_ranks, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "sctr":
            if re.match(re_float, value):
                struct[key] = float(value)
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "eps":
            if re.match(re_int, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "smr":
            if re.match(re_ranks, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "comp":
            if re.match(re_int, value):
                struct[key] = value
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "flag":
            if re.match(re_bool, value):
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

        if key == "op":
            if value == "l":
                value = "long"
            elif value == "s":
                value = "short"

            entity[key] = value.upper()

        if key == "status":
            if value == "p":
                value = "portfolio"
            if value == "r":
                value = "repairing"
            if value == "c":
                value = "charging"
            if value == "l":
                value = "launched"

            entity[key] = value.upper()

        if key == "earnings":
            pass

        if key == "sctr":
            pass

        if key == "grs":
            entity[key] = value.upper()

        if key == "rs":
            entity[key] = value.upper()

        if key == "acc":
            entity[key] = value.upper()

        if key == "eps":
            entity[key] = value.upper()

        if key == "smr":
            entity[key] = value.upper()

        if key == "comp":
            entity[key] = value.upper()

        if key == "note":
            value = value.replace("_", " ", -1)
            entity[key] = value.upper()

        if key == "flag":
            if value == "true" or value == "t":
                entity[key] = True
            elif value == "false" or value == "f":
                entity[key] = False

    return entity


##############################################################################
