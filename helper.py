from typing import Tuple, Dict

##############################################################################


def color_print(rgb: Tuple[int, int, int], message: str):
    print("\033[1;38;2;{};{};{}m{}\033[0m".format(rgb[0], rgb[1], rgb[2],
                                                  message))


##############################################################################


def color_input(rgb: Tuple[int, int, int], message: str) -> str:
    return input("\033[1;38;2;{};{};{}m{}\033[0m".format(
        rgb[0], rgb[1], rgb[2], message))


##############################################################################


def key_value_input(rgb: Tuple[int, int, int], message: str) -> Dict:
    values = color_input(rgb, message)

    pair = {}

    for value in values.split(" "):
        strings = value.split("=")
        key = strings[0].strip()
        value = strings[1].strip()

        pair[key] = value

    return pair


##############################################################################
