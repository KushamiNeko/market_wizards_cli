from typing import Dict, List
import re
import os
import subprocess
import helper
from terminal import TerminalColors
from pages.pages import Pages
from context import Context

##############################################################################


class IBDParser(Pages):

    _actions = ["parse"]

    _path = ""

    def __init__(self, context: Context) -> None:
        super(IBDParser, self).__init__(context)

##############################################################################

    def _process_command(self, command: str) -> None:
        if command == "parse":
            self._command_parse()

##############################################################################

    def _command_parse(self) -> None:
        path = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the folder containing ibd stocks xls files: ")

        path = path.replace("'", "").strip()

        if not os.path.exists(path):
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500),
                "Path does not exist: {}".format(path))
        else:
            self._path = path

        if not self._path:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500),
                "Invalid Path: {}".format(self._path))

        csv_files = []

        for f in os.listdir(self._path):
            ext = os.path.splitext(f)[1]

            if ext != ".xls" and ext != ".csv":
                continue

            if ext == ".csv":
                # helper.color_print(
                # helper.hex_to_rgb(TerminalColors.paper_red_500),
                # "Removing File: {}".format(f))
                # os.remove(os.path.join(LISTS, f))
                pass

            if ext == ".xls":
                self._xls_to_csv(os.path.join(self._path, f), True)

                csv_file = os.path.join(
                    self._path, f.replace(os.path.splitext(f)[1], ".csv", -1))

                csv_files.append(csv_file)

        helper.color_print(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "\nIBD Stocks Lists:\n")

        for csv_file in csv_files:
            with open(csv_file, "r", encoding="ISO-8859-1") as csvf:
                content = csvf.read()
                strings = content.split("\n")

                printing = False

                for s in strings:
                    c = s.split(",")
                    if len(c) >= 1:
                        symbol = c[0]

                        if symbol == "Symbol":
                            printing = True
                            continue

                        if printing and symbol != "":
                            print(symbol)
                        elif printing and symbol == "":
                            printing = False
                            break

##############################################################################

    def _xls_to_csv(self, path: str, debug: bool) -> None:
        if debug:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_light_blue_300),
                "Converting File: {}".format(path))

        subprocess.check_output([
            "libreoffice", "--headless", "--convert-to", "csv", path,
            "--outdir", self._path
        ])


##############################################################################
