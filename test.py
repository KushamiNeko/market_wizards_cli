# import pandas as pd
import re

_regex_pattern = r"([^;]+)=([^;]+)"

test = "price;o=l"

matches = re.finditer(_regex_pattern, test, re.DOTALL)

for match in matches:
    print(match.group(1))
    print(match.group(2))

exit(0)

# path = "/home/neko/Downloads/SC.csv"

# df = pd.read_csv(path)

# loop = (len(df) // 500) + 1

# for i in range(loop):
# s = i * 500
# e = (i + 1) * 500
# if i != (loop - 1):
# slices = df.iloc[s:e]
# l = [x for x in slices["Symbol"].get_values()]
# else:
# slices = df.iloc[s:]
# l = [x for x in slices["Symbol"].get_values()]
# del l[len(l) - 1]

# print("{} symbols".format(len(l)))
# print(",".join(l))
# _regex_ratings = r'\s*<ul\s*class="smartRating">\s*<li>\s*<a\s*class="glossDef"\s*href="[^"]+"\s*rel="[^"]+">\s*<span\s*class="typespan"\s*style="[^"]+">\s*([^<]+)\s*</span>\s*</a>\s*</li>\s*<li>\s*([A-Ea-e0-9+-]+)\s*</li>\s*<li>\s*<a\s*class="passDef"\s*href="[^"]+"\s*rel="[^"]+">\s*<img\s*class="FSIcons"\s*src="[^"]+"\s*width="[^"]+"\s*height="[^"]+"\s*alt="[^"]+">\s*</a>\s*</li>\s*</ul>\s*'

_regex_ratings = r"""\s*<ul\s*class=["']smartRating["']>\s*<li>\s*<a\s*class=["']glossDef["']\s*href=["'][^'"]+["']\s*rel=["'][^'"]+["']>\s*<span\s*class=["']typespan["']\s*style=["'][^'"]+["']>\s*([^<]+)\s*</span>\s*</a>\s*</li>\s*<li>\s*([A-Ea-e0-9+-]+)\s*</li>\s*<li>\s*<a\s*class=["']passDef["']\s*href=["'][^'"]+["']\s*rel=["'][^'"]+["']\s*>\s*<img\s*class=["']FSIcons["']\s*src=["'][^'"]+["']\s*width=["'][^'"]+["']\s*height=["'][^'"]+["']\s*alt=["'][^'"]+["']\s*[/]?>\s*</a>\s*</li>\s*</ul>\s*"""

_regex_eps_due_date = r"""\s*<ul>\s*<li>\s*(EPS Due Date)\s*<\/li>\s*<li>\s*([^<]+)\s*<\/li>\s*<\/ul>\s*"""

_regex_symbol = r"""\s*<span\s*id=["']qteSymb["']\s*itemprop=["']tickerSymbol["']\s*itemscope(?:=["'][^"']?["'])?\s*itemtype=["'][^"']+["']>\s*([A-Z]+)\s*</span>\s*"""

with open("test_resources/ibd_research/test.html", "r") as text:
    content = text.read()
    # print(content)
    # matches = re.finditer(_regex_eps_due_date, content)
    # for m in matches:
    # print(m)

    match = re.findall(_regex_symbol, content, re.DOTALL)
    print(match)
    # print(match.group(1))
    # print(match.group(2))

# match = re.match(r"[Ee]?(\d{8})", "20190107")
# print(match.group(1))
