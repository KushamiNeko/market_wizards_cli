from typing import Tuple, Dict
import datetime
import readline

##############################################################################


def color_print(rgb: Tuple[int, int, int], message: str) -> None:
    # print("\033[1;38;2;{};{};{}m{}\033[0m".format(rgb[0], rgb[1], rgb[2],
    # message))

    print("\033[38;2;{};{};{}m{}\033[0m".format(rgb[0], rgb[1], rgb[2],
                                                message))


##############################################################################


def color_input(rgb: Tuple[int, int, int], message: str) -> str:
    color_print(rgb, message)
    return input()


##############################################################################


def key_value_input(rgb: Tuple[int, int, int], message: str) -> Dict[str, str]:
    values = color_input(rgb, message).strip()

    pair = {}

    if values == "":
        raise ValueError("empty input")

    split = values.split(" ")

    if len(split) < 1:
        raise ValueError("no key value pair")

    for value in values.split(" "):
        strings = value.split("=")

        if len(strings) < 2:
            raise ValueError("no key value pair: {}".format(strings))

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


def hex_to_rgb(hexstr: str) -> Tuple[int, int, int]:
    assert len(hexstr) == 6

    r = int(hexstr[0:2], 16)
    g = int(hexstr[2:4], 16)
    b = int(hexstr[4:6], 16)

    return (r, g, b)


##############################################################################
