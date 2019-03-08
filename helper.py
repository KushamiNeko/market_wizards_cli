from typing import Tuple, Dict
import datetime
import readline
import string
import random
import time
import re

##############################################################################


def color_print(rgb: Tuple[int, int, int], message: str) -> None:
    # print("\033[1;38;2;{};{};{}m{}\033[0m".format(rgb[0], rgb[1], rgb[2],
    # message))

    print("\033[38;2;{};{};{}m{}\033[0m".format(rgb[0], rgb[1], rgb[2],
                                                message.upper()))


##############################################################################


def color_input(rgb: Tuple[int, int, int], message: str) -> str:
    color_print(rgb, message)
    return input()


##############################################################################


def key_value_input(rgb: Tuple[int, int, int], message: str) -> Dict[str, str]:
    user_input = color_input(rgb, message).strip()
    if user_input == "":
        raise ValueError("EMPTY INPUT")

    try:
        pair = key_value_pair(user_input)
        return pair
    except ValueError as err:
        raise err


##############################################################################


def key_value_pair(inputs: str) -> Dict[str, str]:
    regex_pattern = r"([^;]*)=([^;]*)"
    pair = {}

    matches = re.finditer(regex_pattern, inputs, re.DOTALL)

    for match in matches:
        key = match.group(1).strip()
        value = match.group(2).strip()

        if key == "" or value == "":
            raise ValueError("INVALID KEY VALUE PAIR: {}={}".format(
                key, value))

        pair[key] = value

    if not pair:
        raise ValueError("EMPTY KEY VALUE PAIR")

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
