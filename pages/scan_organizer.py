import os
import subprocess
import re
from typing import Generator, Set, List, Callable

import pandas as pd

import config
import helper
from list_printer import ListPrinter
from terminal import TerminalColors
from pages.pages import Pages
from context import Context

##############################################################################


class ScanOrganizer():

    _actions = [
        "ibd stock lists",
        "ibd data tables",
        "stock charts scans",
        "print csv",
        # "print list",
    ]

    def __init__(self, context: Context) -> None:
        self.context = context

        self._stocks_list: Set[str] = set()

        self._page = Pages(self._actions)

        self._handlers = {
            "ibd stock lists": self._command_ibd_stock_lists,
            "ibd data tables": self._command_ibd_data_tables,
            "stock charts scans": self._command_stock_charts_scans,
            "print csv": self._command_print_csv,
            # "print list": self._command_print_list,
        }

##############################################################################

    def main_loop(self) -> None:
        self._page.main_loop(self._process_command)

##############################################################################

    def _process_command(self, command: str) -> None:
        handler = self._handlers.get(command, None)
        if handler:
            handler()

##############################################################################

    def _collect_symbols_from_parser(self, parser: Callable) -> None:
        p = parser()
        generator = p.list_generator()

        for symbol in generator:
            self._stocks_list.add(symbol)

##############################################################################

    def _command_ibd_stock_lists(self) -> None:
        self._collect_symbols_from_parser(_IBDStockListsParser)

##############################################################################

    def _command_ibd_data_tables(self) -> None:
        self._collect_symbols_from_parser(_IBDDataTablesParser)

##############################################################################

    def _command_stock_charts_scans(self) -> None:
        self._collect_symbols_from_parser(_ScanCSVsParser)

##############################################################################

    def _command_print_csv(self) -> None:
        printer = ListPrinter()
        printer.print_csv(list(self._stocks_list))

##############################################################################

    def _command_print_list(self) -> None:
        printer = ListPrinter()
        printer.print_list(list(self._stocks_list))


##############################################################################


class _IBDStockListsParser():
    def __init__(self) -> None:
        pass

##############################################################################

    def list_generator(self) -> Generator:
        path = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the folder containing ibd stocks xls files: ")

        path = path.replace("'", "").strip()

        try:
            csv_files = self._process_xls_files(path, debug=True)

            symbols = self._extract_symbols_from_csv(csv_files)

            for symbol in symbols:
                yield symbol

        except ValueError as err:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500), str(err))

##############################################################################

    def _process_xls_files(self, path: str, debug: bool = False) -> List[str]:
        if path == "":
            raise ValueError("Invalid Path: {}".format(path))

        if not os.path.exists(path):
            raise ValueError("Path does not exist: {}".format(path))

        csv_files = []

        for f in os.listdir(path):
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
                self._xls_to_csv(os.path.join(path, f), path, debug=debug)

                csv_file = os.path.join(
                    path, f.replace(os.path.splitext(f)[1], ".csv", -1))

                csv_files.append(csv_file)

        return csv_files

##############################################################################

    def _xls_to_csv(self,
                    input_file: str,
                    output_path: str,
                    debug: bool = False) -> None:
        if debug:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_light_blue_300),
                "Converting File: {}".format(input_file))

        subprocess.check_output([
            "libreoffice", "--headless", "--convert-to", "csv", input_file,
            "--outdir", output_path
        ])

##############################################################################

    def _extract_symbols_from_csv(self, csv_files: List[str]) -> Set[str]:
        symbols = set()

        for csv_file in csv_files:

            count = 0

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
                            symbols.add(symbol)
                            count += 1

                        elif printing and symbol == "":
                            printing = False
                            break

            helper.color_print(config.COLOR_INFO, "{} STOCKS in {}".format(
                count, csv_file))

        return symbols


##############################################################################


class _IBDDataTablesParser():

    _regex = r'<(?:td|TD)>(?:\s*<font\s*size="\d+">\s*)?\s*([A-Z]+)(?:/\s*[A-Z]+)?(?:\s*</font>\s*)?\s*</(?:td|TD)>'

    def __init__(self) -> None:
        pass

##############################################################################

    def list_generator(self) -> Generator:
        path = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the folder containing ibd data tabels html files: ")

        path = path.replace("'", "").strip()

        try:
            symbols = self._parse_html_files(path)

            for symbol in symbols:
                yield symbol
        except ValueError as err:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500), str(err))

##############################################################################

    def _parse_html_files(self, path: str) -> Set[str]:
        if not os.path.exists(path):
            raise ValueError("Path does not exist: {}".format(path))

        symbols: Set[str] = set()

        for f in os.listdir(path):
            ext = os.path.splitext(f)[1]

            if ext != ".html":
                continue

            count = 0

            with open(os.path.join(path, f), "r") as text:
                content = text.read()
                match = re.finditer(self._regex, content, re.DOTALL)

                for m in match:
                    if not m:
                        continue
                    symbols.add(m.group(1))
                    count += 1

            helper.color_print(config.COLOR_INFO, "{} STOCKS in {}".format(
                count, f))

        return symbols


##############################################################################


class _ScanCSVsParser():
    def __init__(self) -> None:
        pass

##############################################################################

    def list_generator(self) -> Generator:
        path = helper.color_input(
            helper.hex_to_rgb(TerminalColors.paper_amber_300),
            "Please enter the path to the csv file: ")

        path = path.replace("'", "").strip()

        try:
            symbols = self._parse_csv_files(path)

            for symbol in symbols:
                yield symbol

        except ValueError as err:
            helper.color_print(
                helper.hex_to_rgb(TerminalColors.paper_red_500), str(err))

##############################################################################

    def _parse_csv_files(self, path: str) -> Set[str]:
        if not os.path.exists(path):
            raise ValueError("Path does not exist: {}".format(path))

        symbols = set()

        for f in os.listdir(path):
            ext = os.path.splitext(f)[1]

            if ext != ".csv":
                continue

            count = 0

            df = pd.read_csv(os.path.join(path, f))

            for symbol in df["Symbol"].get_values():
                if str(symbol).lower() == "nan":
                    continue

                symbols.add(symbol)
                count += 1

            helper.color_print(config.COLOR_INFO, "{} STOCKS in {}".format(
                count, f))

        return symbols


##############################################################################
