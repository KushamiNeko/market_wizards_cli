from typing import Tuple

##############################################################################


def color_print(rgb: Tuple[int, int, int], message: str):
    print("\033[1;38;2;{};{};{}m{}\033[0m".format(rgb[0], rgb[1], rgb[2],
                                                  message))


##############################################################################


def color_input(rgb: Tuple[int, int, int], message: str) -> str:
    return input("\033[1;38;2;{};{};{}m{}\033[0m".format(
        rgb[0], rgb[1], rgb[2], message))


##############################################################################
