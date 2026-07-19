import pandas as pd

data = {
    "Name": ["Ganesh", "Rahul"],
    "Age": [21, 22],
    "City": ["Chennai", "Hyderabad"]
}

df = pd.DataFrame(data)

df.drop("City", axis=1, inplace=True)

print(df)