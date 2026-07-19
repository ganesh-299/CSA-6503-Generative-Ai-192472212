import pandas as pd

data = {
    "Marks": [80, None, 90, None]
}

df = pd.DataFrame(data)

df.fillna(0, inplace=True)

print(df)