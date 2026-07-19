import pandas as pd

data = {
    "Name": ["Ganesh", "Rahul", "Ganesh"],
    "Age": [21, 22, 21]
}

df = pd.DataFrame(data)

df = df.drop_duplicates()

print(df)