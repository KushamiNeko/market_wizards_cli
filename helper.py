from typing import Tuple, Dict
import datetime

##############################################################################


def color_print(rgb: Tuple[int, int, int], message: str):
    print("\033[1;38;2;{};{};{}m{}\033[0m".format(rgb[0], rgb[1], rgb[2],
                                                  message))


##############################################################################


def color_input(rgb: Tuple[int, int, int], message: str) -> str:
    return input("\033[1;38;2;{};{};{}m{}\033[0m".format(
        rgb[0], rgb[1], rgb[2], message))


##############################################################################


def key_value_input(rgb: Tuple[int, int, int], message: str) -> Dict[str, str]:
    values = color_input(rgb, message).strip()

    pair = {}

    if values == "":
        raise ValueError("empty input")

    split = values.split(" ")

    if len(split) < 2:
        raise ValueError("no key value pair")

    for value in values.split(" "):
        strings = value.split("=")
        key = strings[0].strip()
        value = strings[1].strip()

        pair[key] = value

    return pair


##############################################################################


def days_to_date(date: int) -> int:
    now = int(datetime.datetime.now().strftime("%Y%m%d"))
    days = date - now
    return days


##############################################################################
