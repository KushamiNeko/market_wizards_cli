from typing import Dict, Any
import re

##############################################################################


def check_item(entity: Dict[str, str]) -> Dict[str, Any]:
    struct = {
        "symbol": "",
        "price": "",
        "status": "",
        "earnings": "",
        "grs": "",
        "rs": "",
        "value": "",
        "note": ""
    }

    necessary = ["symbol", "price", "status", "grs", "rs", "value", "flag"]
    # unnecessary = ["earnings", "note"]

    re_symbol = r"[A-Za-z]+"
    re_status = r"(?:earnings|portfolio|charging|launched)"
    re_price = r"[0-9.]"
    re_ranks = r"[A-Ea-e]"
    re_earnings = r"\d{8}"
    re_flag = r"(?:true|false)"

    for key in necessary:
        if key not in entity:
            raise ValueError("{} can not be empty".format(key))

    for key in entity:
        value = entity[key].strip()

        if key == "symbol":
            if re.match(re_symbol, value):
                struct[key] = value.upper()
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "price":
            if re.match(re_price, value):
                struct[key] = float(value)
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "status":
            if re.match(re_status, value):
                struct[key] = value.upper()
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "earnings":
            if re.match(re_earnings, value):
                struct[key] = int(value)
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "grs":
            if re.match(re_ranks, value):
                struct[key] = value.upper()
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "rs":
            if re.match(re_ranks, value):
                struct[key] = value.upper()
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "value":
            if re.match(re_ranks, value):
                struct[key] = value.upper()
            else:
                raise ValueError("{}: invalid value".format(key))

        if key == "note":
            struct[key] = value.upper()

        if key == "flag":
            if re.match(re_flag, value):
                if value == "true":
                    struct[key] = True
                elif value == "false":
                    struct[key] = False
            else:
                raise ValueError("{}: invalid value".format(key))

    return struct


##############################################################################
