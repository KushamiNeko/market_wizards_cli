from typing import Tuple, Dict
import datetime
import readline
import string
import random
import time

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
        raise ValueError("EMPTY INPUT")

    split = values.split(" ")

    if len(split) < 1:
        raise ValueError("NO KEY VALUE PAIR")

    for value in values.split(" "):
        strings = value.split("=")

        if len(strings) < 2:
            raise ValueError("NO KEY VALUE PAIR: {}".format(strings).upper())

        key = strings[0].strip()
        value = strings[1].strip()

        pair[key] = value

    return pair


##############################################################################


def days_to_date(date: int) -> int:
    now = int(datetime.datetime.now().strftime("%Y%m%d"))
    days = date - now

    # if days < 0:
    # days = 0

    return days


##############################################################################


def hex_to_rgb(hexstr: str) -> Tuple[int, int, int]:
    assert len(hexstr) == 6

    r = int(hexstr[0:2], 16)
    g = int(hexstr[2:4], 16)
    b = int(hexstr[4:6], 16)

    return (r, g, b)


##############################################################################


def random_string(length: int = 32,
                  has_letter: bool = True,
                  has_digits: bool = True,
                  has_punctuation: bool = False) -> str:

    random.seed(time.time())

    src = ""
    if has_letter:
        src += string.ascii_letters
    if has_digits:
        src += string.digits
    if has_punctuation:
        src += string.punctuation

    rand_str = ""

    for _ in range(0, length):
        index = random.randint(0, len(src) - 1)
        rand_str += src[index]

    return rand_str


##############################################################################
