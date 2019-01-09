import re
import os
from typing import Dict, Any

##############################################################################


class IBDResearchParser():

    _regex_symbol = r"""\s*<span\s*id=["']qteSymb["']\s*itemprop=["']tickerSymbol["']\s*itemscope(?:=["'][^"']?["'])?\s*itemtype=["'][^"']+["']>\s*([A-Z]+)\s*</span>\s*"""

    _regex_ratings = r"""\s*<ul\s*class=["']smartRating["']>\s*<li>\s*<a\s*class=["']glossDef["']\s*href=["'][^'"]+["']\s*rel=["'][^'"]+["']>\s*<span\s*class=["']typespan["']\s*style=["'][^'"]+["']>\s*([^<]+)\s*</span>\s*</a>\s*</li>\s*<li>\s*([A-Ea-e0-9+-]+)\s*</li>\s*<li>\s*<a\s*class=["']passDef["']\s*href=["'][^'"]+["']\s*rel=["'][^'"]+["']\s*>\s*<img\s*class=["']FSIcons["']\s*src=["'][^'"]+["']\s*width=["'][^'"]+["']\s*height=["'][^'"]+["']\s*alt=["'][^'"]+["']\s*[/]?>\s*</a>\s*</li>\s*</ul>\s*"""

    _regex_daily_price_range = r"""\s*<ul>\s*<li>\s*Today's Range\s*<\/li>\s*<li>\s*<span\s*class=["'][^"']+["']>\s*([0-9.]+)\s*<\/span>\s*[^<]+\s*<span\s*class=["'][^"']+["']>\s*([0-9.]+)\s*<\/span>\s*"""

    # _regex_eps_due_date = r"""\s*<ul>\s*<li>\s*(EPS Due Date)\s*<\/li>\s*<li>\s*([^<]+)\s*<\/li>\s*<\/ul>\s*"""
    _regex_data = r"""\s*<ul>\s*<li>\s*([^<]+)\s*<\/li>\s*<li>\s*([^<]+)\s*<\/li>\s*<\/ul>\s*"""

    _ratings_name = {
        "Composite Rating": "comp",
        "EPS Rating": "eps",
        "RS Rating": "rs",
        "Group RS Rating": "grs",
        "SMR Rating": "smr",
        "Acc/Dis Rating": "acc",
        "EPS Due Date": "earnings",
    }

    def __init__(self):
        self.symbol = ""
        self.ibd_research: Dict[str, Any] = {}

##############################################################################

    def parse(self, filepath: str) -> None:

        if not os.path.exists(filepath):
            raise ValueError("path does not exist: {}".format(filepath))

        ratings: Dict[str, Any] = {}

        with open(filepath, "r") as text:
            content = text.read()

            match_symbol = re.findall(self._regex_symbol, content, re.DOTALL)
            if match_symbol:
                symbol = match_symbol[0]
                self.symbol = symbol

            matches = re.finditer(self._regex_ratings, content, re.DOTALL)

            for match in matches:
                if not match:
                    continue

                rating = match.group(1).strip()
                value = match.group(2).strip()

                match_int = re.match(r"\d+", value, re.DOTALL)
                if match_int:
                    ratings[self._ratings_name[rating]] = int(value)

                match_rank = re.match(r"([A-E])[+-]?", value, re.DOTALL)
                if match_rank:
                    value = match_rank.group(1).strip()
                    ratings[self._ratings_name[rating]] = value

            # match_eps = re.findall(self._regex_eps_due_date, content,
            # re.DOTALL)
            # if match_eps:
            # try:
            # date = self._format_date(match_eps[0][1])
            # ratings[self._ratings_name[match_eps[0][0]]] = date
            # except ValueError:
            # pass

            match_data = re.finditer(self._regex_data, content, re.DOTALL)

            for match in match_data:
                if not match:
                    continue

                label = match.group(1).strip()

                if label == "EPS Due Date":
                    try:
                        date = self._format_date(match.group(2))
                        ratings[self._ratings_name[label]] = date
                    except ValueError:
                        pass

        self.ibd_research = ratings

##############################################################################

    def _format_date(self, ibd_date: str) -> str:

        if not re.match(r"\d{1,2}/\d{1,2}/\d{4}", ibd_date):
            raise ValueError("Invalid IBD Date: {}".format(ibd_date))

        numbers = ibd_date.split("/")
        year = numbers[2].strip().zfill(4)
        month = numbers[0].strip().zfill(2)
        day = numbers[1].strip().zfill(2)

        date = "E{}{}{}".format(year, month, day)

        return date


##############################################################################
