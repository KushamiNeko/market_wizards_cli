import pandas as pd

path = "/home/neko/Downloads/SC.csv"

df = pd.read_csv(path)

loop = (len(df) // 500) + 1

for i in range(loop):
    s = i * 500
    e = (i + 1) * 500
    if i != (loop - 1):
        slices = df.iloc[s:e]
        l = [x for x in slices["Symbol"].get_values()]
    else:
        slices = df.iloc[s:]
        l = [x for x in slices["Symbol"].get_values()]
        del l[len(l) - 1]

    print("{} symbols".format(len(l)))
    print(",".join(l))
